import json
import urllib
import requests



class rail_lines(object):
    """ 
        class to hold rail line types
        chile of python default class object
    """
    
    def enc_req_get(self, url):
        """get API request"""
        key = "f9fed311243b4d7a94c9596d46b566cc"
        headers = {'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(key)}
       
        try:
            #make API request 
            r =  requests.get(url, headers=headers)
            parsed_reponse = json.loads(r.content)
            return parsed_reponse, r.status_code
        except e as error:
            #call requsts get failed-print out status code
            print(error)
            print("request status_code:" + r.status_code)
            exit(1)

    def display_get_mbta_rail_line(self, type, attr_name):
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
        data, stat = self.enc_req_get(rq)
        if stat == 200:
            ld_data = data["data"]
            for rec in ld_data:
                res.append(rec["attributes"][attr_name])
            return res
        else:
            print("An error occurred")

class rail_line_stops(rail_lines):
    """rail line stops, child of rail_lines"""

    def get_all_stops_attr(self, field_name):
        """
        get stop attribute
        """
        res = []
        rq = 'https://api-v3.mbta.com/stops'
        #return requests data and status as tuple 
        data, stat = rail_lines.enc_req_get(self, rq)
        stp_data = data["data"]
        for des in stp_data:
            res.append(des["attributes"][field_name])
        return res

    def filter_stops_for_rail_lines(self):
        """
        
        """
        #initialize lists
        all_rail_lines = []
        all_stops_desc = []
        #initialize dictionary
        rail_stop_count = {}
        #get all rail lines: light and heavy
        all_rail_lines = rail_lines.display_get_mbta_rail_line(self, 0, "long_name") + rail_lines.display_get_mbta_rail_line(self, 1, "long_name")
        all_stops_desc = self.get_all_stops_attr("description")
        for rail_line in all_rail_lines:
            rail_stop_count[rail_line] = 0
            for stop_desc in all_stops_desc:
                try:
                    if 'Green Line' in rail_line:
                        green_letter = rail_line.split()[2]
                        green_mtch = rail_line.split()[0] + ' ' + rail_line.split()[1]
                        mtch_str = '- ' + green_mtch + ' - (' 
                        if '(' + green_letter + ')' in stop_desc:
                            if mtch_str in stop_desc:
                                rail_stop_count[rail_line] += 1
                    else:
                        mtch_str = '- ' + rail_line + ' -'
                        if mtch_str in stop_desc:
                            rail_stop_count[rail_line] += 1
                except:
                    tt = 0
        return rail_stop_count

if __name__ == "__main__":
    

    pre_del ='\n\n################################'
    post_del = '################################\n\n'
    #print out Q1 resuklt
    print("{}{}{}".format(pre_del, 'Question 1 output', post_del))
    rl = rail_lines()
    print("light rail lines USING FILTER method for efficiency and to minimize load on API server:\n\n")
    for rail_line in rl.display_get_mbta_rail_line(0, "long_name"):
        print(rail_line)
    print("\n\nheavy rail lines USING FILTER method for efficiency and to minimize load on API server:\n\n")
    for rail_line in rl.display_get_mbta_rail_line(1, "long_name"):
        print(rail_line)
    
    #print out Q2 results
    print("{}{}{}".format(pre_del, 'Question 2 output', post_del))
    rls = rail_line_stops()
    stops_dict=rls.filter_stops_for_rail_lines()
    #use lambda functions to get min and max dictionary values and corresponding keys
    key_max = max(stops_dict.keys(), key=(lambda k: stops_dict[k]))
    key_min = min(stops_dict.keys(), key=(lambda k: stops_dict[k]))
    #print out min and max
    s1 = "stops on a rail line:"
    s3 = "  on the following line:"
    print("max  {}{}{}{}".format(s1, str(stops_dict[key_max]), s3, key_max))
    print("min  {}{}{}{}".format(s1, str(stops_dict[key_min]), s3, key_min))
