# ubisoft-savegame-backups
automatically backup ubisoft savegames

# Warning
WIP

This is configured for Watch Dogs Legion, the game ID must be manually changed in the savegame directory if you want to get saves for other games.

If you leave this script running, it will continue backing up the same exact savegame state every 10 minutes until you stop it.\
One mistake = very messy


# Usage

[1] Double click

[2] Play

[3] CLOSE WHEN DONE PLAYING!

# Issues
Many.\
[1] timestamp zero-pad should apply to minutes as well\
[2] script WILL backup duplicate game files, it should only backup the savegame if it has changed\
[2] Backup files contains all root directories leading to save file, which is inconvenient
