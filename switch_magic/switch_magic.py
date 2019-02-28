# switch set of magic commands
#
# February 2019
#
# Originally from:
# https://stackoverflow.com/questions/26494747/simple-way-to-choose-which-cells-to-run-in-ipython-notebook-during-run-all
# By: Robbe
#
"""
Magic functions that run or skip cell execution based on the condition on the line.

Put on first line of cell to control execution.

    %%skip_if True
    print(42)

always skips cell execution.

    %%skip_if $skip_flags['steptype']
    print(42)

evaluates `skip_flags` value as the skip condition for running the cell.

    %%run_if True
    print(42)

runs cell.

    %%run_if $run_flags['steptype']
    print(42)

evaluates `run_flags` value as the run condition for the cellself.

    %%time_if $run_flags['steptype']
    print(42)

evaluate `run_flags` value to decide to %%time the cell or go for execution.
"""

__version__ = '0.1.0'


def skip_if(line, cell):
    '''Skips execution of the current line/cell if line evaluates to True.'''
    if eval(line):
        return
    get_ipython().ex(cell)


def run_if(line, cell):
    '''Runs cell if line evaluates to True.'''
    if not eval(line):
        return
    get_ipython().ex(cell)


def time_if(line, cell):
    '''Runs cell if line evaluates to True.'''
    if eval(line):
        get_ipython().magics_manager.magics['cell']['time'](cell=cell)
    else:
        get_ipython().ex(cell)


def load_ipython_extension(shell):
    '''Registers the switch magics when the extension loads.'''
    shell.register_magic_function(skip_if, 'cell')
    shell.register_magic_function(run_if, 'cell')
    shell.register_magic_function(time_if, 'cell')


def unload_ipython_extension(shell):
    '''Unregisters the switch magics when the extension unloads.'''
    del shell.magics_manager.magics['cell']['skip_if']
    del shell.magics_manager.magics['cell']['run_if']
    del shell.magics_manager.magics['cell']['time_if']
