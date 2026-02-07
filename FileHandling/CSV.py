import csv

with open("C://Users//Sujan Kumar Reddy//PycharmProjects//PythonAdvancedProgramming//Dataformats//data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#writing to the csv file
with open("C://Users//Sujan Kumar Reddy//PycharmProjects//PythonAdvancedProgramming//Dataformats//write.csv", "w", newline="" ) as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "marks"])
    writer.writerow([1, "Rahul", 85])
    writer.writerow([2, "Anita", 90])

# append ding the data to csv file
with open("C://Users//Sujan Kumar Reddy//PycharmProjects//PythonAdvancedProgramming//Dataformats//data.csv", "a",newline="") as file:
    writer = csv.writer(file)
    writer.writerow([3, "Kiran", 88])
