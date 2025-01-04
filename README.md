# Google maps timeline parser

Google has stopped the support for Timeline viewer on web. Can be done only on mobile app.

Parses for Google Maps timeline data. It reads the JSON file that you can download from Google Maps and creates a CSV file with that's compatible for [Kepler](https://kepler.gl/demo)

## Download your Google Maps timeline data

Note: Timeline data downloaded via Google Takeout is not the same as the data you see in Google Maps Timeline. 

Download timeline data via Android app:

Location -> Location Services -> Timeline -> Export Timeline data.

Ensure the `json` file contains this structure:

```json
[
  "rawSignals" : {...},
  "semanticSegments": {...}
  "userLocationProfile": {...}
]
```

For this application, all we need is only the `semanticSegments` data.

## Usage

Required: python

update the json filename in the `main.py` file.

```bash
python main.py 'timeline_path' 
(or)
python main.py 'places' 
```

* timeline_path: this will contains all the points and allows you to draw the path on the kepler map.
* place: this contains only the places you visited. (based on the google's probability)

Running this command will generate the `.csv` file in the same directory.

Upload this in the `kepler.gl` and you can see the timeline data.