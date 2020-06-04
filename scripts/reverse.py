import argparse
import gpxpy

parser = argparse.ArgumentParser(description='Collect gpx files')
parser.add_argument('filename', type=str, help='gpxfile to reverse')

if __name__ == '__main__':
    args = parser.parse_args()
    gpx_file = open(args.filename, 'r')
    gpx_object = gpxpy.parse(gpx_file)
    gpx_points = gpx_object.tracks[0].segments[0].points
    new_gpx = gpxpy.gpx.GPX()
    new_gpx.tracks.append(gpxpy.gpx.GPXTrack())
    new_gpx.tracks[0].segments.append(gpxpy.gpx.GPXTrackSegment())
    new_gpx_segment = new_gpx.tracks[0].segments[0]
    for point in gpx_points:
        new_gpx_segment.points.insert(0, point)

    with open(args.filename + '_reversed', 'w') as new_file:
        new_file.write(new_gpx.to_xml())

    print('Created GPX:', new_gpx.to_xml())


