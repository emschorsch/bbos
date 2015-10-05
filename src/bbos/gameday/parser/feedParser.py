from bbos.gameday.parser.parser import Parser
from bbos.config.gamedayConfig import GamedayConfig
from regularExpressions import pattern
import json

class FeedParser(Parser):

    def parse(self, xmlProvider):
        gamePK = self.game.getGameInfo()['game_pk']
        if gamePK is None:
            return

        jsonContent = xmlProvider.getFeedJSON(gamePK)
        if "404 Not Found" in jsonContent: return

        jsonHash = json.loads(jsonContent)
        if not jsonHash: return

        #for item in jsonHash['items'][46]['data']:
        #print jsonHash['items'][46]['id']
        #for item in jsonHash['items'][46]:
        #    print item
        #    print jsonHash['items'][46][item]

        if not 'items' in jsonHash: return

        plays = [item['data'] for item in jsonHash['items'] if 'data' in item and 'scoring' in item['data'] and ' mph' in item['data']['description']]

        for play in plays:
            #print play

            play['mph'] = pattern.capture("""\s(\d\d+)\smph""", play['description'])
            play['distance'] = pattern.capture("""\s(\d\d+)\sfeet""", play['description'])

        filteredPlays = self.mapJsonList(plays, GamedayConfig.parser_feed_plays)

        self.game.setFeedPlays(filteredPlays)

