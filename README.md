# dbcon - database configuration tool
dbcon is an alternative to 
[dbconfig-common](https://people.debian.org/~seanius/policy/dbconfig-common.html/). dbconfig-common is good, but I wasn't able to know how to use it on OS X or other platform, so I reivented it.

## Install

	pip install dbcon
	
## Usage
### Command line

Show databases and users

	dbcon status postgres
	
configure

	dbcon configure mydbconfig.yml
	dbcon configure myproject/settings.py --format django

### Sample configuration file
sample.yml

	dbms: postgres
	database: myapp
	user: myuser
	password: mypassword

### Python API

	import dbcon
	
	
	dbcon.status(dbms='postgres')
	
	dbcon.configure(dbms='postgres',
	                database='myapp',
	                user='myuser',
	                password='mypassword')
	
### Supported configuration file format

 * YAML
 * JSON
 * Django settings.py
 
### Supported DBMS
 * PostgreSQL
 * MySQL (not yet)

### Supported OS
 * OS X
 * Linux (not yet)
 
 
### TODO
 * support python 2.x
 * support linux
 * support mysql
 * support rails
 * fake option
 * confirm when drop
 * interactive interface