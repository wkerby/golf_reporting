#read the data from the csv file
filename = r"C:\Users\wkerb\Dropbox\PC\Desktop\Python\Python\Excel Data\My Old Overton Scorecard.csv"
#specify the list of color tees at Old Overton Country Club from the csv file
colorlist = ['Blue','Black','White','Gold','Red']
tiger_list = []
#ask the user to input his name
user_name = input("Hello! Please enter your first name: ").upper()
name_list = ['JEFF','CLAY','WILL']
if user_name not in name_list:
	user_name = input("Name not recognized. Please enter a valid username:").upper()
else:
	pass
with open(filename,'r') as file_object:
	lines = file_object.readlines()
	for line in lines:
		name = line[0:4]
		if name.upper() == user_name:
				
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
		else:
			pass
#define a dictionary to link average strokes over or under par for every hole on the golf course
#define dictionaries for every hole on the golf course and a tally of every instance of hole-in-one, double eagle, eagle, birdie, par, bogey, double bogey, triple bogey, and max
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
parlist = [4,5,3,4,4,4,4,3,4,5,4,3,4,4,4,5,3,4] #list of par score for all 18 holes at Old Overton Country Club
snowman_list =[]
for posting in tiger_list:
	for hole in golfcoursedata.keys(): #can we make an option for a nine-hole round here?
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
#define the file to which the program will write depending on the name of the user who is entering his new score
if user_name == "WILL":
	filename1 = 'willgolfdata.txt'
elif user_name == "JEFF":
	filename1 = 'jeffgolfdata.txt'
elif user_name == "CLAY":
	filename1 = 'claygolfdata.txt'
#write to the .txt file with a time stamp for the new recording 
with open(filename1, 'w') as file_object1:
	avgstroke_parlist = [] #define the list that details the user's average number of strokes abover or below par for every hole on the golf course
	matching_score_dict = {}
	import datetime
	date = datetime.datetime.now()
	datestr = date.strftime('%c')
	file_object1.write(' \n')
	file_object1.write("******************** Results as of " + datestr + " ********************\n")
	file_object1.write(' \n')
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

#return the average number of strokes above or below par for each hole on the golf course for the specified user

	for score in list(golfcoursedata.values()): #score is a list of all of the scores that have been recorded for a particular hole 
		y = sum(score)/len(score)
		x = round(y,2)
		if len(indexfinder(list(golfcoursedata.values()),score)) == 1:
			if x > parlist[list(golfcoursedata.values()).index(score)]:
				if x - parlist[list(golfcoursedata.values()).index(score)] == 1:
					file_object1.write("You average " + str(round(x - parlist[list(golfcoursedata.values()).index(score)],3)) + " stroke above par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.\n')
					file_object1.write("\n")
				else:
					file_object1.write("You average " + str(round(x - parlist[list(golfcoursedata.values()).index(score)],3)) + " strokes above par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.\n')
					file_object1.write("\n")
				avgstroke_parlist.append(x - parlist[list(golfcoursedata.values()).index(score)])
			if x < parlist[list(golfcoursedata.values()).index(score)]:
				if parlist[list(golfcoursedata.values()).index(score)] - x == 1:
				 	file_object1.write("You average " + str(round(parlist[list(golfcoursedata.values()).index(score)] - x,3)) + " stroke above par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.\n')
				 	file_object1.write("\n")
				else:
					file_object1.write("You average " + str(round(parlist[list(golfcoursedata.values()).index(score)] - x,3)) + " strokes below par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.\n')
					file_object1.write("\n")
				avgstroke_parlist.append(x - parlist[list(golfcoursedata.values()).index(score)])
			if x == parlist[list(golfcoursedata.values()).index(score)]:
				file_object1.write("You average even par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.\n')
				file_object1.write("\n")
				avgstroke_parlist.append(0)
		elif len(indexfinder(list(golfcoursedata.values()),score)) > 1: 
			scorematch_index = indexfinder(list(golfcoursedata.values()),score)
			if matching_score_dict[str(score)] == 0: 
				if x > parlist[list(golfcoursedata.values()).index(score)]:
					if x - parlist[list(golfcoursedata.values()).index(score)] == 1:
						file_object1.write("You average " + str(round(x - parlist[list(golfcoursedata.values()).index(score)],3)) + " stroke above par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.\n')
						file_object1.write("\n")
					else:
						file_object1.write("You average " + str(round(x - parlist[list(golfcoursedata.values()).index(score)],3)) + " strokes above par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.\n')
						file_object1.write("\n")
					avgstroke_parlist.append(x - parlist[list(golfcoursedata.values()).index(score)])
				if x < parlist[list(golfcoursedata.values()).index(score)]:
					if parlist[list(golfcoursedata.values()).index(score)] - x == 1:
						file_object1.write("You average " + str(round(parlist[list(golfcoursedata.values()).index(score)] - x,3)) + " stroke below par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.\n')
						file_object1.write("\n")
					else:
						file_object1.write("You average " + str(round(parlist[list(golfcoursedata.values()).index(score)] - x,3)) + " strokes below par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.\n')
						file_object1.write("\n")
					avgstroke_parlist.append(x - parlist[list(golfcoursedata.values()).index(score)])
				if x == parlist[list(golfcoursedata.values()).index(score)]:
					file_object1.write("You average even par on hole " + str(list(golfcoursedata.values()).index(score) + 1) + '.\n')
					file_object1.write("\n")
					avgstroke_parlist.append(0)
			if matching_score_dict[str(score)] > 0:
				if x > parlist[(indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]])]:
					if x - parlist[indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]]] == 1:
						file_object1.write("You average " + str(round(x - parlist[indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]]],3)) + " stroke above par on hole " + str(indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]] + 1) + '.\n')
						file_object1.write("\n")
					else:
						file_object1.write("You average " + str(round(x - parlist[indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]]],3)) + " strokes above par on hole " + str(indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]] + 1) + '.\n')
						file_object1.write("\n")
					avgstroke_parlist.append(x - parlist[indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]]])
				if x < parlist[(indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]])]:
					if parlist[indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]]] - x == 1:
						file_object1.write("You average " + str(round(parlist[indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]]] - x,3)) + " stroke below par on hole " + str(indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]] + 1) + '.\n')
						file_object1.write("\n")
					else:
						file_object1.write("You average " + str(round(parlist[indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]]] - x,3)) + " strokes below par on hole " + str(indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]] + 1) + '.\n')
						file_object1.write("\n")
					avgstroke_parlist.append(x - parlist[indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]]])
				if x == parlist[(indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]])]:
					file_object1.write("You average even par on hole " + str(indexfinder(list(golfcoursedata.values()),score)[matching_score_dict[str(score)]] + 1)  + '.\n')
					file_object1.write("\n")
					avgstroke_parlist.append(0)
			matching_score_dict[str(score)] += 1

	for posting in tiger_list:
		snowmancounter = 0
		for i in posting:
			if i == 8:
				snowmancounter += 1
		snowman_list.append(snowmancounter)
	file_object1.write("********************")

	#display last 3 scores for every hole and indicate to user whether he is trending up, down, or neither
	file_object1.write("\n")
	file_object1.write("\n")
	file_object1.write("Trends for every hole at Old Overton Country Club:")
	file_object1.write("\n")
	file_object1.write("\n")
	for hole, scores in golfcoursedata.items():
		avgholescore = sum(scores)/len(scores)
		uptrendcount = 0
		downtrendcount = 0
		for i in scores[-2:]:
			if i < avgholescore:
				uptrendcount += 1
			if i > avgholescore:
				downtrendcount += 1
		if uptrendcount == 2:
			file_object1.write(hole + ": - trending down")
		elif downtrendcount == 2:
			file_object1.write(hole + ": + trending up")
		else:
			file_object1.write(hole + ": --- ")
		file_object1.write("\n")
		file_object1.write("\n")

	
#display best and worst 3 holes (if applicable) on the golf course based on average number of strokes above or below par

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
	t1bestlist = []#create lists of holes for which there exists a tie for best, 2nd best, and 3rd best and worst holes on the golf course
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
	file_object1.write("********************")
	file_object1.write("\n")
	file_object1.write("\n")
	if len(set(avgstroke_parlist)) == 1:
		if max(avgstroke_parlist) > 0:
			file_object1.write("You shoot exactly " + str(max(set(avgstroke_parlist))) + " strokes over par for every hole on the golf course!")
		if max(avgstroke_parlist) < 0:
			file_object1.write("You shoot exactly " + str(max(set(avgstroke_parlist))) + " strokes under par for every hole on the golf course!")
	
	if len(set(avgstroke_parlist)) == 2:
		if len(t1bestlist) > 0:
			file_object1.write("You have a " + str(len(t1bestlist)) + "-way tie for best hole on the golf course:")
			file_object1.write("\n")
			file_object1.write("\n")
			for i in t1bestlist:
				file_object1.write("hole " + str(round(i,1)))
		else:
			file_object1.write("Your best hole on the golf course is: ")
			file_object1.write("\n")
			file_object1.write("\n")
			file_object1.write("1. hole " + str((avgstroke_parlist.index(min(avgstroke_parlist))+1)))
		file_object1.write("\n")
	

	if len(set(avgstroke_parlist)) == 3:
		file_object1.write("Your three best holes on the golf course are: ")
		file_object1.write("\n")
		file_object1.write("\n")
		if len(t1bestlist) > 0:
			for i in t1bestlist:
				file_object1.write("T1. hole " + str(round(i,1)))
				file_object1.write("\n")
		else:
			file_object1.write("1. hole " + str((avgstroke_parlist.index(min(avgstroke_parlist))+1)))
		print()
		if len(t2bestlist) > 0:
			for i in t2bestlist: 
				file_object1.write("T2. hole " + str(round(i,1)))
				file_object1.write("\n")
		else:
			file_object1.write("2. hole " + str((avgstroke_parlist.index(min_2nd(avgstroke_parlist))+1)))
		file_object1.write("\n")
		if len(t3bestlist) > 0:
			for i in t3bestlist:
				file_object1.write("T3. hole " + str(round(i,1)))
				file_object1.write("\n")
		else:
			file_object1.write("3. hole " + str((avgstroke_parlist.index(min_3rd(avgstroke_parlist))+1)))
		file_object1.write("\n")

	if len(set(avgstroke_parlist)) == 4:
		file_object1.write("Your two best holes on the golf course are: ")
		file_object1.write("\n")
		file_object1.write("\n")
		if len(t1bestlist) > 0:
			for i in t1bestlist:
				file_object1.write("T1. hole " + str(round(i,1)))
				file_object1.write("\n")
		else: 
			file_object1.write("1. hole " + str((avgstroke_parlist.index(min(avgstroke_parlist))+1)))
		file_object1.write("\n")
		if len(t2bestlist) > 0:
			for i in t2bestlist:
				file_object1.write("T2. hole " + str(round(i,1)))
				file_object1.write("\n")
		else: 
			file_object1.write("2. hole " + str((avgstroke_parlist.index(min_2nd(avgstroke_parlist))+1)))
		file_object1.write("\n")

	if len(set(avgstroke_parlist)) == 5:
		file_object1.write("Your three best holes on the golf course are: ")
		file_object1.write("\n")
		file_object1.write("\n")
		if len(t1bestlist) > 0:
			for i in t1bestlist:
				file_object1.write("T1. hole " + str(round(i,1)))
				file_object1.write("\n")
		else: 
			file_object1.write("1. hole " + str((avgstroke_parlist.index(min(avgstroke_parlist))+1)))
		file_object1.write("\n")
		if len(t2bestlist) > 0:
			for i in t2bestlist:
				file_object1.write("T2. hole " + str(round(i,1)))
				file_object1.write("\n")
		else: 
			file_object1.write("2. hole " + str((avgstroke_parlist.index(min_2d(avgstroke_parlist))+1)))
		file_object1.write("\n")
		if len(t3bestlist) > 0:
			for i in t3bestlist:
				file_object1.write("T3. hole " + str(round(i,1)))
				file_object1.write("\n")
		else:
			file_object1.write("3. hole " + str((avgstroke_parlist.index(min_3rd(avgstroke_parlist))+1)))

	if len(set(avgstroke_parlist)) >= 6:
		file_object1.write("Your three best holes on the golf course are: ")
		file_object1.write("\n")
		file_object1.write("\n")

		if len(t1bestlist) > 0:
			for i in t1bestlist:
				file_object1.write("T1. hole " + str(round(i,1)))
				file_object1.write("\n")
		else:
			file_object1.write('1. hole ' + str((avgstroke_parlist.index(min(avgstroke_parlist))+1)))
		file_object1.write("\n")
	
		if len(t2bestlist) > 0:
			for i in t2bestlist:
				file_object1.write("T2. hole " + str(round(i,1)))
				file_object1.write("\n")
		else:
			file_object1.write('2. hole ' + str((avgstroke_parlist.index(min_2nd(avgstroke_parlist))+1)))
		file_object1.write("\n")
	
		if len(t3bestlist) > 0:
			for i in t3bestlist:
				file_object1.write("T3. hole " + str(round(i,1)))
				file_object1.write("\n")
		else:
			file_object1.write('3. hole ' + str((avgstroke_parlist.index(min_3rd(avgstroke_parlist))+1)))
		file_object1.write("\n")

	file_object1.write("\n")
	if max(set(avgstroke_parlist)) <= 3:
		file_object1.write("\n")
		file_object1.write("Awesome! Keep up the good work here!")
	file_object1.write("\n")
	file_object1.write("\n")
	file_object1.write("********************")
	file_object1.write("\n")
	if len(set(avgstroke_parlist)) == 1:
		pass

	if len(set(avgstroke_parlist)) == 2:
		if len(t1worstlist) > 0:
			file_object1.write("\n")
			file_object1.write("You have a " + str(len(t1worstlist)) + "-way tie for worst hole on the golf course:")
			file_object1.write("\n")
			file_object1.write("\n")
			for i in t1worstlist:
				file_object1.write("T1. hole " + str(round(i,1)))
				file_object1.write("\n")
		else:
			file_object1.write("\n")
			file_object1.write("Your worst hole on the golf course is: ")
			file_object1.write("\n")
			file_object1.write("\n")
			file_object1.write("1. hole " + str((avgstroke_parlist.index(max(avgstroke_parlist))+1))) 
		file_object1.write("\n")

	if len(set(avgstroke_parlist)) == 3:
		file_object1.write("\n")

	if len(set(avgstroke_parlist)) == 4:
		file_object1.write("\n")
		file_object1.write("Your two worst holes on the golf course are: ")
		file_object1.write("\n")
		file_object1.write("\n")
		if len(t1worstlist) > 0:
			for i in t1worstlist:
				file_object1.write("T1. hole " + str(round(i,1)))
				file_object1.write("\n")
		else:
			file_object1.write("1. hole " + str((avgstroke_parlist.index(max(avgstroke_parlist))+1))) 
		file_object1.write("\n")
		if len(t2worstlist) > 0:
			for i in t2worstlist: 
				file_object1.write("T2. hole " + str(round(i,1)))
				file_object1.write("\n")
		else: 
			file_object1.write("2. hole " + str((avgstroke_parlist.index(max_2nd(avgstroke_parlist))+1)))
		file_object1.write("\n")

	if len(set(avgstroke_parlist)) == 5:
		file_object1.write("\n")
		file_object1.write("Your two worst holes on the golf course are: ")
		file_object1.write("\n")
		file_object1.write("\n")
		if len(t1worstlist) > 0:
			for i in t1worstlist:
				file_object1.write("T1. hole " + str(round(i,1)))
				file_object1.write("\n")
		else:
			file_object1.write("1. hole " + str((avgstroke_parlist.index(max(avgstroke_parlist))+1)))
		file_object1.write("\n")
		if len(t2worstlist) > 0:
			for i in t2worstlist: 
				file_object1.write("T2. hole " + str(round(i,1)))
				file_object1.write("\n")
		else: 
			file_object1.write("2. hole " + str((avgstroke_parlist.index(max_2nd(avgstroke_parlist))+1)))
		file_object1.write("\n")


	if len(set(avgstroke_parlist)) >= 6:
		file_object1.write("\n")
		file_object1.write("Your three worst holes on the golf course are: ")
		file_object1.write("\n")
		file_object1.write("\n")
		if len(t1worstlist) > 0:
			for i in t1worstlist:
				file_object1.write("T1. hole " + str(round(i,1)))
				file_object1.write("\n")
		else:
			file_object1.write("1. hole " + str((avgstroke_parlist.index(max(avgstroke_parlist))+1)))
			file_object1.write("\n")
		if len(t2worstlist) > 0:
			for i in t2worstlist:
				file_object1.write("T2. hole " + str(round(i,1)))
				file_object1.write("\n")
		else:
			file_object1.write("2. hole " + str((avgstroke_parlist.index(max_2nd(avgstroke_parlist))+1)))
			file_object1.write("\n")
		if len(t3worstlist) > 0:
			for i in t3worstlist:
				file_object1.write("T3. hole " + str(round(i,1)))
				file_object1.write("\n")
		else:
			file_object1.write("3. hole " + str((avgstroke_parlist.index(max_3rd(avgstroke_parlist))+1)))
			file_object1.write("\n")
	file_object1.write("\n")
	if len(set(avgstroke_parlist)) == 1 or len(set(avgstroke_parlist)) == 3:
		file_object1.write("\n")
	else:
		file_object1.write("Uh-oh! There's a lot of work to do here.")

#display the average number of strokes abover or below par at Old Overton Country Club for the specified user

	file_object1.write("\n")
	file_object1.write("\n")
	file_object1.write('********************')
	file_object1.write("\n")
	avgstroke = (sum(avgstroke_parlist)/len(avgstroke_parlist))
	if avgstroke > 0:
		if avgstroke != 1:
			file_object1.write("\n")
			file_object1.write("You average " + str(round(avgstroke,2)) + " strokes above par through every hole at Old Overton Country Club.")
			file_object1.write("\n")
		if avgstroke == 1:
			file_object1.write("\n")
			file_object1.write("You average 1.0 stroke above par through every hole at Old Overton Country Club.")
			file_object1.write("\n")
	if avgstroke < 0:
		if avgstroke != -1:
			file_object1.write("\n")
			file_object1.write("You average " + str(abs(round(avgstroke,2))) + "strokes below par through every hole at Old Overton Country Club.")
			file_object1.write("\n")
		if avgstroke == -1:
			file_object1.write("\n")
			file_object1.write("You average 1.0 stroke below par through every hole at Old Overton Country Club.")
			file_object1.write("\n")
	if avgstroke == 0:
		file_object1.write("\n")
		file_object1.write("You average even par through every hole at Old Overton Country Club") 
		file_object1.write("\n")

#display the average posted score at Old Overton Country Club for the user

	avgpostedscore = sum(avgstroke_parlist) + 71
	file_object1.write("\n")
	file_object1.write("********************")
	file_object1.write("\n")
	file_object1.write("\n")
	file_object1.write("You average a round of " + str(round(avgpostedscore,1)) + " at Old Overton Country Club.")


#display hole-in-one, double eagle, eagle, birdie, par, bogey, double, triple, and max percentage for rounds at Old Overton Country Club

	file_object1.write("\n")
	file_object1.write("\n")
	file_object1.write("********************")
	file_object1.write("\n")
	file_object1.write("\n")
	file_object1.write("Percentages of each score mark recorded at Old Overton Country Club:")
	file_object1.write("\n")
	file_object1.write("\n")

	hole_in_1_sum = 0 #this code will count the total number of each score mark recorded by adding up each list in the dictionary of lists for each score mark by hole
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
	file_object1.write("Hole-in-one: " + str(round((hole_in_1_sum/sum_all),3)*100) + " %")
	file_object1.write("\n")
	file_object1.write("\n")
	file_object1.write("Double eagle: " + str(round((double_eagle_sum/sum_all),3)*100) + " %")
	file_object1.write("\n")
	file_object1.write("\n")
	file_object1.write("Eagle: " + str(round((eagle_sum/sum_all),3)*100) + " %")
	file_object1.write("\n")
	file_object1.write("\n")
	file_object1.write("Birdie: " + str(round((birdie_sum/sum_all),3)*100) + " %")
	file_object1.write("\n")
	file_object1.write("\n")
	file_object1.write("Par: " + str(round((par_sum/sum_all),3)*100) + " %")
	file_object1.write("\n")
	file_object1.write("\n")
	file_object1.write("Bogey: " + str(round((bogey_sum/sum_all),3)*100) + " %")
	file_object1.write("\n")
	file_object1.write("\n")
	file_object1.write("Double bogey: " + str(round((double_sum/sum_all),3)*100) + " %")
	file_object1.write("\n")
	file_object1.write("\n")
	file_object1.write("Triple bogey: " + str(round((triple_sum/sum_all),3)*100) + " %")
	file_object1.write("\n")
	file_object1.write("\n")
	file_object1.write("Quadruple bogey or worse: " + str(round((max_sum/sum_all),3)*100) + " %")
	file_object1.write("\n")


#display average snowman (i.e. score mark of 8) at Old Overton Country Club

	file_object1.write("\n")
	file_object1.write("********************")
	file_object1.write("\n")
	file_object1.write("\n")
	file_object1.write("Average number of snowmen per round at Old Overton Country Club:")
	file_object1.write("\n")
	file_object1.write("\n")
	snowmanavg = sum(snowman_list)/len(snowman_list)
	file_object1.write(str(round(snowmanavg,2)))
	file_object1.write("\n")
	file_object1.write("\n")
	if snowmanavg > 1.0:
		file_object1.write("Stay frosty my friend!")
		file_object1.write("\n")
	else:
		file_object1.write("You're not as frosty as you think....")
	file_object1.write("\n")
	file_object1.write("********************")


#confirm with the user that his scores have been upate in the system	
print("\nThanks for checking in! Your posting for " + datestr + " has been updated in the system.")
