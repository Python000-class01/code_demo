#!/bin/bash
# database
flask-sqlacodegen 'mysql+pymysql://root:rootroot@localhost/db1' \
--outfile db.py --flask


#table
flask-sqlacodegen 'mysql+pymysql://root:rootroot@localhost/db1' \
--table users \
--outfile users.py --flask
