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


# Parsing an existing file:
# -------------------------
orig_stdout = sys.stdout

gpx_file = open(args.file, 'r', encoding='utf-8')

gpx = gpxpy.parse(gpx_file)


outfile="garmin_"+os.path.basename(args.file)
outfile=outfile.replace(" ","_")

f = open(outfile, 'w')
sys.stdout = f

# We are not using the gpx.to_xml function since we really don't know how to add the extensions


# print header
header='<?xml version="1.0" encoding="utf-8"?><gpx creator="Garmin Desktop App" version="1.1" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/ActivityExtension/v1 http://www8.garmin.com/xmlschemas/ActivityExtensionv1.xsd http://www.garmin.com/xmlschemas/AdventuresExtensions/v1 http://www8.garmin.com/xmlschemas/AdventuresExtensionv1.xsd http://www.garmin.com/xmlschemas/PressureExtension/v1 http://www.garmin.com/xmlschemas/PressureExtensionv1.xsd http://www.garmin.com/xmlschemas/TripExtensions/v1 http://www.garmin.com/xmlschemas/TripExtensionsv1.xsd http://www.garmin.com/xmlschemas/TripMetaDataExtensions/v1 http://www.garmin.com/xmlschemas/TripMetaDataExtensionsv1.xsd http://www.garmin.com/xmlschemas/ViaPointTransportationModeExtensions/v1 http://www.garmin.com/xmlschemas/ViaPointTransportationModeExtensionsv1.xsd http://www.garmin.com/xmlschemas/CreationTimeExtension/v1 http://www.garmin.com/xmlschemas/CreationTimeExtensionsv1.xsd http://www.garmin.com/xmlschemas/AccelerationExtension/v1 http://www.garmin.com/xmlschemas/AccelerationExtensionv1.xsd http://www.garmin.com/xmlschemas/PowerExtension/v1 http://www.garmin.com/xmlschemas/PowerExtensionv1.xsd http://www.garmin.com/xmlschemas/VideoExtension/v1 http://www.garmin.com/xmlschemas/VideoExtensionv1.xsd" xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:wptx1="http://www.garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtrx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:trp="http://www.garmin.com/xmlschemas/TripExtensions/v1" xmlns:adv="http://www.garmin.com/xmlschemas/AdventuresExtensions/v1" xmlns:prs="http://www.garmin.com/xmlschemas/PressureExtension/v1" xmlns:tmd="http://www.garmin.com/xmlschemas/TripMetaDataExtensions/v1" xmlns:vptm="http://www.garmin.com/xmlschemas/ViaPointTransportationModeExtensions/v1" xmlns:ctx="http://www.garmin.com/xmlschemas/CreationTimeExtension/v1" xmlns:gpxacc="http://www.garmin.com/xmlschemas/AccelerationExtension/v1" xmlns:gpxpx="http://www.garmin.com/xmlschemas/PowerExtension/v1" xmlns:vidx1="http://www.garmin.com/xmlschemas/VideoExtension/v1">'

# importing datetime module for now()

# using now() to get current time
current_time = datetime.datetime.now()



def print_wp_extension():
    print ("    <extensions>")
    print ("     <gpxx:WaypointExtension>")
    print ("        <gpxx:DisplayMode>SymbolAndName</gpxx:DisplayMode>")
    print ("      </gpxx:WaypointExtension>")
    print ("      <wptx1:WaypointExtension>")
    print ("        <wptx1:DisplayMode>SymbolAndName</wptx1:DisplayMode>");
    print ("      </wptx1:WaypointExtension>")
    print ("      <ctx:CreationTimeExtension>")
    print ("        <ctx:CreationTime>2022-09-06T20:08:13Z</ctx:CreationTime>")
    print ("      </ctx:CreationTimeExtension>")
    print ("    </extensions>")
 
#print('<?xml version="1.0" encoding="utf-8"?><gpx creator="Garmin Desktop App" version="1.1" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/ActivityExtension/v1 http://www8.garmin.com/xmlschemas/ActivityExtensionv1.xsd http://www.garmin.com/xmlschemas/AdventuresExtensions/v1 http://www8.garmin.com/xmlschemas/AdventuresExtensionv1.xsd http://www.garmin.com/xmlschemas/PressureExtension/v1 http://www.garmin.com/xmlschemas/PressureExtensionv1.xsd http://www.garmin.com/xmlschemas/TripExtensions/v1 http://www.garmin.com/xmlschemas/TripExtensionsv1.xsd http://www.garmin.com/xmlschemas/TripMetaDataExtensions/v1 http://www.garmin.com/xmlschemas/TripMetaDataExtensionsv1.xsd http://www.garmin.com/xmlschemas/ViaPointTransportationModeExtensions/v1 http://www.garmin.com/xmlschemas/ViaPointTransportationModeExtensionsv1.xsd http://www.garmin.com/xmlschemas/CreationTimeExtension/v1 http://www.garmin.com/xmlschemas/CreationTimeExtensionsv1.xsd http://www.garmin.com/xmlschemas/AccelerationExtension/v1 http://www.garmin.com/xmlschemas/AccelerationExtensionv1.xsd http://www.garmin.com/xmlschemas/PowerExtension/v1 http://www.garmin.com/xmlschemas/PowerExtensionv1.xsd http://www.garmin.com/xmlschemas/VideoExtension/v1 http://www.garmin.com/xmlschemas/VideoExtensionv1.xsd" xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:wptx1="http://www.garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtrx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:trp="http://www.garmin.com/xmlschemas/TripExtensions/v1" xmlns:adv="http://www.garmin.com/xmlschemas/AdventuresExtensions/v1" xmlns:prs="http://www.garmin.com/xmlschemas/PressureExtension/v1" xmlns:tmd="http://www.garmin.com/xmlschemas/TripMetaDataExtensions/v1" xmlns:vptm="http://www.garmin.com/xmlschemas/ViaPointTransportationModeExtensions/v1" xmlns:ctx="http://www.garmin.com/xmlschemas/CreationTimeExtension/v1" xmlns:gpxacc="http://www.garmin.com/xmlschemas/AccelerationExtension/v1" xmlns:gpxpx="http://www.garmin.com/xmlschemas/PowerExtension/v1" xmlns:vidx1="http://www.garmin.com/xmlschemas/VideoExtension/v1">\n')
print(header+"\n")


# Let's try without the metadata
# Waypoints
for waypoint in gpx.waypoints:
    if (waypoint.type == "pass"):
        waypoint.sym = "Blind"
        waypoint.type = "user"
    elif (waypoint.type == "salt_lick"):
          waypoint.sym = "Triangle, Yellow"
          waypoint.type = "user"
    elif (waypoint.type == "tower"):
          waypoint.sym = "Tree Stand"
          waypoint.type = "user"
    elif (waypoint.type == "ford"):
          waypoint.sym = "Flag, Yellow"
          waypoint.type = "user"
    elif (waypoint.type == "other"):
          waypoint.sym = "Circle with X"
          waypoint.type = "user"
    elif (waypoint.type == "gathering_place"):
          waypoint.sym = "Restaurant"
          waypoint.type = "user"
    # Remove any forbidden XML characters and replace with correspoinding code
    waypoint.name=waypoint.name.replace("&", "+")


          
    if (waypoint.type != "parking"):      
        print ('  <wpt lat="'+str(waypoint.latitude)+'" lon="'+str(waypoint.longitude)+'">')
        print ('    <time>'+current_time.strftime("%G-%m-%dT%H:%M:%S")+'Z</time>')
        print ('    <name>'+str(waypoint.name)+'</name>')
        print('    <sym>'+waypoint.sym+'</sym>')
        print('    <type>'+waypoint.type+'</type>')
        try:
            waypoint.description=waypoint.description.replace("&","+")
            waypoint.description=waypoint.description.replace("\n"," ")
            #print('    <cmt> From Wehunt'+current_time.strftime("%G-%m%d")+'</cmt>')
            #print('    <desc>From Wehunt'+current_time.strftime("%G-%m%d")+'</desc>')
        except AttributeError:
            #print('    <cmt> </cmt>')
            #print('    <desc> </desc>')
            print('')
#        print_wp_extension
        print ("    <extensions>")
        print ("     <gpxx:WaypointExtension>")
        print ("        <gpxx:DisplayMode>SymbolAndName</gpxx:DisplayMode>")
        print ("      </gpxx:WaypointExtension>")
        print ("      <wptx1:WaypointExtension>")
        print ("        <wptx1:DisplayMode>SymbolAndName</wptx1:DisplayMode>");
        print ("      </wptx1:WaypointExtension>")
        print ("      <ctx:CreationTimeExtension>")
        print ("        <ctx:CreationTime>2022-09-06T20:08:13Z</ctx:CreationTime>")
        print ("      </ctx:CreationTimeExtension>")
        print ("    </extensions>")
        print ('  </wpt>\n')


for track in gpx.tracks:
    track.name=track.name.replace("&", " ")
    
    print("  <trk>");
    print("    <name>"+str(track.name)+"</name>")
    print("    <extensions>")
    print("      <gpxx:TrackExtension>")
    print("        <gpxx:DisplayColor>Red</gpxx:DisplayColor>")
    print("      </gpxx:TrackExtension>")
    print("    </extensions>")

    print("    <trkseg>");
    for segment in track.segments:
        for point in segment.points:
            print('      <trkpt lat="'+str(point.latitude)+'" lon="'+str(point.longitude)+'" />')
            #        print(f'Point at ({point.latitude},{point.longitude}) -> {point.elevation}')

    print("    </trkseg>");

    print("  </trk>\n");
print("</gpx>")
sys.stdout = orig_stdout
f.close()         
#print(gpx.to_xml(version="1.1"))
