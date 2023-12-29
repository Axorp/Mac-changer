# -*- coding: utf-8 -*-

import os 

def mac_degis():
    print("""
    
███████   ██ ██   ██████  ███████ ██████   
██   ██  ██ ██  ██    ██ ██   ██ ██   ██ 
███████   ███   ██    ██ ██████  ██████  
██   ██  ██ ██  ██    ██ ██   ██ ██      
██   ██ ██   ██  ██████  ██   ██ ██      
                                         
                                         
/////////-------------------------
           MAC CHANGER    
        ------------------------///////////
        
            0-   Mac Değiştir
            1-   Mac Adresini elle Değiştir
            2-   Default Mac adresi
                
    """)
                
    islemno = input("İşlem no Giriniz : ")
    if islemno == "0":
        os.system("ifconfig eth0 down") 
        os.system("sudo macchanger -r eth0 ")
        os.system("ifconfig eth0 up")
        print("Mac Adresi Değiştirme Başarılı")
               
    elif islemno == "1":
        mac = input("Mac Adresi giriniz : ")
        os.system("ifconfig eth0 down")
        os.system("sudo macchanger --mac " + mac + " eth0")
        os.system("ifconfig eth0 up")
        print("Mac Manuel olarak başarıyla değiştirildi")
        
    elif islemno == "2":
        os.system("ifconfig eth0 down")
        os.system("sudo macchanger -p eth0")
        os.system("ifconfig eth0 up")
        print("Mac Adresi Default hale getirildi.")

mac_degis()

