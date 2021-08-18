from django.db import models

# Create your models here.

#北海道・東北
#北海道
class Es_model_hokkaido(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
#青森   
class Es_model_aomori(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
#秋田   
class Es_model_akita(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
#岩手   
class Es_model_iwate(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        


#山形   
class Es_model_yamagata(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
#宮城   
class Es_model_miyagi(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
#福島   
class Es_model_fukushima(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
#関東
#群馬
class Es_model_gunma(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
#栃木
class Es_model_tochigi(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
#茨城
class Es_model_ibaraki(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
#埼玉
class Es_model_saitama(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
#千葉
class Es_model_chiba(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
#東京
class Es_model_tokyo(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
#神奈川
class Es_model_kanagawa(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
    
    
#中部   
#新潟
class Es_model_nigata(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
    
#富山
class Es_model_toyama(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
    
#石川
class Es_model_ishikawa(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
    
#福井
class Es_model_fukui(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
    
#長野
class Es_model_nagano(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
#岐阜
class Es_model_gifu(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
#山梨
class Es_model_yamanashi(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
#愛知
class Es_model_aichi(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
#静岡
class Es_model_shizuoka(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
#近畿    
#京都
class Es_model_kyoto(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
    
#滋賀
class Es_model_shiga(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
    
#大阪
class Es_model_osaka(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
#奈良
class Es_model_nara(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
#三重
class Es_model_mie(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
    
#和歌山
class Es_model_wakayama(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
#兵庫
class Es_model_hyougo(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        

#中国    
#鳥取
class Es_model_tottori(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
    
#岡山
class Es_model_okayama(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
    
#島根
class Es_model_shimane(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
    
#広島
class Es_model_hiroshima(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
    
#山口
class Es_model_yamaguchi(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    

#四国    
#香川
class Es_model_kagawa(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
    
#愛媛
class Es_model_ehime(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
    
#徳島
class Es_model_tokushima(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
    
#高知
class Es_model_kouchi(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        

    
#九州・沖縄    
#福岡
class Es_model_fukuoka(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
    
#佐賀
class Es_model_saga(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
    
#長崎
class Es_model_nagasaki(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
    
#大分
class Es_model_oita(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
    
#熊本
class Es_model_kumamoto(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
    
#宮崎
class Es_model_miyazaki(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
    
#鹿児島
class Es_model_kagoshima(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    
    
#沖縄
class Es_model_okinawa(models.Model):
    invest_place = models.CharField(max_length=100)
    invest_price = models.CharField(max_length=100)
    invest_yield = models.CharField(max_length=100)
    invest_age = models.CharField(max_length=100)
    URL = models.URLField()
    postdate = models.DateField(auto_now_add=True)
    
    
    
        
    