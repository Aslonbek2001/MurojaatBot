from app.states import Xodim

###################################################
######## 👇 Universitet xodimlari uchun 👇 #########
###################################################

rektor = Xodim('Rektor', 917999618)
korupsiya = Xodim('Korupsiyaga qarshi kurashish', 917999618)
qabul = Xodim('Qabul komisyasi', 917999618)
buxgalteriya = Xodim('Buxgalteriya', 917999618)
registrator = Xodim('Registrator ofis', 917999618)
hemis = Xodim('Hemis', 85942449)


# 👇 Xodim kiritilgandan So'ng Pastga ham qo'shiladi 👇

xodimlar = {
    'rektor': rektor,
    'hemis': hemis,
    'korupsiya': korupsiya,
    'buxgalteriya': buxgalteriya,
    'registrator': registrator,
    'qabul': qabul,
}


###################################################
######## Murojat qilivchilar uchun ################
###################################################


murojatchilar = {
    'talaba': 'Talaba',
    'abituriyent': 'Abituriyent',
    'xodim': 'Xodim',
    'ota_ona': 'Ota Ona',
    'boshqa': 'Boshqa',
}


###################################################
################ Murojaat turi. ###################
###################################################


murojat_turlari = {
    'shikoyat': 'Shikoyat',
    'taklif': 'Taklif',
    'ariza': 'Ariza',
    'boshqa': 'Boshqa',
    'orqaga': 'Orqaga',
}


###################################################
################# CHANNELS ########################
###################################################
path_to_channel ='https://t.me/'

CHANNELS = {
        "@testgfufff": "GFU|Rasmiy kanali",
    }



""" Super admin, Javob yuborilganligini ko'rish """