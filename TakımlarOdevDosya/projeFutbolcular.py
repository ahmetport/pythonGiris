"""
futbolcular.txt" şeklinde bir dosya oluşturun ve içine Galatasaray,Fenerbahçe ve Beşiktaşta oynayan
 futbolcuları rastgele yerleştirin. Bu dosyadan herbir takımın futbolcularını ayırarak
  "gs.txt" , "fb.txt", "bjk.txt" şeklinde 3 farklı dosyaya yazın.

"futbolcular.txt" dosyasının başlangıç hali şu şekilde olsun.

                Fernando Muslera,Galatasaray
                Atiba Hutchinson,Beşiktaş
                Simon Kjaer,Fenerbahçe
                           //
                           //
                           //
                           //
                           //
"""

with open("futbolcular.txt", "r", encoding="utf-8") as file:
    gs = list()
    bjk = list()
    fb = list()

    for satir in file:
        satir = satir[:-1]
        satir_elemanlari = satir.split(",")
        if (satir_elemanlari[1] == "Fenerbahçe"):
            fb.append(satir + "\n")
        elif (satir_elemanlari[1] == "Galatasaray"):
            gs.append(satir + "\n")

        else:
            bjk.append(satir + "\n")
    with open("gs.txt", "w", encoding="utf-8") as file1:
        for i in gs:
            file1.write(i)

    with open("fb.txt", "w", encoding="utf-8") as file2:
        for i in fb:
            file2.write(i)
    with open("bjk.txt", "w", encoding="utf-8") as file3:
        for i in bjk:
            file3.write(i)