## How to read

use the command `man -l filename.1` to read a man page in the terminal. Use something like `env BROWSER=firefox man -H -l filename.1` to see that file in the browser. Note that aliases (`brp.1`, `brc.1`, etc...) will not display unless the man files are actually installed

## TODO list

- `manage_tty_lock`? Unclear if this program is even used anymore
- Maybe use section 8 instead of 1 for commands that need root
- Crosslinking in generated html files

[small man format reference](https://linux.die.net/man/7/man)

another reference is in `info groff` -> section 4 -> section 4.1
