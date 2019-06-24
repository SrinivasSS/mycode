#!/usr/bin/env python3

import shutil
import os

os.chdir('/home/student/mycode')
shutil.copy('5G_Research/sdn_network.txt','5G_Research/sdn.network.txt.copy')
shutil.copytree('5G_Research/','5G_Research_backup/')
