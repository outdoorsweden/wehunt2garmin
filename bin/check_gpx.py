#!/bin/env python3
import gpxpy
import gpxpy.gpx
from pprint import pprint
#import xml.etree.ElementTree as ET
import datetime
from contextlib import redirect_stdout
import os,sys
import argparse
parser = argparse.ArgumentParser(description='Generate a flat filelist from a potential hierarchical filelist')
parser.add_argument('-file',help='GPX File exported from Wehunt', required=True)


args = parser.parse_args()
gpx_file = open(args.file, 'r', encoding='utf-8')
gpx = gpxpy.parse(gpx_file)

for track in gpx.tracks:
    pprint(track)

for waypoint in gpx.waypoints:
    pprint(waypoint)
