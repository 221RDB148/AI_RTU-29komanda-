# AI_RTU komanda-29
## Programmas dotās prasības
Spēles sākumā cilvēks-spēlētājs izvēlas, ar cik akmentiņiem spēle tiks uzsākta. Akmentiņu diapazons ir no 50 līdz 70.

### Spēles apraksts 

Uz galda atrodas tik daudz akmentiņu, cik izvēlējās cilvēks-spēlētājs. Katram spēlētājam spēles sākumā ir 0 akmentiņu un 0 punktu. Spēlētāji izpilda gājienus pēc kārtas. Spēlētājs savā gājienā drīkst paņemt sev 2 vai 3 akmentiņus. Ja pēc akmentiņu paņemšanas uz galda ir palicis pāra akmentiņu skaits, tad pretinieka punktiem tiek pieskaitīti 2 punkti, bet ja nepāra skaits, tad spēlētāja punktu skaitam tiek pieskaitīti 2 punkti. Spēle beidzas, kad uz galda nepaliek neviens akmentiņš. Spēlētāju punktu skaitam tiek pieskaitīts spēlētājam esošo akmentiņu skaits. Ja spēlētāju punktu skaits ir vienāds, tad rezultāts ir neizšķirts. Pretējā gadījumā uzvar spēlētājs, kam ir vairāk punktu. 

## Izmantošana
Programmu var izmantot bez papildus pakotnēm, taču ieteicams tomēr instalēt zemāk norādītās.
Var palaist arī bez ttkthemes, bet tad jāaizvieto `root = ThemedTk(theme="arc")` ar `root = tk.Tk()`
### Nepieciešamās pakotnes
* `matplotlib` priekš vizualizēšanas iekš `graph.py`
```sh
pip install matplotlib
```
* `ttkthemes` priekš mazliet modernāka UI
```sh
pip install ttkthemes
```
Var arī uzinstalēt visas uzreiz ar
```sh
pip install requirements.txt
```
