# switch_magic
Set of Magic functions for conditional execution of cells in Jupyter notebooks.

## Switch magic commands

### skip_if
<pre>
  production = False
  exploration = True

  %%skip_if production
  print(42)
  42

  %%skip_if exploration
  print(42)
</pre>
skips cell execution if parameter condition is true.


### run_if
<pre>
  production = False
  exploration = True

  %%run_if production
  print(42)

  %%run_if exploration
  print(42)
  42
</pre>
runs cell only if parameter condition is true.


### time_if
<pre>
  production = False
  exploration = True

  %%time_if production
  print(42)
  42

  %%run_if exploration
  print(42)
  42
  Wall time: 1 ms
</pre>
time the cell only if parameter condition is true, otherwise simply execute.


## Using magic alias
<pre>
  switch_board = {
      'exploration': False,
      'production': True
  }

  %alias_magic production -p {switch_board['production']} run_if
  Created `%%production` as an alias for `%%run_if True`.

  %alias_magic exploration -p {switch_board['exploration']} run_if
  Created `%%exploration` as an alias for `%%run_if True`.

  %%production
  print(42)
  42

  %%exploration
  print(42)
</pre>


## Installation

Use:
`pip install switch_magic`
to install the magic command.

First load the magic in a cell:

`%load_ext switch_magic`

and then use the function in your cell to dpaste its content.

`%%skip_if`, `%%run_if` or `%%time_if`.


## TO DO

* add other conditional functions.
