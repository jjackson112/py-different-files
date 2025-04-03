import json
show_data = []
#open txt file in read mode, call the variable to hold the file text_file
with open("television_shows.txt", "r") as text_file:
#write a for loop to search for each line in the text_file variable
  for line in text_file:
    show_data.append(line)

#write a second with statement to open a file called best_shows.json in write mode
with open("best_shows.json", "w") as write_file:
  json.dump(show_data, write_file)