from lxml import html
import requests
import json
import base64
import time
file = open("nomor-brainly-id.txt","r")
startnum = file.readlines()[0]
j = startnum
n = 50000000
for i in range(int(j), n):
    link = ("https://brainly.co.id/tugas/" + str(i))
    fetch = requests.get(link)
    status = fetch.status_code
    if status == 200:
        file1 = open("nomor-brainly-id.txt","w")
        file1.writelines(str(i))
        file1.close()
        print (link)
        tree = html.fromstring(fetch.content) 
        title = tree.xpath('//h1[@data-testid="question_box_text"]/span/text()')
        isi = tree.xpath('//div[contains(concat (" ", normalize-space(@data-testid), " "), "answer_box_text")]/text()')
        isiii = str(title)
	isii = str(isi)
        br = "</br>"
        mytext = isii.replace("\\n",  br).replace("\\xa0", "").replace("\u", "").replace("u'", "'").replace("'", "").replace("u\xa0,", "").replace("u'", "").replace("[", "").replace("]", "")
	juduls = isiii.replace("\\n",  br).replace("\\xa0", "").replace("\u", "").replace("u'", "'").replace("'", "").replace("u\xa0,", "").replace("u'", "").replace("[", "").replace("]", "")
	description = juduls + '&ensp;' + mytext
        url = "https://jogjaprov.com/wp-json/wp/v2/posts"
        user = "admin"
        password = "IbNf 6jk7 8Ec5 EbuV S1Tb wYOU"
        credentials = user + ':' + password
        token = base64.b64encode(credentials.encode())
        header = {'Authorization': 'Basic ' + token.decode('utf-8')}
        post = {
            'title'    : title,
            'status'   : 'publish', 
            'content'  : description,
            'slugs': 'tanya-jawab'
        }
        responce = requests.post(url , headers=header, data=post)
        resp = responce.status_code
        if resp == 201:
            print (resp)
file.close()
