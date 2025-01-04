import json
import csv
from datetime import datetime


def extract_timeline_points(in_json):
    json_data = json.loads(open(in_json).read())

    for semantic_segment in json_data['semanticSegments']:
        if 'timelinePath' in semantic_segment:
            for timeline_path in semantic_segment['timelinePath']:
                latitude, longitude = timeline_path['point'].replace('°', '').split(', ')
                time = datetime.strptime(timeline_path['time'], '%Y-%m-%dT%H:%M:%S.%f%z')
                date = time.strftime('%Y-%m-%d')

                yield [date, time.isoformat(), float(longitude), float(latitude)]
                

def collect_timeline_path(in_json, out_csv):
    # Read data from JSON file
    timeline_points = extract_timeline_points(in_json)
    # Add the Headers
    data_records = [['Date', 'Time', 'Longitude', 'Latitude']]
    for row in timeline_points:
        data_records.append(row)

    # Write data to CSV file
    csv_writer = csv.writer(open(out_csv, 'w', newline=''))
    csv_writer.writerows(data_records)
