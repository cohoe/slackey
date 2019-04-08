#!/usr/bin/env python3

import os
import sys
import json

if len(sys.argv) < 2:
  print("Must run `%s path_to_generate_from`" % sys.argv[0])
  exit(1)

path = sys.argv[1]

if not os.path.isdir(path):
  print("Path %s does not exist." % path)
  exit(1)

files = os.listdir(path)

slugs = []
for slug in files:
  slugs.append({ "gif": "%s/%s" % (path, slug) })

print(json.dumps(slugs, indent=4, sort_keys=True))
