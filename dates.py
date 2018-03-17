import numpy as np
import argparse
from datetime import datetime as dt

argp = argparse.ArgumentParser(description='Determine the difference between two dates.')
argp.add_argument('-s', '--start', metavar='START', default='',
					help='Enter the start date ()')
argp.add_argument('-e', '--end', metavar='END', default='',
					help='Enter the end date ()')
args = argp.parse_args()

d0 = dt.strptime(args.start, "%m/%d/%y").date()
d1 = dt.strptime(args.end, "%m/%d/%y").date()

days = np.busday_count(d0, d1)
weeks = days / 5.0

print ("%.2f" % weeks)
