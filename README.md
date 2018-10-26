# dynmapinfo

A Python library for interacting with the most popular DynMap plugin for Minecraft servers.

## Documentation

`class dynmap.DynMap(url,protocol)` - A DynMap instance. For protocol `protocol` and url `url`, this will use the DynMap instance at `{protocol}://{url}`.

`dynmap.DynMap.get(method,raw=False,version=None,json=False)` - Gets the `method` method. If `raw` is `True`, returns raw text. If `version` is supplied, overrides reported version of instance. If `json` is `True`, returns json-parsed output.

`dynmap.DynMap.getupdate(self,world,timestamp=None)` - Gets an update for world `world`. Automatically calculates timestamp if `timestamp` not supplied.

`dynmap.DynMap.players(self,world,timestamp=None)` - Lists the players in world `world`. Automatically calculates timestamp if `timestamp` not supplied.

To see an example of this library in use, see included `playerinfo.py` script.
