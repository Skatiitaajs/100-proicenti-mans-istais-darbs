# Projekta darba plāns

## 1. Bibliotēkas izvēle

Sākumā izvēlējos Python standarta bibliotēku `random`, jo tā ir pieejama
uzreiz pēc Python instalēšanas. Man bija svarīgi izvēlēties bibliotēku,
kuru var parādīt ar vienkāršiem piemēriem.

## 2. Dokumentācijas apskate

Paskatījos Python dokumentācijā, kādas funkcijas ir `random` modulī.
No saraksta izvēlējos 15 funkcijas. Centos paņemt ne tikai ļoti vienkāršās
funkcijas, bet arī dažas grūtākas, lai parādītu plašāku izpratni.

## 3. Piemēru izveide

Katrai funkcijai izveidoju atsevišķu failu mapē `examples`. Katrā failā ir:

- funkcijas nosaukums;
- īss paskaidrojums;
- komentāri latviešu valodā;
- vienkāršs piemērs;
- rezultāta izvadīšana ar `print()`.

## 4. Galvenā programma

Pēc tam izveidoju `main.py`, kur lietotājs var izvēlēties piemēru pēc
numura. Šo daļu veidoju vienkāršu, lai kodu varētu viegli izskaidrot.

## 5. Vizuālā programma

Lai projekts būtu pilnīgāks, pievienoju arī `gui.py`. Tajā izmantots
`tkinter`, kas ir Python standarta bibliotēkā. Lietotājs var izvēlēties
funkciju sarakstā un nospiest pogu.

## 6. Dokumentācija

Uzrakstīju `README.md` un `cheat_sheet.md`. README vairāk paskaidro pašu
projektu, bet Cheat Sheet ir īss palīgs par `random` funkcijām.

## 7. Ko es varu izskaidrot prezentācijā

- Kāpēc izvēlējos `random`.
- Kas ir pseido-nejauši skaitļi.
- Kā strādā `seed()`.
- Kā atšķiras `choice()`, `choices()` un `sample()`.
- Kāpēc `random` nevajadzētu izmantot parolēm.

## 8. Pārbaude

Pārbaudīju, ka piemēri palaižas un galvenā programma parāda izvēlni.
Ja projektu liek GitHub, svarīgi izveidot vairākus commit, nevis visu
ielikt vienā reizē.
