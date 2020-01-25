import json
import urllib
import requests

class rail_lines(object):
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
        res = []
        if type == 0:
            rail_type = "light"
        else:
            rail_type = "heavy"
        rq = 'https://api-v3.mbta.com/routes?filter[type]=' + str(type)
        #print("\n\n\n" + rail_type + " rail lines USING FILTER method for efficiency and to minimize load on API server:\n")
        data, stat = self.enc_req_get(rq)
        if stat == 200:
            ld_data = data["data"]
            for rec in ld_data:
                res.append(rec["attributes"]["long_name"])
                #print(rec["attributes"]["long_name"])
            return res
        else:
            print("An error occurred")

class rail_line_stops(rail_lines):
    """stops, child of rail_lines"""

    def get_all_stops_attr(self, field_name):
        res = []
        rq = 'https://api-v3.mbta.com/stops'
        data, stat = rail_lines.enc_req_get(self, rq)
        stp_data = data["data"]
        for des in stp_data:
            res.append(des["attributes"][field_name])
        return res

    def filter_stops_for_rail_lines(self):
        all_rail_lines = []
        all_stops_desc = []
        rali_stop_count = {}
        all_rail_lines = rail_lines.display_get_mbta_rail_line(self,0) + rail_lines.display_get_mbta_rail_line(self,1)
        all_stops_desc = self.get_all_stops_attr("description")
        for rail_line in all_rail_lines:
            rali_stop_count[rail_line] = 0
            for stop_desc in all_stops_desc:
                try:
                    if 'Green Line' in rail_line:
                        green_letter = rail_line.split()[2]
                        green_mtch = rail_line.split()[0] + ' ' + rail_line.split()[1]
                        mtch_str = '- ' + green_mtch + ' - (' 
                        if '(' + green_letter + ')' in stop_desc:
                            if mtch_str in stop_desc:
                                rali_stop_count[rail_line] += 1
                    else:
                        mtch_str = '- ' + rail_line + ' -'
                        if mtch_str in stop_desc:
                            rali_stop_count[rail_line] += 1
                except:
                    tt = 0
        return rali_stop_count


if __name__ == "__main__":
    
    
    print("\n\n################################Question 1 output################################\n\n")
    rl = rail_lines()
    print("light rail lines USING FILTER method for efficiency and to minimize load on API server:\n\n")
    for rail_line in rl.display_get_mbta_rail_line(0):
        print(rail_line)
    print("\n\nheavy rail lines USING FILTER method for efficiency and to minimize load on API server:\n\n")
    for rail_line in rl.display_get_mbta_rail_line(1):
        print(rail_line)
    

    print("\n\n\n################################Question 2 output################################\n\n")
    rls = rail_line_stops()
    stops_dict=rls.filter_stops_for_rail_lines()
    key_max = max(stops_dict.keys(), key=(lambda k: stops_dict[k]))
    key_min = min(stops_dict.keys(), key=(lambda k: stops_dict[k]))
    print("max stops on a rail line:" + str(stops_dict[key_max]) + "  on the following line:" + key_max)
    print("min stops on a rail line:" + str(stops_dict[key_min]) + "  on the following line:" + key_min )

