test1="Biz Suriyaya, Əfqanıstana baxıb şükür edə bilmərik. Biz Azərbaycan sərhədlərindən kənarda Azərbaycan qurmuşuq. 100 il əvvəlki Azərbaycanı qoruya bilsək bugün nümunə göstərilən biz olardıq. Bizim Xoyskimiz, Topçubaşovumuz, Cavidimiz, Zərdabimiz və s. olub. Biz istifadə edə bilmədiyimiz potensialımıza heyifsilənməliyik. Finlandiya ola bilməyimizin qarşısında duran səriştəsizliyimizlə mübarizə aparmalıyıq."

test2="Şəkil Napolidə yerləşən bir metro stansiyasından imiş. Biz hələ də kondisionerli qatar gözləyirik."

test3="Bizə vurulan ən böyük ziyan doğru və etibarlı məlumatı əldə etməyin mümkünsüz hala gətirilməsi oldu. Biz də  bu məlumat çirkliliyinin yaratdığı zil qaranlıqda bir-birilə dalaşan isanlar halına gəldik."

test4="Bugün Həsən bəy Zərdabinin yandırdığı çıraq ilə həqiqət axtarışına çıxılan gündür. Xalqın mədəni durumunu göstərən bir neçə sahə vardır, lakin xalqın siyasi durumunu göstərən birbaşa mətbuatdır. Mətbuatın durumu isə bizim əsərimizdir. Çünki mətbuatın tək gücü iliklərinə qədər həqiqətə inanan və susayan insanların varlığıdır. Biz isə heç vaxt o həqiqətin axtarışında olmadıq. İnanmaq istədiklərimiz ilə qane olduq."

test5="Yəqin ki, sümüklərinə belə rahatlıq vermədiyimiz, bu dünyadan yorğun, nigaran köçən Həsən bəy Zərdabi düşünməzdi ki, uğrunda vuruşduğu xalq bir gün mətbuat satıb ev alanların, “3 ayaqlı doğulan heyvan” xəbərlərinin ümidinə qalacaq. Hər keçən gün “Əkinçi” ilə atılan təməlləri, təfəkkürü daha çox biçir, alaq otlarının ümidinə buraxırıq və əgər indi nəsə çətin, mümkünsüz, xəyal kimi görünürsə səbəb yalnızca özümüzük. Heç kimə göydən enməyib, enməyəcək də. Mətbuatı şəffaf olmayan heç bir xalq xoşbəxt və azad olmayıb, olmayacaq."

test6="Bütün reallıqları nəzər alsaq Respublika möcüzə idi. Möcüzənin, inancın zəfərə dönüşməsi idi. O özəl insanlar əsarətə “dur” dedilər, o duyğunu, tükənməyən ümidi, həyəcanı bizlərə bəxş etdilər. Son nəfəsə qədər də ideallara sadiq qaldılar. Onlar fırtına quşu idi. Ən sərt fırtınada fırtınaya qarşı uçdular. Həm də qarşılıqsız və heç durmadan. Ruhları şad olsun, sülh içində yatsınlar."

test7="Kim olursa olsun dövrü mütləq şəkildə aydınlanır. Bəlkə də zamanında 37 repressiyasına aparan yolu hazırlayanların, 20-ci ildə işğala şərait yaradanların bir gün dövranın dönəcəyi ağıllarına belə gəlməzdi. Hər dövr mütləq işıqlanır, yazılır, aydınlanır. O tarixi gün gəldiyində qəhrəman kimi yazılanlar, anılanlar hər zaman Xoyskilər, Cavidlər- mübarizə aparanlar olur. Çünki onlar hər zaman səmimi sevilib, sevilir və seviləcək. Onlara söylənən sözlər qorxudan, şirin görünmək üçün, mənfəət üçün olmur, olmayacaq."

test8="Əmək müqaviləsi Azerbaycanin və ABŞ bildirişi” e-sistemində 12 mindən çox əcnəbi ilə müqavilə bildirişi qeydiyyatdadır zombi mənim hekayəmin əsas hissəsidir əməyin Bakıda doğum hadisəsi baş vermişdir. Sağ qalanlardan ikisi reanimasiya şöbəsinə qaldırılıb"

string_list = [test1, test2, test3, test4, test5, test6, test7, test8]

def AppendToDataframe(df, stringlist=string_list):
    for text in stringlist:
        d = {'Text': text}
        df=df.append(d, ignore_index=True)
        d={}
    return df