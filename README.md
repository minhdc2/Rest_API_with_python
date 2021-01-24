I. INTRUCTIONS
The pack includes 3 *.py files:
1. hw_rest_api.py - REST_API engine
2. hw_rest_api_post.py - Run to POST input data
3. hw_rest_api_get.py - Run to GET calculated quantile using input data from POST request

II. TEST CASES \n
Local host environment


Ex1: {'pool': [1,7,2,6], 'percentile': 99.5} \n
	python hw_rest_api_post.py
	![Local_host.PNG](attachment:Local_host.PNG)
	
	python hw_rest_api_get.py

	np.quantile()	

Ex2: {'pool': [100, 50, 500, 400, 700, 200], 'percentile': 80} \n
	python hw_rest_api_post.py

	python hw_rest_api_get.py

	np.quantile()

Ex3: {'pool': [100, 90, 80, 70, 60, 50, 40, 30, 20, 10], 'percentile': 94} \n
	python hw_rest_api_post.py

	python hw_rest_api_get.py

	np.quantile()
