# Git Pointers Übung: Branches als Pointer verstehen

## Anleitung

Bearbeite die Datei [`answers.py`](./answers.py) und trage deine Antworten ein:

```python
# Beispiel:
answers = {
    1: "A",  # Frage 1: Option A
    2: "D",  # Frage 2: Option D
    # ... fülle alle 15 Fragen aus
}
```

---

## Fragen


---
layout: post
title: "Lecture 3 Part 1 Übung: Git Pointer und Branches verstehen"
date: 2025-10-23 10:00:00 +0200
tags: [lecture-3-part-1, exercise, git, branches, pointers, workflows]
lang: de
permalink: /de/exercises/lecture-3-part-1-git-pointers/
---

# Lecture 3 Part 1 Übung: Git Pointer und Branches verstehen

## Anleitung
- Diese Übung testet dein Verständnis von Git Branches als Pointer
- Jede Frage zeigt einen Git-Graphen mit Commits, Branches, HEAD und/oder Tags
- Studiere jeden Graphen sorgfältig, bevor du deine Antwort auswählst
- Jede Frage hat 4 Optionen mit genau einer richtigen Antwort
- Konzentriere dich darauf zu verstehen, was die Pointer dir über den Git-Zustand verraten

---

## Frage 1: Einen neuen Branch erstellen

**Du bist auf dem `main` Branch und führst `git checkout -b feature/new-ui` aus. Wie sieht der Git-Graph unmittelbar nach diesem Befehl aus?**

```
Vorher:
"Add login"  "Fix bug"  "Add dashboard"
     ↓           ↓           ↓
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l
                              ↑
                           main ← HEAD
```

A)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l
                              ↑
                           main
                    feature/new-ui ← HEAD
```

B)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  m2n3o4p
                              ↑            ↑
                           main    feature/new-ui ← HEAD
```

C)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l
                              ↑
                    feature/new-ui ← HEAD
```

D)
```
  a1b2c3d  ←  e4f5g6h
                  ↑
                main

                    i7j8k9l
                        ↑
              feature/new-ui ← HEAD
```

---

## Frage 2: Erster Commit auf dem Feature Branch

**Nachdem du `feature/new-ui` erstellt hast, machst du einen Commit. Wie sieht der Graph aus?**

```
Vor dem Commit:
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l
                              ↑
                           main
                    feature/new-ui ← HEAD
```

A)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s
                              ↑            ↑
                           main     feature/new-ui
```

B)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s
                                           ↑
                                         main
                                  feature/new-ui ← HEAD
```

C)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l
                              ↑
                           main

                          p9q8r7s
                              ↑
                    feature/new-ui ← HEAD
```

D)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s
                              ↑            ↑
                           main     feature/new-ui ← HEAD
```

---

## Frage 3: Mehrere Commits auf dem Feature Branch

**Du machst zwei weitere Commits auf `feature/new-ui`. Was ist jetzt der Zustand?**

```
Ausgangsposition:
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s
                              ↑            ↑
                           main     feature/new-ui ← HEAD

Nach 2 weiteren Commits:
```

A)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                                                                   ↑
                                                                 main
                                                          feature/new-ui ← HEAD
```

B)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                              ↑                                       ↑
                           main                              feature/new-ui ← HEAD
```

C)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l
                              ↑
                           main

                          p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                                                       ↑
                                              feature/new-ui ← HEAD
```

D)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  t1u2v3w  ←  x4y5z6a
                              ↑                        ↑
                           main                 feature/new-ui ← HEAD
```

---

## Frage 4: Zum Main Branch wechseln

**Du führst `git checkout main` aus. Was passiert mit den Pointern?**

```
Vor dem Checkout:
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                              ↑                                       ↑
                           main                              feature/new-ui ← HEAD
```

A)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                              ↑                                       ↑
                         main ← HEAD                          feature/new-ui
```

B)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l
                              ↑
                         main ← HEAD
```

C)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l
                              ↑
                         main ← HEAD

                          p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                                                       ↑
                                              feature/new-ui
```

D)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                                                                   ↑
                                                            main ← HEAD
                                                            feature/new-ui
```

---

## Frage 5: Fast-Forward Merge

**Während du auf `main` bist, führst du `git merge feature/new-ui` aus und Git führt einen "Fast-Forward" Merge durch. Was ist das Ergebnis?**

```
Vor dem Merge:
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                              ↑                                       ↑
                         main ← HEAD                          feature/new-ui
```

A)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a  ←  merge-commit
                                                                               ↑
                                                                          main ← HEAD
                                                                          feature/new-ui
```

B)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                                                                   ↑
                                                              main ← HEAD
                                                              feature/new-ui
```

C)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                              ↑                                       ↑
                         main ← HEAD                          feature/new-ui
```

D)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l
                              ↑
                         main ← HEAD
                         feature/new-ui
```

---

## Frage 6: Einen Tag hinzufügen

**Nach dem Merge erstellst du einen Tag: `git tag -a v1.0 -m "Release 1.0"`. Wohin zeigt der Tag-Pointer?**

```
Vor dem Tag:
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                                                                   ↑
                                                              main ← HEAD
                                                              feature/new-ui
```

A)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                              ↑                                       ↑
                           (v1.0)                                main ← HEAD
                                                              feature/new-ui
```

B)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                                                                   ↑
                                                              main ← HEAD
                                                              feature/new-ui
                                                                 (v1.0)
```

C)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a  ←  v1.0-tag
                                                                               ↑
                                                                          main ← HEAD
                                                                          feature/new-ui
```

D)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l
                              ↑
                           (v1.0)

                          p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                                                       ↑
                                                  main ← HEAD
                                                  feature/new-ui
```

---

## Frage 7: Divergierende Branches (Teil 1)

**Du wechselst zu `main` und machst einen Commit. Währenddessen bleibt `feature/new-ui` wo es ist. Was ist der Zustand?**

```
Ausgangszustand:
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                                                                   ↑
                                                              main ← HEAD
                                                              feature/new-ui
                                                                 (v1.0)

Nach: git checkout main, dann einen Commit machen
```

A)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a  ←  b7c8d9e
                                                                   ↑            ↑
                                                           feature/new-ui  main ← HEAD
                                                              (v1.0)
```

B)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                                                                   ↑
                                                           feature/new-ui
                                                              (v1.0)

                                                             b7c8d9e
                                                                 ↑
                                                            main ← HEAD
```

C)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a  ←  b7c8d9e
                                                                   ↑            ↑
                                                           feature/new-ui  main ← HEAD
                                                              (v1.0)        feature/new-ui
```

D)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a  ←  b7c8d9e
                                                                   ↑            ↑
                                                              (v1.0)        main ← HEAD
                                                           feature/new-ui
```

---

## Frage 8: Divergierende Branches (Teil 2)

**Du wechselst zu `feature/new-ui` und machst dort ebenfalls einen Commit. Was jetzt?**

```
Ausgangszustand:
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a  ←  b7c8d9e
                                                                   ↑            ↑
                                                              (v1.0)        main ← HEAD
                                                           feature/new-ui

Nach: git checkout feature/new-ui, dann einen Commit machen
```

A)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a  ←  b7c8d9e  ←  f1g2h3i
                                                                   ↑            ↑            ↑
                                                              (v1.0)         main    feature/new-ui ← HEAD
```

B)
```
                                        b7c8d9e
                                            ↑
                                          main
                                           ↙
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                                                                   ↑  ↘
                                                              (v1.0)    f1g2h3i
                                                                           ↑
                                                                   feature/new-ui ← HEAD
```

C)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                                                                   ↑
                                                              (v1.0)

                          b7c8d9e                             f1g2h3i
                              ↑                                   ↑
                            main                          feature/new-ui ← HEAD
```

D)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a  ←  b7c8d9e
                                                                   ↑            ↑
                                                              (v1.0)         main
                                                                                ↖
                                                                                 f1g2h3i
                                                                                    ↑
                                                                            feature/new-ui ← HEAD
```

---

## Frage 9: Einen Commit auschecken (Detached HEAD)

**Du führst `git checkout x4y5z6a` (der Commit mit Tag v1.0) aus. In welchem Zustand ist Git?**

```
Vor dem Checkout:
                                        b7c8d9e
                                            ↑
                                        main ← HEAD
                                           ↙
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                                                                   ↑  ↘
                                                              (v1.0)    f1g2h3i
                                                                           ↑
                                                                   feature/new-ui
```

A)
```
                                        b7c8d9e
                                            ↑
                                          main
                                           ↙
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                                                                   ↑  ↘
                                                                 HEAD    f1g2h3i
                                                              (v1.0)         ↑
                                                                     feature/new-ui
```

B)
```
                                        b7c8d9e
                                            ↑
                                          main
                                           ↙
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                                                              HEAD ↑  ↘
                                                              (v1.0)    f1g2h3i
                                                                           ↑
                                                                   feature/new-ui
```

C)
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                                                                   ↑
                                                                 HEAD
                                                              (v1.0) (detached)
```

D)
```
                                        b7c8d9e
                                            ↑
                                          main
                                           ↙
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                                                             ↑   ↑  ↘
                                                           HEAD    f1g2h3i
                                                        (detached)     ↑
                                                              (v1.0) feature/new-ui
```

---

## Frage 10: Einen Branch umbenennen

**Du benennst einen Branch mit `git branch -m old-name new-name` um. Was ändert sich tatsächlich?**

```
Vor dem Umbenennen:
                                                              ↱  b7c8d9e
                                                             /       ↑
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a     main
                                                                   ↑  ↖
                                                              (v1.0)    f1g2h3i
                                                                           ↑
                                                                   feature/old-name ← HEAD
```

A) Der Commit `f1g2h3i` bekommt einen neuen Hash, weil der Branch-Name Teil des Commits ist

B) Ein neuer Commit wird mit dem neuen Branch-Namen erstellt, und der alte Commit wird gelöscht

C) Nur der Name des Branch-Pointers ändert sich; der Commit `f1g2h3i` und der Tag `v1.0` bleiben unverändert

D) Der Tag `v1.0` wird zur Spitze des umbenannten Branches verschoben, um den neuen Namen zu verfolgen


---

## Frage 11: Remote-Tracking Branches verstehen

**Du führst `git branch -a` aus und siehst diese Ausgabe. Was sind die drei Arten von Referenzen, die gezeigt werden?**

```bash
$ git branch -a
  main
  feature/new-feature
  remotes/origin/main
  remotes/origin/feature/old-pr
```

A) Alle vier sind lokale Branches, zu denen du direkt committen kannst

B) `main` und `feature/new-feature` sind lokale Branches; `remotes/origin/main` und `remotes/origin/feature/old-pr` sind Remote-Branches auf GitHub

C) `main` und `feature/new-feature` sind lokale Branches, wo du arbeitest; `remotes/origin/main` und `remotes/origin/feature/old-pr` sind lokale Lesezeichen, die GitHubs Zustand zeigen

D) `remotes/origin/*` sind Remote-Branches, zu denen du mit `git push` committen kannst

---

## Frage 12: Was passiert nach git fetch

**Du führst `git fetch origin` aus. Was aktualisiert dieser Befehl?**

```bash
Vor dem Fetch:
GitHub (origin):
  main → x4y5z6a (neuester Commit)

Dein lokales Git:
  main → i7j8k9l (veraltet)
  remotes/origin/main → i7j8k9l (veraltetes Lesezeichen)

Nach dem Fetch:
```

A) Nur dein lokaler `main` Branch aktualisiert sich auf `x4y5z6a`

B) Nur `remotes/origin/main` aktualisiert sich auf `x4y5z6a`; dein lokaler `main` bleibt bei `i7j8k9l`

C) Sowohl `main` als auch `remotes/origin/main` aktualisieren sich auf `x4y5z6a`

D) Keiner aktualisiert sich; du brauchst `git pull`, um etwas zu aktualisieren

---

## Frage 13: Veraltete Remote-Tracking Branches

**Ein PR wurde gemergt und der Feature-Branch wurde auf GitHub gelöscht. Du führst lokal `git branch -a` aus. Was siehst du?**

```bash
GitHub (origin):
  main (einziger Branch, der existiert)

Dein lokales Git hat noch nicht gefetcht:
```

A)

```bash
  main
  remotes/origin/main
```

B)

```bash
  main
  remotes/origin/main
  remotes/origin/feature/old-pr  ← Wird immer noch angezeigt!
```

C)

```bash
  main
  feature/old-pr (automatisch gelöscht)
  remotes/origin/main
```

D) Git erkennt die Löschung automatisch und entfernt `remotes/origin/feature/old-pr`

---

## Frage 14: git fetch --prune verstehen

**Was macht `git fetch --prune` anders als `git fetch`?**

```bash
Situation:
- GitHub hat feature/old-pr gelöscht
- Dein lokales Git hat immer noch remotes/origin/feature/old-pr

Du führst aus: git fetch --prune
```

A) Lädt neue Commits herunter und löscht zwangsweise deinen lokalen `feature/old-pr` Branch

B) Lädt neue Commits herunter und entfernt die veraltete `remotes/origin/feature/old-pr` Referenz

C) Entfernt nur veraltete Remote-Tracking Branches ohne neue Commits herunterzuladen

D) Löscht sowohl den lokalen Branch als auch den Remote-Tracking Branch für `feature/old-pr`


---

## Frage 15: git pull --prune Workflow

**Du hast gerade einen PR auf GitHub gemergt und der Feature-Branch wurde automatisch gelöscht. Du führst `git checkout main` und dann `git pull --prune` aus. Was passiert?**

```bash
Vorher:
GitHub: main → x4y5z6a (hat gemergten PR)
        feature/old-pr gelöscht ✅

Lokal:  main → i7j8k9l (veraltet)
        feature/old-pr → p9q8r7s (existiert noch lokal)
        remotes/origin/main → i7j8k9l (veraltet)
        remotes/origin/feature/old-pr → p9q8r7s (veraltet!)

Nach git pull --prune:
```

A)
```
Lokal:  main → x4y5z6a (aktualisiert)
        remotes/origin/main → x4y5z6a (aktualisiert)
```

B)
```
Lokal:  main → x4y5z6a (aktualisiert)
        feature/old-pr gelöscht
        remotes/origin/main → x4y5z6a (aktualisiert)
```

C)
```
Lokal:  main → x4y5z6a (aktualisiert)
        feature/old-pr → p9q8r7s (existiert noch)
        remotes/origin/main → x4y5z6a (aktualisiert)
```

D)
```
Lokal:  main → i7j8k9l (unverändert)
        remotes/origin/main → x4y5z6a (aktualisiert)
        remotes/origin/feature/old-pr gelöscht
```

---

## Frage 16: Die Lesezeichen-Analogie

**Laut der "Lesezeichen-Analogie" der Vorlesung, was repräsentieren Remote-Tracking Branches?**

```
GitHub (die Websites) hat:
  - main Branch
  - feature/xyz Branch

Dein lokales Git hat:
  - Lokale Branches (main, feature/xyz)
  - Remote-Tracking Branches (remotes/origin/main, remotes/origin/feature/xyz)
```

A) Remote-Tracking Branches SIND die tatsächlichen Remote-Branches, nur mit einem anderen Namen

B) Remote-Tracking Branches sind wie Lesezeichen in deinem Browser - sie zeigen darauf, wo GitHubs Branches waren, als du zuletzt nachgesehen hast

C) Remote-Tracking Branches sind Backups deiner lokalen Branches, falls du deine Arbeit verlierst

D) Remote-Tracking Branches sind temporäre Referenzen, die nach dem Merge verschwinden


---

## Frage 17: Veraltete Referenzen verhindern

**Du möchtest, dass Git automatisch veraltete Remote-Tracking Branches jedes Mal entfernt, wenn du fetchst. Was solltest du konfigurieren?**

A) `git config --global fetch.prune true`

B) `git config --global branch.autocleanup true`

C) `git config --global remote.pruneOnFetch true`

D) `git branch --set-upstream-to=origin/main`


---

## Frage 18: Gemergte Branches prüfen

**Du möchtest sehen, welche lokalen Branches in `main` gemergt wurden, bevor du sie löschst. Welcher Befehl zeigt das?**

A) `git branch --merged main`

B) `git branch --no-merged`

C) `git remote prune origin --dry-run`

D) `git log --merged`


---

## Frage 19: Squash Merge Branch-Löschung

**Dein PR wurde mit "Squash and merge" auf GitHub gemergt. Der Branch wurde dort gelöscht. Jetzt versuchst du, deinen lokalen Branch zu löschen:**

```bash
$ git branch -d feature/squashed
error: The branch 'feature/squashed' is not fully merged.
```

**Warum sagt Git das, und was solltest du tun?**

A) Git liegt falsch; führe `git branch -D feature/squashed` (erzwungenes Löschen) aus, nachdem du bestätigt hast, dass der PR gemergt wurde

B) Der PR wurde nicht wirklich gemergt; prüfe GitHub nochmal

C) Du musst zuerst `git pull --rebase` ausführen, um den Squash-Commit zu synchronisieren

D) Lokale Branches können nicht gelöscht werden, wenn sie mit Squash gemergt wurden; lass ihn stehen

---

## Frage 20: Vollständiges Aufräumen nach PR-Merge

**Dein PR wurde mit "Create a merge commit" (nicht Squash) gemergt und GitHub hat den Remote-Branch automatisch gelöscht. Was ist der vollständige Aufräum-Workflow?**

```bash
Ausgangszustand:
- GitHub: main (aktualisiert mit deinem PR durch Merge-Commit), feature/xyz gelöscht
- Lokal: main (veraltet), feature/xyz (existiert noch),
         remotes/origin/feature/xyz (veraltet)
```

A)

```bash
git checkout main
git branch -d feature/xyz
```

B)

```bash
git fetch --prune
git checkout main
git pull
```

C)

```bash
git checkout main
git pull --prune
git branch -d feature/xyz
```

D)

```bash
git remote prune origin
git branch -D feature/xyz
```

---