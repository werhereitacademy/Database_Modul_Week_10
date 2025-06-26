-- Drop table if it already exists
DROP TABLE IF EXISTS Basvurular;

-- Create the Basvurular table
CREATE TABLE Basvurular (
    id SERIAL PRIMARY KEY,
    zaman_damgasi TIMESTAMP,
    ad_soyad VARCHAR(100),
    mail_adresi VARCHAR(100),
    telefon_numarasi VARCHAR(20),
    posta_kodu VARCHAR(10),
    yasadiginiz_eyalet VARCHAR(50),
    su_anki_durumunuz TEXT,
    egitim_tercihi TEXT,
    ekonomik_durum TEXT,
    dil_kursuna_devam BOOLEAN,
    ingilizce_seviye VARCHAR(20),
    hollandaca_seviye VARCHAR(20),
    belediye_baskisi TEXT,
    bootcamp_bitirdi BOOLEAN,
    online_it_kursu BOOLEAN,
    it_tecrubesi BOOLEAN,
    projeye_dahil BOOLEAN,
    calisma_istekleri TEXT,
    katilim_nedenleri TEXT,
    motivasyon TEXT,
    mentor_gorusmesi VARCHAR(20),
    basvuru_donemi VARCHAR(10),
    yesil_tik_olan VARCHAR(10),
    ek_1 VARCHAR(10),
    ek_2 VARCHAR(10),
    ek_3 VARCHAR(10),
    ek_4 VARCHAR(10)
);

-- Insert all data in one go
INSERT INTO Basvurular (
    zaman_damgasi, ad_soyad, mail_adresi, telefon_numarasi, posta_kodu, 
    yasadiginiz_eyalet, su_anki_durumunuz, egitim_tercihi, ekonomik_durum, 
    dil_kursuna_devam, ingilizce_seviye, hollandaca_seviye, belediye_baskisi, 
    bootcamp_bitirdi, online_it_kursu, it_tecrubesi, projeye_dahil, 
    calisma_istekleri, katilim_nedenleri, motivasyon, mentor_gorusmesi,
    basvuru_donemi, yesil_tik_olan, ek_1, ek_2, ek_3, ek_4
) VALUES
('2023-04-29 13:55:18', 'ahmet selim-yeni', 'yldrm@gmail.com', '3168499580', '6861BW', 'Noord-Holland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Tester', 'Uitkering Alıyorum', TRUE, 'B1', 'B1', 'Kısmen', FALSE, FALSE, TRUE, FALSE, 'Tester, Web Tasarım, Software Developer, Data Engineer, Cyber Security', 'Teknik bir iş olduğu için daha az dil gereksinimi olduğunu düşündünüyorum, Bu sektörde çok fazla eleman ihtiyacı olduğu için, IT ile ilgili eğitimim veya iş tecrübem olduğu için, İngilizce çalışabilme imkanı olduğu için, Bu mesleği yapabileceğime inanıyorum', 'Ben Bilgisayar ogretmeniydim. Ve it alanında devam etmek istiyorum. Bir çok arkadaşım bu alanda kurs alıp kısa sürede iş buldular. Bu imkanlar beni motive ediyor', 'OK', 'VIT3', NULL, '22', '33', '45', 'DONE'),
('2023-04-29 13:55:18', 'ahmet selim', 'yldrm@gmail.com', '3168499580', '6861BW', 'Noord-Holland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Tester', 'Uitkering Alıyorum', TRUE, 'B1', 'B1', 'Kısmen', FALSE, FALSE, TRUE, FALSE, 'Tester, Web Tasarım, Software Developer, Data Engineer, Cyber Security', 'Teknik bir iş olduğu için daha az dil gereksinimi olduğunu düşündünüyorum, Bu sektörde çok fazla eleman ihtiyacı olduğu için, IT ile ilgili eğitimim veya iş tecrübem olduğu için, İngilizce çalışabilme imkanı olduğu için, Bu mesleği yapabileceğime inanıyorum', 'Ben Bilgisayar ogretmeniydim. Ve it alanında devam etmek istiyorum. Bir çok arkadaşım bu alanda kurs alıp kısa sürede iş buldular. Bu imkanlar beni motive ediyor', 'OK', 'VIT3', NULL, '22', '33', '45', 'DONE'),
('2023-04-29 21:44:05', 'mehmet kirmizi', 'meztr@gmail.com', '687522681', '9713VH', 'Noord-Holland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'İngilizce eğitimine ihtiyacım var.', 'Uitkering Alıyorum', TRUE, 'A2', 'A2', 'Bir yillik sure zarfinda calismaya baslamam bekleniyor.', FALSE, FALSE, FALSE, FALSE, 'Data Engineer, Datascience alaninda calismak istiyorum.', 'Bu sektörde çok fazla eleman ihtiyacı olduğu için, İngilizce çalışabilme imkanı olduğu için, Bu mesleği yapabileceğime inanıyorum, Bu alana ilgim ve istegim var.', 'Teknoloji ve bilimdeki yeniliklere karsi yuksek ilgim var. Fen bilgisi ogretmenliginden mezun oldum. Sayisal alandan mezun oldugum icin bu alanin bana uygun oldugunu dusunuyorum. Gelecegin sekillenmesinde IT sektorunun cok buyuk etkisi olacagini biliyorum. Calisma sartlari da benim icin uygun oldugu icin bu alanda ilerlemek istiyorum. Bu alanda sizinle buyuk yol katedecegime eminim.', 'OK', 'VIT3', NULL, '22', '4', '17', 'DONE'),
('2023-04-29 21:44:05', 'mehmet kirmizi', 'meztr@gmail.com', '687522681', '9713VH', 'Noord-Holland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'İngilizce eğitimine ihtiyacım var.', 'Uitkering Alıyorum', TRUE, 'A2', 'A2', 'Bir yillik sure zarfinda calismaya baslamam bekleniyor.', FALSE, FALSE, FALSE, FALSE, 'Data Engineer, Datascience alaninda calismak istiyorum.', 'Bu sektörde çok fazla eleman ihtiyacı olduğu için, İngilizce çalışabilme imkanı olduğu için, Bu mesleği yapabileceğime inanıyorum, Bu alana ilgim ve istegim var.', 'Teknoloji ve bilimdeki yeniliklere karsi yuksek ilgim var. Fen bilgisi ogretmenliginden mezun oldum. Sayisal alandan mezun oldugum icin bu alanin bana uygun oldugunu dusunuyorum. Gelecegin sekillenmesinde IT sektorunun cok buyuk etkisi olacagini biliyorum. Calisma sartlari da benim icin uygun oldugu icin bu alanda ilerlemek istiyorum. Bu alanda sizinle buyuk yol katedecegime eminim.', 'OK', 'VIT3', NULL, '22', '4', '17', 'DONE'),
('2023-04-29 23:39:58', 'yasin kaya', 'bugdayci2@gmail.com', '3168547878', '9716BS', 'Noord-Brabant', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Cybersecurity eğitimine katılmak istiyorum', 'Uitkering Alıyorum', FALSE, 'A1', 'B1', 'Hayır', FALSE, FALSE, FALSE, FALSE, 'Tester, Web Tasarım, Cyber Security', 'Çevremde bir çok kişi bu sektöre girdiği için, Kararsızım ama bir eğitim alıp yapıp yapamayacağımı görmek istiyorum?, Bu sektördeki maaşların iyi olduğunu düşünüyorum, Bu sektörde çok fazla eleman ihtiyacı olduğu için, Kendi mesleğini yapma imkanım olmadığını düşündüğüm için, Bu mesleği yapabileceğime inanıyorum', 'It alanı hep cekici gelmistir. Yuksek maas almak ve bilgisayarda ugrasmak avrupada yazilimci olmak kulaga hos geliyor:)', 'OK', 'VIT3', NULL, '22', '55', '70', 'DONE'),
('2023-04-30 12:19:21', 'zeynep yilmaz', 'karaman@gmail.com', '610404574', '3232BD', 'Noord-Brabant', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Cybersecurity eğitimine katılmak istiyorum', 'Uitkering Alıyorum', TRUE, 'A2', 'A1', 'Hayır', TRUE, TRUE, TRUE, FALSE, 'Cyber Security', 'IT ile ilgili eğitimim veya iş tecrübem olduğu için, İngilizce çalışabilme imkanı olduğu için, Kendi mesleğini yapma imkanım olmadığını düşündüğüm için, Bu mesleği yapabileceğime inanıyorum', '3 yıllık bir IT geçmişim var. Javascript biliyorum ve fullstack web/mobil uygulama geliştirici olarak freelance çalışmalar yaptım. Ve Oak Academy bünyesinde cybersecurity kursu aldım. İngilizce seviyem işe girmek için yeterli değil. En büyük ihtiyacım, şu an için İngilizcemi geliştirmek. Ardından kolayca işe girebilirim. Tekrar meslek eğitimi almayacağım.', 'ATANMADI', 'VIT3', NULL, '22', '2', '18', 'DONE'),
('2023-04-30 12:41:56', 'zeki duran', 'kilinc1686@gmail.com', '639293042', '9715EP', 'Utrecht', 'Kampta, oturum görüşmesi bekliyorum', 'Cybersecurity eğitimine katılmak istiyorum', 'Uitkering Alıyorum', FALSE, 'B2 ve üzeri', 'A1', 'Hayır', TRUE, FALSE, TRUE, FALSE, 'Tester, Scrum Master, DevOps Engineer, Web Tasarım, Software Developer, Cyber Security', 'Bu sektörde çok fazla eleman ihtiyacı olduğu için, IT ile ilgili eğitimim veya iş tecrübem olduğu için, İngilizce çalışabilme imkanı olduğu için, Kendi mesleğini yapma imkanım olmadığını düşündüğüm için, Bu mesleği yapabileceğime inanıyorum', 'IT ye özel ilgim ve becerin olduğunu düşünüyorum.', 'ATANMADI', 'VIT3', NULL, '222', '55', '77', 'DONE'),
('2023-04-30 14:38:18', 'mustafa celik', 'yamandogan@icloud.com', '685070759', '2343XR', 'Noord-Brabant', 'Kampta, oturum aldım, belediyem belli , ev bekliyorum', 'Full stack, desktop ve embedded deneyimim var.', 'Diğer', TRUE, 'B1', 'A1', 'Kampta kalıyorum', TRUE, TRUE, FALSE, FALSE, 'Tester, DevOps Engineer, Web Tasarım, Software Developer', 'Kendi mesleğini yapma imkanım olmadığını düşündüğüm için, Bu mesleği yapabileceğime inanıyorum', 'IT sektöründe çalışmak için 33 yaşımda TRde Bilgisayar mühendisliğini kazandım ve 1 sene okudum. Halihazırda devam eden Claruswayin full stack developer kursum var. İnfotech academy de Tester bölüm koordinatörü ve Java Instructor olarak görev yaptım. İngilizcemi geliştirmek için Amsterdam üniversitesi right2Education kursundan A2/B1 kursu almaktayım. Dutch A1+ sertifikam mevcut. İstekliyim.', 'ATANMADI', 'VIT3', NULL, NULL, NULL, NULL, NULL),
('2023-04-30 21:38:19', 'nuh kececi', 'sultan@hotmail.com', '649497077', '1703JG', 'Zuid-Holland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Ingilizce seviyemin artmasi icin kursa ihtiyacim var.', 'Uitkering Alıyorum', TRUE, 'B1', 'A2', 'Kısmen', FALSE, TRUE, FALSE, FALSE, 'Data Engineer, Cyber Security', 'Bu sektördeki maaşların iyi olduğunu düşünüyorum, Bu sektörde çok fazla eleman ihtiyacı olduğu için, İngilizce çalışabilme imkanı olduğu için, Kendi mesleğini yapma imkanım olmadığını düşündüğüm için, Bu mesleği yapabileceğime inanıyorum', 'Türkiye''de 10 yıl Ankara Üniversitesi Hukuk Fakültesi''nde İdare Hukuku kürsüsünde araştırma görevlisi olarak çalıştım. Yaptığım araştırmalar neticesinde burda mesleğimi devam ettirme olanağım çok az veya nerdeyse mümkün değil. Entegrasyon konusunda yeni kanuna tabiyim. Dolayısıyla dil konusunda gelmek istediğim seviye konusunda da belediye sorun çıkaracak. Bu yüzden başka alanlara yönelmem gerektiğini düşünüyorum. IT sektörü büyük bir hızla gelişen ve çok sayıda yetişmiş elemana ihtiyaç duyan bir alandır. Geleceğin en önemli sektörüdür. Kendimi bu alanda geliştirmek istiyorum. Geçmiş mesleğim dolayısıyla planlı, sürekli ve disiplinli çalışmaya açığım.Sabırlı birisiyim. Yabancı dil konusunda da belli bir düzeyde altyapım da vardır. Bu sebeplerle IT sektöründe kariyer yapmak istiyorum.', 'OK', 'VIT3', NULL, NULL, NULL, NULL, NULL),
('2023-05-01 01:39:19', 'sahin okur', 'akilinc1686@gmail.com', '686247782', '7496DD', 'Gelderland', 'Kampta, oturum görüşmesi bekliyorum', 'Software Testing', 'Diğer', FALSE, 'B1', 'A1', 'Belediyem belli degil', TRUE, TRUE, TRUE, FALSE, 'Web Tasarım, Software Developer, Data Engineer, Cyber Security', 'IT ile ilgili eğitimim veya iş tecrübem olduğu için, İngilizce çalışabilme imkanı olduğu için', 'Daha önce 18 yıl elektronik öğretmenliği yaptım. 15 temmuzdan sonra da sanayide değişik alanlarda embedded sistem ve masa üstü programlar gelistirdim. Yaklasik 3 yildir da full stack olarak çalıştım. Bu işi yapabileceğimi dusunuyorum', 'OK', 'VIT3', NULL, NULL, NULL, NULL, NULL),
('2023-05-01 16:41:41', 'mehmet dogan', 'tatesozer@outlook.com', '43273091', '9502SJ', 'Zuid-Holland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Data Engineer/ cloud Engineer', 'Kısmen Uitkering Alıyorum - Parttime Çalışıyorum', FALSE, 'A2', 'B2 ve üzeri', 'Hayır', TRUE, TRUE, FALSE, FALSE, 'Tester', 'Teknik bir iş olduğu için daha az dil gereksinimi olduğunu düşündünüyorum, Bu sektörde çok fazla eleman ihtiyacı olduğu için, Ingilizce seviyemin artmasi icin dil destegine ihtiyacim var.', 'IT ye özel ilgim ve becerin olduğunu düşünüyorum.', 'OK', 'VIT3', NULL, NULL, NULL, NULL, NULL),
('2023-05-02 22:02:10', 'ahmet citlak', 'kihgad@gmail.com', '685644911', '7322CA', 'Noord-Brabant', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Cybersecurity eğitimine katılmak istiyorum', 'Uitkering Alıyorum', FALSE, 'B2 ve üzeri', 'A2', 'Hayır', TRUE, TRUE, FALSE, FALSE, 'Tester', 'Kararsızım ama bir eğitim alıp yapıp yapamayacağımı görmek istiyorum?, Teknik bir iş olduğu için daha az dil gereksinimi olduğunu düşündünüyorum, Bu sektördeki maaşların iyi olduğunu düşünüyorum, Bu sektörde çok fazla eleman ihtiyacı olduğu için, İngilizce çalışabilme imkanı olduğu için', 'Remote çalışma imkanı, İngilizce çalışma imkanı', 'ATANMADI', 'VIT3', NULL, NULL, NULL, NULL, NULL),
('2023-05-03 23:54:00', 'sevil gulsen', 'tyt@outlook.com', '687234214', '1186TW', 'Utrecht', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Powerplatform eğitimine katılmak istiyorum', 'Uitkering Alıyorum', FALSE, 'B2 ve üzeri', 'B1', 'Kısmen', TRUE, TRUE, FALSE, FALSE, 'Cloud Engineer, Tester, Scrum Master, DevOps Engineer, Data Engineer, Cyber Security', 'İngilizce çalışabilme imkanı olduğu için, Kendi mesleğini yapma imkanım olmadığını düşündüğüm için, Bu mesleği yapabileceğime inanıyorum', 'IT ye özel ilgim ve becerin olduğunu düşünüyorum.', 'ATANMADI', 'VIT3', NULL, NULL, NULL, NULL, NULL),
('2023-05-04 01:19:08', 'melike guney', 'bahar27@gmail.com', '648673634', '7331RD', 'Zuid-Holland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Salesforce', 'Uitkering Alıyorum', TRUE, 'B1', 'B1', 'Kısmen', FALSE, FALSE, FALSE, FALSE, 'Kararsızım', 'IT ile ilgili eğitimim veya iş tecrübem olduğu için, İngilizce çalışabilme imkanı olduğu için, Bu mesleği yapabileceğime inanıyorum', 'Bilgisayar Öğretmenliği mezunuyum, fakat şuan öğretmenlik yapmayı düşünmüyorum. Fakat IT alanında devam etmek istiyorum', 'ATANMADI', 'VIT3', NULL, NULL, NULL, NULL, NULL),
('2023-05-06 00:23:13', 'esma donmez', 'bsbns@gmail.com', '685768954', '7322CA', 'Noord-Holland', 'Kampta, oturum görüşmesi bekliyorum', 'Cybersecurity eğitimine katılmak istiyorum', 'Diğer', FALSE, 'B2 ve üzeri', 'A1', 'Hayır', FALSE, TRUE, TRUE, FALSE, 'Scrum Master, Software Developer, IT project management', 'IT ile ilgili eğitimim veya iş tecrübem olduğu için, İngilizce çalışabilme imkanı olduğu için', 'Ülkemde daha önce kamu kurumlarında ve özel sektörde IT alanında, farklı pozisyonlarda çalıştım. Burada da bu alanlardan birinde çalışmaya devam edebileceğimi düşünüyorum. Ancak birden fazla farklı alanda hem çalıştığım hem de eğitim aldığım için hangi alanda yoluma devam etmemin daha faydalı olacağı konusunda kararsızım. Hem bu konuda fikir edinebilmek, hem de bir mülteci olarak profesyonel iş yaşamına başlangıçta yapılabilecek koçluğun bana büyük katkı sağlayacağını düşündüğüm için bu projeye katılmak istiyorum.', 'OK', 'VIT3', NULL, NULL, NULL, NULL, NULL),
('2023-05-06 22:55:32', 'enver unal', 'kariparduc1977@gmail.com', '626119720', '5552AB', 'Noord-Holland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Powerplatform eğitimine katılmak istiyorum', 'Uitkering Alıyorum', FALSE, 'B2 ve üzeri', 'A1', 'Hayır', TRUE, TRUE, FALSE, FALSE, 'Salesforce admin/developer', 'Bu sektördeki maaşların iyi olduğunu düşünüyorum, İngilizce çalışabilme imkanı olduğu için, Bu mesleği yapabileceğime inanıyorum', 'Yaşım 42 ve 3 cocuğum var.Maalesef kendi ulkemde dibi gordukten sonra buralara gelmek nasip oldu.Her yönüyle yeni bir başlangıç istiyorum.IT sektörü bu konuda benim için çok cazip bir alan,bu yolda yürümek istiyorum.Ve bu konuda bana faydası olabilecek her fırsatı değerlendirmeye çalışıyorum.', 'OK', 'VIT3', NULL, NULL, NULL, NULL, NULL),
('2023-05-06 23:34:21', 'murat uraz', 'akif.nl@gmail.com', '685424757', '2912EH', 'Gelderland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'İngilizcemin yeterli olup olmadığını bilmiyorum', 'Uitkering Alıyorum', TRUE, 'A1', 'A2', 'Kısmen', FALSE, FALSE, TRUE, FALSE, 'Cyber Security', 'Teknik bir iş olduğu için daha az dil gereksinimi olduğunu düşündünüyorum, Bu sektörde çok fazla eleman ihtiyacı olduğu için, Bu mesleği yapabileceğime inanıyorum', 'Yılşarca güvenlik sektöründe çalıştım Logo muhasebe programı son kullanıcı eğitimi verdim ve fatura tasarımı yaptım Cyber security alanı ilgimi çekiyor bu imkanı değerlendirmek istiyorum', 'OK', 'VIT3', NULL, NULL, NULL, NULL, NULL),
('2023-05-07 13:32:15', 'yusuf akdogan', 'rantore@gmail.com', '684377617', '5513PH', 'Noord-Brabant', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Cybersecurity eğitimine katılmak istiyorum', 'Uitkering Alıyorum', TRUE, 'A1', 'B1', 'Kısmen', FALSE, TRUE, FALSE, TRUE, 'Cloud Engineer, Tester, Web Tasarım, Software Developer', 'Teknik bir iş olduğu için daha az dil gereksinimi olduğunu düşündünüyorum, Bu sektördeki maaşların iyi olduğunu düşünüyorum, Bu sektörde çok fazla eleman ihtiyacı olduğu için, IT ile ilgili eğitimim veya iş tecrübem olduğu için, Bu mesleği yapabileceğime inanıyorum', 'Üniversite eğitimim Matematik üzerine. Matematiksel zekam, analitik düşüncem, problem çözme kabiliyetim ve Analiz ve sentez beceriminin çok iyi olduğunu, uzun süre ekran karşısında durabileceğimi, Hazır programları ve programlama dillerini hızlı bir şekilde öğrenip kullanabileceğimi biliyorum. bu sebeple uzun vadede IT sektöründe başarılı olacağıma inanıyorum.', 'ATANMADI', 'VIT3', NULL, NULL, NULL, NULL, NULL),
('2023-05-10 10:23:17', 'emrah dikici', 'deniz5@gmail.com', '616873780', '3512PZ', 'Noord-Brabant', 'Kampta, oturum aldım, belediyem belli , ev bekliyorum', 'Cybersecurity eğitimine katılmak istiyorum', 'Uitkering Alıyorum', TRUE, 'A1', 'A1', 'Hayır', FALSE, FALSE, FALSE, FALSE, 'Kararsızım, Hiç bir fikrim yok, Tester', 'Kararsızım ama bir eğitim alıp yapıp yapamayacağımı görmek istiyorum?, Diğer sektörler hakkındaki iş imkanları hakkında yeterince bilgim yok, Bu sektördeki maaşların iyi olduğunu düşünüyorum, Bu sektörde çok fazla eleman ihtiyacı olduğu için, Kendi mesleğini yapma imkanım olmadığını düşündüğüm için, Bu mesleği yapabileceğime inanıyorum', 'Yaşım 46.Muhasebe mesleğimi yapma imkanım yok.En iyi alternatifin bu olduğunu düşünüyorum.', 'ATANMADI', 'VIT3', NULL, NULL, NULL, NULL, NULL),
('2023-05-10 10:23:17', 'emrah dikici', 'deniz5@gmail.com', '616873780', '3512PZ', 'Noord-Brabant', 'Kampta, oturum aldım, belediyem belli , ev bekliyorum', 'Cybersecurity eğitimine katılmak istiyorum', 'Uitkering Alıyorum', TRUE, 'A1', 'A1', 'Hayır', FALSE, FALSE, FALSE, FALSE, 'Kararsızım, Hiç bir fikrim yok, Tester', 'Kararsızım ama bir eğitim alıp yapıp yapamayacağımı görmek istiyorum?, Diğer sektörler hakkındaki iş imkanları hakkında yeterince bilgim yok, Bu sektördeki maaşların iyi olduğunu düşünüyorum, Bu sektörde çok fazla eleman ihtiyacı olduğu için, Kendi mesleğini yapma imkanım olmadığını düşündüğüm için, Bu mesleği yapabileceğime inanıyorum', 'Yaşım 46.Muhasebe mesleğimi yapma imkanım yok.En iyi alternatifin bu olduğunu düşünüyorum.', 'ATANMADI', 'VIT3', NULL, NULL, NULL, NULL, NULL),
('2023-05-10 10:29:25', 'mehmet kilinc', 'hikyasar@gmail.com', '684744177', '1023VA', 'Zuid-Holland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Bu eğitimler ilgi alanım dışında başka alanlardaki eğitimlere katılmak istiyorum', 'Uitkering Alıyorum', TRUE, 'B1', 'A2', 'Evet', TRUE, TRUE, FALSE, FALSE, 'Cloud Engineer, Cyber Security', 'IT ile ilgili eğitimim veya iş tecrübem olduğu için, İngilizce çalışabilme imkanı olduğu için, Bu mesleği yapabileceğime inanıyorum', 'ben ingilizce ogretmeniyim ve burada ogretmenlikle ilgili bikac deneyimim oldu ve ogretmenlikten devam etmeme karari aldim. cybersecurity egitimim var ustune ekleyip is bulmak istiyorum.', 'ATANMADI', 'VIT3', NULL, NULL, NULL, NULL, NULL),
('2023-05-10 12:35:18', 'hasan maltepe', 'mustafa1988@gmail.com', '684726936', '5625CR', 'Zuid-Holland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Bu eğitimler ilgi alanım dışında başka alanlardaki eğitimlere katılmak istiyorum', 'Uitkering Alıyorum', FALSE, 'A2', 'B2 ve üzeri', 'Kısmen', FALSE, TRUE, FALSE, FALSE, 'Kararsızım, Cyber Security', 'Çevremde bir çok kişi bu sektöre girdiği için, Bu sektörde çok fazla eleman ihtiyacı olduğu için, Bu mesleği yapabileceğime inanıyorum', 'Yeni şeyler ögrenmek içim hevesliyim ve gerekli motivasyina sahibim. Günümüzün ve geleceğin önemli bir meslek alanı olan bu sektörde kariyer yapma imkanı benim için güzel bir fırsat olacaktır. Zamanın gerisinde kalmak istemiyorum. Teknolojik yeniliklere uyum sağlayarak kendimi geliştirmek istiyorum. Takım çalışmasına uyum sağlayan ve yeniliklere açık biriyim. Gerekli yönlendirme , bilgilendirme ve rehberlik ile doğru bir adım atacağıma inanıyorum...', 'OK', 'VIT3', NULL, NULL, NULL, NULL, NULL),
('2023-05-11 09:28:25', 'hikmet sivri', 'sultan@hotmail.com', '687892645', '1474PD', 'Zuid-Holland', 'Kampta, oturum görüşmesi bekliyorum', 'Cybersecurity eğitimine katılmak istiyorum', 'Uitkering Alıyorum', FALSE, 'A2', 'A1', 'HENUZ KAMPTA KALIYORUM.', FALSE, FALSE, FALSE, FALSE, 'Kararsızım, Data Engineer', 'İngilizce çalışabilme imkanı olduğu için, Kendi mesleğini yapma imkanım olmadığını düşündüğüm için, Bu mesleği yapabileceğime inanıyorum', 'Kendi ulkemdeyken avukatlik yapiyordum. burada meslegime devam etme sansim yok. her ne kadar avukat olsam da sayisal ogrencisiydim. analitik zeka yapisina sahip oldugumu ve bu iste basarili olabilecegimi dusunuyorum. ayrica evrensel bir meslek olmasi da beni bu sektore yonlendiren sebeplerden birisi. dogru egitim aldiktan sonra bu sektorde ilerleyebilecegimi dusunuyorum.', 'OK', 'VIT3', NULL, NULL, NULL, NULL, NULL),
('2023-05-18 11:19:09', 'sinan kus', 'neberberr@gmail.com', '3069718679', '1474PD', 'Zuid-Holland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Cybersecurity eğitimine katılmak istiyorum', 'Eşim Çalıştığı için uitkering almıyoruz', TRUE, 'B2 ve üzeri', 'B1', 'Hayır', TRUE, FALSE, FALSE, FALSE, 'Cloud Engineer', 'Bu sektördeki maaşların iyi olduğunu düşünüyorum, IT ile ilgili eğitimim veya iş tecrübem olduğu için, Kendi mesleğini yapma imkanım olmadığını düşündüğüm için, Bu mesleği yapabileceğime inanıyorum', 'IT ye özel ilgim ve becerin olduğunu düşünüyorum.', 'OK', 'VIT3', NULL, NULL, NULL, NULL, NULL),
('2023-05-21 16:51:57', 'mustafa berber', 'all88@gmail.com', '612672855', '5673MH', 'Zuid-Holland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Bu eğitimler ilgi alanım dışında başka alanlardaki eğitimlere katılmak istiyorum', 'Uitkering Alıyorum', TRUE, 'A2', 'B2 ve üzeri', 'Kısmen', FALSE, FALSE, FALSE, TRUE, 'Kararsızım', 'Bu sektördeki maaşların iyi olduğunu düşünüyorum, Bu sektörde çok fazla eleman ihtiyacı olduğu için', 'IT ye özel ilgim ve becerin olduğunu düşünüyorum.', 'ATANMADI', 'VIT3', NULL, NULL, NULL, NULL, NULL),
('2023-05-21 21:35:50', 'olcay deniz', 'bircan@gmail.com', '3168548999', '5673MH', 'Noord-Brabant', 'Kampta, oturum aldım, belediyem belli , ev bekliyorum', 'İngilizcemi geliştirmek istiyorum.', 'Diğer', TRUE, 'B1', 'A1', 'Hayır', TRUE, TRUE, FALSE, FALSE, 'Data Engineer, Data Science, Data Analyst', 'IT ile ilgili eğitimim veya iş tecrübem olduğu için, Bu mesleği yapabileceğime inanıyorum', 'IT sektorunde calisabilmek bu alanda ozgun projeler yapabilmek beni gercekten heyecanlandiriyor, guzel bir egitim ve mentor destegiyle de bu alnda basarili olabilecegime inaniyorum.', 'ATANMADI', 'VIT3', NULL, NULL, NULL, NULL, NULL),
('2023-05-21 22:49:30', 'asiye turan', 'salihba@icloud.com', '684536214', '3981EC', 'Utrecht', 'Kampta, oturum görüşmesi bekliyorum', 'Cybersecurity eğitimine katılmak istiyorum', 'Diğer', FALSE, 'A2', 'A1', 'Henüz belediye belirlenmedi', FALSE, TRUE, TRUE, FALSE, 'Tester, Web Tasarım, Software Developer', 'IT ile ilgili eğitimim veya iş tecrübem olduğu için', 'Zaten bu sektörde eğitimim ve tecrübem bulunduğu için bu sektörde bulunan iş imkanlarını değerlendirmek istiyorum', 'ATANMADI', 'VIT3', NULL, NULL, NULL, NULL, NULL),
('2023-05-21 23:19:31', 'suat koksal', 'genesis@gmail.com', '641118933', '5384CT', 'Noord-Holland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Cybersecurity eğitimine katılmak istiyorum', 'Uitkering Alıyorum', TRUE, 'A2', 'A1', 'Hayır', TRUE, TRUE, TRUE, FALSE, 'Cyber Security', 'IT ile ilgili eğitimim veya iş tecrübem olduğu için, İngilizce çalışabilme imkanı olduğu için, Kendi mesleğini yapma imkanım olmadığını düşündüğüm için, Bu mesleği yapabileceğime inanıyorum', 'Formu daha önce de doldurmuştum ancak iletişim bilgilerimi doğru girdiğimden emin olmadığım için tekrar dolduruyorum. 6 aylık bir Cyber Security bootcamp i bitirdim. İngilizcemi yeterli düzeye getirdiğim zaman işe girebilecek düzeyde olacağıma inanıyorum.', 'OK', 'VIT3', NULL, NULL, NULL, NULL, NULL),
('2023-05-21 23:49:48', 'talat balkan', 'dastan5@gmail.com', '620099967', '3311LH', 'Utrecht', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Cybersecurity eğitimine katılmak istiyorum', 'Diğer', TRUE, 'A2', 'A2', 'Kısmen', FALSE, TRUE, FALSE, FALSE, 'Data Engineer, Cyber Security, Data Analysis', 'Bu sektördeki maaşların iyi olduğunu düşünüyorum, Bu sektörde çok fazla eleman ihtiyacı olduğu için, İngilizce çalışabilme imkanı olduğu için, Kendi mesleğini yapma imkanım olmadığını düşündüğüm için, Bu mesleği yapabileceğime inanıyorum', 'Ankara Üniversitesi Hukuk Fakültesi İdare Hukuku kürsüsünde 10 yıl araştırma görevlisi olarak çalıştım. Diploma denklik süreci sonunda elde ettiğim belgelerde Türk hukuku ile Hollanda hukuku arasında ülkeler arasında farklılıklardan ötürü bazı farkların bulunduğuna ilişkin ifadeler bulunmaktadır. Ayrıca bu ülkede benzer bir mesleği sürdürmek için C1 seviyesinde Hollandaca ve İngilizce gerekmektedir. Entegrasyon süreci açısından yeni kanuna tabiiyim. Dolayısıyla belediyenin dil konusunda bana bu konuda kesinlikle yardımcı olmayacağını düşünüyorum. Ben de farklı alternatiflere yönelmek istedim. Gelecek açısından IT sektörü en önemli iş alanıdır. Ayrıca globaldir ve diğer birçok meslek gibi sınırlarla bağlı değildir. Bu nedenle bu alanda kariyer yapmak istiyorum. Belli bir seviyede de ingilizce altyapım vardır. Önceki mesleğimden dolayı planlı ve disiplinli çalışmaya alışığım. Ayrıca sabırlı birisiyim. Bu nedenlerden ötürü IT sektöründe kariyer yapabileceğime ve başarılı olacağıma inanıyorum.', 'ATANMADI', 'VIT3', NULL, NULL, NULL, NULL, NULL),
--('2023-05-22 15:42:43', 'burhan yilmaz', 'nuri@gmail.com', '657932104', '5331AS', 'Noord-Holland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Bu eğitimler ilgi alanım dışında başka alanlardaki eğitimlere katılmak istiyorum', 'Uitkering Alıyorum', FALSE, 'A2', 'A2', 'Hayır', FALSE, FALSE, FALSE, FALSE, 'Software Developer, Cyber Security', 'Bu mesleği yapabileceğime inanıyorum', 'Yapabilecegime inandigim icin karar verdim', NULL, 'VIT3', NULL, NULL, NULL, NULL),
--('2023-05-22 15:42:43', 'burhan yilmaz', 'nuri@gmail.com', '657932104', '5331AS', 'Noord-Holland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Bu eğitimler ilgi alanım dışında başka alanlardaki eğitimlere katılmak istiyorum', 'Uitkering Alıyorum', FALSE, 'A2', 'A2', 'Hayır', FALSE, FALSE, FALSE, FALSE, 'Software Developer, Cyber Security', 'Bu mesleği yapabileceğime inanıyorum', 'Yapabilecegime inandigim icin karar verdim', NULL, 'VIT3', NULL, NULL, NULL, NULL),
('2021-05-16 22:55:32', 'Gönül Su', 'gönülsu@deneme.com', '626117733', '5125AB', 'Flevoland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Powerplatform eğitimine katılmak istiyorum', 'Uitkering Alıyorum', FALSE, 'B2 ve üzeri', 'A1', 'Hayır', TRUE, TRUE, FALSE, FALSE, 'Salesforce admin/developer', 'Bu sektördeki maaşların iyi olduğunu düşünüyorum, İngilizce çalışabilme imkanı olduğu için, Bu mesleği yapabileceğime inanıyorum', 'Yaşım 42 ve 3 cocuğum var.Maalesef kendi ulkemde dibi gordukten sonra buralara gelmek nasip oldu.Her yönüyle yeni bir başlangıç istiyorum.IT sektörü bu konuda benim için çok cazip bir alan,bu yolda yürümek istiyorum.Ve bu konuda bana faydası olabilecek her fırsatı değerlendirmeye çalışıyorum.', 'OK', 'VIT3', NULL, NULL, NULL, NULL, NULL),
('2023-05-21 23:19:31', 'sua koksal', 'genesis@gmail.com', '641118933', '5384CT', 'Noord-Holland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Cybersecurity eğitimine katılmak istiyorum', 'Uitkering Alıyorum', TRUE, 'A2', 'A1', 'Hayır', TRUE, TRUE, TRUE, FALSE, 'Cyber Security', 'IT ile ilgili eğitimim veya iş tecrübem olduğu için, İngilizce çalışabilme imkanı olduğu için, Kendi mesleğini yapma imkanım olmadığını düşündüğüm için, Bu mesleği yapabileceğime inanıyorum', 'Formu daha önce de doldurmuştum ancak iletişim bilgilerimi doğru girdiğimden emin olmadığım için tekrar dolduruyorum. 6 aylık bir Cyber Security bootcamp i bitirdim. İngilizcemi yeterli düzeye getirdiğim zaman işe girebilecek düzeyde olacağıma inanıyorum.', 'OK', 'VIT3', NULL, NULL, NULL, NULL, NULL);

-- Verify the data was inserted correctly
SELECT COUNT(*) AS total_records FROM Basvurular;




-- Tablo oluşturma (eğer zaten varsa önce sil)
DROP TABLE IF EXISTS Kullanicilar;
CREATE TABLE Kullanicilar (
    id SERIAL PRIMARY KEY,
    kullanici VARCHAR(50) NOT NULL UNIQUE,
    parola VARCHAR(100) NOT NULL,
    yetki VARCHAR(20) NOT NULL
);

-- Tüm verileri ekleme
INSERT INTO Kullanicilar (kullanici, parola, yetki) VALUES
('ahmet', 'werhere', 'admin'),
('mehmet', 'itforever', 'user'),
('selim', 'cyber_warrior', 'user'),
('a', 'b', 'admin'),
('s', 'd', 'user');

-- Verilerin başarıyla eklendiğini kontrol etme
SELECT * FROM Kullanicilar;


-- Drop table if it already exists
DROP TABLE IF EXISTS Mentor;

-- Create the Mentor table
CREATE TABLE Mentor (
    id SERIAL PRIMARY KEY,
    gorusme_tarihi DATE,
    mentinin_adi_soyadi VARCHAR(100),
    mentorun_adi_soyadi VARCHAR(100),
    katilimci_it_bilgisi INTEGER,
    vit_projesine_uygunluk TEXT,
    mentor_gorusu TEXT,
    katilimci_yogunluk INTEGER,
    yorumlar TEXT
);

-- Insert all data in one go
INSERT INTO Mentor (
    gorusme_tarihi, mentinin_adi_soyadi, mentorun_adi_soyadi, 
    katilimci_it_bilgisi, vit_projesine_uygunluk, mentor_gorusu, 
    katilimci_yogunluk, yorumlar
) VALUES
('2023-05-10', 'esma donmez', 'Ugur Atalay-yeni', 2, 'Başka bir sektöre yönlendirilmeli', 'Başka bir sektöre yönlendirilmeli', 7, 'Katilimci B1 hollandaca kursunu bitirmis, yaz ayindan sonra bir kez daha B1 kursu almak istiyor. Ingilizce ogretmenligi mezunu ancak okullarda idarecilik alaninda calismis, Ingilizceden uzak kalmis. Ingilizcesini gelistirmek istiyor. Bu konuda UAF in destegi hatirlatildi. Hollandacanin oneminden bahsedildi. Ogretmen olarak calismak da katilimcinin secenekleri arasinda. IT ve ogretmenlik arasinda kaldigini hissettim. IT alaninda calismak konusunda tecrube paylasimi yapildi. Bu asamada Dil bilgisini biraz daha gelistirdikten sonra tekrar bir degerlendirilmeye alinmasinin uygun olacagini dusunuyorum.'),
('2023-05-12', 'murat uraz', 'Yasin Bostanci', 6, 'Başka bir sektöre yönlendirilmeli', 'Başka bir sektöre yönlendirilmeli', 3, 'Bilgisayar ogretmeni bu acidan verilen egitimleri kolay kavrayacaktir. Motivasyonu yuksek.'),
('2023-05-15', 'emrah dikici', 'Ibrahim Sahin', 6, 'Başka bir sektöre yönlendirilmeli', 'Başka bir sektöre yönlendirilmeli', 7, 'Katilimcinin ingilizce seviyesi ana dili seviyesinde. Universite mezunu degil fakat IT yle alakali freelance olarak birkac proje yapmis ve tecrubesi var.Ailevi durumundan dolayi yasinin cok genc olmasina ragmen okuldan ziyade ise yonlenmek istiyor. Direk ITPH e yonlendirilmesi uygun olur.'),
('2023-05-16', 'hasan maltepe', 'Ugur Atalay', 2, 'Başka bir sektöre yönlendirilmeli', 'Başka bir sektöre yönlendirilmeli', 10, 'Katilimci 7 yildir Hollanda''da da yasiyor. Zamaninda belediye baskisiyla bir ise yonlendirilmis. Halihazirda haftalik 40 saat bir iste calisiyor. VIT projesi belediyeler tarafindan finanse edilecegi icin katilimci arkadasin finanslama kisminin nasil olacagi soru isareti. Bu husus katilimciya aktarildi. Bununla alakali bir alternatif uzerine konusuldu. Haftasonu veya aksamlari egitim verilen IT egitim kurslari hatirlatildi.'),
('2023-05-09', 'nuh kececi', 'Muhammed Ari', 3, 'Bir sonraki VIT projesine katilmasi daha uygun olur', 'Bir sonraki VIT projesine katilmasi daha uygun olur', 1, 'It backgroundu yok, dersanecilik yapmis bir arkadasimiz henuz Hollandaca ogrenimine yeni baslamis, Ingilizcesi henuz yok denecek kadar o acidan belki 1 veya 1,5 yil sonra  VIT programina katilabilir.'),
('2023-05-09', 'sahin okur', 'Muhammed Ari', 1, 'Bir sonraki VIT projesine katilmasi daha uygun olur', 'Bir sonraki VIT projesine katilmasi daha uygun olur', 1, 'Daha once Python kursuna katilim saglamis. Ingilizce kursundan sonra ITPH''a yonlendirilebilir.'),
('2023-05-05', 'zeynep yilmaz', 'Harun', 10, 'Diger', 'diger secenekte yazdim detayli', 9, 'IT gecmisi var, TR''de scrum master''a denk bir pozisyonda calismis. Burada developer olarak calismak istiyor ama oncelikle bilgilerini yenilemek icin Hack Your Future tarzi bir yerde egitim almak istiyor. Suan icin kampta ve oturum bekliyor. VIT''e uygun bir aday degil. is arama surecinde tekrar temasta olacagiz'),
('2023-05-05', 'yasin kaya', 'Harun', 9, 'Direkt bireysel koçluk ile işe yönlendirilmesi uygun olur', 'Direkt bireysel koçluk ile işe yönlendirilmesi uygun olur', 7, 'Bu aday Salesforce kursu bitirmis, Bir muddet is aramis ama tecrube eksikligi nedeniyle olumsuz yanitlar almis, ogretmenlik gecmisi nedeniyle bir gun asistan ogretmen olarak calisiyor ama Salesforce ya da SAP alanlarinda is bulmak istiyor, onceligi ise girmek yeni bir IT kursu dusunmuyor. Kendisine jobport hesabi actirip is ilanlarina bakmayi planliyorum.'),
('2023-05-15', 'yusuf akdogan', 'Ibrahim Sahin', 9, 'Direkt bireysel koçluk ile işe yönlendirilmesi uygun olur', 'Direkt bireysel koçluk ile işe yönlendirilmesi uygun olur', 5, 'Cyber security kursu bitirmis. B1 seviye ingilizcesi var. Ise girmek istiyor. Is arama konusunda kocluk yapilabilir.'),
('2023-05-10', 'mehmet dogan', 'Abdulkadir', 5, 'Diger', 'Gorusmeye katilmadigi icin birsey yazamiyorum.', 5, 'Katilimci hala kampta ev bekliyor.Hollandaca dil seviyesi A1/A2 civarinda. Ingilizcesi de B1 civarinda.Dil ogrenmeye devam ediyor.Hollandaca ogrenmesi icin tesvik edildi.'),
('2023-05-11', 'melike guney', 'Ugur Atalay', 5, 'Diger', 'Katilim saglanmadi.', 5, 'Katılımcı 25 aydır kampta kalıyor. Belediyesi belli ev bekliyor. Daha önce yaptığı işlerde bilgisayar sistemlerini kullanmış. Bazı programlara aşina. Dil konusunda zamana ihtiyacı var. Sonraki VIT projeleri için düşünülebilir.'),
('2023-05-09', 'zeki duran', 'Abdulkadir', 10, 'Direkt bireysel koçluk ile işe yönlendirilmesi uygun olur', 'Katilimci hem direk ITPH''te baslamaya hem de bireysel kocluk ile ise baslamaya uygun.', 3, 'Katilimci Hack Your Future programini bitirmis. Ingilizce seviyesi yeterli. Suan hollandaca dersi aliyor.Haziran-Temmuz gibi b1 hollandaca sinavina giricek. Eylul ayinda basliyacak olan ITPH programlarina uygun. Herhangi bir is, staj imkanida olursa degerlendirilebilir.'),
('2023-04-05', 'mehmet kirmizi', 'Yasin Bostanci', 6, 'VIT projesi ilk IT eğitimi alıp ITPH a yönlendirilmesi uygun olur', 'VIT projesi ilk IT eğitimi alıp ITPH a yönlendirilmesi uygun olur', 4, 'Katilimci henuz oturum asamasinda, oturum mulakat sonucunu bekliyor. Cyber security alaninda calismak istiyor. Daha henuz eve cikmadigindan Vit projesi, takibinde itph a yonlendirilmesi uygundur.'),
('2023-05-02', 'ahmet selim', 'Harun', 9, 'VIT projesi ingilizce eğitimi alıp ITPH a yönlendirilmesi uygun olur', 'VIT projesi ingilizce eğitimi alıp ITPH a yönlendirilmesi uygun olur', 1, 'Bu arkadas bekar, genc dinamik, motivasyonu yerinde. Oturumu var ama belediye sansizligindan dolayi 3 senedir hala kampta. Data alaninda kurs bitirmis olmasina ragmen dili calismaya hazir seviyede degil. VIT''in Ingilizce kursuna devam edebilir ama belirttigim gibi halen kampta. ITPH''in data kursuna da katilmak istedigini belirtti bence bu da faydali olur'),
('2023-05-10', 'ahmet citlak', 'ibrahim firat', 7, 'VIT projesi ingilizce eğitimi alıp ITPH a yönlendirilmesi uygun olur', 'VIT projesi ingilizce eğitimi alıp ITPH a yönlendirilmesi uygun olur', 7, 'evli , 2 cocuk var. bilgisayar mühendisliği mezunu.   buraya geleli 1,5 yıl olmus.  Mesleği ile ilgili hiç çalışmamış. hollandaca öğrenme noktasında motivasyonu düşük. Eski kanuna tabi. Şu anda iş dili konusunda kararsız. eğer iş dilinin ingilizce olması noktasında karar alırsa bizimle irtibata geçecek. o zaman ingilizce kursu ve devamı ile ilgili yardımcı olunabilir. Ama hollandacasını ilerletme noktasında karar alırsa daha sonraki aşamalarda dahil olabilir projeye.'),
('2023-05-16', 'sinan kus', 'Muhammed Ari', 10, 'VIT projesi kapsamında direkt ITPH a yönlendirilmesi uygun olur.', 'VIT projesi kapsamında direkt ITPH a yönlendirilmesi uygun olur.', 3, 'Cybersecurity konusunda istekli, kapasite olarak direkt iletilebilir ancak herhangi bir backgroundu henuz yok. Kendisi net olarak direkt Cybersecurity konusuna baslamak istiyor.'),
('2023-05-17', 'mustafa berber', 'Ibrahim Sahin', 10, 'VIT projesi kapsamında direkt ITPH a yönlendirilmesi uygun olur.', 'VIT projesi kapsamında direkt ITPH a yönlendirilmesi uygun olur.', 7, 'C1 seviyesinde Hollandaca biliyor, ingilizce kursu takip ediyor. IT ile ilgili arastirma yapmis, online kurs takip etmis ve bu alanda calismak icin hevesli. Bunlar esinin de calisiyor olmasiyla birlikte dusunuldugunde direk ITPH akademiye yonlendirilmesi uygun olur.'),
('2023-05-19', 'talat balkan', 'Yasin Bostanci', 2, 'VIT projesi kapsamında direkt ITPH a yönlendirilmesi uygun olur.', 'VIT projesi kapsamında direkt ITPH a yönlendirilmesi uygun olur.', 5, 'Katilimcinin Hollandaca dil seviyesi B2 ve halihazirda online python kursunu takip ediyor. Proje icin yeterli vakti mevcut ve motive. VIT projesine ingilizce dil destegiyle katilabilir. Hali hazirda uitkering aliyor belediye bu konuda baski yapmiyor. Projeye katilimini muhtemelen destekleyecektir.Bilgisayarla calismayi cok seviyor.Cin dili ve edebiyati mezunu.'),
('2023-05-09', 'mustafa celik', 'Abdulkadir', 9, 'VIT projesinin tamamına katılması uygun olur', 'VIT projesinin tamamına katılması uygun olur', 3, 'Katilimcinin ingilizce destege ihtiyaci var.Hollandaca B1 ve kurs takip ediyor. IT tecrubesi yok. Motive gorunuyor. Belediyesinin VIT e nasil bakacagini bilmiyor. Eylul ayina kadar VIT e hazirlanmak istiyor bu yuzden uygun kaynak sordu.'),
('2023-05-10', 'sevil gulsen', 'ibrahim firat', 4, 'VIT projesinin tamamına katılması uygun olur', 'VIT projesinin tamamına katılması uygun olur', 7, 'yaklaşık 2 yıldır Hollandada. tarih öğretmeni ,akademisyenlik yapmıs. B1 kursuna başlayacak. yeni kanuna tabi. 1 cocuk var.  gonullu olarak çalışıyor. beledıye sıkıstırmaya baslamıs. kendi mesleginin karsılıgı burada yok. formasyon alması gerekiyormus. Belediye ogretmenlik yapmasına cok sıcak bakmıyor. grafik tasarımına ilgisi var. web tasarım noktasında da düşüncesi var. vit projesinin tamamına katılması uygun olur'),
('2023-05-12', 'enver unal', 'Yasin Bostanci', 7, 'VIT projesinin tamamına katılması uygun olur', 'VIT projesinin tamamına katılması uygun olur', 1, 'Daha onceki VIT projesine katilmis,fakat son mulakatta belirtilen randevu saatinden 1 saat  kadar sonra mentor gorusmeye gelmis. bu surede konsantrasyonunun bozuldugunu ve mulakata odaklanamadigini soyledi. Tekrar degerlendirilmesi uygun olur.'),
('2023-05-15', 'mehmet kilinc', 'Ibrahim Sahin', 5, 'VIT projesinin tamamına katılması uygun olur', 'VIT projesinin tamamına katılması uygun olur', 7, 'A2-B1 kursu takip ediyor. Bilincli bir aday. Once dil konusunu halledip bir sonraki VIT projesine katilmak istiyor.'),
('2023-05-16', 'hikmet sivri', 'Muhammed Ari', 6, 'VIT projesinin tamamına katılması uygun olur', 'VIT projesinin tamamına katılması uygun olur', 6, 'matematik ogretmeni, uzun sure java egitimi almis fakat iki dildede cok geride, felemenkceyi belli bir seviyeye getirip tekrar werhere surecine dahil olacak.'),
('2023-05-18', 'olcay deniz', 'ibrahim firat', 2, 'VIT projesinin tamamına katılması uygun olur', 'VIT projesinin tamamına katılması uygun olur', 8, 'Daha onceki vit projesinin teknik mulakatinda elenmisti. Abi bir okulda gonullu olarak ogretmenlik yapmis ama onlar normal is teklif etmeyince devam etmemis.  IT konusunda motivasyonu zayif. Full time calisma konusunda isteksiz. parttime yapacagi is bakiyor. ehliyetini almis , parttime okul minibusleri surmeyi dusunuyor. B1 hollandacasi var. IT hakkinda pek bilgiside yok gecmisten. Bence baska sektore yonlendirilmeli'),
('2023-05-18', 'asiye turan', 'ibrahim firat', 5, 'VIT projesinin tamamına katılması uygun olur', 'VIT projesinin tamamına katılması uygun olur', 5, 'Katilimci Testerlik egitimini tamamlamis. Ingilizcesi b2, hollandacasi B1 seviyelerinde. Is ararken Hollandaca konusunda cok sikinti cekmis. Yakin zamanda Motopp adli kurumda Mendix developer egitimine baslamis. Su asamada baska bir seyle ilgilenmek istemiyor. Ilerleyen zamanlarda Tester ya da Mendix developer alanlarinda is firsatlarina acik olabilir.'),
('2023-05-19', 'suat koksal', 'Yasin Bostanci', 6, 'VIT projesinin tamamına katılması uygun olur', 'VIT projesinin tamamına katılması uygun olur', 5, 'Aday Hollandaya 5 yil once gelmis, bu sure zarfinda dil egitimini B2 getirmis ve A2 sinavlarini gecmis. IT konusunda bilgi birikimi bulunmamakla beraber, hala biraz kararsizlik yasamaktadir. Bu yil yapilacak olan egitime katilmak istemektedir.'),
('2023-05-19', 'burhan yilmaz', 'Ibrahim Sahin', 4, 'VIT projesinin tamamına katılması uygun olur', 'VIT projesinin tamamına katılması uygun olur', 7, 'Katilimci hukuk mezunu. 2 yildir Hollanda da. Belediyesinden baski soz konusu degil. VIT projesinin ilk grubu icin de basvurmus ama ozel sebepler dolayisiyla gorusmeye katilamamis. Hollandacasi B1 baslangic seviyesinde. Su an dil kursu takip ediyor. Ingilizcesi de tam olarak oturmamis oldugundan hollandacasi su asamada iyi bir seviyeye getirdikten sonra VIT projesine basvurmasi daha uygun olabilir.');

-- Verify the data was inserted correctly
SELECT COUNT(*) AS total_records FROM Mentor;

-- Drop table if it already exists
DROP TABLE IF EXISTS Mulakatlar;

-- Tablo oluşturma
CREATE TABLE Mulakatlar (
    id SERIAL PRIMARY KEY,
    ad_soyad VARCHAR(100) NOT NULL,
    proje_gonderilis_tarihi DATE,
    projenin_gelis_tarihi DATE
);

-- Veri ekleme komutları
INSERT INTO Mulakatlar (ad_soyad, proje_gonderilis_tarihi, projenin_gelis_tarihi) VALUES
('ahmet selim', '2023-06-13', '2023-08-07'),
('mehmet kirmizi', '2023-06-13', '2023-08-07'),
('yasin kaya', '2023-06-08', NULL),
('zeynep yilmaz', '2023-06-15', '2023-08-08'),
('zeki duran', '2023-06-17', '2023-08-08'),
('mustafa celik', '2023-06-17', '2023-08-08'),
('nuh kececi', '2023-06-18', NULL),
('sahin okur', '2023-06-18', '2023-08-08'),
('mehmet dogan', '2023-06-18', '2023-08-09'),
('ahmet citlak', '2023-06-18', NULL),
('sevil gulsen', '2023-06-14', '2023-08-08'),
('melike guney', '2023-06-19', '2023-08-08'),
('esma donmez', '2023-06-12', NULL),
('enver unal', '2023-05-31', '2023-08-09'),
('murat uraz', '2023-06-19', NULL),
('yusuf akdogan', '2023-06-20', '2023-08-10'),
('emrah dikici', '2023-06-20', '2023-08-10'),
('Ali Veli', '2022-01-01', NULL),
('Hasan Huseyin', '2023-02-02', '2023-02-12');

Select *
From mulakatlar;


-- Drop table if it already exists
DROP TABLE IF EXISTS VIT1;

-- Create the VIT1 table
CREATE TABLE VIT1 (
    id SERIAL PRIMARY KEY,
    zaman_damgasi TIMESTAMP,
    ad_soyad VARCHAR(100),
    mail_adresi VARCHAR(100),
    telefon_numarasi VARCHAR(20),
    posta_kodu VARCHAR(10),
    yasadiginiz_eyalet VARCHAR(50),
    su_anki_durumunuz TEXT,
    egitim_tercihi TEXT,
    ekonomik_durum TEXT,
    dil_kursuna_devam BOOLEAN,
    ingilizce_seviye VARCHAR(20),
    hollandaca_seviye VARCHAR(20),
    belediye_baskisi TEXT,
    bootcamp_bitirdi BOOLEAN,
    online_it_kursu BOOLEAN,
    it_tecrubesi BOOLEAN,
    projeye_dahil BOOLEAN,
    calisma_istekleri TEXT,
    katilim_nedenleri TEXT,
    motivasyon TEXT,
    mentor_gorusmesi VARCHAR(20),
    ek_kolon1 VARCHAR(10),
    ek_kolon2 VARCHAR(10),
    ek_kolon3 VARCHAR(10),
    ek_kolon4 VARCHAR(10),
    durum VARCHAR(20),
    ek_kolon5 VARCHAR(10),
    ek_kolon6 VARCHAR(10),
    ek_kolon7 VARCHAR(10)
);

-- Temizlenmiş ve düzeltilmiş veri girişi

INSERT INTO VIT1 (
    zaman_damgasi, ad_soyad, mail_adresi, telefon_numarasi, posta_kodu, 
    yasadiginiz_eyalet, su_anki_durumunuz, egitim_tercihi, ekonomik_durum, 
    dil_kursuna_devam, ingilizce_seviye, hollandaca_seviye, belediye_baskisi, 
    bootcamp_bitirdi, online_it_kursu, it_tecrubesi, projeye_dahil, 
    calisma_istekleri, katilim_nedenleri, motivasyon, mentor_gorusmesi,
    ek_kolon1, ek_kolon2, ek_kolon3, ek_kolon4, durum, ek_kolon5, ek_kolon6, ek_kolon7
) VALUES
('2021-10-05 15:42:43', 'Kızıl Toprak', 'kızıltoprak@deneme.com', '655544332', '3522RT', 'Groningen', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Bu eğitimler ilgi alanım dışında başka alanlardaki eğitimlere katılmak istiyorum', 'Uitkering Alıyorum', FALSE, 'A2', 'A2', 'Hayır', FALSE, FALSE, FALSE, FALSE, 'Software Developer, Cyber Security', 'Bu mesleği yapabileceğime inanıyorum', 'Yapabileceğime inandığım için karar verdim', 'BEKLENİYOR', NULL, NULL, NULL, NULL, 'AKTIF', NULL, NULL, NULL),

('2021-01-04 13:55:18', 'Denek Ateş', 'denekates@deneme.com', '31684992228', '3566BG', 'Gelderland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Tester', 'Uitkering Alıyorum', TRUE, 'B1', 'B1', 'Kısmen', FALSE, FALSE, TRUE, FALSE, 'Tester, Web Tasarım, Software Developer, Data Engineer, Cyber Security', 'Teknik bir iş olduğu için daha az dil gereksinimi olduğunu düşünüyorum, IT sektöründe eleman ihtiyacı olduğu için, IT eğitimim veya iş tecrübem olduğu için, İngilizce çalışabilme imkanı olduğu için, Bu mesleği yapabileceğime inanıyorum', 'Bilgisayar öğretmeniyim. IT alanında devam etmek istiyorum. Çevremde birçok kişi bu alanda kurs alıp iş buldu. Bu beni motive ediyor.', 'TAMAMLANDI', '22', '33', '45', NULL, 'AKTIF', NULL, NULL, NULL),

('2021-05-05 22:49:30', 'Mavi Tahta', 'mavitahta@deneme.com', '684534456', '3987ET', 'Utrecht', 'Kampta, oturum görüşmesi bekliyorum', 'Cybersecurity eğitimine katılmak istiyorum', 'Diğer', FALSE, 'A2', 'A1', 'Henüz belediye belirlenmedi', FALSE, TRUE, TRUE, FALSE, 'Tester, Web Tasarım, Software Developer', 'IT eğitimim veya iş tecrübem olduğu için', 'Bu sektörde eğitimim ve tecrübem olduğu için sektördeki iş imkanlarını değerlendirmek istiyorum', 'BEKLENİYOR', NULL, NULL, NULL, NULL, 'PASIF', NULL, NULL, NULL),

('2021-05-16 22:55:32', 'Gönül Su', 'gönülsu@deneme.com', '626117733', '5125AB', 'Flevoland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Powerplatform eğitimine katılmak istiyorum', 'Uitkering Alıyorum', FALSE, 'B2+', 'A1', 'Hayır', TRUE, TRUE, FALSE, FALSE, 'Salesforce admin/developer', 'Sektörde maaşların iyi olduğunu düşünüyorum, İngilizce çalışabilme imkanı olduğu için, Bu mesleği yapabileceğime inanıyorum', '42 yaşındayım, 3 çocuğum var. Türkiye’de zor süreçlerden sonra buraya geldim. IT sektörü benim için yeni bir başlangıç ve fırsat.', 'TAMAMLANDI', NULL, NULL, NULL, NULL, 'AKTIF', NULL, NULL, NULL),

('2021-05-15 22:49:30', 'Gönüllü Pehlivan', 'pehlivangönüllü@deneme.com', '684534456', '1811ET', 'Nord Holland', 'Kampta, oturum görüşmesi bekliyorum', 'Cybersecurity eğitimine katılmak istiyorum', 'Diğer', FALSE, 'A2', 'A1', 'Henüz belediye belirlenmedi', FALSE, TRUE, TRUE, FALSE, 'Tester, Web Tasarım, Software Developer', 'IT eğitimim veya iş tecrübem olduğu için', 'Bu sektörde eğitimim ve tecrübem olduğu için sektördeki iş imkanlarını değerlendirmek istiyorum', 'BEKLENİYOR', NULL, NULL, NULL, NULL, 'PASIF', NULL, NULL, NULL),

('2021-10-25 15:42:43', 'Jon Snow', 'jonsnow@deneme.com', '655544332', '3520JS', 'Groningen', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Bu eğitimler ilgi alanım dışında başka alanlardaki eğitimlere katılmak istiyorum', 'Uitkering Alıyorum', FALSE, 'A2', 'A2', 'Hayır', FALSE, FALSE, FALSE, FALSE, 'Software Developer, Cyber Security', 'Bu mesleği yapabileceğime inanıyorum', 'Yapabileceğime inandığım için karar verdim', 'BEKLENİYOR', NULL, NULL, NULL, NULL, 'AKTIF', NULL, NULL, NULL),

('2021-10-25 15:41:00', 'Daenerys Targaryen', 'targaryen@deneme.com', '655544330', '3520JS', 'Groningen', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Bu eğitimler ilgi alanım dışında başka alanlardaki eğitimlere katılmak istiyorum', 'Uitkering Alıyorum', FALSE, 'A2', 'A2', 'Hayır', FALSE, FALSE, FALSE, FALSE, 'Software Developer, Cyber Security', 'Bu mesleği yapabileceğime inanıyorum', 'Yapabileceğime inandığım için karar verdim', 'BEKLENİYOR', NULL, NULL, NULL, NULL, 'AKTIF', NULL, NULL, NULL);

-- Verify the data was inserted correctly
SELECT COUNT(*) AS total_records FROM VIT1;
Select *
From public.vit1;


-- Drop table if it already exists
DROP TABLE IF EXISTS VIT2;

-- Create the VIT2 table
CREATE TABLE VIT2 (
    id SERIAL PRIMARY KEY,
    zaman_damgasi TIMESTAMP,
    ad_soyad VARCHAR(100),
    mail_adresi VARCHAR(100),
    telefon_numarasi VARCHAR(20),
    posta_kodu VARCHAR(10),
    yasadiginiz_eyalet VARCHAR(50),
    su_anki_durumunuz TEXT,
    egitim_tercihi TEXT,
    ekonomik_durum TEXT,
    dil_kursuna_devam BOOLEAN,
    ingilizce_seviye VARCHAR(20),
    hollandaca_seviye VARCHAR(20),
    belediye_baskisi TEXT,
    bootcamp_bitirdi BOOLEAN,
    online_it_kursu BOOLEAN,
    it_tecrubesi BOOLEAN,
    projeye_dahil BOOLEAN,
    calisma_istekleri TEXT,
    katilim_nedenleri TEXT,
    motivasyon TEXT,
    mentor_gorusmesi VARCHAR(20)
);

-- Insert all data in one go
INSERT INTO VIT2 (
    zaman_damgasi, ad_soyad, mail_adresi, telefon_numarasi, posta_kodu, 
    yasadiginiz_eyalet, su_anki_durumunuz, egitim_tercihi, ekonomik_durum, 
    dil_kursuna_devam, ingilizce_seviye, hollandaca_seviye, belediye_baskisi, 
    bootcamp_bitirdi, online_it_kursu, it_tecrubesi, projeye_dahil, 
    calisma_istekleri, katilim_nedenleri, motivasyon, mentor_gorusmesi
) VALUES
('2022-04-29 13:55:18', 'ahmet selim', 'yldrm@gmail.com', '3168499580', '6861BW', 'Noord-Holland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Tester', 'Uitkering Alıyorum', TRUE, 'B1', 'B1', 'Kısmen', FALSE, FALSE, TRUE, FALSE, 'Tester, Web Tasarım, Software Developer, Data Engineer, Cyber Security', 'Teknik bir iş olduğu için daha az dil gereksinimi olduğunu düşündünüyorum, Bu sektörde çok fazla eleman ihtiyacı olduğu için, IT ile ilgili eğitimim veya iş tecrübem olduğu için, İngilizce çalışabilme imkanı olduğu için, Bu mesleği yapabileceğime inanıyorum', 'Ben Bilgisayar ogretmeniydim. Ve it alanında devam etmek istiyorum. Bir çok arkadaşım bu alanda kurs alıp kısa sürede iş buldular. Bu imkanlar beni motive ediyor', 'OK'),
('2022-05-06 00:23:13', 'esma donmez', 'bsbns@gmail.com', '685768954', '7322CA', 'Noord-Holland', 'Kampta, oturum görüşmesi bekliyorum', 'Cybersecurity eğitimine katılmak istiyorum', 'Diğer', FALSE, 'B2 ve üzeri', 'A1', 'Hayır', FALSE, TRUE, TRUE, FALSE, 'Scrum Master, Software Developer, IT project management', 'IT ile ilgili eğitimim veya iş tecrübem olduğu için, İngilizce çalışabilme imkanı olduğu için', 'Ülkemde daha önce kamu kurumlarında ve özel sektörde IT alanında, farklı pozisyonlarda çalıştım. Burada da bu alanlardan birinde çalışmaya devam edebileceğimi düşünüyorum. Ancak birden fazla farklı alanda hem çalıştığım hem de eğitim aldığım için hangi alanda yoluma devam etmemin daha faydalı olacağı konusunda kararsızım. Hem bu konuda fikir edinebilmek, hem de bir mülteci olarak profesyonel iş yaşamına başlangıçta yapılabilecek koçluğun bana büyük katkı sağlayacağını düşündüğüm için bu projeye katılmak istiyorum.', 'OK'),
('2022-05-06 22:55:32', 'enver unal', 'kariparduc1977@gmail.com', '626119720', '5552AB', 'Noord-Holland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Powerplatform eğitimine katılmak istiyorum', 'Uitkering Alıyorum', FALSE, 'B2 ve üzeri', 'A1', 'Hayır', TRUE, TRUE, FALSE, FALSE, 'Salesforce admin/developer', 'Bu sektördeki maaşların iyi olduğunu düşünüyorum, İngilizce çalışabilme imkanı olduğu için, Bu mesleği yapabileceğime inanıyorum', 'Yaşım 42 ve 3 cocuğum var.Maalesef kendi ulkemde dibi gordukten sonra buralara gelmek nasip oldu.Her yönüyle yeni bir başlangıç istiyorum.IT sektörü bu konuda benim için çok cazip bir alan,bu yolda yürümek istiyorum.Ve bu konuda bana faydası olabilecek her fırsatı değerlendirmeye çalışıyorum.', 'OK'),
('2022-05-21 22:49:30', 'asiye turan', 'salihba@icloud.com', '684536214', '3981EC', 'Utrecht', 'Kampta, oturum görüşmesi bekliyorum', 'Cybersecurity eğitimine katılmak istiyorum', 'Diğer', FALSE, 'A2', 'A1', 'Henüz belediye belirlenmedi', FALSE, TRUE, TRUE, FALSE, 'Tester, Web Tasarım, Software Developer', 'IT ile ilgili eğitimim veya iş tecrübem olduğu için', 'Zaten bu sektörde eğitimim ve tecrübem bulunduğu için bu sektörde bulunan iş imkanlarını değerlendirmek istiyorum', 'ATANMADI'),
('2022-05-22 15:42:43', 'burhan yilmaz', 'nuri@gmail.com', '657932104', '5331AS', 'Noord-Holland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Bu eğitimler ilgi alanım dışında başka alanlardaki eğitimlere katılmak istiyorum', 'Uitkering Alıyorum', FALSE, 'A2', 'A2', 'Hayır', FALSE, FALSE, FALSE, FALSE, 'Software Developer, Cyber Security', 'Bu mesleği yapabileceğime inanıyorum', 'Yapabilecegime inandigim icin karar verdim', NULL),
('2022-05-10 15:42:43', 'Kızıl Toprak', 'kızıltoprak@deneme.com', '655544332', '3522RT', 'Groningen', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Bu eğitimler ilgi alanım dışında başka alanlardaki eğitimlere katılmak istiyorum', 'Uitkering Alıyorum', FALSE, 'A2', 'A2', 'Hayır', FALSE, FALSE, FALSE, FALSE, 'Software Developer, Cyber Security', 'Bu mesleği yapabileceğime inanıyorum', 'Yapabilecegime inandigim icin karar verdim', NULL),
('2022-04-01 13:55:18', 'Denek Ateş', 'denekates@deneme.com', '3168499222', '3566BG', 'Gelderland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Tester', 'Uitkering Alıyorum', TRUE, 'B1', 'B1', 'Kısmen', FALSE, FALSE, TRUE, FALSE, 'Tester, Web Tasarım, Software Developer, Data Engineer, Cyber Security', 'Teknik bir iş olduğu için daha az dil gereksinimi olduğunu düşündünüyorum, Bu sektörde çok fazla eleman ihtiyacı olduğu için, IT ile ilgili eğitimim veya iş tecrübem olduğu için, İngilizce çalışabilme imkanı olduğu için, Bu mesleği yapabileceğime inanıyorum', 'Ben Bilgisayar ogretmeniydim. Ve it alanında devam etmek istiyorum. Bir çok arkadaşım bu alanda kurs alıp kısa sürede iş buldular. Bu imkanlar beni motive ediyor', 'OK'),
('2022-05-05 22:49:30', 'Mavi Tahta', 'mavitahta@deneme.com', '684534456', '3987ET', 'Utrecht', 'Kampta, oturum görüşmesi bekliyorum', 'Cybersecurity eğitimine katılmak istiyorum', 'Diğer', FALSE, 'A2', 'A1', 'Henüz belediye belirlenmedi', FALSE, TRUE, TRUE, FALSE, 'Tester, Web Tasarım, Software Developer', 'IT ile ilgili eğitimim veya iş tecrübem olduğu için', 'Zaten bu sektörde eğitimim ve tecrübem bulunduğu için bu sektörde bulunan iş imkanlarını değerlendirmek istiyorum', 'ATANMADI'),
('2022-05-16 22:55:32', 'Gönül Su', 'gönülsu@deneme.com', '626117733', '5125AB', 'Flevoland', 'Eve geçtim (dil çalışıyorum ve/veya iş arıyorum ve/veya çalışıyorum)', 'Powerplatform eğitimine katılmak istiyorum', 'Uitkering Alıyorum', FALSE, 'B2 ve üzeri', 'A1', 'Hayır', TRUE, TRUE, FALSE, FALSE, 'Salesforce admin/developer', 'Bu sektördeki maaşların iyi olduğunu düşünüyorum, İngilizce çalışabilme imkanı olduğu için, Bu mesleği yapabileceğime inanıyorum', 'Yaşım 42 ve 3 cocuğum var.Maalesef kendi ulkemde dibi gordukten sonra buralara gelmek nasip oldu.Her yönüyle yeni bir başlangıç istiyorum.IT sektörü bu konuda benim için çok cazip bir alan,bu yolda yürümek istiyorum.Ve bu konuda bana faydası olabilecek her fırsatı değerlendirmeye çalışıyorum.', 'OK');

-- Verify the data was inserted correctly
SELECT COUNT(*) AS total_records FROM VIT2;
Select *
From vit2;


CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    start_time TIMESTAMP NOT NULL,
    participants TEXT,
    organizer VARCHAR(255)
);

INSERT INTO events (title, start_time, participants, organizer)
VALUES 
    ('Python Training', '2025-07-01 10:00:00', 'alice@example.com, bob@example.com', 'instructor@example.com'),
    ('Project Meeting', '2025-07-03 14:00:00', 'teamlead@example.com, member1@example.com', 'manager@example.com');