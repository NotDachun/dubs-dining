from  ph2 import ParseHub
import time
import csv
ph = ParseHub('tcKUBVECXT3u')

def writeDataToCSV(run, name):
    data = run.get_data()
    with open('testCreatedCSV' + name  + '.csv', 'w') as csvfile:
            fieldnames = ['Date', 'Time', 'Charge', 'RemainingBalance', 'Location']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for map in data['Transaction']:
                writer.writerow(map)

dataCollector = ph.projects[0]
run = dataCollector.run()
while run.check_available() == 0:
    print('Waiting')
    time.sleep(10)

if run.check_available() == 1:
    writeDataToCSV(run, 'Daniel')






    #with open('testCreatedCSV.csv') as csvfile:
     #   reader = csv.DictReader(csvfile)
      #  for row in reader:
       #     print(row['Date'], row['Charge'])
