## Update CSV to give the filenames as part of the final column description
## to make manual updates of GeoServer and MapStore easier.
## The filename can be easily removed by splitting on the first whitespace.
import csv

# Read the CSV file
with open('vector_layers_manual.csv', 'r', newline='') as infile:
    reader = csv.reader(infile)
    data = list(reader)

# Process the data
for row in data:
    new_string = f"{row[0]}__{row[1]}"
    if row[-1].startswith('SF ') or row[-1].startswith('RF '):
        row[-1] = row[-1][3:]  # remove SF/RF
    row[-1] = f"{new_string} {row[-1]}"

# Write the modified data to a new CSV file
with open('vector_layers_manual2.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)
