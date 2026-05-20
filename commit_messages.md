# Ieteicamie GitHub commit ziņojumi

Projektam vēlams neveidot tikai vienu commit. Labāk darbu sadalīt vairākos loģiskos soļos.

1. `Izveido projekta pamatstruktūru`
2. `Pievieno random bibliotēkas funkciju piemērus`
3. `Izveido galveno izvēlnes programmu`
4. `Pievieno random bibliotēkas cheat sheet`
5. `Papildina README ar palaišanas instrukcijām un secinājumiem`
6. `Pārskata komentārus un projekta noformējumu`

## Ieteicamā secība GitHub darbam

```bash
git init
git add README.md cheat_sheet.md requirements.txt commit_messages.md
git commit -m "Izveido projekta pamatstruktūru"

git add examples/
git commit -m "Pievieno random bibliotēkas funkciju piemērus"

git add main.py
git commit -m "Izveido galveno izvēlnes programmu"

git add README.md cheat_sheet.md
git commit -m "Papildina README ar palaišanas instrukcijām un secinājumiem"
```
