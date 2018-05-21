## How to read

use the command `man -l filename.1` to read a man page in the terminal. Use something like `env BROWSER=firefox man -H -l filename.1` to see that file in the browser. Note that aliases (`brp.1`, `brc.1`, etc...) will not display unless the man files are actually installed

## TODO list

- brpath -> cross
- brg/distros -> brl-fetch/distros
- no need to edit strata.conf
- brl which reads extended filesystem attrs
- user.bedrock.unignored attribute
- strat has -h/--help
- strat has -a for --arg0
- brl reenable
- brl version
- brl list has -a/--include-aliases, -h/--help
- brl list takes an optional category, one of enabled, disabled, unignored, ignored, aliases
- brl which takes -b/--bin, -f/--filepath, -p/--pid, -x/--xwindow, -h/--help
- brl which listings need --, also have -L/-R/-M
- brl remove, rename, reenable has -f/--force and -h/--help
- brl ignore, unignore, alias, deref, version, report has -h/--help
- brl status
- brl update has -m/--mirror, -f/--file, -s/--skip-check, -h/--help
- init uses the [init] section of bedrock.conf
- crossfs uses the [global] and [cross] sections of bedrock.conf
- crossfs format for .config-filesystem in /bedrock/cross
- email is danthau@bedrocklinux.org - put in BUGS sections
- Integrate man pages into website?

[small man format reference](https://linux.die.net/man/7/man)

another reference is in `info groff` -> section 4 -> section 4.1
