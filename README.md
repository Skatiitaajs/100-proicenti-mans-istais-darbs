# Python bibliotēkas `random` izpēte

## Projekta mērķis

Šajā darbā es izpētīju Python standarta bibliotēkas moduli `random`.
Mērķis bija saprast, kā Python var veidot nejaušus skaitļus, izvēlēties
nejaušus elementus no saraksta un izmantot to vienkāršās programmās.

Projektā ir:

- īss bibliotēkas skaidrojums;
- Cheat Sheet ar 15 funkcijām;
- katrai funkcijai savs `.py` fails;
- konsoles programma ar izvēlni;
- vienkārša vizuālā programma ar `tkinter`.

## Kāpēc izvēlējos `random`

Es izvēlējos `random`, jo tā ir iekļauta pašā Python un nav jāinstalē
papildu bibliotēkas. Man šī bibliotēka šķita piemērota, jo tās piemērus
var viegli saprast: metamais kauliņš, izloze, skolēna izvēle no saraksta,
kāršu sajaukšana un līdzīgas situācijas.

Vēl viens iemesls ir tas, ka `random` labi parāda, ka programmēšanā var
veidot arī mazus eksperimentus un simulācijas, ne tikai aprēķinus pēc
vienas formulas.

## Īsi par bibliotēkas uzbūvi

`random` ir Python standarta bibliotēkas modulis. Tas izmanto
pseido-nejaušu skaitļu ģeneratoru. Tas nozīmē, ka rezultāti izskatās
nejauši, bet tos izveido algoritms.

Svarīga funkcija ir `seed()`. Ar to var iestatīt sākuma vērtību, lai
programma atkārtoti dotu tos pašus rezultātus. Tas ir noderīgi, ja
piemērs jāpārbauda vai jāparāda skolotājam.

## Izmantotās funkcijas

1. `random.seed()` - iestata sākuma vērtību nejaušajam ģeneratoram.
2. `random.random()` - izveido decimālskaitli no 0.0 līdz 1.0.
3. `random.randint()` - izveido veselu skaitli starp divām robežām.
4. `random.randrange()` - izvēlas skaitli no `range()` intervāla.
5. `random.choice()` - izvēlas vienu elementu no saraksta.
6. `random.choices()` - izvēlas vairākus elementus, atļaujot atkārtošanos.
7. `random.shuffle()` - sajauc saraksta elementus.
8. `random.sample()` - izvēlas vairākus unikālus elementus.
9. `random.uniform()` - izveido decimālskaitli starp divām robežām.
10. `random.triangular()` - izveido skaitli, kas biežāk ir ap tipisko vērtību.
11. `random.gauss()` - izmanto Gausa jeb normālo sadalījumu.
12. `random.normalvariate()` - arī izmanto normālo sadalījumu.
13. `random.getrandbits()` - izveido nejaušu skaitli no bitiem.
14. `random.randbytes()` - izveido nejaušus baitus.
15. `random.betavariate()` - izveido skaitli no 0 līdz 1, piemēram, proporcijai.

## Projekta struktūra

```text
100% mans īstais darbs/
├── .gitignore
├── README.md
├── main.py
├── gui.py
├── cheat_sheet.md
├── project_plan.md
├── requirements.txt
└── examples/
    ├── __init__.py
    ├── function_01.py
    ├── function_02.py
    ├── function_03.py
    ├── function_04.py
    ├── function_05.py
    ├── function_06.py
    ├── function_07.py
    ├── function_08.py
    ├── function_09.py
    ├── function_10.py
    ├── function_11.py
    ├── function_12.py
    ├── function_13.py
    ├── function_14.py
    └── function_15.py
```

## Kā palaist

Konsoles programmu var palaist ar komandu:

```bash
python main.py
```

Tad jāievada funkcijas numurs no 1 līdz 15.

Vizuālo programmu var palaist ar komandu:

```bash
python gui.py
```

Atsevišķu piemēru var palaist arī tieši, piemēram:

```bash
python examples/function_03.py
```

## Izmantotie avoti

- Python standarta bibliotēka: https://docs.python.org/3/library/index.html
- `random` dokumentācija: https://docs.python.org/3/library/random.html
- Uzdevumā dotā populāro bibliotēku saite: https://www.geeksforgeeks.org/blogs/python-libraries-to-know/

## Ieguvumi

- Bibliotēka jau ir Python sastāvā.
- Funkcijas ir īsas un salīdzinoši viegli saprotamas.
- To var izmantot spēlēs, izlozēs, testos un vienkāršās simulācijās.
- Ar `seed()` var iegūt atkārtojamus rezultātus, kas ir ērti mācību darbā.
- Piemērus var palaist gan konsolē, gan vizuālā logā.

## Ierobežojumi

- `random` nav domāts drošām parolēm vai slepeniem kodiem.
- Rezultāti nav pilnīgi nejauši, jo tos aprēķina algoritms.
- Dažas funkcijas ir saistītas ar statistiku, tāpēc tās sākumā var būt grūtāk saprast.
- Ja visur lieto vienādu `seed()`, rezultāti kļūst paredzami.

## Pašvērtējums

Manuprāt, projekts atbilst uzdevuma prasībām, jo ir aprakstītas 15
funkcijas un katrai ir savs piemēra fails. Komentārus rakstīju tā, lai
varētu pats izskaidrot, ko dara katra rinda. `main.py` ļauj izvēlēties
piemēru pēc numura, bet `gui.py` dod vienkāršu vizuālo variantu.

Grūtākā daļa bija izskaidrot tās funkcijas, kas saistītas ar sadalījumiem,
piemēram, `gauss()` un `betavariate()`. Tāpēc piemēros centos izmantot
ikdienišķas situācijas, piemēram, vērtējumu, augumu vai darba progresu.

## Ieteicamie commit nosaukumi

1. `Izveido projekta sākuma failus`
2. `Pievieno random funkciju piemērus`
3. `Izveido konsoles izvēlni`
4. `Pievieno tkinter vizuālo programmu`
5. `Uzraksta cheat sheet un projekta aprakstu`
6. `Sakārto komentārus un README failu`
