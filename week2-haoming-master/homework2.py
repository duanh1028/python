def histograim(data, n, l, h):
    # data is a list
    # n is an integer
    # l and h are floats
    
    # Write your code here
	hist = [0] * n
	w = (h - l) / n

	for i in range(0, n):
		count = 0
		for j in data:
			if j >= l + i * w and j < l + (i + 1) * w:
				count = count + 1
		hist[i] = count

    # return the variable storing the histogram
    # Output should be a list
	return hist

	pass



def addressbook(name_to_phone, name_to_address):
    #name_to_phone and name_to_address are both dictionaries
    
    # Write your code here
	# load to address_to_all
	address_to_all = {}
	for name in name_to_address:
		if name_to_address[name] not in address_to_all:
			address_to_all[name_to_address[name]] = ([name], name_to_phone[name])
		else:
			address_to_all[name_to_address[name]][0].append(name)

	#print stuff
	for name in address_to_all:
		length = len(address_to_all[name][0])
		if length > 1:
			error = []
			for i in range(1, length):
				if name_to_phone[address_to_all[name][0][0]] != name_to_phone[address_to_all[name][0][i]]:
					error.append(address_to_all[name][0][i])
			print("Warning: ", end = "")
			err_length = len(error)
			for i in range(0, err_length):
				if i == 1:
					print(error[i], end = "")
				else:
					print(error[i], end = "")
			print(" has a different number for", name, "than", address_to_all[name][0][0] + ". Using the number for", address_to_all[name][0][i], ".")

    # return the variable storing address_to_all
    # Output should be a dictionary
	return address_to_all
