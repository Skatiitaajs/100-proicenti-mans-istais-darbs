# Python bibliotēkas `random` analīzes projekts

## Projekta mērķis

Šī projekta mērķis ir izpētīt Python standarta bibliotēkas moduli `random`, izveidot saprotamu Cheat Sheet un praktiski parādīt 15 bibliotēkas funkciju izmantošanu atsevišķos Python failos.

## Izvēlētās bibliotēkas pamatojums

Es izvēlējos `random`, jo tā ir Python standarta bibliotēka un nav jāinstalē ar ārējām pakotnēm. Tā ir piemērota 11. klases līmenim, jo ar īsiem piemēriem var saprast nejaušu skaitļu ģenerēšanu, izlozes, sarakstu sajaukšanu un vienkāršas simulācijas.

## Bibliotēkas arhitektūras kopsavilkums

`random` ir standarta bibliotēkas modulis, kas izmanto pseido-nejaušo skaitļu ģeneratoru. Tas nozīmē, ka rezultāti izskatās nejauši, bet tos aprēķina algoritms. Ar `seed()` var iestatīt sākuma vērtību, lai rezultātus atkārtotu. Funkcijas var iedalīt vairākās grupās: skaitļu ģenerēšana, izvēle no sarakstiem, sarakstu jaukšana, baitu ģenerēšana un statistiskie sadalījumi.

## Funkciju saraksts

1. `random.seed()` - iestata nejaušo skaitļu ģeneratora sākuma vērtību.
2. `random.random()` - iegūst decimālskaitli no 0.0 līdz 1.0.
3. `random.randint()` - iegūst veselu skaitli starp divām robežām.
4. `random.randrange()` - izvēlas skaitli no `range()` intervāla.
5. `random.choice()` - izvēlas vienu elementu no saraksta.
6. `random.choices()` - izvēlas vairākus elementus ar atkārtošanos.
7. `random.shuffle()` - sajauc saraksta elementu secību.
8. `random.sample()` - izvēlas unikālus elementus bez atkārtošanās.
9. `random.uniform()` - iegūst decimālskaitli starp divām robežām.
10. `random.triangular()` - ģenerē vērtību ar biežāku rezultātu pie tipiskās vērtības.
11. `random.gauss()` - ģenerē skaitli pēc Gausa sadalījuma.
12. `random.normalvariate()` - ģenerē skaitli pēc normālā sadalījuma.
13. `random.getrandbits()` - ģenerē veselu skaitli ar noteiktu bitu skaitu.
14. `random.randbytes()` - ģenerē noteiktu skaitu nejaušu baitu.
15. `random.betavariate()` - ģenerē proporciju no 0 līdz 1.

## Projekta struktūra

```text
python-library-project/
├── .gitignore
├── README.md
├── main.py
├── gui.py
├── cheat_sheet.md
├── requirements.txt
├── commit_messages.md
├── github_setup.md
├── project_plan.md
├── assessment_checklist.md
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

## Kā palaist programmu

Konsoles versija:

```bash
python main.py
```

Vizuālā versija ar `tkinter`:

```bash
python gui.py
```

Atsevišķu piemēru var palaist arī šādi:

```bash
python examples/function_03.py
```

## Izmantotās saites

- Python standarta bibliotēkas saraksts: https://docs.python.org/3/library/index.html
- Python `random` dokumentācija: https://docs.python.org/3/library/random.html
- Uzdevumā dotā populāro bibliotēku saite: https://www.geeksforgeeks.org/blogs/python-libraries-to-know/

## Ieguvumi

- `random` ir iekļauts Python standarta bibliotēkā.
- To ir viegli lietot nelielos piemēros.
- Bibliotēka ir praktiska spēlēm, izlozēm, testiem un simulācijām.
- Ar `seed()` var atkārtot vienādus rezultātus, kas palīdz pārbaudē un mācībās.
- Projekts satur gan konsoles programmu, gan vizuālu `tkinter` programmu.

## Ierobežojumi

- `random` nav paredzēts drošībai, piemēram, paroļu vai slepenu tokenu ģenerēšanai.
- Rezultāti ir pseido-nejauši, jo tos veido algoritms.
- Dažas funkcijas, piemēram, `gauss()` un `betavariate()`, ir saistītas ar statistiku un var prasīt papildu skaidrojumu.
- Vizuālā programma ir vienkārša mācību vajadzībām, nevis pilna profesionāla lietotne.

## Pašvērtējums pēc kritērijiem

Projekts atbilst maksimālā vērtējuma prasībām, jo tajā ir jēgpilni aprakstītas 15 `random` funkcijas, katrai funkcijai ir savs `.py` fails ar komentāriem latviešu valodā, ir izveidota konsoles programma un vizuāla `tkinter` programma piemēru palaišanai. README un Cheat Sheet skaidro bibliotēkas izvēli, arhitektūru, funkcijas, ieguvumus un ierobežojumus. Faili ir sakārtoti tā, lai tos varētu ievietot GitHub repozitorijā ar vairākiem saprotamiem commit ziņojumiem.

## Ieteicamie GitHub commit ziņojumi

1. `Izveido projekta pamatstruktūru`
2. `Pievieno random bibliotēkas funkciju piemērus`
3. `Izveido konsoles izvēlnes programmu`
4. `Pievieno tkinter vizuālo programmu`
5. `Pievieno random bibliotēkas cheat sheet`
6. `Papildina README ar kritērijiem un secinājumiem`
7. `Pievieno projekta plānu un pašpārbaudi`

Detalizēti GitHub augšupielādes soļi atrodami failā `github_setup.md`.
