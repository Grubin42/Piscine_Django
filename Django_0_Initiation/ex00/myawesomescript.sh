#!/bin/sh

if [ -z "$1" ]; then
  echo "Usage: $0 <bit.ly_url>"
  exit 1
fi

# Afficher l'URL finale après toutes les redirections
curl -L -s -w "%{url_effective}\n" -o /dev/null "$1"