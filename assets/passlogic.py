#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import json
import pandas

plogic_url = os.getenv('PASSLOGIC_URL', default="")
#plogic_url = os.getenv('PASSLOGIC_URL', default="").strip("\"'")
plogic_json = os.getenv('PASSLOGIC', default="[[0,0],[1,0],[2,0],[3,0],[0,10],[0,11],[0,12],[0,13]]")
plogic = json.loads(plogic_json)

pldf = pandas.io.html.read_html(plogic_url)[0]
print("PassLogic random number table", file=sys.stderr)
print(pldf.iloc[0:4,0:14], file=sys.stderr)

plist = [ pldf.iat[i[0], i[1]] for i in plogic ]
pw = ''.join(plist)
print(pw)
