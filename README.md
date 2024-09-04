# wehunt2garmin
This is a script that converts GPX output from wehunt to Garmin


## Linux
Install python on your machine.
>pip install gpxpy

Run .../bin/wehunt2garmin.py -file wehunt/wehunt_example.gpx 

## Windows
Install python from https://python.org
In cmd window:
>pip install gpxpy


To run:
1. Goto the location where you unpacked the scripts
2. python bin/wehunt2garmin.py -file <path to gpx file from wehunt>
3. A "garmin_<wehunt file name>.gpx" file will be created. Import to basemap and install in you garmin
