## To run tests, use the following code:

```
pip install coverage
pip install pytest

# If you are not already in the Tests directory, run the following, otherwise skip to the next step.
cd Tests\ 

coverage run -m pytest test_filename.py
```

In case you want to run all the tests together, run the following 

```
coverage run -m pytest
```