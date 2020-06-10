import sys
import os
import click
from core import commands as clients_commands


def clear(): return os.system('cls')

if __name__ == "__main__":
    clear()
print("""
       _         _
      (_)       | |
  ___  _  _ __  | |__    ___  _ __
 / __|| || '_ \ | '_ \  / _ \| '__|
| (__ | || |_) || | | ||  __/| |
 \___||_|| .__/ |_| |_| \___||_|
         | |
         |_|
    """)
clients_commands.cli()
