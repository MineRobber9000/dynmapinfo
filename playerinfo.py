import dynmap,argparse

parser = argparse.ArgumentParser(description="Gets all player info from DynMap.")
parser.add_argument("baseurl",help="The URL of the DynMap instance. (i.e; \"somniumscape.net:3397\"")
parser.add_argument("world",help="The target world. Must be tracked by the DynMap instance at baseurl.")
parser.add_argument("-s","--secure",action="store_true",help="Use HTTPS instead of HTTP")
args = parser.parse_args()

protocol = "http"
if args.secure:
	protocol = "https"
map = dynmap.DynMap(args.baseurl,protocol)
for player in map.players(args.world):
	print "{} at {!s} health with {!s} armor points. Location: x = {!s}, y = {!s}, z = {!s}, d = {!s}".format(player.name,player.health,player.armor,player.x,player.y,player.z,player.world)
