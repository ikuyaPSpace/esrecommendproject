from django.shortcuts import render
from django.views.generic import ListView
from .models import Es_model_hokkaido, Es_model_aomori, Es_model_akita, Es_model_iwate, Es_model_yamagata, Es_model_miyagi, Es_model_fukushima, Es_model_gunma, Es_model_tochigi, Es_model_ibaraki, Es_model_saitama, Es_model_chiba, Es_model_tokyo, Es_model_kanagawa, Es_model_nigata, Es_model_toyama, Es_model_ishikawa, Es_model_fukui, Es_model_nagano, Es_model_gifu, Es_model_yamanashi, Es_model_aichi, Es_model_shizuoka, Es_model_kyoto, Es_model_shiga, Es_model_osaka, Es_model_nara, Es_model_mie, Es_model_wakayama, Es_model_hyougo, Es_model_tottori, Es_model_okayama, Es_model_shimane, Es_model_hiroshima, Es_model_yamaguchi, Es_model_kagawa, Es_model_ehime, Es_model_tokushima, Es_model_kouchi, Es_model_fukuoka, Es_model_saga, Es_model_nagasaki, Es_model_oita, Es_model_kumamoto, Es_model_miyazaki, Es_model_kagoshima, Es_model_okinawa

# Create your views here.

#top
class Es_top(ListView):
    template_name = 'es_top.html'
    model = Es_model_hokkaido

#北海道
class Es_model_hokkaido_List(ListView):
    template_name = 'es_list_hokkaido.html'
    model = Es_model_hokkaido

#青森    
class Es_model_aomori_List(ListView):
    template_name = 'es_list_aomori.html'
    model = Es_model_aomori

#秋田    
class Es_model_akita_List(ListView):
    template_name = 'es_list_akita.html'
    model = Es_model_akita
    
#岩手    
class Es_model_iwate_List(ListView):
    template_name = 'es_list_iwate.html'
    model = Es_model_iwate
    
#山形    
class Es_model_yamagata_List(ListView):
    template_name = 'es_list_yamagata.html'
    model = Es_model_yamagata
    
#宮城    
class Es_model_miyagi_List(ListView):
    template_name = 'es_list_miyagi.html'
    model = Es_model_miyagi
    
#福島    
class Es_model_fukushima_List(ListView):
    template_name = 'es_list_fukushima.html'
    model = Es_model_fukushima
    
#群馬    
class Es_model_gunma_List(ListView):
    template_name = 'es_list_gunma.html'
    model = Es_model_gunma
    
#栃木    
class Es_model_tochigi_List(ListView):
    template_name = 'es_list_tochigi.html'
    model = Es_model_tochigi
    
#茨城    
class Es_model_ibaraki_List(ListView):
    template_name = 'es_list_ibaraki.html'
    model = Es_model_ibaraki
    
#埼玉    
class Es_model_saitama_List(ListView):
    template_name = 'es_list_saitama.html'
    model = Es_model_saitama
    
#千葉    
class Es_model_chiba_List(ListView):
    template_name = 'es_list_chiba.html'
    model = Es_model_chiba
    
#東京    
class Es_model_tokyo_List(ListView):
    template_name = 'es_list_tokyo.html'
    model = Es_model_tokyo
    
#神奈川    
class Es_model_kanagawa_List(ListView):
    template_name = 'es_list_kanagawa.html'
    model = Es_model_kanagawa
    
#新潟    
class Es_model_nigata_List(ListView):
    template_name = 'es_list_nigata.html'
    model = Es_model_nigata
    
#富山    
class Es_model_toyama_List(ListView):
    template_name = 'es_list_toyama.html'
    model = Es_model_toyama
    
#石川    
class Es_model_ishikawa_List(ListView):
    template_name = 'es_list_ishikawa.html'
    model = Es_model_ishikawa
    
#福井    
class Es_model_fukui_List(ListView):
    template_name = 'es_list_fukui.html'
    model = Es_model_fukui
    
#長野    
class Es_model_nagano_List(ListView):
    template_name = 'es_list_nagano.html'
    model = Es_model_nagano
    
#岐阜    
class Es_model_gifu_List(ListView):
    template_name = 'es_list_gifu.html'
    model = Es_model_gifu
    
#山梨    
class Es_model_yamanashi_List(ListView):
    template_name = 'es_list_yamanashi.html'
    model = Es_model_yamanashi
    
#愛知    
class Es_model_aichi_List(ListView):
    template_name = 'es_list_aichi.html'
    model = Es_model_aichi
    
#静岡    
class Es_model_shizuoka_List(ListView):
    template_name = 'es_list_shizuoka.html'
    model = Es_model_shizuoka
    
#京都    
class Es_model_kyoto_List(ListView):
    template_name = 'es_list_kyoto.html'
    model = Es_model_kyoto
    
#滋賀    
class Es_model_shiga_List(ListView):
    template_name = 'es_list_shiga.html'
    model = Es_model_shiga
    
#大阪    
class Es_model_osaka_List(ListView):
    template_name = 'es_list_osaka.html'
    model = Es_model_osaka
    
#奈良    
class Es_model_nara_List(ListView):
    template_name = 'es_list_nara.html'
    model = Es_model_nara
    
#三重    
class Es_model_mie_List(ListView):
    template_name = 'es_list_mie.html'
    model = Es_model_mie
    
#和歌山    
class Es_model_wakayama_List(ListView):
    template_name = 'es_list_wakayama.html'
    model = Es_model_wakayama
    
#兵庫    
class Es_model_hyougo_List(ListView):
    template_name = 'es_list_hyougo.html'
    model = Es_model_hyougo
    
#鳥取    
class Es_model_tottori_List(ListView):
    template_name = 'es_list_tottori.html'
    model = Es_model_tottori
    
#岡山    
class Es_model_okayama_List(ListView):
    template_name = 'es_list_okayama.html'
    model = Es_model_okayama
        
#島根    
class Es_model_shimane_List(ListView):
    template_name = 'es_list_shimane.html'
    model = Es_model_shimane
    
#広島    
class Es_model_hiroshima_List(ListView):
    template_name = 'es_list_hiroshima.html'
    model = Es_model_hiroshima
    
#山口    
class Es_model_yamaguchi_List(ListView):
    template_name = 'es_list_yamaguchi.html'
    model = Es_model_yamaguchi
    
#香川    
class Es_model_kagawa_List(ListView):
    template_name = 'es_list_kagawa.html'
    model = Es_model_kagawa
    
#愛媛    
class Es_model_ehime_List(ListView):
    template_name = 'es_list_ehime.html'
    model = Es_model_ehime
    
#徳島    
class Es_model_tokushima_List(ListView):
    template_name = 'es_list_tokushima.html'
    model = Es_model_tokushima
    
#高知    
class Es_model_kouchi_List(ListView):
    template_name = 'es_list_kouchi.html'
    model = Es_model_kouchi
    
#福岡    
class Es_model_fukuoka_List(ListView):
    template_name = 'es_list_fukuoka.html'
    model = Es_model_fukuoka
    
#佐賀    
class Es_model_saga_List(ListView):
    template_name = 'es_list_saga.html'
    model = Es_model_saga
    
#長崎    
class Es_model_nagasaki_List(ListView):
    template_name = 'es_list_nagasaki.html'
    model = Es_model_nagasaki
    
#大分    
class Es_model_oita_List(ListView):
    template_name = 'es_list_oita.html'
    model = Es_model_oita
    
#熊本    
class Es_model_kumamoto_List(ListView):
    template_name = 'es_list_kumamoto.html'
    model = Es_model_kumamoto
    
#宮崎    
class Es_model_miyazaki_List(ListView):
    template_name = 'es_list_miyazaki.html'
    model = Es_model_miyazaki
  
#鹿児島    
class Es_model_kagoshima_List(ListView):
    template_name = 'es_list_kagoshima.html'
    model = Es_model_kagoshima
    
#沖縄    
class Es_model_okinawa_List(ListView):
    template_name = 'es_list_okinawa.html'
    model = Es_model_okinawa
  