#!/usr/bin/env python2
import os, sys, shutil
here = os.path.dirname(os.path.realpath(os.path.abspath(__file__)))
wd = os.path.join(here, '..', '..', '..', '..', 'pc-basic')
sys.path.insert(0, wd)
from docsrc import makedoc
# generate online doc
makedoc(os.path.join(here, 'header.html'), os.path.join(here, 'index.html'), embedded_style=False)
# generate offline doc
makedoc()
shutil.copy(os.path.join(wd, 'doc', 'PC-BASIC_documentation.html'), here)
# generate PDF
os.system('prince %s' % os.path.join(wd, 'doc', 'PC-BASIC_documentation.html'))
shutil.copy(os.path.join(wd, 'doc', 'PC-BASIC_documentation.pdf'), here)
# get styles
shutil.copy(os.path.join(wd, 'docsrc', 'doc.css'), here)
