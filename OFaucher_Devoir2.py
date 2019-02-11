#coding: utf-8

import json
import csv
import requests

fichier = "Banq.csv"

url = "http://collections.banq.qc.ca/api/service-notice?handle=52327/"

entete = {
	"User-Agent":"Olivier Fauccher: journaliste",
	"From":"faucher.olivier@courrier.uqam.ca"
}

p = ["Handle", "Titre", "Auteur", "Année de création", "Description du matériel", "URL"]

f = open(fichier,"a")

banq = csv.writer(f)

banq .writerow(p)



for x in range(1000, 2001):
	
	req = requests.get(url + str(x), headers=entete)

	if req.status_code == 200:

		doc = req.json()

		s = []

		if doc["type"] == "audio":

			title = doc["titre"].split(" /")

			s.append(x)

			s.append(title[0])

			s.append(doc["auteurs"][0])

			s.append(doc["dateCreation"])

			s.append(doc["descriptionMat"])

			s.append(doc["noticeComplete"][0]["liens"][0]["url"])

			print(s)

			f = open(fichier,"a")

			banq = csv.writer(f)

			banq .writerow(s)
