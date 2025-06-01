# Kayıp Veri ile Başa Çıkma Yöntemleri
## Kayıp Verileri Silme (Omission)
Bir veri bilimi projesinde kayıp veri ile karşılaşınca akla gelen ilk yöntem kayıp veriyi görmezden gelmektir (omitting). Kayıp veriyi silerek görmezden gelebiliriz. İki farklı kayıp veri silme yöntemi vardır bunlar tam satır silme (Case-wise Deletion) ve çiftler halinde silme (Pair-wise Deletion) yöntemleridir.
### Tam Satır Silme (Casewise Deletion - Listwise Deletion)
Tam satır silme veri setinde herhangi bir kayıp veri noktası içeren satırların silinmesi işlemidir. Bu işlem zamandan büyük tasarruf sağlarken aynı zamanda veri setinin azalmasına yani örneklemin küçülmesine neden olur. Bu azalmanın sonucunda eğitilen modellerin genelleme yetenekleri azalabilir aynı zamanda modellerin yanlı olmasına neden olabilir. Bu yöntem genellikle büyük veri setlerinde tercih edilir.
### Çiftler Halinde Silme (Pairwise Deletion)
Çiftler halinde silme yönteminde sadece analiz için kullanıcak değişkenlerdeki kayıp veriler silinir. Bu da görece basit bir yöntemdir. Tam satır silmeden farklı olarak daha az veri silinmiş olur fakat sonuç olarak örneklem küçülür bunun sonucunda eğitilen model yeterince genel olamaz ya da yanlı olabilir. Bu yöntem de genellikle büyük veri setlerinde tercih edilir.
## İstatiksel Yöntemler ile Doldurma
Örneklem küçükse veya veriyi silmek gerçekten büyük bir yanlılığa neden olacaksa kayıp veri doldurma(missing value imputation) gerçekten iyi bir çözüm olacaktır. Genellikle çoğu projede verileri silmek yerine doldurmak tercih edilir. Veri doldurmak çoğunlukla maliyetli ve proje süresini uzatan bir yöntemdir. Veri doldurma yöntemleri denince akla ilk gelen yöntemler istatistiksel yöntemlerdir. Bu yöntemler veri setinin istatiksel parametreleri korunarak kayıp verilerin yerine konulması ile gerçekleştirilir. Bu yöntemler verilerin türlerine bakılarak gerçekleştirilir örneğin kayıp veri olan değişken devamlı (continuous) bir veri ise ortalama (mean) ile doldurma yöntemi seçilirken kategorik(categorical) bir veri ise mod (mode) ile doldurma yöntemi seçilir.
### Ortalama(Mean) ile Doldurma
Değişkenin veri türü devamlı(continuous) veya sıralı(ordinal) ve değişken normal dağılım sergiliyorsa eksik veriler ortalama ile doldurulabilir. Verilerin ortalama ile doldurulması değişkenin ortalamasında bir değişkenliğe sebep olmaz fakat değişkenin varyansını(variance) azaltır. Bu durum zaman zaman yanlılığa neden olabilir.
### Medyan(Median) ile Doldurma
Medyan ile doldurma yöntemi ortalama ile doldurma yönteminin uygun olmadığı durumlarda kullanılır. Değişken normal dağılmıyorsa veya aykırı değer (outlier) içeriyorsa eksik veri doldurma yöntemi olarak medyan ile doldurma yöntemi tercih edilmelidir. Bu durumda değişkenin varyansını (variance) azaltırken zaman zaman yanlılığa neden olabilir.
### Mod(Mode) ile Doldurma
Değişkenin veri türü kategorik (categorical) ise eksik veriler mod (en çok tekrar eden değer) ile doldurulabilir. İlk başta iyi bir yöntem gibi görünse de mod ile doldurmak, değişkendeki ençok tekrar eden değerin sayısının artmasına ve bir yanlılığa neden olur. Mod ile doldurma yöntemi değişken çok sayıda eşsiz(unique) değer var ise kullanılmamalıdır.
### Önceki veya Sonraki Değerler ile Doldurma
Genellikle zaman serisi (time series) verilerinde kullanılan bu yöntemde, eksik veriler bir önceki veya bir sonraki anda bulunan değerler ile doldurulur. Bu yaklaşım, zaman serisi verilerinin doğal yapısını ve veriler arasındaki zamansal ilişkiyi korumaya yardımcı olduğu için yaygın olarak tercih edilmektedir. Özellikle düzenli aralıklarla toplanan verilerde ve kısa süreli eksik veri durumlarında çokça kullanılmaktadır. Bu yöntem, veri setindeki genel trendi ve mevsimsel desenleri korumada başarılıdır.
## Makine Öğrenmesi Yöntemleri
### Regresyon(Regression) ile Doldurma
Bu yöntemde eksik veri barındıran değişken diğer değişkenler kullanılarak tahmin edilir. Kayıp veriler barındıran değişken devamlı(continuous) ise doğrusal regresyon(lineer regression) kullanılarak doldurulur. Bu yöntemde eksik veri bulunduran değişken bağımlı(dependent) diğer değişkenler bağımsız(independent) değişkenler olarak değerlendirilir.
### K-En Yakın Komşu(kNN) ile Doldurma
Eksik veri barındıran değişken kategorik(categorical) ise kNN yöntemi kullanılabilir. Bu yöntemde kayıp veri barındıran gözlem ona benzer gözlemlere bakılarak doldurulur. Bu algoritmanın benzerlik açısından faklı ölçütleri var. Veri için en doğru benzerlik yöntemi seçilmelidir.
### Beklenti Maksimizasyonu (Expectation-Maximization)
Günümüzde literatürde oldukça kullanılan bir yöntemdir. Beklenti Maximizasyonu (Expectation-Maximization) algoritması, kayıp veriler içeren istatistiksel modellerde, model parametrelerinin en uygun (maksimum likelihood) tahminlerini yapmak için kullanılan yinelemeli (iterative) bir yöntemdir. Algoritma, önce parametreler için bir başlangıç tahmini yapar, ardından her adımda iki aşamalı bir süreç izler:

- E-adımında, mevcut parametrelerle gözlemlenemeyen verilerin olasılık dağılımı tahmin edilir (beklenen değer hesaplanır)
- M-adımında ise bu beklenen değerlere göre parametreler yeniden optimize edilir.

Bu adımlar, modelin gözlemlenen veriye uyumu artana kadar tekrarlanır. EM algoritması, özellikle Gaussian Karışım Modelleri (Gaussian Mixture Model), Gizli Markov Modelleri (Hidden Markov Model) ve eksik veri içeren problemlerde yaygın olarak kullanılır.
