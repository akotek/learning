# How to run new .sql script/s:

1. create timestamped up&down files (from migration ns):
  ```clojure
  (create-migration-files! "test-table")
  ```
  which builds 2x files:
  
	* (now()-test-table.up.sql) # create file
	* (now()-test-table.down.sql) # rollback file
  
> timestamps are important to avoid feature-branches-clashes (if yoav codes in branch X and shir in branch Y but merge later)

2. write your .sql script (specify 2x files)
3. push to git under /resources/migration
4. run okapi with "migration" or "rollback" args,
 ```
 java -server -jar ./okapi-standalone.jar ./okapi.edn ARGssSSSS
 ```

extra:

1. when performing more than 1x .sql command, use ```"--;;"``` as separator 
2. ```"SELECT * FROM ragtime_migrations ORDER BY created_at DESC limit =?"``` to print yourself last-n migrations performed
