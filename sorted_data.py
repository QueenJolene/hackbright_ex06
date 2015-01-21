"""
Your job is to write a program named 'sorted_data.py' 
that reads the file scores.txt, then spits out the ratings
in alphabetical order by restaurant.
"""

def split_file(file_name):

    scores_file = open(file_name, "r")
    score_dict ={}
    for line in scores_file:
        line = line.rstrip()
        score_split = line.split(":")
        score_dict[score_split[0]] = score_split[1]
    
    return score_dict

score_dict = split_file("scores.txt")
sorted_keys = sorted(score_dict)

for key in sorted_keys:
    print "Restaurant '%s' is rated at %s" % (key, score_dict[key])

# code review by cynthia
