# Testing git commit
from django.shortcuts import render

def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_request = requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=25&API_KEY=1FF598CD-79A4-4C22-8476-9EDD2A8C1718")
		category_description = ""
		category_color = ""
		try:
			api = json.loads(api_request.content)
			if api[0]['Category']['Name'] == "Good":
				category_description = "(0-50) : Air quality is acceptable; Air quality posses little to no risk."
				category_color = "good"
			if api[0]['Category']['Name'] == "Moderate":
				category_description = "(51-100) : Air quality is acceptable; However, some pollutants there may be some health concerns for individuals who are sensitive to air pollutions."
				category_color = "moderate"
			if api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
				category_description = "(101-150) : Although general public is not likely to be affected by this AQI range, however people with lung diseases, heart diseases, older adults and children are at greater risk from the exposure to the ozone and from the presence of particles in the air."
				category_color = "usg"
			if api[0]['Category']['Name'] == "Unhealthy":
				category_description = "(151-200) : Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
				category_color = "unhealthy"
			if api[0]['Category']['Name'] == "Very Unhealthy":
				category_description = "(201-300) : HEALTH ALERT !!! Everyone may experience more serious health effects."
				category_color = "veryunhealthy"
			if api[0]['Category']['Name'] == "Hazardous":
				category_description = "(301-500) : HEALTH WARNING !!! This entire population is more likely to be affected."
				category_color = "hazardous"
		except Exception as e:
			api = "Error..."

		return render(request, 'home.html',
			{'api': api, 
			'category_description' : category_description, 
			'category_color' : category_color
			}
		)

	else:
		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=1FF598CD-79A4-4C22-8476-9EDD2A8C1718")
		category_description = ""
		category_color = ""
		try:
			api = json.loads(api_request.content)
			if api[0]['Category']['Name'] == "Good":
				category_description = "(0-50) : Air quality is acceptable; Air quality posses little to no risk."
				category_color = "good"
			if api[0]['Category']['Name'] == "Moderate":
				category_description = "(51-100) : Air quality is acceptable; However, some pollutants there may be some health concerns for individuals who are sensitive to air pollutions."
				category_color = "moderate"
			if api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
				category_description = "(101-150) : Although general public is not likely to be affected by this AQI range, however people with lung diseases, heart diseases, older adults and children are at greater risk from the exposure to the ozone and from the presence of particles in the air."
				category_color = "usg"
			if api[0]['Category']['Name'] == "Unhealthy":
				category_description = "(151-200) : Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
				category_color = "unhealthy"
			if api[0]['Category']['Name'] == "Very Unhealthy":
				category_description = "(201-300) : HEALTH ALERT !!! Everyone may experience more serious health effects."
				category_color = "veryunhealthy"
			if api[0]['Category']['Name'] == "Hazardous":
				category_description = "(301-500) : HEALTH WARNING !!! This entire population is more likely to be affected."
				category_color = "hazardous"
		except Exception as e:
			api = "Error..."

		return render(request, 'home.html',
			{'api': api, 
			'category_description' : category_description, 
			'category_color' : category_color
			}
		)

def about(request):
	return render(request, 'about.html', {})