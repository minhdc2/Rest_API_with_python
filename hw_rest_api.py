from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
app = Flask(__name__)
api = Api(app)

class command(Resource):
	# Define POST function to put JSON data into 'example' variable. 
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('pool', type = int, action = 'append')
        parser.add_argument('percentile', type = float)
        params = parser.parse_args()

        unit = {
          'pool': params['pool'],
          'percentile': params['percentile']
        }
		
		
        global example
        #'example' is a global variable which contains input data
        example = []
        example.append(unit)

        return unit, 200
	
	# Define GET function to display calculated quantile using input data from POST request.
    def get(self):
		
        def sort_func(seq): 
        	# Define sort function in case sort() is not allowed to be used.
            ln = len(seq)
            for k in range(ln):
                for i in range(ln-1):
                    if seq[i] > seq[i+1]:
                        seq[i], seq[i+1] = seq[i+1], seq[i]
            return seq

        def quantile_calc(seq, perc):
        	# Define quantile calculation function
            sort_func(seq)
            ln = len(seq)
            pos = (ln-1)*perc/100 + 1
            n = int(pos)
            calc_quantile = round(pool[n-1] + (pool[n] - pool[n-1])*(pos - n), 3)
            return calc_quantile
		
        pool = example[0]['pool'] # Assign value to 'pool' variable
        percentile = example[0]['percentile'] # Assign value to 'percentile' variable
        val = quantile_calc(pool, percentile) # Use 'pool' and 'percentile' variable to calculate quantile

        return val, 200

api.add_resource(command, '/example')

if __name__ == '__main__':
    app.run(debug=True)



