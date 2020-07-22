#Python Program to find the occurences of a character in a string


def Occurences(input_string):
	answer = []
	answer_index = -1
	sorted_character = sorted(input_string)
	for i in range(len(sorted_character)):
		#create a new list to append if the character is changed
		if(sorted_character[i - 1] != sorted_character[i]):
			answer.append([sorted_character[i],1])
			answer_index+=1
		#increase the number of the character
		else:
			answer[answer_index][1]+=1
	return answer

def main():
	input_string = input("Please input a string: ")
	print("output: ", Occurences(input_string))

main()