import requests
import bs4
import sendmail
import json

def mkdata(st):
	req = requests.get('https://okky.kr/jobs/contract?jobType=CONTRACT&filter.minPay=700&page='+str(st))
	html = req.text
	#soup = bs4.BeautifulSoup(html, 'html.parser')
	soup = bs4.BeautifulSoup(html, 'html.parser')
	#print(soup)
	data = [
		json.loads(x.string) for x in soup.find_all("script",type="application/json")
	]
	#print(data)
	for i in data:
		list = i['props']['pageProps']['result']['content']

	return list

def searchjob(rr):
	
	result = '''
	<html><head>
	<style>
	table{border: solid 1px black; border-collapse:collapse}
	td{border: solid 1px black ; text-align:center; }
	tr{border: solid 1px black }
	</style>
	</head><body>
	<h2>okky jobs 구인</h2>
	<table>
	<colgroup><col width="5%"><col width="25%"><col width="15%"><col width="20%"></colgroup>
	<tr style="border:solid 1px black"><td>번호</td><td>링크</td><td>금액</td><td>일정</td><td>위치</td><td>기술사항</td></tr>
	'''
	for t in  range(len(rr)):
		#print(rr[t])
		#print(' , '.join([s['name'] for s in  rr[t]['recruitResponse']['tags']]))
		result += '<tr style="background-color: #bbdefb"><td>'+str(t+1)+'</td><td><a href="https://jobs.okky.kr/recruits/'+str(rr[t]['id'])+'">'+rr[t]['title']+'</a></td>'
		result += '<td>'+str(rr[t]['recruitResponse']['minPay'])+' ~ '+str(rr[t]['recruitResponse']['maxPay'])+'</td>'
		result += '<td>'+str(rr[t]['recruitResponse']['startDate'])+'</td>'
		result += '<td>'+str(rr[t]['recruitResponse']['city'])+' '+str(rr[t]['recruitResponse']['district'])+'</td>'
		#result += '<td>'+str(rr[t]['recruitResponse']['tags'][:])+'</td></tr>'	
		result += '<td>'+' , '.join([s['name'] for s in rr[t]['recruitResponse']['tags']])+'</td></tr>'

	return result

if __name__ == '__main__':
	result2  =''
	rr = []
	for x in range(1,6):
		rr +=  mkdata(x)

	result2  = searchjob(rr)
	result2 +='</table></body></html>'
	#print(result2)
	
	sendmail.sendmail2('noreply@gmail.com','yayoye117@gmail.com','Jobs - OKKY',result2)

