Slackey
=======

Upload lots of hockey logos to Slack.

1) Stash your logo files in a place under `logos/` (128x128, transparent PNG).

2) Generate and save a json manifest (`./generate_json.py logos/ncaa > logos/ncaa.json`)

3) Run `slackey.py --file logos/ncaa.json` or whatever your manifest was.
