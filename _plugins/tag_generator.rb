# frozen_string_literal: true

module Jekyll
  # Generates one page per tag slug under /tags/<slug>/.
  #
  # Tags come from two places, and both must be covered or the site ships
  # dead links:
  #
  #   1. `tags:` in post front matter, which Jekyll collects into site.tags.
  #   2. `tech_stack:`/`tools:` in collection documents (projects, csumb).
  #      Jekyll does NOT collect these, but _includes/project-card.html
  #      renders them as links to /tags/<slug>/, so they need pages too.
  class TagPageGenerator < Generator
    safe true

    TECH_KEYS = %w[tech_stack tools].freeze

    def generate(site)
      build_index(site).each_value do |entry|
        site.pages << TagPage.new(site, site.source, entry)
      end
    end

    private

    # slug => { slug:, label:, posts: [], docs: [] }
    def build_index(site)
      index = {}
      add_all(index, site.posts.docs, :posts)
      add_all(index, collection_docs(site), :docs)
      index
    end

    def add_all(index, documents, bucket)
      documents.each do |doc|
        tag_names(doc).each do |name|
          list = entry_for(index, name)[bucket]
          list << doc unless list.include?(doc)
        end
      end
    end

    def entry_for(index, name)
      slug = Jekyll::Utils.slugify(name)
      index[slug] ||= { slug: slug, label: name, posts: [], docs: [] }
    end

    def collection_docs(site)
      site.collections.reject { |label, _| label == 'posts' }
          .flat_map { |_, collection| collection.docs }
    end

    # Accepts both `- Python` and `- name: Python` shapes, plus a plain
    # `tags:` list on a collection document.
    def tag_names(doc)
      values = TECH_KEYS.flat_map { |key| Array(doc.data[key]) }
      values += Array(doc.data['tags'])
      values.filter_map do |value|
        name = value.is_a?(Hash) ? value['name'] : value
        stripped = name.to_s.strip
        stripped unless stripped.empty?
      end
    end
  end

  # A single /tags/<slug>/index.html page.
  class TagPage < Page
    def initialize(site, base, entry) # rubocop:disable Lint/MissingSuper
      @site = site
      @base = base
      @dir  = File.join('tags', entry[:slug])
      @name = 'index.html'

      process(@name)
      read_yaml(File.join(base, '_layouts'), 'tag.html')
      populate(entry)
    end

    private

    def populate(entry)
      data['tag'] = entry[:label]
      data['tagged_posts'] = entry[:posts].sort_by(&:date).reverse
      data['tagged_docs'] = entry[:docs]
      data['title'] = "Tagged: \"#{entry[:label]}\""
    end
  end
end
