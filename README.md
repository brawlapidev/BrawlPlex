# BrawlPlex
BrawlPlex is a tool for quickly and easaly using Brawl Stars API. Before using this package learn how Brawl Stars API works. Do not edit _config variables, thay contain parts of the API endpoints.
## Moduals
### Player
Has two functions "get_player_info" and "get_player_battlelog". Boath function take two arguments firstly the target accoun tag (without #) and your Brawl Stars API key. You can load your API key from a text file by using "BrawlPlex.get_API_key(file_path)".
### Clubs
Has two functions "get_club_info" and "get_club_members". Boath take two arguments club tag (without #) and secondly your API key.
### Brawlers
Has two functions "get_brawler_list". It takes only your API key. The other function is "get_brawler_info". It takes brawler tag and your API key.
### Events
Has only one function "get_event_list". It takes only the API key.
### Rankings
Has 5 functions.
1. "get_player_rankings" it takes 5 arguments county code (or global), limit (limits the number of items returned), return before and after (obtained from previus response), your API key.
2. "get_club_rankings" it takes 5 arguments county code (or global), limit (limits the number of items returned), return before and after (obtained from previus response), your API key.
3. "get_brawler_rankings" it takes 6 arguments county code (or global), limit (limits the number of items returned), brawler tag, return before and after (obtained from previus response), your API key.
4. "get_powerplay_seasons" it takes 5 arguments county code (or global), limit (limits the number of items returned), return before and after (obtained from previus response), your API key.
5. "get_powerplay_season_rankings" it takes 6 arguments county code (or global), county spasific season id, limit (limits the number of items returned), return before and after (obtained from previus response), your API key.