
import pandas as pd
from matplotlib import pyplot as plt



plt.style.use("fivethirtyeight")
data = pd.read_csv('population.csv');



#Phân data thành các phần nhỏ
data_populations = data['Population (2020)'];
data_Net = data['Net Change'];
data_Des = data['Density'];
data_Yearly =data['Yearly Change %'];
data_Land_area = data['Land Area'];
data_Migrants = data['Migrants (net)'];
data_Urban_pop = data['Urban Pop %'];
data_Fert = data['Fert. Rate'];
data_Med = data['Med. Age (Age)'];
data_Worldshare=data['World Share %'];

datas = []
dataa = [
   datas,
   data_populations,
   data_Net,
   
   data_Yearly,
   data_Land_area,
   data_Migrants,
   data_Urban_pop,
   data_Fert,
   data_Med,
   data_Worldshare,
   data_Des,
]

in_1 = int(input("1) Xem tất cả \n2) Xem đơn \n") );

import function 
while True : 


 while in_1 == 1 :
  n = int(input("Nhập top muốn xem : "))
  for i in dataa :
    function.Year(i,n)
  in_1 = int(input("1) Xem tất cả \n2) Xem đơn \n 3) Thôi") )
 while in_1 == 2: 
     in_ = int(input(" Nhap dữ liệu muốn xem: \n 1) Population (2020) \n 2) Net Change \n 3) Yearly Change \n 4) Land Area\n 5) Migrants (net) \n 6) Urban Pop % \n 7) Fert. Rate \n 8) Med. Age \n 9) World Share % \n 10) Density \n "));
     m = int(input("Nhập top muốn xem : "))
     function.Year(dataa[in_],m);
     in_1 = int(input("1) Xem tất cả \n2) Xem đơn \n 3) Thôi") )
 while in_1 == 3 :
    print("Ket Thuc")
    break;
