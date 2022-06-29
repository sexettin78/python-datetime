
from datetime import datetime
p =  datetime.now() #tüm tarıh saat ve zamanı p adlı değişkene aktardık. now() yerine today() da kullanabiliriz
p.year #yıl
p.month #ay
p.day #gün
p.hour #saat
p.minute #dakika
p.second #saniye

tarih = datetime.ctime(p) #tarihi okunaklı karakter dizisine çevirir

datetime.strftime(p, "%a") #strftime kullanımı
"""
%a = haftanın gününü kısaltarak gösterir
%A = haftanın gününü gösterir
%b = ayın gününü kısaltarak gösterir
%B = ayın gününü gösterir
%c = tarih, saat, zamanı gösterir
%d = günü sayı olarak gösterir
%j = belirli bir tarihi yılın kaçıncı günü olduğunu gösterir
%m = ayı sayı olarak gösterir
%U = belirli bir tarihi yılın kaçıncı ayı olduğunu gösterir
%y = yıl değerinin son 2 rakamını gösterir
%Y = yıl değerinin tamamını gösterir
%x = tarih bilgisini gösterir
%X = saat bilgisini gösterir

bu çıktılar ingilizce olacaktır. bunları türkçe yapmak için;
import locale
locale.setlocale(locale.LC_ALL, 'Turkish')
""" 

datetime.strptime #böylece verileri tekrar biçimlendirebiliriz. örneğin: datetime.strptime(p, "saat: %X")

zamandamgasi=datetime.timestamp(p) #zaman damgası oluşturduk

zaman = datetime.fromtimestamp(zamandamgasi) #üretilen zaman damgasını tekrar normal zamana çevirir

#zaman üzerinde işlem
t = datetime.today()
z = datetime(2010,5,20)
t-z #şuanki zamandan belirttiğimiz tarihi çıkartır

