class TravelBlog:
	total_blogs = 0


tb1 = TravelBlog()
setattr(tb1, "name", 'Франция')
setattr(tb1, "days", 6)
TravelBlog.total_blogs += 1

tb2 = TravelBlog()
setattr(tb2, "name", 'Италия')
setattr(tb2, "days", 5)
TravelBlog.total_blogs += 1