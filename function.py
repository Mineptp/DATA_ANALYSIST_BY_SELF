from matplotlib import pyplot as plt
import pandas as pd


data = pd.read_csv('population.csv');
data_country = data['Country (or dependency)'] 



def Year(a,n)  :
  country_fil= []

  item_str= []
  print(len(data))
  country= [] #tao 1 mang để chứa các nước ứng với số liệu
  Ele_top_sort = [];
  Ele_na = []

  country_fill = []
  item_sort = []
  co = True ;
  cos = 0;
  
  
  for i in range ( len(a))   : # phân truongwf hợp các data có lữ liệu % 
    if( isinstance(a[i], str)) :
      co = False;              
       
      Ele_na.append(float(a[i].replace("%", ""))); # loại bỏ % và in ra kiểu float
 
      
  if ( co == True) :
    Year_sort = sorted(a , reverse=True) #sắp xếp cácthứ tự data mà ng dùng muốn xem
    Ele_top_sort = Year_sort[:n]  #Lấy top 
    Ele_top_sort.reverse();
  else : 
     Ele_sort_nan = sorted(Ele_na,reverse = True )
     Ele_top_sort = Ele_sort_nan[:n] ;
     Ele_top_sort.reverse() 
   

  for  item in Ele_top_sort   : #chạy vòng lặp 1-> item chưa các data đã đc sắp xếp
       
       item_str.append(str(item)+'%')  
       item_sort.append(item)     
    
  if (co == True) : #trường hợp mảng ko có kí hiệu %
     
     for item3 in item_sort:
        
        for item2 in range (len(data)) : #chạy vòng lặp 2-> item2 đc chạy để trong len để có thể lấy đc vị trí tỏng file csv 
         
          if(item3 == a[item2]):  #so sánh để lấy vị trí ( item2)
            #printitem2
            country.append(data_country[item2])

  else :  #trường hợp mảng  có kí hiệu %
       for item3 in range (len(item_str)) :
    
        for item2 in range (len(data)) : #chạy vòng lặp 2-> item2 đc chạy để trong len để có thể lấy đc vị trí tỏng file csv 
         
          if(item_str[item3] == a[item2]):  #so sánh để lấy vị trí ( item2)
        
           country.append(data_country[item2])    # lấy đc vị trí ta sẽ dùng vị trí đó để tra ra số liệu đó của nước nào và tập hợp chugf bằng 1 mảng khác
  # print(Ele_top_sort)
  
  for i in country: #dò trong mảng các nước
    count_coun = country.count(i) #kiểm tra xem các nước nào bị trùn lặp trong mảng
    cos += count_coun #đếm biến cos , vì nếu ko trùng thì chắc chắn giá trị cos sẽ bằng số top muốn xe
    
  for i in country:
    if cos > n: # nếu cos vượt quá số top
        if i not in country_fill: # dò xem cái nào chưa có trong mảng country gốc và add vào và ko tính cái trùng
            country_fill.append(i)
            country_fil = country_fill[:n] #lọc lấy các nước cần thiết 
    else :    
           country_fil.append(i);# trường hợp ko bị trùng
  print(country_fil)
  if len(country) > 0 and len(Ele_top_sort) > 0: #ktra lỡ bảng trống và ko có data thì sẽ ko chayk lập bảng
   
   
   plt.barh(country_fil, Ele_top_sort) #vẽ biểu đồ ưu tiên trục y
     
   plt.ylabel("Country")#tên trục y
   plt.xlabel("Data for " + a.name ); #tên trục x

   plt.tight_layout()
   plt.show()
   

