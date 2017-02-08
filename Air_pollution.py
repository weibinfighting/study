import requests
from bs4 import BeautifulSoup

url = 'http://datacenter.mep.gov.cn/report/air_daily/airDairyCityHour.jsp?city=%C4%CF%BE%A9%CA%D0&startdate=2014-01-01%2017:00&enddate=2016-12-26%2017:00&page=2'
soure = requests.get(url)
soup = BeautifulSoup(soure.text,'lxml')
print(soup)
time = soup.select('tbody > tr:nth-child > td:nth-child(3)')
index = soup.select('#report1 > tbody > tr:nth-child > td:nth-child(4)')
rank = soup.select('#report1 > tbody > tr:nth-child > td:nth-child(5)')
pollution = soup.select('#report1 > tbody > tr:nth-child > td:nth-child(6)')
print('\n______\n*******\n',time,'\n_____\n',index,'\n***********\n',rank,'\n***********\n',pollution,'\n***********\n')
Data_time,Data_index,Data_rank,Data_pollution = [],[],[],[]
for time,index,rank,pollution in zip(time,index,rank,pollution):
    print(time.get_text(),'\n~~~~\n')
    Data_time.append(time.get_text())
    print(index.get_text(),'\n~~~~\n')
    Data_index.append(index.get_text())
    print(rank.get_text(),'\n~~~~\n')
    Data_rank.append(rank.get_text())
    print(pollution.get_text(),'\n~~~~\n')
    Data_pollution.append(pollution.get_text())
print(Data_time,Data_index,Data_rank,Data_pollution,sep="\n__________\n")
#f = open(r'F:\R\file\job1.txt','a')
#for i in list(range(0,len(Data_posion))):
#    print(Data_posion[i]+' '+Data_salary[i]+' '+Data_place)#+' '+Data_size[i]+' '+Data_peonum[i]+' '+Data_experience+' '+Data_eq+'\n')
#    f.write(Data_posion[i]+' '+Data_salary[i]+' '+Data_place)#+' '+Data_size[i]+' '+Data_peonum[i]+' '+Data_experience+' '+Data_eq+'\n')
#print()
#f.close()
print('done')























#<td class="report1_4" style="color:#00FF00;">2016-12-26&nbsp;17:00</td>
##report1 > tbody > tr:nth-child(3) > td:nth-child(3)
##