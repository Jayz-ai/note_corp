#!/usr/bin/env bash
# 新規記事の下書きフォルダを作成する
# usage: scripts/new-article.sh <slug> [paid|free|500] ["タイトル"]
#   500 = 500円ライン（templates/article-500.md）
set -euo pipefail

slug="${1:-}"
type="${2:-paid}"
title="${3:-$slug}"

if [[ -z "$slug" || ! "$slug" =~ ^[a-z0-9-]+$ ]]; then
  echo "usage: $0 <slug(半角英小文字・数字・ハイフン)> [paid|free|500] [\"タイトル\"]" >&2
  exit 1
fi
if [[ "$type" != "paid" && "$type" != "free" && "$type" != "500" ]]; then
  echo "type は paid / free / 500 のどれかを指定してください" >&2
  exit 1
fi

root="$(cd "$(dirname "$0")/.." && pwd)"
date="$(date +%F)"
dir="$root/content/drafts/$date-$slug"

if [[ -e "$dir" ]]; then
  echo "既に存在します: $dir" >&2
  exit 1
fi

mkdir -p "$dir/images"
touch "$dir/images/.gitkeep"
esc_title="$(printf '%s' "$title" | sed -e 's/[\/&|]/\\&/g')"
sed -e "s|{{TITLE}}|$esc_title|g" -e "s|{{DATE}}|$date|g" \
  "$root/templates/article-$type.md" > "$dir/article.md"

echo "作成しました: ${dir#$root/}/article.md"
