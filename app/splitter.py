#!/usr/bin/env python3
def string_2_dict(ascii_string):
	format = 'ascii'
	new_string = ascii_string.decode(format)
	labels_start = ['mac_controller', 'mac_point', 'dbi', 'timestamp']
	labels_usual = ['mac_controller', 'timestamp']
	db_doc = []

	for item in new_string.split("="):
		one_doc_string = item.split(";")
		if len(one_doc_string) == 4:
			dictio = dict(zip(labels_start, one_doc_string))
			db_doc.append(dictio)
		else:
			dictio = dict(zip(labels_usual, one_doc_string))
			db_doc.append(dictio)

	return db_doc

if __name__ == "__main__":
	result = string_2_dict("a4:v2:as:54;h6:bb:8e:30;-70;1496124.120847")
	print(result)