#!/bin/bash
# Generate HTML from jemdoc sources in src/
# Usage: bash generate.sh
# Prerequisite: conda activate jemdoc
set -e
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

echo "==> Generating HTML from src/*.jemdoc ..."
for f in src/*.jemdoc; do
    echo "  Processing $(basename "$f") ..."
    python jemdoc "$f"
done

echo "==> Moving HTML to root ..."
mv -f src/*.html "$ROOT"/

echo "==> Done. Generated pages:"
ls -1 "$ROOT"/*.html | while read f; do echo "    $(basename "$f")"; done
