#read the data from the csv file
filename = '/Users/jefferykerby/Documents/Old Overton Scorecard.csv'
#specify the list of color tees at Old Overton Country Club
colorlist = ['Blue','Black','White','Gold','Red']
tiger_list = []
	
with open(filename,'r') as file_object:
	lines = file_object.readlines()
	for line in lines:
		if 'Blue' in line:
			partition = 'Blue'
			indexfinder = line.index(partition[0])
			real_index = indexfinder + (len(partition)+1)
			data_line = line[real_index:]
		elif 'Black' in line:
			partition = 'Black'
			indexfinder = line.index(partition[0])
			real_index = indexfinder + (len(partition)+1)
			data_line = line[real_index:]
		elif 'White' in line:
			partition = 'White'
			indexfinder = line.index(partition[4])
			real_index = indexfinder + (len(partition)-3)
			data_line = line[real_index:]
		elif 'Gold' in line:
			partition = 'Gold'
			indexfinder = line.index(partition[0])
			real_index = indexfinder + (len(partition)+1)
			data_line = line[real_index:]
		elif 'Red' in line:
			partition = 'Red'
			indexfinder = line.index(partition[0])
			real_index = indexfinder + (len(partition)+1)
			data_line = line[real_index:]
		else:
			partition = "None"
		if partition in colorlist:
			element_finder = []
			line_list = []
			for i,x in enumerate(data_line):
				if x == ",":
					element_finder.append(i)
			for i in list(range(0,35)):
				if i not in element_finder:
					line_list.append(int(data_line[i]))
			tiger_list.append(line_list)

golfcoursedata = {'hole 1':[],'hole 2':[],'hole 3':[],'hole 4':[],'hole 5':[],'hole 6':[],'hole 7':[],'hole 8':[],'hole 9':[],'hole 10':[],'hole 11':[],'hole 12':[],'hole 13':[],'hole 14':[],'hole 15':[],'hole 16':[],'hole 17':[],'hole 18':[]}
hole_in_1_dict = {'hole 1':[],'hole 2':[],'hole 3':[],'hole 4':[],'hole 5':[],'hole 6':[],'hole 7':[],'hole 8':[],'hole 9':[],'hole 10':[],'hole 11':[],'hole 12':[],'hole 13':[],'hole 14':[],'hole 15':[],'hole 16':[],'hole 17':[],'hole 18':[]}
double_eagle_dict = {'hole 1':[],'hole 2':[],'hole 3':[],'hole 4':[],'hole 5':[],'hole 6':[],'hole 7':[],'hole 8':[],'hole 9':[],'hole 10':[],'hole 11':[],'hole 12':[],'hole 13':[],'hole 14':[],'hole 15':[],'hole 16':[],'hole 17':[],'hole 18':[]}
eagle_dict = {'hole 1':[],'hole 2':[],'hole 3':[],'hole 4':[],'hole 5':[],'hole 6':[],'hole 7':[],'hole 8':[],'hole 9':[],'hole 10':[],'hole 11':[],'hole 12':[],'hole 13':[],'hole 14':[],'hole 15':[],'hole 16':[],'hole 17':[],'hole 18':[]}
birdie_dict = {'hole 1':[],'hole 2':[],'hole 3':[],'hole 4':[],'hole 5':[],'hole 6':[],'hole 7':[],'hole 8':[],'hole 9':[],'hole 10':[],'hole 11':[],'hole 12':[],'hole 13':[],'hole 14':[],'hole 15':[],'hole 16':[],'hole 17':[],'hole 18':[]}
par_dict = {'hole 1':[],'hole 2':[],'hole 3':[],'hole 4':[],'hole 5':[],'hole 6':[],'hole 7':[],'hole 8':[],'hole 9':[],'hole 10':[],'hole 11':[],'hole 12':[],'hole 13':[],'hole 14':[],'hole 15':[],'hole 16':[],'hole 17':[],'hole 18':[]}
bogey_dict = {'hole 1':[],'hole 2':[],'hole 3':[],'hole 4':[],'hole 5':[],'hole 6':[],'hole 7':[],'hole 8':[],'hole 9':[],'hole 10':[],'hole 11':[],'hole 12':[],'hole 13':[],'hole 14':[],'hole 15':[],'hole 16':[],'hole 17':[],'hole 18':[]}
double_dict = {'hole 1':[],'hole 2':[],'hole 3':[],'hole 4':[],'hole 5':[],'hole 6':[],'hole 7':[],'hole 8':[],'hole 9':[],'hole 10':[],'hole 11':[],'hole 12':[],'hole 13':[],'hole 14':[],'hole 15':[],'hole 16':[],'hole 17':[],'hole 18':[]}
triple_dict = {'hole 1':[],'hole 2':[],'hole 3':[],'hole 4':[],'hole 5':[],'hole 6':[],'hole 7':[],'hole 8':[],'hole 9':[],'hole 10':[],'hole 11':[],'hole 12':[],'hole 13':[],'hole 14':[],'hole 15':[],'hole 16':[],'hole 17':[],'hole 18':[]}
max_dict = {'hole 1':[],'hole 2':[],'hole 3':[],'hole 4':[],'hole 5':[],'hole 6':[],'hole 7':[],'hole 8':[],'hole 9':[],'hole 10':[],'hole 11':[],'hole 12':[],'hole 13':[],'hole 14':[],'hole 15':[],'hole 16':[],'hole 17':[],'hole 18':[]}
parlist = [4,5,3,4,4,4,4,3,4,5,4,3,4,4,4,5,3,4] #list of par score for all 18 holes on the golf course
snowmantick_list =[]
snowmancounter = 0
for posting in tiger_list:
	for hole in golfcoursedata.keys(): 
			golfcoursedata[hole].append(posting[list(golfcoursedata.keys()).index(hole)])

for hole, value in golfcoursedata.items():
	for score in value:
		z = score - parlist[list(golfcoursedata.keys()).index(hole)]
	
		if z == -3:
			if parlist[list(golfcoursedata.keys()).index(hole)] == 4:
		 		hole_in_1_dict[hole].append(1)
			if parlist[list(golfcoursedata.keys()).index(hole)] == 5:
				double_eagle_dict[hole].append(1)
		if z == -2:
			if parlist[list(golfcoursedata.keys()).index(hole)] == 4 or 5:
				eagle_dict[hole].append(1)
			if parlist[list(golfcoursedata.keys()).index(hole)] == 3:
				hole_in_1_dict[hole].append(1)
		if z == -1:
			birdie_dict[hole].append(1)
		if z == 0:
			par_dict[hole].append(1)
		if z == 1:
			bogey_dict[hole].append(1)
		if z == 2:
			double_dict[hole].append(1)
		if z == 3:
			triple_dict[hole].append(1)
		if z >= 4:
			max_dict[hole].append(1)

avgstroke_parlist = [] #define the list that details the user's average number of strokes abover or below par
matching_score_dict = {}
print()
print("**********RESULTS**********")
print()
def duplicateremove(listx):
	blanklist = []
	for i in listx:
		if i not in blanklist:
			blanklist.append(i)
	return blanklist
for i in duplicateremove(list(golfcoursedata.values())):
	matching_score_dict[str(i)] = 0
def indexfinder(listx,item):
	return [i for i,x in enumerate(listx) if x == item]
#---RETURN AVERAGE NUMBER OF STROKES ABOVE OR BELOW PAR FOR EACH HOLE ON THE GOLF COURSE FOR THE USER---

for score in list(golfcoursedata.values()): 
	x = sum(score)/len(score)
	if len(indexfinder(list(golfcoursedata.values()),score)) == 1:
		if x > parlist[list(golfcoursedata.values()).index(score)]:
			if x - parlist[list(golfcoursedata.values()).index(score)] == 1:
				print("You average " + str(x - parlist[list(golfcoursedata.values()).index(score)]) + " stroke above par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.')
			else:
				print("You average " + str(x - parlist[list(golfcoursedata.values()).index(score)]) + " strokes above par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.')
			avgstroke_parlist.append(x - parlist[list(golfcoursedata.values()).index(score)])
		if x < parlist[list(golfcoursedata.values()).index(score)]:
			if parlist[list(golfcoursedata.values()).index(score)] - x == 1:
				 print("You average " + str(parlist[list(golfcoursedata.values()).index(score)] - x) + " stroke above par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.')
			else:
				print("You average " + str(parlist[list(golfcoursedata.values()).index(score)] - x) + " strokes below par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.')
			avgstroke_parlist.append(x - parlist[list(golfcoursedata.values()).index(score)])
		if x == parlist[list(golfcoursedata.values()).index(score)]:
			print ("You average even par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.')
			avgstroke_parlist.append(0)
	elif len(indexfinder(list(golfcoursedata.values()),score)) > 1: #<---- focus on this piece of code
		scorematch_index = indexfinder(list(golfcoursedata.values()),score)
		if matching_score_dict[str(score)] == 0: #<--- score is currently a list
			if x > parlist[list(golfcoursedata.values()).index(score)]:
				if x - parlist[list(golfcoursedata.values()).index(score)] == 1:
					print("You average " + str(x - parlist[list(golfcoursedata.values()).index(score)]) + " stroke above par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.')
				else:
					print("You average " + str(x - parlist[list(golfcoursedata.values()).index(score)]) + " strokes above par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.')
				avgstroke_parlist.append(x - parlist[list(golfcoursedata.values()).index(score)])
			if x < parlist[list(golfcoursedata.values()).index(score)]:
				if parlist[list(golfcoursedata.values()).index(score)] - x == 1:
					print("You average " + str(parlist[list(golfcoursedata.values()).index(score)] - x) + " stroke below par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.')
				else:
					print("You average " + str(parlist[list(golfcoursedata.values()).index(score)] - x) + " strokes below par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.')
				avgstroke_parlist.append(x - parlist[list(golfcoursedata.values()).index(score)])
			if x == parlist[list(golfcoursedata.values()).index(score)]:
				print ("You average even par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.')
				avgstroke_parlist.append(0)
		if matching_score_dict[str(score)] > 0:
			if x > parlist[(indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]])]:
				if x - parlist[indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]]] == 1:
					print("You average " + str(x - parlist[indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]]]) + " stroke above par on hole " + str(indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]] + 1) + '.')
				else:
					print("You average " + str(x - parlist[indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]]]) + " strokes above par on hole " + str(indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]] + 1) + '.')
				avgstroke_parlist.append(x - parlist[indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]]])
			if x < parlist[(indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]])]:
				if parlist[indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]]] - x == 1:
					print ("You average " + str(parlist[indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]]] - x) + " stroke below par on hole " + str(indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]] + 1) + '.')
				else:
					print ("You average " + str(parlist[indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]]] - x) + " strokes below par on hole " + str(indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]] + 1) + '.')
				avgstroke_parlist.append(x - parlist[indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]]])
			if x == parlist[(indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]])]:
				print ("You average even par on hole " + str(indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]] + 1)  + '.')
				avgstroke_parlist.append(0)
		matching_score_dict[str(score)] += 1
	if score == 8:
		snowmancounter +=1
snowmantick_list.append(snowmancounter)

print()
#---DISPLAY BEST AND WORST 3 HOLES ON GOLF COURSE FOR USER BASED ON AVERAGE STROKES ABOVER OR BELOW PAR---
def tiefinder(listx):
	tiefinder_set = set(listx)
	contains_tie = len(listx) != len(tiefinder_set)
	return contains_tie
def min_2nd(listx):
	return sorted(set(listx))[1]      	
def min_3rd(listx):
	return sorted(set(listx))[2]
def max_2nd(listx):
	return sorted(set(listx))[-2]
def max_3rd(listx):
	return sorted(set(listx))[-3]

def repeatlist(listx):
	indexdictionary = {}
	for z in set(listx):
		counter = 0
		for i,x in enumerate(listx): 
			if x == z:
				counter += 1
				indexdictionary[z] = counter
	replist = [] 
	for score in list(indexdictionary.keys()):
		if indexdictionary[score] > 1:
			replist.append(score)
	return replist

repeatedlist = repeatlist(avgstroke_parlist)
samplecounter = 0
bestlist = []
t1bestlist = []
t2bestlist = []
t3bestlist = []

worstlist = []
t1worstlist = []
t2worstlist = []
t3worstlist = []
continuenum = 0
catchlist = [] #check to see if this loop works for max_2nd, max_3rd, min_2nd, min_3rd

if len(repeatedlist) > 0: #adds holes to a tie list for the first, second, and third best holes on the course (probably has something to do with continuenum)
	for score in repeatedlist:

		if len(set(avgstroke_parlist)) == 1:
			
			if score == min(avgstroke_parlist):
				continuenum += 1
				for i,x in enumerate(avgstroke_parlist):
					if x == score:
						t1bestlist.append(i+1)

		if len(set(avgstroke_parlist)) == 2:
			
			if score == min(avgstroke_parlist):
				continuenum += 1
				for i,x in enumerate(avgstroke_parlist):
					if x == score:
						t1bestlist.append(i+1)
			if score == max(avgstroke_parlist):
				continuenum += 1
				for i,x in enumerate(avgstroke_parlist):
					if x == score:
						t1worstlist.append(i+1)

		if len(set(avgstroke_parlist)) == 3:
			
			if score == min(avgstroke_parlist):
				continuenum += 1
				for i,x in enumerate(avgstroke_parlist):
					if x == score:
						t1bestlist.append(i+1)
			if score == max(avgstroke_parlist):
				continuenum += 1
				for i,x in enumerate(avgstroke_parlist):
					if x == score:
						t3bestlist.append(i+1)
			if score == min_2nd(avgstroke_parlist):
				continuenum += 1
				for i,x in enumerate(avgstroke_parlist):
					if x == score:
						t2bestlist.append(i+1)

		if len(set(avgstroke_parlist)) == 4:

			if score == min(avgstroke_parlist):
				continuenum += 1
				for i,x in enumerate(avgstroke_parlist):
					if x == score:
						t1bestlist.append(i+1)
			if score == max(avgstroke_parlist):
				continuenum += 1
				for i,x in enumerate(avgstroke_parlist):
					if x == score:
						t1worstlist.append(i+1)
			if score == min_2nd(avgstroke_parlist):
				continuenum += 1
				for i,x in enumerate(avgstroke_parlist):
					if x == score:
						t2bestlist.append(i+1)
						t3worstlist.append(i+1)
			if score == min_3rd(avgstroke_parlist):
				continuenum += 1
				for i,x in enumerate(avgstroke_parlist):
					if x == score:
						t3bestlist.append(i+1)
						t2worstlist.append(i+1)

		if len(set(avgstroke_parlist)) == 5:

			if score == min(avgstroke_parlist):
				continuenum += 1
				for i,x in enumerate(avgstroke_parlist):
					if x == score:
						t1bestlist.append(i+1)
			if score == max(avgstroke_parlist):
				continuenum += 1
				for i,x in enumerate(avgstroke_parlist):
					if x == score:
						t1worstlist.append(i+1)
			if score == min_2nd(avgstroke_parlist):
				continuenum += 1
				for i,x in enumerate(avgstroke_parlist):
					if x == score:
						t2bestlist.append(i+1)
			if score == max_2nd(avgstroke_parlist):
				continuenum += 1
				for i,x in enumerate(avgstroke_parlist):
					if x == score:
						t2worstlist.append(i+1)
			if score == min_3rd(avgstroke_parlist):
				continuenum += 1
				for i,x in enumerate(avgstroke_parlist):
					if x == score:
						t3bestlist.append(i+1)
						t3worstlist.append(i+1)

		if len(set(avgstroke_parlist)) >= 6:

			if score == min(avgstroke_parlist):
				continuenum += 1
				for i,x in enumerate(avgstroke_parlist):
					if x == score:
						t1bestlist.append(i+1)
			if score == max(avgstroke_parlist):
				continuenum += 1
				for i,x in enumerate(avgstroke_parlist):
					if x == score:
						t1worstlist.append(i+1)
			if score == min_2nd(avgstroke_parlist):
				continuenum += 1
				for i,x in enumerate(avgstroke_parlist):
					if x == score:
						t2bestlist.append(i+1)
			if score == max_2nd(avgstroke_parlist):
				continuenum += 1
				for i,x in enumerate(avgstroke_parlist):
					if x == score:
						t2worstlist.append(i+1)
			if score == min_3rd(avgstroke_parlist):
				continuenum += 1
				for i,x in enumerate(avgstroke_parlist):
					if x == score:
						t3bestlist.append(i+1)
			if score == max_3rd(avgstroke_parlist):
				continuenum += 1
				for i,x in enumerate(avgstroke_parlist):
					if x == score:
						t3worstlist.append(i+1)
						
print(continuenum)

if continuenum < len(set(avgstroke_parlist)): #tells the code that there are unique 1st,2nd, and 3rd best or worst holes on the golf course
	while samplecounter < len(set(avgstroke_parlist)) - continuenum: #provides a list of unique 1st, 2nd, and 3rd best and worst holes on the golf course

		for i,x in enumerate(avgstroke_parlist):
			if x not in repeatedlist:

				if len(set(avgstroke_parlist)) == 1:
			
					if x == min(avgstroke_parlist):
						for i,x in enumerate(avgstroke_parlist):
							if x == score:
								bestlist.append(i+1)
						samplecounter += 1

				if len(set(avgstroke_parlist)) == 2:
			
					if x == min(avgstroke_parlist):
						for i,x in enumerate(avgstroke_parlist):
							if x == score:
								bestlist.append(i+1)
						samplecounter += 1
					if x == max(avgstroke_parlist):
						for i,x in enumerate(avgstroke_parlist):
							if x == score:
								worstlist.append(i+1)
						samplecounter += 1

				if len(set(avgstroke_parlist)) == 3:
			
					if x == min(avgstroke_parlist):
						for i,x in enumerate(avgstroke_parlist):
							if x == score:
								bestlist.append(i+1)
						samplecounter += 1
					if x == max(avgstroke_parlist):
						for i,x in enumerate(avgstroke_parlist):
							if x == score:
								bestlist.append(i+1)
						samplecounter += 1
					if x == min_2nd(avgstroke_parlist):
						for i,x in enumerate(avgstroke_parlist):
							if x == score:
								bestlist.append(i+1)
						samplecounter += 1

				if len(set(avgstroke_parlist)) == 4:

					if x == min(avgstroke_parlist):
						for i,x in enumerate(avgstroke_parlist):
							if x == score:
								bestlist.append(i+1)
						samplecounter += 1
					if x == max(avgstroke_parlist):
						for i,x in enumerate(avgstroke_parlist):
							if x == score:
								worstlist.append(i+1)
						samplecounter += 1
					if x == min_2nd(avgstroke_parlist):
						for i,x in enumerate(avgstroke_parlist):
							if x == score:
								bestlist.append(i+1)
						samplecounter += 1
					if x == min_3rd(avgstroke_parlist):
						for i,x in enumerate(avgstroke_parlist):
							if x == score:
								worstlist.append(i+1)
						samplecounter += 1

				if len(set(avgstroke_parlist)) == 5:

					if x == min(avgstroke_parlist):
						for i,x in enumerate(avgstroke_parlist):
							if x == score:
								bestlist.append(i+1)
						samplecounter += 1
					if x == max(avgstroke_parlist):
						for i,x in enumerate(avgstroke_parlist):
							if x == score:
								worstlist.append(i+1)
						samplecounter += 1
					if x == min_2nd(avgstroke_parlist):
						for i,x in enumerate(avgstroke_parlist):
							if x == score:
								bestlist.append(i+1)
						samplecounter += 1
					if x == max_2nd(avgstroke_parlist):
						for i,x in enumerate(avgstroke_parlist):
							if x == score:
								worstlist.append(i+1)
						samplecounter += 1
					if x == min_3rd(avgstroke_parlist):
						for i,x in enumerate(avgstroke_parlist):
							if x == score:
								bestlist.append(i+1)
						samplecounter += 1

				if len(set(avgstroke_parlist)) >= 6:  #stopped here

					if x == min(avgstroke_parlist):
						for i,x in enumerate(avgstroke_parlist):
							if x == score:
								bestlist.append(i+1)
						samplecounter += 1
					if x == max(avgstroke_parlist):
						for i,x in enumerate(avgstroke_parlist):
							if x == score:
								worstlist.append(i+1)
						samplecounter += 1
					if x == min_2nd(avgstroke_parlist):
						for i,x in enumerate(avgstroke_parlist):
							if x == score:
								bestlist.append(i+1)
						samplecounter += 1
					if x == max_2nd(avgstroke_parlist):
						for i,x in enumerate(avgstroke_parlist):
							if x == score:
								worstlist.append(i+1)
						samplecounter += 1
					if x == min_3rd(avgstroke_parlist):
						for i,x in enumerate(avgstroke_parlist):
							if x == score:
								bestlist.append(i+1)
						samplecounter += 1
					if x == max_3rd(avgstroke_parlist):
						for i,x in enumerate(avgstroke_parlist):
							if x == score:
								worstlist.append(i+1)
						samplecounter += 1		
print()
print("********************")
print()
#print("Your best 3 holes on the golf course are:")#<----need to fix so that it ranks the holes in order, doesn't just display in the order of the for loop
print()
if len(set(avgstroke_parlist)) == 1:
	if max(avgstroke_parlist) > 0:
		print("You shoot exactly " + str(max(set(avgstroke_parlist))) + " strokes over par for every hole on the golf course!")
	if max(avgstroke_parlist) < 0:
		print("You shoot exactly " + str(max(set(avgstroke_parlist))) + " strokes under par for every hole on the golf course!")
	
if len(set(avgstroke_parlist)) == 2:
	if len(t1bestlist) > 0:
		print("You have a " + str(len(t1bestlist)) + "-way tie for best hole on the golf course:")
		print()
		for i in t1bestlist:
			print("hole " + str(round(i,1)))
	else:
		print("Your best hole on the golf course is: ")
		print()
		print("1. hole " + str((avgstroke_parlist.index(min(avgstroke_parlist))+1)))
	print()
	

if len(set(avgstroke_parlist)) == 3:
	print("Your three best holes on the golf course are: ")
	print()
	if len(t1bestlist) > 0:
		for i in t1bestlist:
			print("T1. hole " + str(round(i,1)))
	else:
		print("1. hole " + str((avgstroke_parlist.index(min(avgstroke_parlist))+1)))
	print()
	if len(t2bestlist) > 0:
		for i in t2bestlist: 
			print("T2. hole " + str(round(i,1)))
	else:
		print("2. hole " + str((avgstroke_parlist.index(min_2nd(avgstroke_parlist))+1)))
	print()
	if len(t3bestlist) > 0:
		for i in t3bestlist:
			print("T3. hole " + str(round(i,1)))
	else:
		print("3. hole " + str((avgstroke_parlist.index(min_3rd(avgstroke_parlist))+1)))
	print()

if len(set(avgstroke_parlist)) == 4:
	print("Your two best holes on the golf course are: ")
	print()
	if len(t1bestlist) > 0:
		for i in t1bestlist:
			print("T1. hole " + str(round(i,1)))
	else: 
		print("1. hole " + str((avgstroke_parlist.index(min(avgstroke_parlist))+1)))
	print()
	if len(t2bestlist) > 0:
		for i in t2bestlist:
			print("T2. hole " + str(round(i,1)))
	else: 
		print("2. hole " + str((avgstroke_parlist.index(min_2nd(avgstroke_parlist))+1)))
	print()

if len(set(avgstroke_parlist)) == 5:
	print("Your three best holes on the golf course are: ")
	print()
	if len(t1bestlist) > 0:
		for i in t1bestlist:
			print("T1. hole " + str(round(i,1)))
	else: 
		print("1. hole " + str((avgstroke_parlist.index(min(avgstroke_parlist))+1)))
	print()
	if len(t2bestlist) > 0:
		for i in t2bestlist:
			print("T2. hole " + str(round(i,1)))
	else: 
		print("2. hole " + str((avgstroke_parlist.index(min_2d(avgstroke_parlist))+1)))
	print()
	if len(t3bestlist) > 0:
		for i in t3bestlist:
			print("T3. hole " + str(round(i,1)))
	else:
		print("3. hole " + str((avgstroke_parlist.index(min_3rd(avgstroke_parlist))+1)))

if len(set(avgstroke_parlist)) >= 6:
	print("Your three best holes on the golf course are: ")
	print()

	if len(t1bestlist) > 0:
		for i in t1bestlist:
			print("T1. hole " + str(round(i,1)))
	else:
		print('1. hole ' + str((avgstroke_parlist.index(min(avgstroke_parlist))+1)))
	print()
	
	if len(t2bestlist) > 0:
		for i in t2bestlist:
			print("T2. hole " + str(round(i,1)))
	else:
		print('2. hole ' + str((avgstroke_parlist.index(min_2nd(avgstroke_parlist))+1)))
	print()
	
	if len(t3bestlist) > 0:
		for i in t3bestlist:
			print("T3. hole " + str(round(i,1)))
	else:
		print('3. hole ' + str((avgstroke_parlist.index(min_3rd(avgstroke_parlist))+1)))
	print()

print()
if max(set(avgstroke_parlist)) <= 3:
	print("Awesome! Keep up the good work here!")
print()
print("********************")
print()
if len(set(avgstroke_parlist)) == 1:
	pass

if len(set(avgstroke_parlist)) == 2:
	if len(t1worstlist) > 0:
		print("You have a " + str(len(t1worstlist)) + "-way tie for worst hole on the golf course:")
		print()
		for i in t1worstlist:
			print("hole " + str(round(i,1)))
	else:
		print("Your worst hole on the golf course is: ")
		print()
		print("1. hole " + str((avgstroke_parlist.index(max(avgstroke_parlist))+1))) 
	print()

if len(set(avgstroke_parlist)) == 3:
	print()

if len(set(avgstroke_parlist)) == 4:
	print("Your two worst holes on the golf course are: ")
	print()
	if len(t1worstlist) > 0:
		for i in t1worstlist:
			print("T1. hole " + str(round(i,1)))
	else:
		print("1. hole " + str((avgstroke_parlist.index(max(avgstroke_parlist))+1))) 
	print()
	if len(t2worstlist) > 0:
		for i in t2worstlist: 
			print("T2. hole " + str(round(i,1)))
	else: 
		print("2. hole " + str((avgstroke_parlist.index(max_2nd(avgstroke_parlist))+1)))
	print()

if len(set(avgstroke_parlist)) == 5:
	print("Your two worst holes on the golf course are: ")
	print()
	if len(t1worstlist) > 0:
		for i in t1worstlist:
			print("T1. hole " + str(round(i,1)))
	else:
		print("1. hole " + str((avgstroke_parlist.index(max(avgstroke_parlist))+1)))
	print()
	if len(t2worstlist) > 0:
		for i in t2worstlist: 
			print("T2. hole " + str(round(i,1)))
	else: 
		print("2. hole " + str((avgstroke_parlist.index(max_2nd(avgstroke_parlist))+1)))
	print()


if len(set(avgstroke_parlist)) >= 6:
	print("Your three worst holes on the golf course are: ")
	print()
	if len(t1worstlist) > 0:
		for i in t1worstlist:
			print("T1. hole " + str(round(i,1)))
	else:
		print("1. hole " + str((avgstroke_parlist.index(max(avgstroke_parlist))+1)))
	if len(t2worstlist) > 0:
		for i in t2worstlist:
			print("T2. hole " + str(round(i,1)))
	else:
		print("2. hole " + str((avgstroke_parlist.index(max_2nd(avgstroke_parlist))+1)))
	if len(t3worstlist) > 0:
		for i in t3worstlist:
			print("T3. hole " + str(round(i,1)))
	else:
		print("3. hole " + str((avgstroke_parlist.index(max_3rd(avgstroke_parlist))+1)))
print()
if len(set(avgstroke_parlist)) == 1 or len(set(avgstroke_parlist)) == 3:
	print()
else:
	print("Yeesh! There's a lot of work to do here.")

#---DISPLAY AVERAGE NUMBER OF STROKES ABOVE OR BELOW PAR AT OLD OVERTON FOR THE USER--
print()
print('********************')
print()
avgstroke = (sum(avgstroke_parlist)/len(avgstroke_parlist))
if avgstroke > 0:
        if avgstroke != 1:
                print("You average " + str(round(avgstroke,3)) + " strokes above par through every hole at Old Overton Country Club.")
        if avgstroke == 1:
                print("You average 1.0 stroke above par through every hole at Old Overton Country Club.")
if avgstroke < 0:
        if avgstroke != -1:
                print("You average " + str(abs(round(avgstroke,3))) + " strokes below par through every hole at Old Overton Country Club.")
        if avgstroke == -1:
                print("You average 1.0 strokes below par through every hole at Old Overton Country Club.")
if avgstroke == 0:
	print("You average even par through every hole at Old Overton Country Club.")
                
     

#---DISPLAY AVERAGE POSTED SCORE AT OLD OVERTON FOR THE USER---
avgpostedscore = sum(avgstroke_parlist) + 71
print()
print("********************")
print()
print("You average a round of " + str(round(avgpostedscore,2)) + " at Old Overton Country Club.")

#---DISPLAY EAGLE,BIRDIE,PAR,BOGEY,DOUBLE,TRIPLE,and MAX PERCENTAGE FOR ROUNDS AT OLD OVERTON---
print()
print("********************")
print()
print("Fractions of each score mark recorded at Old Overton Country Club:")
print()

hole_in_1_sum = 0 #this code wil count the total number of each score mark recorded by adding up each list in the dictionary of lists for each score mark by hole
for tick in list(hole_in_1_dict.values()):
	hole_in_1_sum += sum(tick)
double_eagle_sum = 0
for tick in list(double_eagle_dict.values()):
	double_eagle_sum += sum(tick)
eagle_sum = 0 
for tick in list(eagle_dict.values()):
	eagle_sum += sum(tick)
birdie_sum = 0
for tick in list(birdie_dict.values()):
	birdie_sum += sum(tick)
par_sum = 0
for tick in list(par_dict.values()):
	par_sum += sum(tick)
bogey_sum = 0
for tick in list(bogey_dict.values()):
	bogey_sum += sum(tick)
double_sum = 0
for tick in list(double_dict.values()):
	double_sum += sum(tick)
triple_sum = 0
for tick in list(triple_dict.values()):
	triple_sum += sum(tick)
max_sum = 0
for tick in list(max_dict.values()):
	max_sum += sum(tick)
sum_all = hole_in_1_sum + double_eagle_sum + eagle_sum + birdie_sum + par_sum + bogey_sum + double_sum + triple_sum + max_sum
print("Hole-in-one: \n \n" + str(round((hole_in_1_sum/sum_all),2)*100) + " %")
print()
print("Double eagle: \n \n" + str(round((double_eagle_sum/sum_all),2)*100) + " %")
print()
print("Eagle: \n \n" + str(round((eagle_sum/sum_all),2)*100) + " %")
print()
print("Birdie: \n \n" + str(round((birdie_sum/sum_all),2)*100) + " %")
print()
print("Par: \n \n" + str(round((par_sum/sum_all),2)*100) + " %")
print()
print("Bogey:  \n \n" + str(round((bogey_sum/sum_all),2)*100) + " %")
print()
print("Double bogey: \n \n" + str(round((double_sum/sum_all),2)*100) + " %")
print()
print("Triple bogey: \n \n" + str(round((triple_sum/sum_all),2)*100) + " %")
print()
print("Quadruple bogey or worse: \n \n" + str(round((max_sum/sum_all),2)*100) + " %")

#---DISPLAY AVERAGE SNOWMAN COUNT AT OLD OVERTON---
print()
print("********************")
print()
print("Average number of snowmen per round at Old Overton Country Club")
print()
snowmanavg = sum(snowmantick_list)/len(snowmantick_list)
print(str(round(snowmanavg,2)))
print()
if snowmanavg > 1.0:
	print("Stay frosty my friend!")
else:
	print("You're not as frosty as you think....")










		

