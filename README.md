# bbos

The Baseball on a Stick project

Developed by willkoky at sourceforge: https://sourceforge.net/projects/baseballonastic/

This is a forked version with minor bugfixes and tweaks from the 6.0 version.
These include:

-Unicode encoding bugfix  
-Added pitcher and batter ids to gameday.Pitches table


To initialize database follow instructions here:
https://sourceforge.net/p/baseballonastic/discussion/820145/thread/6c3b62ed/#b775

and run:
mysql -h localhost -P 3306 -u bbos -pbbos -e "source ../sql/createGamedaySchema.sql"

mysql -h localhost -P 3306 -u bbos -pbbos -e "source ../sql/retrosheet.sql"
