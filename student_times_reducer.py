#!/usr/bin/python
import sys


hr_post_history = [0]*24
old_key = None

for line in sys.stdin:
	data = line.strip().split("\t")
	
	if len(data) != 2:
		continue
	
	# Output for each new key
	this_key, hr_added_at = data
	if old_key and old_key != this_key:
		# Get hours when user posts the most (include ties)
		top_post_hours = [idx for idx,value in enumerate(hr_post_history) if value == max(hr_post_history)]
		for hour in top_post_hours:
			print("{0}\t{1}".format(old_key, hour)) 
		hr_post_history = [0]*24
		
	old_key = this_key		
	
	# Check if hr_added_at is a valid int hour
	if int(hr_added_at) < 0 or int(hr_added_at) >= 24:
		continue
	# Increment hour corresponding to the post
	hr_post_history[int(hr_added_at)]+=1

# Output final key
if old_key != None:
	top_post_hour = hr_post_history.index(max(hr_post_history))
	print("{0}\t{1}".format(old_key, top_post_hour)) 


