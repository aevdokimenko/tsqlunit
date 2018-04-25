# Summary

TSQLUnit is a framework to write tests for applications written in Transact-SQL. It follows the tradition of the "xUnit" framework that is available for almost all programming languages.

## Installation
1. Unzip the file.Unzip the file. You can use winzip or the open source 7-zip. 
2. Connect to your database as dbo using the SQL Query Analyzer, execute the tsqlunit.sql file. 

## Remove
1. Connect to your database as dbo using the SQL Query Analyzer, execute the removetsqlunit.sql file.

## Original project
**Author**: [Henrik Ekelund](https://sourceforge.net/u/ekelund/profile/)  
**Project space at Sourceforge**: [TSQLUnit](https://sourceforge.net/projects/tsqlunit/)

## License
LGPL, see http://www.opensource.org/licenses/lgpl-license.php

## Release history
### Release 0.92
1. Adds Assert function

### Bug-fix release 0.91
Fixed bugs:
1. Fail Message Limitation	aevdokimenko	
2. Line 43 of proc tsu_error raises errors	aevdokimenko	
3. I can't install on DB with collation %_CS_%  (case sensitive)	
4. Test suite name is not displayed in output	
5. Mis-spelled Columns and SP Names	
6. Rollback transaction problem	
7. Return success or failure on x complete	

### Original release 0.9
