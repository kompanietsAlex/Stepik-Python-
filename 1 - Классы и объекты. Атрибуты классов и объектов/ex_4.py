class Notes:
	pass


d = {"uid": 1005435,
	 "title": "Шутка",
	 "author": "И.С. Бах",
	 "pages": 2}

for k, v in d.items():
	setattr(Notes, k, v)

print(getattr(Notes, "author"))