# ubisoft-savegame-backups
automatically backup ubisoft savegames

# Warning
WIP

This is configured for Watch Dogs Legion, the game ID must be manually changed in the savegame directory if you want to get saves for other games.

If you leave this script running, it will continue backing up the same exact savegame state every 10 minutes until you stop it.\
Forgetting to close = very messy


# Usage

[1] Double click

[2] Play

[3] CLOSE WHEN DONE PLAYING!

# Issues
Many.\
[1] timestamp zero-pad should apply to minutes as well.\
[2] Script WILL backup duplicate game files, it should only backup the savegame if it has changed.\
[3] Backup files contains all root directories leading to save file, which is inconvenient.\
[4] Script can't auto-set ubisoft ID if there are multiple to choose from. See [get_ubisoft_id() function](https://github.com/Deconkle/ubisoft-savegame-backups/blob/main/main.py#L6-L13).
