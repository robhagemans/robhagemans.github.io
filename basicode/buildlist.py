#!/usr/bin/env python2

import os

types = 'bc', 'bc2', 'bc3', 'b3c', 'bas', 'asc'

print '<ol>'
for root, dirs, files in sorted(os.walk('basicode/')):
    print '    <li>' + root
    print '        <ol>'
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
                        print '            <li><a href="'+ os.path.join(root, name) + '" onclick="return loadFile(this);">' + title + '</a></li>'
    print '        </ol>\n    </li>'
print '</ol>'
