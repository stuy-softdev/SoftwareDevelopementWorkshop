"""
1. Read through the file using csv.DictReader to create a dictionary
2. Generate a random job
    a. Generate a random number from 0 to 99.8 (total percentage).
    b. Enumerate through the dictionary and add the percentage of each key to a total sum variable.
    c. Compare percentage sum to the random percentage: If percentage sum is greater, return the current job. Otherwise continue.
    d. Every job has an interval of size x (where x is the key value) out of 99.8 (basically percentage) that the random number could be in.
3. Percentage tester: Create a new dictionary that shows how often each job occurs compared to its actual percent in occupations.csv.
    a. We generated a random  job 100,000 times and tallied how often each job occured
    b. Each key is printed with its actual value from occupations and its value in the tally dictionary divided by 1,000 (100,000/1000 = 100)
"""

from flask import Flask
import csv, random

app = Flask(__name__)     #create instance of class Flask




def read_csv():
    with open ("occupations.csv", "r") as file:
        reader = csv.DictReader(file)
        occupations_dict = {x['Job Class']:float(x['Percentage']) for x in reader}
    return occupations_dict


def random_job(occupations):
    rand_num = random.random() * occupations["Total"]
    per_sum = 0
    for i, per in enumerate(occupations.values()):
        per_sum += per
        if per_sum > rand_num:
            return list(occupations.keys())[i]



def percent_tester(occupation):
    tally = {}
    for i in range(100000):
        job = random_job(occupations)  #replace with the random function your testing
        if job in tally:
            tally[job] += 1
        else:
            tally[job] = 1        
    tally["Total"] = 0
    for i in occupations.keys():
        print(i)
        print(occupations[i])
        if i in tally:
            percent = tally[i]/1000
            print(percent)
            tally["Total"] += percent
        else:
            print(0)

@app.route("/")            #assign fxn to route
def get_job():
    #print(__name__)
    occupations = read_csv()
    occupation_list = "<br>"
    for occupation in occupations.keys():
        if occupation != "Total":
            occupation_list += occupation + "<br>"
        
    text = f'''
<b> The Tallyers: Saxon and Rona </b>
<br>
All Occupations: {occupation_list}
<br>
<b> Random Job </b>: {random_job(occupations)}
'''
    return text

  
if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()
    