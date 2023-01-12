import os
import csv

csvpath=os.join(".","Resources","budget_data.csv")
with open (csvpath) as csvfile:
    cvs_reader=csv.reader(csvfile,delimiter=".")
    cvs_header=next(cvsfile)
    
  


      
                