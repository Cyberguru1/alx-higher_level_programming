# 0x02. Python - import & modules
## Modules

> A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__.
## Command Line Arguments

## Common utility scripts often need to process
> command line arguments. These arguments are stored in the sys module’s argv attribute as a list. For instance the following output results from running python demo.py one two three at the command line:

```
import sys 
print(sys.argv)
['demo.py', 'one', 'two', 'three']
```
> The argparse module provides a more sophisticated mechanism to process command line arguments. The following script extracts one or more filenames and an optional number of lines to be displayed: