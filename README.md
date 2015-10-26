# Overview
Allows quick iteration / experimentation on sqlalchemy operations to prove sqlalchemy behaves in a certain way.

Two tables in sql light (product, product_project) that have a relationship are setup. You can use sqlalchemy to do operations and see what behavior / results are.

# Setup (not tested - ideally write a make file that does this)
1. virtualenv venv
2. source venv/bin/activate
3. pip install -r requirements.txt

# Execute
- python test.py