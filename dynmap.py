import requests,time

class Player:
	"""A player as represented by DynMap."""
	def __init__(self,**kwargs):
		self.__dict__.update(kwargs)
		self.data = kwargs

class DynMap:
	"""A DynMap instance."""
	def __init__(self,url,protocol="http"):
		self.baseurl="{}://{}/{{}}".format(protocol,url)
		self.version = self.get("version.js",True).text[21:-4]
		self.configlines = self.get("standalone/config.js?_="+self.version,True).text.split("\n")
		self.configlines = filter(None,[l.rstrip() for l in self.configlines])
		self.updateurl = self.configlines[3][14:-2]

	def get(self,method,raw=False,version=None,json=False):
		if raw:
			return requests.get(self.baseurl.format(method))
		if version is None:
			if not hasattr(self,"version"):
				raise Exception("Version is required for non-raw requests.")
			version = self.version
		r = self.get("up/{}?_={}".format(method,version),True)
		if json:
			return r.json()
		else:
			return r.text

	def getupdate(self,world,timestamp=None):
		if timestamp is None:
			timestamp = int(round(time.time()-0.5))
		return self.get(self.updateurl.format(world=world,timestamp=str(timestamp)),json=True)

	def players(self,world,timestamp=None):
		update = self.getupdate(world,timestamp)
		ret = []
		for player in update["players"]:
			ret.append(Player(**player))
		return ret
