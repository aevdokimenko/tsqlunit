import os
import string
import adodbapi
import unittest



_computername=r"(local)"
_database='Northwind'
_uid="sa"
_pwd=""
constr="Provider=SQLOLEDB.1; User ID=%s;Password=%s; Initial Catalog=%s; Data Source=%s" % (_uid,
                                                                                            _pwd,
                                                                                            _database,
                                                                                            _computername)

class TestInstallTSQLUnit(unittest.TestCase):
    def setUp(self):
        self.conn=adodbapi.connect(constr)
        self.crsr=self.conn.cursor()
        
        self.crsr.execute("select count(*) from sysobjects where xtype='P' and name LIKE 'ut[_]%' ")
        assert self.crsr.fetchone()[0]==0,"""Error when setting up testcases, old testcases in database.
        Please remove testcases starting with ut and underscore"""

    def testRemoveTSQLUnit(self):
        self.crsr.execute("select count(*) from sysobjects")
        row=self.crsr.fetchone()
        numberOfSysobjectsBeforeInstallation=row[0]
        
        self.installTSQLUnit()
        self.removeTSQLUnit()

        self.crsr.execute("select count(*) from sysobjects")
        row=self.crsr.fetchone()
        numberOfSysobjectsAfterRemoval=row[0]
        assert numberOfSysobjectsBeforeInstallation == numberOfSysobjectsAfterRemoval, \
              ' Nr before:%i, and after %i' %(numberOfSysobjectsBeforeInstallation,numberOfSysobjectsAfterRemoval)

    def testInstallTSQLUnit(self):
        self.installTSQLUnit()
        ok=1
        #The file hould only contain row with prompts (numbers and >:s)
        f=open("osqloutput.txt")
        s=f.read()
        rows=string.split(s,'>')
        for row in rows:
            row=string.strip(row) #remove whitespace
            for ch in row:
                if not(ch in string.digits):
                    ok=0
                    print "SQL MESSAGE:" + row
                    break
        assert ok, 'There were error messages from the database'

    def testOtherTestsOnNewlyInstalledTSQLunit(self):
        print "Running tests in the newly installed database:"
        self.installTSQLUnit()
        import test_tsqlunit
        othertests=unittest.TestLoader().loadTestsFromModule(test_tsqlunit)
        result=unittest.TextTestRunner().run(othertests)
        assert result.failures==[] , "The tests in test_tsqlunit returned %i failures" % len(result.failures)
        assert result.errors==[], "The tests in test_tsqlunit returned %i errors" % len(result.errors)
        print "Now continuing with the installation tests:"
        
    def installTSQLUnit(self):
        self.runSQLScript("tsqlunit.sql")
    def removeTSQLUnit(self):
        self.runSQLScript("removetsqlunit.sql")
       
    def runSQLScript(self,sqlFile):        
        cmdline= "osql -U %s -P %s -S %s -d %s -i %s -o osqloutput.txt" % ( _uid ,_pwd ,_computername, _database, sqlFile)
        os.system(cmdline)

    def tearDown(self):
        try:
            self.removeTSQLUnit()
            os.remove("osqloutput.txt")
        except:
            pass
        self.conn.rollback()
        self.conn.close()
        self.conn=None
        self.crsr=None


        

if __name__ == '__main__':

    unittest.main()