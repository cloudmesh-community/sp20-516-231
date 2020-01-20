Create a new virtual environment called ENV3

`python -m venv ENV3`

Activate it

`ENV3\Scripts\activate`

Install a package

`pip install numpy`

Test installation
```
python
>>> import numpy as np
>>> quit()
```
Deactivate the virtual environment

`deactivate`

Activate it again and verify that numpy is still there
```
ENV3\Scripts\activate
python
>>> import numpy as np
>>> quit()
```
