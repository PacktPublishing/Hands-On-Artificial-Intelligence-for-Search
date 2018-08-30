'''
@author: Devangini Patel
'''

#connections between places

navigation = {}
navigation["Bus Stop"] = {"Library"}
navigation["Library"] = {"Bus Stop", "Car Park", "Student Center"}
navigation["Car Park"] = {"Library", "Maths Building", "Store"}
navigation["Maths Building"] = {"Car Park", "Canteen"}
navigation["Student Center"] = {"Library", "Store" , "Theater"}
navigation["Store"] = {"Student Center", "Car Park", "Canteen", "Sports Center"}
navigation["Canteen"] = {"Maths Building", "Maths Building", "AI Lab"}
navigation["AI Lab"] = {"Canteen"}
navigation["Theater"] = {"Student Center", "Sports Center"}
navigation["Sports Center"] = {"Theater", "Store"}
