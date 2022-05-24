from unicodedata import name
import requests
import http.client
import json
import re

get="get_student_details"
rollno=input("Enter your rollno: ")
url="http://1.6.113.224/?action=" + get + "&rollno=" + rollno


response = requests.get(url)
parse_data = json.loads(response.text)

name = parse_data['data']['FirstName'] + " " + parse_data['data']['MiddleName']  + " " + parse_data['data']['LastName']
print("Name: " + name)
print("DOB: " + parse_data['data']['DOB'])
print("semester: " + parse_data['data']['Semester'])
print("Department: " + parse_data['data']['Department'])