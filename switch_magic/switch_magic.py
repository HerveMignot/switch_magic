# skip magic command
#
# November 2018
#
# Originally from:
# https://stackoverflow.com/questions/26494747/simple-way-to-choose-which-cells-to-run-in-ipython-notebook-during-run-all
# By: Robbe
#
"""
Magic function that skip cell execution based on the condition on the line.

Place on first line of cell to control execution.

    %skip True
    print(42)

skips cell execution.

    %skip $run_flags['steptype'] is False
    print(42)

to evaluate `run_flags` variable as skip condition.
"""

__version__ = '0.1.0'


def skip(line, cell=None):
    '''Skips execution of the current line/cell if line evaluates to True.'''
    if eval(line):
        return
    get_ipython().ex(cell)

def load_ipython_extension(shell):
    '''Registers the skip magic when the extension loads.'''
    shell.register_magic_function(skip, 'line_cell')

def unload_ipython_extension(shell):
    '''Unregisters the skip magic when the extension unloads.'''
    del shell.magics_manager.magics['cell']['skip']
