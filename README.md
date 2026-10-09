# shardovyrrix 1.0.0

Original offline fullscreen paddle-and-brick game. Break every row to advance through levels. Three lives; losing a ball resets its launch. Space launches, A/D or arrows move the paddle, P pauses, R resets the session, Q quits. Session-only scores, no saving or accounts.

Python3+curses standard library, color blocks and monochrome fallback. Minimum60x24; gameplay pauses below that size. No pip packages, network or commercial game assets. Install checks source/dependencies, no automatic package install.

    bash app-store.sh install
    bash app-store.sh run
    python3 -m unittest -v

Six core tests, fullscreen gameplay/resize/exit/terminal restoration and actual pixels checked on Linux. Physical Raspberry Pi and non-Linux untested. MIT license.
