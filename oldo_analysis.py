golfcoursedata = {'hole1':[],'hole2':[],'hole3':[],'hole4':[],'hole5':[],'hole6':[],'hole7':[],'hole8':[],'hole9':[],'hole10':[],'hole11':[],'hole12':[],'hole13':[],'hole14':[],'hole15':[],'hole16':[],'hole17':[],'hole18':[]}
#scorelist = [4,5,3,4,4,4,4,3,4,5,4,3,4,4,4,5,3,4] #in the future, allow the user to input scores
scorelist = [6,6,4,4,5,4,8,5,5,6,6,5,4,4,6,7,4,4]
parlist = [4,5,3,4,4,4,4,3,4,5,4,3,4,4,4,5,3,4] #list of par score for all 18 holes on the golf course
#scorelist = []
#score_hole1 = int(input("Enter score for hole 1:"))#Is there a way to loop through this?
#scorelist.append(score_hole1)
#score_hole2 = int(input("Enter score for hole 2:"))
#scorelist.append(score_hole2)
#score_hole3 = int(input("Enter score for hole 3:"))
#scorelist.append(score_hole3)
#score_hole4 = int(input("Enter score for hole 4:"))
#scorelist.append(score_hole4)
#score_hole5 = int(input("Enter score for hole 5:"))
#scorelist.append(score_hole5)
#score_hole6 = int(input("Enter score for hole 6:"))
#scorelist.append(score_hole6)
#score_hole7 = int(input("Enter score for hole 7:"))
#scorelist.append(score_hole7)
#score_hole8 = int(input("Enter score for hole 8:"))
#scorelist.append(score_hole8)
#score_hole9 = int(input("Enter score for hole 9:"))
#scorelist.append(score_hole9)
#score_hole10 = int(input("Enter score for hole 10:"))
#scorelist.append(score_hole10)
#score_hole11 = int(input("Enter score for hole 11:"))
#scorelist.append(score_hole11)
#score_hole12 = int(input("Enter score for hole 12:"))
#scorelist.append(score_hole12)
#score_hole13 = int(input("Enter score for hole 13:"))
#scorelist.append(score_hole13)
#score_hole14 = int(input("Enter score for hole 14:"))
#scorelist.append(score_hole14)
#score_hole15 = int(input("Enter score for hole 15:"))
#scorelist.append(score_hole15)
#score_hole16 = int(input("Enter score for hole 16:"))
#scorelist.append(score_hole16)
#score_hole17 = int(input("Enter score for hole 17:"))
#scorelist.append(score_hole17)
#score_hole18 = int(input("Enter score for hole 18:"))
#scorelist.append(score_hole18)
for hole in list(golfcoursedata.keys()):
    golfcoursedata[hole].append(scorelist[list(golfcoursedata.keys()).index(hole)]) #appends the score for the nth hole on the golfcourse to the list of lists golfcoursedata.values()
def indexfinder(listx,item):
	return [i for i,x in enumerate(listx) if x == item]
avgstroke_parlist = [] #define the list that details the user's average number of strokes abover or below par

#---RETURN TO USER AVERAGE NUMBER OF STROKES ABOVE OR BELOW PAR FOR EACH HOLE ON THE GOLF COURSE---
for score in list(golfcoursedata.values()): #for all lists of recorded scores for each hole on the golf course
    x = sum(score)/len(score) #average the recorded scores for each hole
    if len(indexfinder(list(golfcoursedata.values()),score)) == 1: #if no two lists of recorded scores for each hole are the same
        if x > parlist[list(golfcoursedata.values()).index(score)]: #if the average score is greater than par for this hole
            print("You average " + str(x - parlist[golfcoursedata.values().index(score)]) + " strokes above par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.')
            avgstroke_parlist.append(x - parlist[golfcoursedata.values().index(score)])
        if x < parlist[list(golfcoursedata.values()).index(score)]:
            print("You average " + str(parlist[golfcoursedata.values().index(score)] - x) + " strokes below par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.')
            avgstroke_parlist.append(x - parlist[golfcoursedata.values().index(score)])
        else:
            print ("You average even par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.')
            avgstroke_parlist.append(0)

    elif len(indexfinder(list(golfcoursedata.values()),score)) > 1: # if two or more lists of recorded scores for each hole are the same
    	count = 0
    	for index in indexfinder(list(golfcoursedata.values()),score): #run through the list of indexes in golfcoursedata.values() lists with matching lists 
    		if count == 0: #if the list is the first matching list to appear in golfcoursedata.values()
    		 	if x > parlist[list(golfcoursedata.values()).index(score)]:
                            print("You average " + str(x - parlist[list(golfcoursedata.values()).index(score)]) + " strokes above par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.')
                            avgstroke_parlist.append(x - parlist[list(golfcoursedata.values()).index(score)])
    		 	if x < parlist[list(golfcoursedata.values()).index(score)]:
                            print("You average " + str(parlist[list(golfcoursedata.values()).index(score)] - x) + " strokes below par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.')
                            avgstroke_parlist.append(x - parlist[list(golfcoursedata.values()).index(score)])
    		 	else:
                            print ("You average even par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.')
                            avgstroke_parlist.append(0)

    		else: #if the list is NOT the first matching list to apper in golfcoursedata.values()
    			if x > parlist[(indexfinder(list(golfcoursedata.values()),score)[count])]:
                            print("You average " + str(x - parlist[indexfinder(list(golfcoursedata.values()),score)[count]]) + " strokes above par on hole " + str(indexfinder(list(golfcoursedata.values()),score)[count] + 1) + '.')
                            avgstroke_parlist.append(x - parlist[indexfinder(list(golfcoursedata.values()),score)[count]])
    			if x < parlist[(indexfinder(list(golfcoursedata.values()),score)[count])]:
                            print ("You average " + str(parlist[indexfinder(list(golfcoursedata.values()),score)[count]] - x) + " strokes below par on hole " + str(indexfinder(list(golfcoursedata.values()),score)[count] + 1) + '.')
                            avgstroke_parlist.append(x - parlist[indexfinder(list(golfcoursedata.values(),score))[count]])
    			else:
                            print ("You average even par on hole " + str(indexfinder(list(golfcoursedata.values()),score)[count] + 1)  + '.')
                            avgstroke_parlist.append(0)

    		count +=1

#RETURN TO USER BEST HOLES ON THE COURSE BASED OFF OF AVERAGE STROKES ABOVER OR BELOW PAR NEED TO MAKE AVGSTROKE_PARLIST A DICTIONARY SO KEYS WILL FOLLOW VALUES
    
















                  




