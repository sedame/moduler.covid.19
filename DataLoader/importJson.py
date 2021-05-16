import mysql.connector as MC
import json

json_data = open("DataLoader/covid.json").read()
json_obj=json.loads(json_data)

try:
	conn = MC.connect(host="localhost",user="root",password="viesurnous", database="covid")

	cursor = conn.cursor()
	
	for item in json_obj:

		ncommunique=item.get("id_communique")
		date=item.get("date_communique")
		test=item.get("nb_tests")
		cas=item.get("nb_cas")
		contact=item.get("nb_cas_contact")
		communautaire=item.get("nb_cas_communautaire")
		gueris=item.get("nb_gueris")
		deces = item.get("nb_deces")
		try:
			cursor.execute  ("INSERT INTO Communiques values(%s,%s,%s,%s,%s,%s,%s,%s,NOW())",(ncommunique,date,test,cas,contact,communautaire,gueris,deces))
		except Exception:
			pass
		conn.commit()


except MC.Error as err:
	print(err)
finally:
	if(conn.is_connected()):
		cursor.close() 		
		conn.close()