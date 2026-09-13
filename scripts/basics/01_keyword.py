"""
Module: script_02
Description: List all the available python keywords to the console.
Functions:
- help: Provides information about Python built-in functions.
Example:
  help(keyword)
"""

import keyword

print("Python keywords:", keyword.kwlist)
print("Keywords length:", len(keyword.kwlist))
