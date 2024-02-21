pack_iphone_list = ('''

                        1.Iphone 15 ProMAX
                        2.Iphone 15 Pro 
                        3.Iphone 15 

''')
iphone15promaxspeci = ('''
                                                Iphone 15 Pro MAX
                                                Cost = 1300$
                                                Ram = 12 GB 
                                                Rom = 256 GB 1300$ / 512 GB 1350$ / 1 TB 1400$ Cost are Changeable
                                                .
                                                .
                                                .
                                                .
                                                .
                                                
''')
iphone15prospeci = ('''
                                                ............................
                                                ..........................
                                                ..................
                                                ................
                                                Changeable when if you want to your shop 
                                                
''')
iphone15speci = ('''
                                                Not Exist in Demo 
''')

used_iphone_list = ('''
                        1.Iphone 14 ProMAX
                        2.Iphone 14 Pro
                        3.Iphone 14
                        4.Iphone 13 Pro MAX 
                        5.Iphone 13 Pro
                        6.Iphone 13
                        7.Iphone 12 Pro MAX 
                        8.Iphone 11 Pro Max
                        9.Iphone X MAX
                        10.Iphone XS
                        11.Iphone XR
                        12.Iphone X
                        13.Iphone 8 Plus
                        14.Iphone 8
                        15.Iphone 7 Plus  
                        16. ....................
''')
print('''Welcome Example Store AI Bot
'To buy full web-app Contact to here saborrasooli5@gmail.com '
''')
print('''
                                   
                                    List of Iphone
                          1)Pack Iphone           2)Used Iphone
''')
chose_coustomer = input('Which Type of IPhone Do You Want Chose By Number >  ')
if chose_coustomer == '1':
    print(pack_iphone_list)
    Pack_iphone_select = input('Which Model You need Chose By Number >  ')
    if Pack_iphone_select == '1':
        print(iphone15promaxspeci)
    if Pack_iphone_select == '2':
        print(iphone15prospeci)
    if Pack_iphone_select == '3':
        print(iphone15speci)
if chose_coustomer == '2':
    print(used_iphone_list)
else:
    print('''
    Chose By Number! 
    I don`t recognize you enter in number
    Coded By Saborrasoolipy
    ''')
print('''
Follow me at Github : github.com/saborrasoolipy
email you suggestion at : Saborrasooli5@gmail.com   
We also have Web Design 
Contact us!!!

''')