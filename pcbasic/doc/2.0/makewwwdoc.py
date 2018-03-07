#!/usr/bin/env python2
import os, sys, shutil
here = os.path.dirname(os.path.realpath(os.path.abspath(__file__)))
wd = os.path.join(here, '..', '..', '..', '..', 'pc-basic')
sys.path.insert(0, wd)
from docsrc.makedoc import makedoc
makedoc(os.path.join(here, 'header.html'), os.path.join(here, 'index.html'), embedded_style=False)
shutil.copy(os.path.join(wd, 'docsrc', 'doc.css'), here)
