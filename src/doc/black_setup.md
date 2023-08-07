# Setting up black - "the uncompromising code formatter"

[black](https://black.readthedocs.io/en/stable/index.html) is an opinionated
Python code formatter that follows a strict subset of PEP-8. The coding 
style it adheres to does not allow a lot of configuration (which is 
on purpose).

To quote black's documentation:
> By using Black, you agree to cede control over minutiae of hand-formatting.
> In return, Black gives you speed, determinism, and freedom from pycodestyle 
> nagging about formatting. You will save time and mental energy for more
> important matters.

> Black makes code review faster by producing the smallest diffs possible.
> Blackened code looks the same regardless of the project you’re reading. 
> Formatting becomes transparent after a while and you can focus on the 
> content instead.

This document describes the solution for running a black daemon 
([blackd](https://black.readthedocs.io/en/stable/blackd.html)) on your 
development machine and connecting it to PyCharm, so that any Python file is 
reformatted on every save.

The document also gives some tips on day-to-day black usage.

## Setting up black on your development machine

1. Install black using pip (already done for Car Repair Shop):
   ```bash
   pip install black
   pip install 'black[d]'
   ```
2. Install black in your Poetry virtual environment as a development 
   dependency (already done for Car Repair Shop):
   ```bash
   poetry add black[d] -D
   ```
3. Install **BlackConnect** plugin for PyCharm.
4. Configure BlackConnect plugin in PyCharm:
   
   - Check `Trigger when saving changed files`.
   - Set `Line length` to 80.
   - Click on `Check connection` button to verify everything is working.
   
That should be it.