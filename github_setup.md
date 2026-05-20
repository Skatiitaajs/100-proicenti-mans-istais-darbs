# GitHub repozitorija izveides soļi

Šie soļi ir vajadzīgi, lai pilnībā izpildītu vērtēšanas kritēriju par GitHub un vairākiem commit.

## 1. Izveido jaunu GitHub repozitoriju

1. Atver https://github.com/
2. Nospied **New repository**.
3. Nosaukums, piemēram: `python-random-library-project`.
4. Izvēlies **Public** vai **Private** pēc skolotāja prasībām.
5. Neatzīmē README izveidi GitHub lapā, jo README jau ir projektā.

## 2. Atver projektu terminālī

```bash
cd python-library-project
```

## 3. Izveido vairākus commit

```bash
git init
git add .gitignore README.md requirements.txt
git commit -m "Izveido projekta pamatstruktūru"

git add examples/
git commit -m "Pievieno random bibliotēkas funkciju piemērus"

git add main.py
git commit -m "Izveido konsoles izvēlnes programmu"

git add gui.py
git commit -m "Pievieno tkinter vizuālo programmu"

git add cheat_sheet.md
git commit -m "Pievieno random bibliotēkas cheat sheet"

git add commit_messages.md project_plan.md assessment_checklist.md github_setup.md
git commit -m "Pievieno projekta plānu un pašpārbaudi"
```

## 4. Pievieno GitHub saiti un augšupielādē projektu

GitHub lapā pēc repozitorija izveides būs redzama tava repozitorija adrese. Aizvieto zemāk esošo saiti ar savu adresi.

```bash
git branch -M main
git remote add origin https://github.com/tavs-lietotajvards/python-random-library-project.git
git push -u origin main
```

## 5. Pārbaude pirms iesniegšanas

- GitHub lapā ir redzami visi projekta faili.
- GitHub sadaļā **Commits** ir vairāki commit, nevis tikai viens.
- README fails GitHub lapā atveras un ir salasāms.
- Skolotājam nosūtīta pareizā GitHub repozitorija saite.
