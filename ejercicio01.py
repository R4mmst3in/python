## Print a list of word separated with commas

list_of_words = ["This","is","my","beautiful","world"]
result = ""
for i in range(len(list_of_words)):
	result += list_of_words[i]
	if i < len(list_of_words) -1:
		result+=","
print (result)

## Forma
DELIMITER = ","
print(DELIMITER.join(list_of_words))
