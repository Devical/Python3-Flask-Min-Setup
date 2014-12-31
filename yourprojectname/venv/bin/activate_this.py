#! /usr/bin/python3

import os
import site
import sys

# Define Paths
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if sys.platform == 'win32':
    site_packages = os.path.join(base, 'Lib', 'site-packages')
else:
    site_packages = os.path.join(base, 'lib', 'python{}'.format(sys.version[:3]), 'site-packages')

# Remember original sys.path and os path
prev_sys_path = list(sys.path)
prev_os_path = os.environ['PATH']

# Add os path BEFORE old path
os.environ['PATH'] = base + os.pathsep + os.path.join(base, 'bin') + os.pathsep + prev_os_path

# Add new site-packages directory
site.addsitedir(site_packages)

# Reorder sys.path so new directories at the front.
new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path

