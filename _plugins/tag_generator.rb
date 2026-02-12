module Jekyll
  class TagPageGenerator < Generator
    safe true

    def generate(site)
      # Extract all unique tags and map them to their slugified version
      tag_slugs = {}
      site.tags.each_key do |tag|
        slug = Jekyll::Utils.slugify(tag.to_s)
        tag_slugs[slug] ||= []
        tag_slugs[slug] << tag
      end

      # Create one page per unique slug
      tag_slugs.each do |slug, tags|
        # We use the first tag name as the representative for the title
        site.pages << TagPage.new(site, site.source, slug, tags.first)
      end
    end
  end

  class TagPage < Page
    def initialize(site, base, slug, tag)
      @site = site
      @base = base
      @dir  = File.join('tags', slug)
      @name = 'index.html'

      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'tag.html')
      self.data['tag'] = tag
      self.data['title'] = "Posts Tagged: \"#{tag}\""
    end
  end
end
