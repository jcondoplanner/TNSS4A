import csv

# Define the chunk size
chunk_size = 10000

# Read and write the file in chunks
with open('vwCollision.txt', 'r', encoding='latin-1') as txt_file, open('output3.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    while True:
        lines = txt_file.readlines(chunk_size)
        if not lines:
            break
        for line in lines:
            writer.writerow(line.strip().split('|'))
