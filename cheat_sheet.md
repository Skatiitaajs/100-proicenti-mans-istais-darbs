# Cheat Sheet: `random`

## Kas tā ir par bibliotēku?

`random` ir Python standarta bibliotēkas modulis, ar kuru var iegūt
nejaušus skaitļus, izvēlēties nejaušus elementus un sajaukt sarakstus.
Tā nav jāinstalē atsevišķi.

## Kur to var izmantot?

- spēlēs, piemēram, metamā kauliņa simulācijai;
- izlozēs;
- nejaušu testa datu veidošanā;
- sarakstu sajaukšanā;
- vienkāršās simulācijās.

## Arhitektūra īsumā

`random` izmanto pseido-nejaušu skaitļu ģeneratoru. Tas nozīmē, ka
rezultāts izskatās nejaušs, bet patiesībā to aprēķina algoritms. Ja
izmanto `seed()`, var panākt, ka rezultāti atkārtojas. Tas ir noderīgi
mācību piemēros, jo skolotājs un skolēns var redzēt vienādu rezultātu.

Funkcijas var sadalīt vairākās grupās:

- skaitļu ģenerēšana;
- izvēle no sarakstiem;
- sarakstu sajaukšana;
- baitu ģenerēšana;
- statistiski sadalījumi.

Svarīgi: paroles un slepenus kodus ar `random` labāk neveidot. Tam Python
ir cita bibliotēka - `secrets`.

## 15 funkcijas ar piemēriem

### 1. `random.seed()`

Iestata sākuma vērtību. Ja sākuma vērtība ir vienāda, rezultāti atkārtojas.

```python
import random

random.seed(25)  # Iestatu sākuma vērtību
print(random.randint(1, 100))  # Rezultāts būs atkārtojams
```

### 2. `random.random()`

Izveido decimālskaitli no 0.0 līdz gandrīz 1.0.

```python
import random

number = random.random()  # Nejaušs decimālskaitlis
print(number)
```

### 3. `random.randint()`

Izveido veselu skaitli starp divām robežām. Abas robežas ir iekļautas.

```python
import random

dice = random.randint(1, 6)  # Metamais kauliņš
print(dice)
```

### 4. `random.randrange()`

Izvēlas skaitli no `range()` intervāla.

```python
import random

even_number = random.randrange(0, 22, 2)  # Pāra skaitlis no 0 līdz 20
print(even_number)
```

### 5. `random.choice()`

Izvēlas vienu elementu no saraksta.

```python
import random

students = ["Anna", "Jānis", "Marta"]
chosen = random.choice(students)  # Izvēlas vienu skolēnu
print(chosen)
```

### 6. `random.choices()`

Izvēlas vairākus elementus. Elements var atkārtoties.

```python
import random

prizes = ["mazā balva", "vidējā balva", "lielā balva"]
result = random.choices(prizes, weights=[70, 25, 5], k=5)
print(result)
```

### 7. `random.shuffle()`

Sajauc sarakstu. Funkcija maina pašu sarakstu.

```python
import random

cards = ["A", "K", "Q", "J"]
random.shuffle(cards)  # Sajauc kārtis
print(cards)
```

### 8. `random.sample()`

Izvēlas vairākus elementus bez atkārtošanās.

```python
import random

participants = ["Anna", "Jānis", "Marta", "Rihards"]
winners = random.sample(participants, k=2)
print(winners)
```

### 9. `random.uniform()`

Izveido decimālskaitli starp divām robežām.

```python
import random

temperature = random.uniform(18.0, 24.0)
print(round(temperature, 1))
```

### 10. `random.triangular()`

Izveido skaitli, kas biežāk ir tuvumā tipiskajai vērtībai.

```python
import random

travel_time = random.triangular(10, 40, 20)
print(round(travel_time, 1))
```

### 11. `random.gauss()`

Izveido skaitli pēc Gausa sadalījuma.

```python
import random

grade = random.gauss(7, 1.5)  # Ap vidējo vērtējumu 7
print(round(grade, 1))
```

### 12. `random.normalvariate()`

Arī izmanto normālo sadalījumu. To var lietot līdzīgi kā `gauss()`.

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
print(data.hex())  # Ērtāks pieraksts
```

### 15. `random.betavariate()`

Izveido skaitli no 0 līdz 1. To var uztvert kā proporciju.

```python
import random

progress = random.betavariate(2, 5)
print(round(progress * 100, 1), "%")
```

## Ieguvumi

- Nav jāinstalē papildu pakotnes.
- Piemēri ir īsi un viegli izmēģināmi.
- Bibliotēka der spēlēm, izlozēm un simulācijām.
- `seed()` palīdz atkārtot rezultātus.

## Ierobežojumi

- Tā nav piemērota parolēm un drošības kodiem.
- Rezultāti ir pseido-nejauši.
- Dažām funkcijām vajag saprast statistikas pamatus.
- Ja nepareizi lieto `seed()`, rezultāti var kļūt pārāk paredzami.

## Mans secinājums

`random` ir laba bibliotēka šādam skolas projektam, jo tā ir vienkārša,
bet ar to var parādīt daudz dažādu situāciju. Man visvieglāk saprotamas
bija `randint()`, `choice()` un `shuffle()`, jo tās var uzreiz sasaistīt
ar spēlēm vai izlozēm. Sarežģītākas bija sadalījumu funkcijas, piemēram,
`gauss()` un `betavariate()`, jo tur jau jādomā par statistiku.
