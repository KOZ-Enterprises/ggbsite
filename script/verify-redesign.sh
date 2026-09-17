#!/usr/bin/env bash
# Verification assertions for the navbar/home redesign.
# Each check greps the BUILT site, not the source, so Liquid errors surface.
set -u
fail=0
check() { # check <name> <expected-count> <pattern> <file>
  local n
  n=$(grep -c -- "$3" "$4" 2>/dev/null) || true
  [ -n "$n" ] || n=0
  if [ "$n" -ge "$2" ]; then
    echo "  PASS  $1"
  else
    echo "  FAIL  $1 (found $n, wanted >=$2) in $4"
    fail=1
  fi
}
absent() { # absent <name> <pattern> <file>
  if grep -q -- "$2" "$3" 2>/dev/null; then
    echo "  FAIL  $1 (pattern still present) in $3"
    fail=1
  else
    echo "  PASS  $1"
  fi
}

echo "== Task 1: fonts + status =="
check "Chakra Petch loaded"  1 "Chakra+Petch"  _site/index.html
check "Roboto Mono loaded"   1 "Roboto+Mono"   _site/index.html

echo "== Task 2: navbar =="
check  "nav-shell present"       1 'class="nav-shell"'          _site/index.html
check  "toggle id preserved"     1 'id="myNavbar"'              _site/index.html
check  "nav mark image"          1 'branding/logo/ggbytes-transparent-g.png' _site/index.html
check  "Coursework label"        1 '>Coursework<'               _site/index.html
check  "home link active"        1 'nav-item active'            _site/index.html
check  "caption tail splittable" 1 'class="nav-caption-rest"'   _site/index.html
check  "hamburger bars"          3 'class="nav-icon-bar"'       _site/index.html
absent "old navbar markup gone"    'class="navbar"'             _site/index.html
absent "old nav-links gone"        'class="nav-links"'          _site/index.html
absent "fa-bars glyph gone"        'fa fa-bars'                 _site/index.html

exit $fail
