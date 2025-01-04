import argparse
from timeline_path import collect_timeline_path
from places import collect_places

def main():
    parser = argparse.ArgumentParser(description='Maps Data Command Line Application')
    parser.add_argument('option', choices=['timeline_path', 'places'], help='Choose an option to run')

    args = parser.parse_args()
    
    #replace this with the timeline.json
    input_json = './timeline.json'
    
    timeline_path_csv = './timeline_path.csv'
    places_csv = './places.csv'

    if args.option == 'timeline_path':
        collect_timeline_path(input_json, timeline_path_csv)
    elif args.option == 'places':
        collect_places(input_json, places_csv)

if __name__ == '__main__':
    main()