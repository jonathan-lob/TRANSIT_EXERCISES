import json
import urllib
import requests

class rail_lines():
	def enc_req_get(self, url):
	    """get API request"""
	    headers = {'Accept': 'application/json', 'Authorization': 'Bearer f9fed311243b4d7a94c9596d46b566cc'}
	    key = "f9fed311243b4d7a94c9596d46b566cc"
	    try:
	    	r =  requests.get(url, headers=headers)
	    	parsed_reponse=json.loads(r.content)
	    	return parsed_reponse, r.status_code
	    except e as error:
		    print(error)
		    print("request status_code:" + r.status_code)

	def display_get_mbta_rail_line(self, type):
		"""
				get _light_rail [type]=0
				get _heavy_rail [type]=1
		"""
		if type == 0:
			rail_type = "light"
		else:
			rail_type = "heavy"
		rq = 'https://api-v3.mbta.com/routes?filter[type]=' + str(type)
		print("\n\n\n" + rail_type + " rail lines USING FILTER method for efficiency and to minimize load on API server:\n")
		data, stat = self.enc_req_get(rq)
		if stat == 200:
			ld_data = data["data"]
			for rec in ld_data:
			    print(rec["attributes"]["long_name"])
		else:
			print("An error occurred")


if __name__ == "__main__":
