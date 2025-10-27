# Git Pointers Übung: Branches als Pointer verstehen

## 📚 Lernziele

Nach Abschluss dieser Übung wirst du die wichtigsten Konzepte aus der Vorlesung verstehen.

## 📝 Anleitung

### Schritt 1: Übung lesen

Öffne [`exercise.md`](./exercise.md) und lies jede Frage sorgfältig durch.

### Schritt 2: Antworten eintragen

Bearbeite die Datei [`answers.py`](./answers.py) und trage deine Antworten ein:

```python
# Beispiel:
answers = {
    1: "A",  # Frage 1: Option A
    2: "D",  # Frage 2: Option D
    # ... fülle alle 20 Fragen aus
}
```

### Schritt 3: Lokal testen (optional)

Bevor du pushst, kannst du deine Antworten lokal testen:

```bash
# Dependencies installieren
uv sync

# Tests ausführen
uv run pytest tests/test_answers.py -v
```

### Schritt 4: Über Git einreichen

```bash
# Änderungen zum Commit vormerken
git add answers.py

# Commit erstellen
git commit -m "Submit Git Pointers Exercise answers"

# Änderungen pushen
git push
```

### Schritt 5: Autograding überprüfen

Nach dem Pushen führt GitHub Actions automatisch Tests aus.

1. Gehe im Repository auf den „Actions“ Tab  
2. Klicke auf den neuesten Workflow Run  
3. Überprüfe, ob die Tests bestanden ✅ oder fehlgeschlagen ❌ sind

Wenn Tests fehlschlagen:
- Lies die Fehlermeldungen aufmerksam durch  
- Aktualisiere `answers.py`  
- Committe und pushe erneut  

## 📊 Bewertung

- **17–20 richtig**: Excellent! 🏆
- **14–16 richtig**: Good understanding! 👍
- **10–13 richtig**: Grundverständnis vorhanden – wiederhole die Lecture Notes 📖
- **Unter 10**: Bitte sieh dir die Lecture erneut an und versuche es nochmal 🔄  

## 🆘 Hilfe bekommen

Wenn du nicht weiterkommst:
1. Schau dir die Lecture Slides erneut an  
2. Probiere die Practice Examples aus  
3. Stelle Fragen im Course Forum  
4. Nimm an den Office Hours teil  

## ⏰ Abgabefrist

Überprüfe deinen Course Calendar für die Deadline.

Viel Erfolg! 🚀
