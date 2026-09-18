#!/usr/bin/env bash
# Serve the built _site for visual checks. Usage: ./script/preview.sh [port]
# Build first - this serves static output and does NOT rebuild on change.
set -eu
PORT="${1:-4111}"
cd "$(dirname "$0")/../_site"
echo "Serving _site on http://127.0.0.1:${PORT}/  (Ctrl-C to stop)"
python -m http.server "$PORT"
