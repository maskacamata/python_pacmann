# latihan























# # soal 1 | row & col
# myList = [['ayam', 'gajah', 'harimau', 'kuda', 'elang'],
#           ['angsa', 'badak', 'singa', 'keledai', 'lovebird']]

# def check_structure(inputList):
    
#     jumlah_row = len(inputList)
#     jumlah_col = len(inputList[0])

#     data_shape = [jumlah_row, jumlah_col]
#     return [jumlah_row, jumlah_col]

# data_shape = check_structure(myList)

# print(data_shape)

# soal 2 | weigthed average
# data = [10, 20, 30, 40, 50]
# w = [0.10, 0.20, 0.25, 0.3, 0.15]

# data = [12, 13.5, 9.8, 10.3]
# w = [0.10, 0.20, 0.30, 0.40]

# def calc_weighted_avg(inputData, weight):
#     lv_nilai_total = 0
#     lv_jumlah_data = len(inputData)

#     for i in range(len(inputData)):
#         lv_nilai_total = lv_nilai_total + ( inputData[i] * weight[i] )
    
#     lv_avg = lv_nilai_total / lv_jumlah_data

#     return lv_nilai_total

# nilai_total = calc_weighted_avg(data, w)
# print(nilai_total)

# # soal 3 | Which toko is profitable?
# toko_ID = ['A001', 'B002', 'C003', 'D004']
# revenues = [80000, 120000, 57000, 450000]
# costs = [90000, 110000, 57000, 420000]

# def profitable_toko(tokoList, revenueList, costList):
#     profitable_toko = []
#     for i in range(len(tokoList)):
#         if revenueList[i] > costList[i]:
#             profitable_toko.append(tokoList[i])
    
#     return profitable_toko

# toko_profit = profitable_toko(toko_ID, revenues, costs)

# print(toko_profit)

# soal 4 | Phone number cleansing
# phone_lists = [
#     '821233clea21123',
#     '082321123321',
#     '+6282-456-654-456',
#     '+62 82 789 987 789',
#     '14045',
#     '82145-451-145'
# ]

# def clean_phone_number(phoneList):
#     # cek awalan 62
#     for i in range(len(phoneList)):
#         phone_nr_temp = phoneList[i]
#         cleansed_nr = ''

#         for j in range(len(phone_nr_temp)):
#             # print(phone_nr_temp[j])

#             if phone_nr_temp[j] in ('0123456789'):
#                 cleansed_nr = cleansed_nr+phone_nr_temp[j]    

#         # jumlah digit
#         if len(cleansed_nr) < 11:
#             cleansed_nr = 'invalid number'
#             not_valid = True
#         else:
#             not_valid = False

#         if not_valid == False:
#             if len(cleansed_nr) == 11:
#                 cleansed_nr = '62'+cleansed_nr
#             elif len(cleansed_nr) > 11:
#                 if cleansed_nr[0] == '0':
#                     cleansed_nr = cleansed_nr.replace('0','62', 1)

#         phoneList[i] = cleansed_nr    
    
#     return phoneList

# cleansed_list = clean_phone_number(phone_lists)
# print(cleansed_list)

# soal 5 | Nearest tourism object
# def calc_dist(coord_obj_a, coord_obj_b):
#     distance = ( ( (coord_obj_a[0] - coord_obj_b[0]) ** 2 ) +  ( (coord_obj_a[1] - coord_obj_b[1]) ** 2 ) ) ** 0.5
#     return distance

# def find_nearest(current_coor, tourism_coor, tourism_name):
#     nearest = {'tourism_name':'', 'distance':0.0}

#     for i in range(len(tourism_name)):
#         distance = calc_dist(current_coor, tourism_coor[i])

#         if nearest['distance'] == 0.0:
#             nearest.update({'tourism_name': tourism_name[i], 
#                             'distance':distance})
#         elif nearest['distance'] > 0:
#             if distance < nearest['distance']:
#                 nearest.update({'tourism_name': tourism_name[i], 
#                                 'distance':distance})
    
#     return nearest

# tourism_name = [
#     'Pantai A',
#     'Jembatan B',
#     'Taman C',
#     'Danau D',
#     'Perpustakaan E',
#     'Mall F',
#     'Monumen G',
#     'Taman Hutan H',
#     'Air terjun I',
#     'Gunung J'
# ]

# tourism_coor = [
#     [-34.93, -31.23],
#     [-77.90, 79.90],
#     [46.67, 40.44],
#     [21.83, 1.94],
#     [41.77, -63.44],
#     [-1.10, -47.22],
#     [68.81, 64.65],
#     [-21.23, 22.03],
#     [68.30, -69.73],
#     [12.82, 30.75],
# ]

# current_coor = [-2.21, 3.15]

# nearest = find_nearest(current_coor, tourism_coor, tourism_name)
# print(nearest)

# soal 6 | size people in same groups
# def distribute_user(peopleNum, groupNum):
#     # create grup
#     group_list = []
#     for i in range(groupNum):
#         group_list.append(0)

#     peopleLast = peopleNum
#     for people in range(peopleNum):
#         if peopleLast == 0:
#             exit

#         for i in range(groupNum):
            
#             if peopleLast != 0:
#                 group_list[i] = group_list[i] + 1
#                 peopleLast = peopleLast - 1
#             elif peopleLast == 0:
#                 exit
    
#     return group_list

# n = 35
# k = 4

# group_size = distribute_user(n,k)
# print(group_size)

# soal 7 


