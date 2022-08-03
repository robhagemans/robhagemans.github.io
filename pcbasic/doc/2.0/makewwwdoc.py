#!/usr/bin/env python3

import os, sys, shutil, subprocess

here = os.path.dirname(os.path.realpath(os.path.abspath(__file__)))
wd = os.path.join(here, '..', '..', '..', '..', 'pc-basic')
sys.path.insert(0, wd)

from docs import make_htmldoc

# generate online doc
make_htmldoc(
    here, 'index.html',
    header=os.path.join(here, 'header.html'),
    embedded_style=False
)
# generate offline doc
make_htmldoc(here, 'PC-BASIC_documentation.html')
# front page
shutil.copy(os.path.join(wd, 'docs', 'source', 'cover.png'), here)
# generate PDF
subprocess.call(
    ('prince', os.path.join(here, 'PC-BASIC_documentation.html'))
)
#shutil.copy(os.path.join(wd, 'build', 'doc', 'PC-BASIC_documentation.html'), here)
#shutil.copy(os.path.join(wd, 'build', 'doc', 'PC-BASIC_documentation.pdf'), here)
# get styles
shutil.copy(os.path.join(wd, 'docs', 'source', 'doc.css'), here)
