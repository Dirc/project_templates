

from optparse import OptionParser

#retrieve options given
parser = OptionParser()
usage = "usage: %prog [options]"

parser.add_option("--targethost", help="specify targethost to check connection", dest="targethost", default="lsrv8006")

options, arguments = parser.parse_args()

# get option
server=options.targethost

print server



