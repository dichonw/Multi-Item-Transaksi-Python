import os
clear = lambda : os.system('cls')

ulang = "y"
while ulang=="y" or ulang=="Y":
    kodeMenu = [1,2]
    namaMenu = ['makanan', 'minuman']
    kodeMkn =[1,2,3,4,5,6]
    kodeMnm =[1,2,3,4,5]
    makanan = ['Nasi Goreng','Lontong Goreng','Bakso Goreng','Rujak Goreng','Rujak Bakso','Rujak Bakso Pecel ']
    minuman = ['Teh Dingin/Hangat/panas','Kopi Dingin','Kopi Teh Panas','Coca Cola Dingin','Coca Cola Panas']
    hargaMkn = [15000,14900,12900,13000,15000,17000]
    hargaMnm = [2500,5000,6500,3500,5000]
    cartNm = []
    cartHrg = []
    cartQty = []
    cartSubtotal = []
  
    inp = 1
    while inp < 3:
        clear()
        print ("==============================================")
        print("{:^44}".format("Selamat Datang"))
        print("{:^44}".format("Kantin Fakultas Tek. Informatika"))
        print ("==============================================")
        print("{:^44}".format("Pilihan Menu ="))
        print("{:^44}".format("1. Makanan | 2. Minuman"))
        print ("==============================================")
        pil = int(input("Masukan Kode Menu = "))
        inp = pil
        if inp <= len(kodeMenu) :

            i = 0
            while i<len(kodeMenu):
                if kodeMenu[i] == inp:
                    nmMenu = namaMenu[i]
                i+=1

            clear()
            print ("==============================================")
            print("{:^44}".format("PILIHAN MENU " + nmMenu.upper()))


            if nmMenu == 'makanan' :
                print("==============================================")
                nmr = 1
                a = 0
                for nama in makanan:
                    hrg = hargaMkn[a]
                    print(str(nmr) + ". " + "{:24}".format(str(nama)) + "| Rp " + format(hrg,',.2f'))
                    nmr = nmr + 1
                    a = a + 1
                print("==============================================")
                pilihanMkn = int(input("Masukan Kode Menu   = "))
                inpMkn = pilihanMkn

                if inpMkn <= len(makanan) :
                    i = 0
                    while i<len(makanan):
                        if kodeMkn[i] == inpMkn:
                            nmMakan = makanan[i]
                            hrgMakan = hargaMkn[i]
                        i+=1
                else:
                    break
                
                qtyMkn     = int(input("Jumlah " + nmMakan + " = "))
                tot_byrMkn = hrgMakan * int(qtyMkn)
                clear()
                print ("==============================================")
                print("{:^44}".format("MENU " + nmMenu.upper() + " TERPILIH"))
                print ("==============================================")
                print("Nama Menu = " + nmMakan)
                print("Harga     = Rp " + format(hrgMakan,',.2f'))
                print("Jumlah    = " + str(qtyMkn))
                print("==============================================")
                print("SubTotal  = Rp " + format(tot_byrMkn,',.2f'))

                jmlNm = len(cartNm)
                cartNm.insert(jmlNm, nmMakan)
                jmlHrg = len(cartNm)
                cartHrg.insert(jmlHrg, hrgMakan)
                jmlQty = len(cartNm)
                cartQty.insert(jmlQty, qtyMkn)
                jmlSubtotal = len(cartSubtotal)
                cartSubtotal.insert(jmlSubtotal, tot_byrMkn)

            elif nmMenu == 'minuman' :
                print("==============================================")
                nmr = 1
                a = 0
                for nama in minuman:
                    hrg = hargaMnm[a]
                    print(str(nmr) + ". " + "{:24}".format(str(nama)) + "| Rp " + format(hrg,',.2f'))
                    nmr = nmr + 1
                    a = a + 1
                print("==============================================")
                pilihanMnm = int(input("Masukan Kode Menu   = "))
                inpMnm = pilihanMnm

                if inpMnm <= len(minuman) :
                    i = 0
                    while i<len(minuman):
                        if kodeMnm[i] == inpMnm:
                            nmMinum = minuman[i]
                            hrgMinum = hargaMnm[i]
                        i+=1
                else:
                    break
                qtyMnm     = int(input("Jumlah " + nmMinum + " = "))
                tot_byrMnm = hrgMinum * int(qtyMnm)
                clear()
                print ("==============================================")
                print("{:^44}".format("MENU " + nmMenu.upper() + " TERPILIH"))
                print ("==============================================")
                print("Nama Menu = " + nmMinum)
                print("Harga     = Rp " + format(hrgMinum,',.2f'))
                print("Jumlah    = " + str(qtyMnm))
                print("==============================================")
                print("SubTotal  = Rp " + format(tot_byrMnm,',.2f'))
                
                jmlNm = len(cartNm)
                cartNm.insert(jmlNm, nmMinum)
                jmlHrg = len(cartNm)
                cartHrg.insert(jmlHrg, hrgMinum)
                jmlQty = len(cartNm)
                cartQty.insert(jmlQty, qtyMnm)
                jmlSubtotal = len(cartSubtotal)
                cartSubtotal.insert(jmlSubtotal, tot_byrMnm)

            else :
                break
            
            print("")
            ulang = input('Tambah Menu lain? (y/t) : ')
            if ulang == 't' or ulang == 'T':
                clear()
                print("===================================================")
                print("{:^49}".format("DETAIL TRANSAKSI"))
                print("===================================================")
                nmr = 1
                a = 0
                for nama in cartNm:
                    hrg = cartHrg[a]
                    qty = cartQty[a]
                    subtotal = cartSubtotal[a]
                    print("{:26}".format(str(nama)) + str(qty) +" X " + "{:10}".format(str(format(hrg,',.2f'))) + "= " + format(subtotal,',.2f'))
                    nmr = nmr + 1
                    a = a + 1
                print("===================================================")
                totalByr = sum(cartSubtotal)
                print("{:49}".format("Total Bayar = " + format(totalByr,',.2f')))
                
                bayar = 0
                while bayar < totalByr :
                    bayar = int(input("Bayar = "))

                    if bayar < totalByr :
                        print("Uang Anda Kurang Kak!!!")
                    kembalian = bayar - totalByr
                    
                else :
                    print("Kembalian = " + format(kembalian,',.2f'))
                    break
        else:
            break




    
    
            
        