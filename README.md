# dbcon - database configuration tool
dbcon is an alternative to 
[dbconfig-common](https://people.debian.org/~seanius/policy/dbconfig-common.html/). dbconfig-common is good, but I wasn't able to know how to use it on OS X or other platform, so I reivented it.

## Install

	pip install dbcon
	
## Usage
### Command line

Show databases and users

	dbcon.py status --dbms=postgres
	
apply configuration

	dbcon.py apply --dbms=postgres --database=myapp --user=myuser --password=mypassword
	
	dbconfigure apply --file myproject/settings.py

### Python API

	import dbconfigure
	
	
	dbconfigure.status(dbms='postgres')
	
	dbconfigure.apply(dbms='postgres',
	                  host='localhost',
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
 