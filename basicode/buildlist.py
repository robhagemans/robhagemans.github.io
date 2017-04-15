#!/usr/bin/env python2

import os
import json

types = 'bc', 'bc2', 'bc3', 'b3c', 'bas', 'asc'

collection = {};

for root, dirs, files in sorted(os.walk('basicode/')):
    root_name = root[len('basicode/'):]
    collection[root_name] = {}
    for name in sorted(files):
        isbc = [name.lower().endswith(t) for t in types]
        if True in isbc:
            with open(os.path.join(root, name), 'r') as f:
                for line in f:
                    if line.strip().startswith('1000 '):
                        try:
                            title = line.split('REM')[1].strip() or name
                            title = ''.join(c for c in title if c.isalnum() or c in (' ', '-', '.', ',')).strip().title()
                        except IndexError:
                            title = name
                        collection[root_name][title] = os.path.join(root, name)

print json.dumps(collection)
