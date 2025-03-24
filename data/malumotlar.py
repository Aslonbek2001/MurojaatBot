from app.states import Xodim

###################################################
########### Universitet xodimlari uchun ###########


rektor = Xodim('Rektor1', 917999618)
korupsiya = Xodim('Korupsiyaga qarshi kurashish', 917999618)
qabul = Xodim('Qabul komisyasi', 917999618)
buxgalteriya = Xodim('Buxgalteriya', 917999618)
registrator = Xodim('Registrator ofis', 917999618)
hemis = Xodim('Hemis', 917999618)
test1 = Xodim("Test1", 13372189)



# Bu yerga ham kiritildi

xodimlar = {
    'rektor': rektor,
    'hemis': hemis,
    'korupsiya': korupsiya,
    'buxgalteriya': buxgalteriya,
    'registrator': registrator,
    'qabul': qabul,
    'test1': test1,
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


murojat_turlari = {
    'shikoyat': 'Shikoyat',
    'taklif': 'Taklif',
    'ariza': 'Ariza',
    'boshqa': 'Boshqa',
    'orqaga': 'Orqaga',
}


CHANNELS = ("@testgfufff",)



