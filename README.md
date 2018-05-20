## How to read

use the command `man -l filename.1` to read a man page in the terminal. Use something like `env BROWSER=firefox man -H -l filename.1` to see that file in the browser. Note that aliases (`brp.1`, `brc.1`, etc...) will not display unless the man files are actually installed

TODO list

- `brl`
	- strat
	- fetch (get)
	- which
	- remove
	- rename
	- enable
	- disable
	- fix
	- ignore
	- unignore
	- alias
	- deref
	- update
	- report
- `init` - This name will conflict with the built in init command, maybe `bedrock_init`?
- `manage_tty_lock`? Unclear if this program is even used anymore
- Maybe use section 8 instead of 1 for commands that need root

[small man format reference](https://linux.die.net/man/7/man)
