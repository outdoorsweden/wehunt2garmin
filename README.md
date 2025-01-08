PÅ SVENSKA:
# wehunt2garmin
Det här är ett program som konverterar symbolerna i GPX filen från Wehunt till
de symboler som garmin använder.  För att kunna använda det krävs att du har python och ett
pythontillägg som heter gpxpy installerat.

## Linux
Installera python på din maskin med den metod som rekommenderas för din linux distribution.
Google är en bra hjälp där.
Exempel Red Hat: 
>sudo yum install python

Sen installerar man gpxpy så här:
>pip install gpxpy

Kör <sökvägen till wehunt2garmin>/bin/wehunt2garmin.py -file wehunt/wehunt_example.gpx 
för att se att det fungerar.

## Windows
Installera python from https://python.org
I cmd fönstret:
>pip install gpxpy


För att köra programmet
1. Gå till platsen där du packade upp wehunt2garmin filen som du laddade ner.
2. python bin/wehunt2garmin.py -file <sökvägen till gpx filen från wehunt>
3. A 'garmin_"wehunt filnamn".gpx' skapas. Importera till basemap och installera i din garminpejl eller
kopiera diret till pejlen mha filhanteraren.


IN ENGLISH:

# wehunt2garmin
This is a script that converts GPX output from wehunt to Garmin


## Linux
Install python on your machine using the prefereed method for your linux distribution.
Example Red Hat: 
>sudo yum install python

Then install gpxpy
>pip install gpxpy

Run .../bin/wehunt2garmin.py -file wehunt/wehunt_example.gpx 

## Windows
Install python from https://python.org
In cmd window:
>pip install gpxpy


To run:
1. Goto the location where you unpacked the scripts
2. python bin/wehunt2garmin.py -file <path to gpx file from wehunt>
3. A 'garmin_"wehunt file name".gpx' file will be created. Import to basemap and install in your garmin device or
copy directly into the garmin device using your file manager.
