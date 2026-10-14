# The Tallyers: Rona Wassercug, Saxon Rassner and Marcos Lehman
from flask import Flask, render_template
import csv, random

app = Flask(__name__)     #create instance of class Flask

#reads occupations.csv and returns dictionary with pairs of job(str): percentage(float)
def read_csv(): 
    with open ("data/occupations.csv", "r") as file:
        reader = csv.DictReader(file)
        occupations_dict = {x['Job Class']:(float(x['Percentage']),x['Link']) for x in reader}
    return occupations_dict

#selects a random job from dictionary (not "total")
def random_job(occupations):
    rand_num = random.random() * occupations["Total"][0] #gets random num between 0 and total percentage
    per_sum = 0
    #loop find where rand_num falls if all the percentages were "lined up"
    for i, tup in enumerate(occupations.values()):
        per_sum += tup[0] 
        if per_sum > rand_num: 
            return list(occupations.keys())[i]


#tests random_job to make sure weighs are acurate
def percent_tester(occupation):
    tally = {}
    #tallies jobs choosen for 100000 tests
    for i in range(100000):
        job = random_job(occupations)  #replace with the random function your testing
        if job in tally:
            tally[job] += 1
        else:
            tally[job] = 1        
    tally["Total"] = 0
    #prints the percentage of the times it was chosen in tests and the given percentage
    for i in occupations.keys():
        print(i)
        print(occupations[i])
        if i in tally:
            percent = tally[i]/1000
            print(percent)
            tally["Total"] += percent
        else:
            print(0)
            
            
def make_link(link):
    return f'<a href="{link}">{link}</a>' # configures HTML to make link clickable
            

@app.route("/wdywtbwygu")
def get_job():
    occupations = read_csv()
    occupation_list = [[x, occupations[x][0], make_link(occupations[x][1])] for x in occupations.keys()][:-1]
    rand_job = random_job(occupations)
    return render_template('tablified.html', jobs = occupation_list,
                           job = rand_job, headers = ["Job Class", "Percentage of Workforce", "Link"] )


if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()
    