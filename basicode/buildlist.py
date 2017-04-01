#!/usr/bin/env python2

import os

types = 'bc', 'bc2', 'bc3', 'b3c', 'bas', 'asc'

print '<ol>'
for root, dirs, files in os.walk('basicode/'):
    print '      <li>' + root + '</li>'
    print '      <ol>'
    for name in files:
        if [name.lower().endswith(t) for t in types]:
            with open(os.path.join(root, name), 'r') as f:
                for line in f:
                    if line.startswith('1000 '):
                        title = line.split('REM')[-1].strip() or name
                        print '        <li><a href="'+ os.path.join(root, name) + '" onclick="return loadFile(this);">' + line.split('REM')[-1].strip()+ '</a></li>'
    print '      </ol>'
print '</ol>'
