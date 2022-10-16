# Module_3_python-challenge

- Assignment 3 for UMN Data Bootcamp: PyBank and PyPoll

For this assignment, I used the base python commands along with functions from the os and the csv modules, 
I also used the Counter() from the collections module.

For both PyBank and PyPoll, I read in the data with the csv.reader and used the csv.DictReader() to convert the csvfile into a dictionary. 
This stores each column as a seperate dictionary, the csv headers for each column is stored as the key for each column and 
the rest of the rows as the values.

For both PyBank and PyPoll, I approached the next part of the script in a similar manner. I created empty lists to hold each column of the data and 
I used a for loop to append the values into the lists. I then used these lists for each of the calculations that the assignment required. 

For the PyRoll script, I used the Counter function to count the unique values in the candidate column, this was an easy function to use
but required a few additional steps to extract the keys and values as variables to use to print out the results both to the terminal and the txtfile.

In order to just code the results just one time, I saved the f-strings as a tuple, which I then used to both 
print out the results to the terminal and the txtfile.
