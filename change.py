import json

with open("daily.json", 'r', encoding='utf-8') as file:
	data = json.load(file)
	for j in range(3):
		for i in range(8):
			classname = str(j + 1) + "-" + str(i + 1)
			data[classname][2] = data[classname][4]
	with open("daily_output.json", "w", encoding='utf-8') as file2:
		json.dump(data, file2, ensure_ascii=False, indent=4)
	
