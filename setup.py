#! /usr/bin/python
# $Id: setup.py,v 1.9 2012/05/23 08:50:10 nanard Exp $
# the MiniUPnP Project (c) 2007-2014 Thomas Bernard
# http://miniupnp.tuxfamily.org/ or http://miniupnp.free.fr/
#
# python script to build the miniupnpc module under unix
#
# replace libminiupnpc.a by libminiupnpc.so for shared library usage
from distutils.core import setup, Extension
from distutils import sysconfig

import os
import subprocess

# build static lib if not exists
prj_root = os.path.dirname(__file__)
if not os.path.exists(os.path.join(prj_root, "libminiupnpc.a")):
    subprocess.call(['make', 'upnpc-static'])

sysconfig.get_config_vars()["OPT"] = ''
sysconfig.get_config_vars()["CFLAGS"] = ''
setup(name="miniupnpc",
      version=open('VERSION').read().strip(),
      author='Thomas BERNARD',
      author_email='miniupnp@free.fr',
      license=open('LICENSE').read(),
      url='https://github.com/chenhouwu/miniupnpc',
      description='miniUPnP client',
      long_description=open('README').read(),
      ext_modules=[
         Extension(name="miniupnpc", sources=["miniupnpcmodule.c"],
                   extra_objects=["libminiupnpc.a"])
      ])
