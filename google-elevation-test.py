import googlemaps
import sys

def getLatLongFromAddress(address):

	geocode_result = gmaps.geocode(address)
	geometry = [d['geometry'] for d in geocode_result if 'geometry' in d]
	location = [d['location'] for d in geometry if 'location' in d]
	lat = [d['lat'] for d in location if 'lat' in d]
	lng = [d['lng'] for d in location if 'lng' in d]
	return lat[0], lng[0]

def getElevationFromLatLong(lat, lng):
	elev = gmaps.elevation((lat,lng))
	elev = [d['elevation'] for d in elev if 'elevation' in d][0]
	return elev


gmaps = googlemaps.Client(key='AIzaSyAPiKPjpIqk0kQLvK0IIPyFstWvvA3Mtrw')

if len(sys.argv) == 1:
	address = 'Ben Nevis, Scotland'
elif len(sys.argv) == 2:
	address = sys.argv[1]	
	dest_address = None
elif len(sys.argv) == 3:
	address = sys.argv[1]
	dest_address = sys.argv[2]
else:
	print ("Too many arguments - give only one or two addresses")
	exit(0);

if dest_address == None:
	lat, lng = getLatLongFromAddress(address)
	elev = getElevationFromLatLong(lat, lng)
	print ("The elevation of %s is %s metres") % (address, round(elev, 2))
else:
	lat, lng = getLatLongFromAddress(address)
	source_elev = getElevationFromLatLong(lat, lng)
	lat, lng = getLatLongFromAddress(dest_address)
	dest_elev = getElevationFromLatLong(lat, lng)

	diff = abs(source_elev - dest_elev)

	print("The difference in elevation between %s and %s is %s metres.") % (address, dest_address, round(diff, 2))




