# Mierzenie_wysokosci_slonca

### Urządzenie zostało zaprogramowane za pomocą Raspberry Pi Pico i z wykorzystaniem języka Python.

Celem urządzenia było wyznaczenie wysokości słońca w sanym momencie. Składa sięz dwóch serwomechanizmów i fotorezystorów. Szkic wykonania:

![obraz](https://user-images.githubusercontent.com/72561914/151588740-e3d7eb76-8bd5-4da4-b60d-91f2f205f822.png)

Rurka będzie nam wyznaczała wysokość słońca. Aby mogła się poruszać we wszystkie potrzebne kierunki, pierwszy serwomechanizm pozwoli nam o ruch 360 stopni w poziomie, a zaś drugi w pionie. Żeby wiedzieć jakie ustawienie jest potrzebne, będziemy na podstawie porównania wartości z fotorezystora przesuwać odpowiednio fotorezystory.

Schemat układu:

![obraz](https://user-images.githubusercontent.com/72561914/151588808-28dd9966-b170-4f57-af83-68765d40c2ab.png)

Zdjęcie wykonania:

![obraz](https://user-images.githubusercontent.com/72561914/151588865-05b1a66c-ab2d-49a7-aaa1-04ede18c1647.png)

### Uwagi:
Porejkt działa jedynie poprawnie w otwartych przestrzeniach i gdy nie jest zachmurzone niebo. W innym przypadku ustala położenie źródła światła.
