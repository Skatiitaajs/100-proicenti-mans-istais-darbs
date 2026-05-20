# Cheat Sheet: Python standarta bibliotēka `random`

## Bibliotēkas nosaukums

`random` - Python standarta bibliotēkas modulis pseido-nejaušu skaitļu ģenerēšanai.

## Kam bibliotēka paredzēta?

`random` palīdz veidot nejaušus skaitļus, izvēlēties nejaušus saraksta elementus, sajaukt sarakstus un veidot vienkāršas simulācijas.

## Kurās situācijās to izmanto?

- Spēlēs, piemēram, metamā kauliņa vai kāršu jaukšanas simulācijai.
- Mācību piemēros, kuros vajag nejaušus datus.
- Izlozēs un nejaušā izvēlē.
- Vienkāršās simulācijās, piemēram, temperatūras vai ceļa laika modelēšanai.
- Testēšanā, ja vajag ģenerēt dažādus piemēra datus.

## Bibliotēkas arhitektūra vienkāršā valodā

- `random` ir viens modulis Python standarta bibliotēkā, tāpēc tas nav jāinstalē atsevišķi.
- Moduļa pamatā ir pseido-nejaušo skaitļu ģenerators. Tas nozīmē, ka rezultāti izskatās nejauši, bet tos veido algoritms.
- Daudzas funkcijas izmanto kopīgu iekšējo ģeneratoru.
- `seed()` ļauj iestatīt sākuma vērtību, lai rezultātus varētu atkārtot.
- Funkcijas var iedalīt grupās: skaitļu ģenerēšana, izvēle no secībām, sarakstu jaukšana, baitu ģenerēšana un statistiskie sadalījumi.
- Drošības vajadzībām, piemēram, paroļu vai slepenu tokenu ģenerēšanai, jāizmanto `secrets`, nevis `random`.

## 15 izvēlētās funkcijas

### 1. `random.seed()`

Iestata sākuma vērtību nejaušo skaitļu ģeneratoram. Tas palīdz atkārtot vienus un tos pašus rezultātus.

```python
import random

random.seed(25)  # Vienāda seed vērtība dod vienādu secību
print(random.randint(1, 100))
```

### 2. `random.random()`

Atgriež nejaušu decimālskaitli no 0.0 līdz 1.0.

```python
import random

number = random.random()  # Skaitlis ir intervālā [0.0, 1.0)
print(number)
```

### 3. `random.randint()`

Atgriež nejaušu veselu skaitli starp divām robežām, ieskaitot abas robežas.

```python
import random

dice = random.randint(1, 6)  # Var iegūt 1, 2, 3, 4, 5 vai 6
print(dice)
```

### 4. `random.randrange()`

Izvēlas nejaušu skaitli no `range()` intervāla. Beigu robeža nav iekļauta.

```python
import random

even_number = random.randrange(0, 22, 2)  # Pāra skaitlis no 0 līdz 20
print(even_number)
```

### 5. `random.choice()`

Izvēlas vienu nejaušu elementu no saraksta, teksta virknes vai citas secības.

```python
import random

students = ["Anna", "Jānis", "Marta"]
print(random.choice(students))  # Izvēlas vienu skolēnu
```

### 6. `random.choices()`

Izvēlas vairākus elementus, un elementi var atkārtoties. Ar `weights` var norādīt izvēles iespējamību.

```python
import random

prizes = ["mazā balva", "vidējā balva", "lielā balva"]
result = random.choices(prizes, weights=[70, 25, 5], k=5)
print(result)
```

### 7. `random.shuffle()`

Sajauc saraksta elementus nejaušā secībā. Funkcija maina pašu sarakstu.

```python
import random

cards = ["A", "K", "Q", "J"]
random.shuffle(cards)  # Maina esošo sarakstu
print(cards)
```

### 8. `random.sample()`

Izvēlas vairākus unikālus elementus bez atkārtošanās.

```python
import random

participants = ["Anna", "Jānis", "Marta", "Rihards"]
winners = random.sample(participants, k=2)
print(winners)
```

### 9. `random.uniform()`

Atgriež nejaušu decimālskaitli starp divām robežām.

```python
import random

temperature = random.uniform(18.0, 24.0)
print(round(temperature, 1))
```

### 10. `random.triangular()`

Atgriež skaitli, kas biežāk ir tuvumā norādītajai tipiskajai vērtībai.

```python
import random

travel_time = random.triangular(10, 40, 20)
print(round(travel_time, 1))
```

### 11. `random.gauss()`

Ģenerē skaitli pēc normālā jeb Gausa sadalījuma.

```python
import random

grade = random.gauss(7, 1.5)  # Vidēji ap 7 ballēm
print(round(grade, 1))
```

### 12. `random.normalvariate()`

Arī ģenerē skaitli pēc normālā sadalījuma un ir noderīga simulācijām.

```python
import random

height = random.normalvariate(170, 8)
print(round(height, 1))
```

### 13. `random.getrandbits()`

Izveido nejaušu veselu skaitli ar noteiktu bitu skaitu.

```python
import random

number = random.getrandbits(8)
print(number)
print(format(number, "08b"))  # Binārais pieraksts
```

### 14. `random.randbytes()`

Izveido noteiktu skaitu nejaušu baitu.

```python
import random

data = random.randbytes(4)
print(data)
print(data.hex())
```

### 15. `random.betavariate()`

Atgriež skaitli no 0 līdz 1, ko var izmantot proporcijām vai procentiem.

```python
import random

progress = random.betavariate(2, 5)
print(round(progress * 100, 1), "%")
```

## Ieguvumi

- Bibliotēka ir iekļauta Python, tāpēc nav jāinstalē papildu pakotnes.
- Funkcijas ir īsas un viegli saprotamas.
- Ļauj veidot spēles, izlozes, testus un simulācijas.
- Ar `seed()` var atkārtot rezultātus, kas palīdz mācībās un testēšanā.

## Ierobežojumi

- `random` nav piemērots drošības vajadzībām, piemēram, paroļu vai slepenu tokenu ģenerēšanai.
- Rezultāti ir pseido-nejauši, nevis pilnīgi nejauši.
- Dažas sadalījumu funkcijas, piemēram, `gauss()` un `betavariate()`, prasa matemātisku izpratni.
- Ja `seed()` tiek lietots nepareizi, rezultāti var būt pārāk paredzami.

## Secinājums

`random` ir ļoti piemērota bibliotēka 11. klases projektam, jo tā ir viegli pieejama, praktiska un saprotama. Tā labi parāda, kā programmās izmantot nejaušību, bet vienlaikus iemāca svarīgu ierobežojumu: pseido-nejaušus skaitļus nedrīkst izmantot drošības uzdevumiem.
