import xml.etree.ElementTree as ET
import csv
import os

junit_path = 'test-results/junit.xml'
csv_path = 'test-results/result.csv'

if os.path.exists(junit_path):
    tree = ET.parse(junit_path)
    root = tree.getroot()

    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Test Name', 'Status', 'Time'])

        for testcase in root.iter('testcase'):
            name = testcase.get('name')
            time = testcase.get('time')
            status = 'passed'
            if testcase.find('failure') is not None:
                status = 'failed'
            elif testcase.find('error') is not None:
                status = 'error'
            elif testcase.find('skipped') is not None:
                status = 'skipped'
            writer.writerow([name, status, time])
else:
    print(f"{junit_path} not found.")
