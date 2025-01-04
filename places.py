import json
import csv
from datetime import datetime
                
def extract_places(in_json):
    # Open location history data
    json_data = json.loads(open(in_json).read())

    for segment in json_data['semanticSegments']:
        if 'visit' in segment:
            visit = segment['visit']
            if 'topCandidate' in visit and 'placeLocation' in visit['topCandidate']:
                place_location = visit['topCandidate']['placeLocation']
                latitude, longitude = place_location['latLng'].replace('°', '').split(', ')
                start_time = datetime.strptime(segment['startTime'], '%Y-%m-%dT%H:%M:%S.%f%z')
                date = start_time.strftime('%Y-%m-%d')
                place_id = visit['topCandidate']['placeId']

                yield [date, start_time.isoformat(), float(longitude), float(latitude), place_id]


def collect_places(in_json, out_csv):
    # Read data from JSON file
    places_points = extract_places(in_json)
    # Add the Headers
    data_records = [['Date', 'Time', 'Longitude', 'Latitude', 'Place ID']]
    for row in places_points:
        data_records.append(row)

    # Write data to CSV file
    csv_writer = csv.writer(open(out_csv, 'w', newline=''))
    csv_writer.writerows(data_records)
