import csv 
import json 

def make_json(csvFilePath, jsonFilePath): 
   
  with open(csvFilePath, 'r', encoding='utf-8') as csvf, open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
    csvReader = csv.DictReader(csvf) 
    for row in csvReader:
      data = {}
      data = row
      jsonf.write("POST  http://localhost:9200/app/customers\n")
      jsonf.write(json.dumps(data, indent=4)+"\n") 
          
csvFilePath = r'customer_data.csv'
jsonFilePath = r'create_customer_record.json'

make_json(csvFilePath, jsonFilePath)