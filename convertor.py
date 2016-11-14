import csv
with open("Louis_Tomlinson.csv", "r") as infile, open("Louis_Tomlinson1.csv", "w") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    for row in reader:
        writer.writerow(item.replace(",", "") for item in row)
    for row in reader:
        writer.writerow(item.replace("?", "") for item in row)
    for row in reader:
        writer.writerow(item.replace("@", "") for item in row)
            
    # for row in reader:
    #     writer.writerow(  for item in row)



# Input : result.csv
# Output: output.csv
# Task: converted the improper csv file to a proper csv file by fixing the commas 
 
