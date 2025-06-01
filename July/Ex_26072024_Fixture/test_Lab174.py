import csv
import pandas as pd

class Test_CRUD(object):
    def test_update_1(self):
        # Read the file
        with open('July/Ex_26072024_Fixture/userdata.csv',"r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row[0], row[1])

    def test_update_2(self):
        df = pd.read_csv('July/Ex_26072024_Fixture/userdata.csv')
        print(df)
        
