# "Git i GitHub - Podstawowe Komendy"

## Git: Co to jest?
- System kontroli wersji.
- Pozwala śledzić zmiany w kodzie źródłowym.

## Dlaczego Git?
- Śledzenie historii projektu.
- Współpraca z innymi programistami.
- Bezpieczne przechowywanie kodu.

## Podstawowe Komendy Git:

### Inicjalizacja Repozytorium:
```bash
git init
```
Dodawanie Plików do Stage:
```bash
git add nazwa_pliku
```
Zapisanie Zmian w Repozytorium:
```bash
git commit -m "Opis zmian"
```
Sprawdzanie Statusu Repozytorium:
```bash
git status
```
Sprawdzanie Historii Commitów:
```bash
git log
```
Przywracanie Poprzednich Wersji Pliku:
```bash
git checkout nazwa_pliku
```
Tworzenie Nowego Brancha:
```bash
git branch nowy_branch
```
Przełączanie się między Branchami:
```bash
git checkout nazwa_brancha
```
Utworzenie nowego brancha i przełączenie się na niego:
```bash
git checkout -b nazwa_brancha
```
Łączenie Branchy:
```bash
git merge nazwa_brancha
```
Pobieranie Zmian z Repozytorium Zdalnego:
```bash
git pull origin master
```
Wysyłanie Zmian do Repozytorium Zdalnego:
```bash
git push origin master
```
Zapisanie bieżących zmian na stosie:
```bash
git stash
```
Zapisanie i przywrócenie zmian w jednym poleceniu:
```bash
git stash pop
```
Pokazanie listy zapisanych na stosie zmian:
```bash
git stash list
```
Dodanie zdalnego repozytorium o nazwie "origin":
```bash
git remote add origin URL_repozytorium
```
Pokazanie szczegółów dotyczących repozytorium zdalnego "origin":
```bash
git remote -v
```