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


## Frage 1: Einen neuen Branch erstellen

**Sie befinden sich auf dem Branch `main` und führen `git checkout -b feature/new-ui` aus. Wie sieht der Git-Graph unmittelbar nach diesem Befehl aus?**

```
Before:
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

## Frage 2: Erster Commit auf dem Feature-Branch

**Nachdem Sie `feature/new-ui` erstellt haben, führen Sie einen Commit aus. Wie sieht der Graph danach aus?**

```
Before commit:
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

## Frage 3: Mehrere Commits auf dem Feature-Branch

**Sie erstellen zwei weitere Commits auf `feature/new-ui`. Wie sieht der Zustand jetzt aus?**

```
Ausgangszustand:
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

## Frage 4: Zum Main-Branch wechseln

**Sie führen `git checkout main` aus. Was passiert mit den Pointern?**

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

## Frage 5: Fast-Forward-Merge

**Sie befinden sich auf `main` und führen `git merge feature/new-ui` aus. Git führt einen Fast-Forward-Merge durch. Wie sieht das Ergebnis aus?**

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

## Frage 6: Ein Tag hinzufügen

**Nach dem Merge erstellen Sie ein Tag: `git tag -a v1.0 -m "Release 1.0"`. Auf welchen Commit zeigt dieses Tag?**

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

**Sie wechseln zu `main` und erstellen dort einen Commit. `feature/new-ui` bleibt unverändert. Wie sieht der Zustand aus?**

```
Ausgangszustand:
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                                                                   ↑
                                                              main ← HEAD
                                                              feature/new-ui
                                                                 (v1.0)

Nach: git checkout main, dann ein Commit
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
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                              ↑                                       ↑
                         main ← HEAD                          feature/new-ui
                                                                 (v1.0)
                                                                 
                                                             b7c8d9e
```


---

## Frage 8: Divergierende Branches (Teil 2)

**Sie wechseln zu `feature/new-ui` und machen dort ebenfalls einen Commit. Wie sieht der Zustand jetzt aus?**

```
Ausgangszustand:
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a  ←  b7c8d9e
                                                                   ↑            ↑
                                                           feature/new-ui  main
                                                              (v1.0)

Nach: git checkout feature/new-ui, dann ein Commit
```

A) 
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a  ←  b7c8d9e  ←  f1g2h3i
                                                                   ↑            ↑            ↑
                                                              (v1.0)         main    feature/new-ui ← HEAD
```

B) 
```
                                                              ↱  b7c8d9e
                                                             /       ↑
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a     main
                                                                   ↑  ↖
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

## Frage 9: Drei-Wege-Merge

**Sie mergen `feature/new-ui` in `main`. Git führt einen Drei-Wege-Merge aus. Wie sieht das Ergebnis aus?**

```
Vor dem Merge:
                                                              ↱  b7c8d9e
                                                             /       ↑
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a     main ← HEAD
                                                                   ↑  ↖
                                                              (v1.0)    f1g2h3i
                                                                           ↑
                                                                   feature/new-ui
```

A) 
```
                                                              ↱  b7c8d9e  ↖
                                                             /              ↘
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a          j4k5l6m
                                                                   ↑  ↖         ↗    ↑
                                                              (v1.0)    f1g2h3i   main ← HEAD
                                                                           ↑         feature/new-ui
                                                                   feature/new-ui
```

B) 
```
                                                              ↱  b7c8d9e  ↖
                                                             /              ↘
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a          j4k5l6m
                                                                   ↑  ↖         ↗    ↑
                                                              (v1.0)    f1g2h3i   main ← HEAD
                                                                           ↑         
                                                                   feature/new-ui
```

C) 
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a  ←  b7c8d9e  ←  f1g2h3i
                                                                   ↑                        ↑
                                                              (v1.0)                   main ← HEAD
                                                                                       feature/new-ui
```

D) 
```
                                                              ↱  b7c8d9e
                                                             /       ↑
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a     main ← HEAD
                                                                   ↑  ↖         feature/new-ui
                                                              (v1.0)    f1g2h3i
```


---

## Frage 10: Einen gemergten Branch löschen

**Sie löschen `feature/new-ui` mit `git branch -d feature/new-ui`. Was passiert?**

```
Vor dem Löschen:
                                                              ↱  b7c8d9e  ↖
                                                             /              ↘
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a          j4k5l6m
                                                                   ↑  ↖         ↗    ↑
                                                              (v1.0)    f1g2h3i   main ← HEAD
                                                                           ↑         
                                                                   feature/new-ui
```

A) 
```
                                                              ↱  b7c8d9e  ↖
                                                             /              ↘
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a          j4k5l6m
                                                                   ↑            ↗    ↑
                                                              (v1.0)              main ← HEAD
```

B) 
```
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a
                                                                   ↑
                                                              main ← HEAD
                                                                 (v1.0)
```

C) 
```
                                                              ↱  b7c8d9e  ↖
                                                             /              ↘
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a          j4k5l6m
                                                                              ↗    ↑
                                                                                main ← HEAD
                                                                                   (v1.0)
```

D) 
```
                                                              ↱  b7c8d9e  ↖
                                                             /              ↘
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a          j4k5l6m
                                                                   ↑  ↖         ↗    ↑
                                                              (v1.0)    [deleted]  main ← HEAD
```

---

## Frage 11: Einen Commit auschecken (Detached HEAD)

**Sie führen `git checkout x4y5z6a` aus (der Commit ist mit v1.0 getaggt). In welchem Zustand befindet sich Git?**

```
Vor dem Checkout:
                                                              ↱  b7c8d9e  ↖
                                                             /              ↘
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a          j4k5l6m
                                                                   ↑            ↗    ↑
                                                              (v1.0)              main ← HEAD
```

A) 
```
                                                              ↱  b7c8d9e  ↖
                                                             /              ↘
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a          j4k5l6m
                                                                   ↑            ↗    ↑
                                                              (v1.0)              main
                                                                 HEAD
```

B) 
```
                                                              ↱  b7c8d9e  ↖
                                                             /              ↘
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a          j4k5l6m
                                                                HEAD ↑       ↗    ↑
                                                              (v1.0)              main
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
                                                              ↱  b7c8d9e  ↖
                                                             /              ↘
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a          j4k5l6m
                                                             ↑   ↑            ↗    ↑
                                                           HEAD (v1.0)           main
                                                        (detached)
```

---

## Frage 12: Branch umbenennen

**Sie benennen einen Branch mit `git branch -m old-name new-name` um. Was ändert sich tatsächlich?**

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

A) Der Commit `f1g2h3i` erhält einen neuen Hash, weil der Branch-Name Teil des Commits ist  
B) Es entsteht ein neuer Commit mit dem neuen Namen, der alte Commit wird gelöscht  
C) Nur der Name des Branch-Pointers ändert sich; `f1g2h3i` und `v1.0` bleiben unverändert  
D) Das Tag `v1.0` wandert an die Spitze des umbenannten Branches, um dem neuen Namen zu folgen

---

## Frage 13: Merge-Typ bestimmen

**Sie möchten `feature/ui` in `main` mergen. Woran erkennen Sie, ob Git einen Fast-Forward oder einen Drei-Wege-Merge durchführen wird?**

```
Szenario 1:
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s
                              ↑            ↑
                           main      feature/ui

Szenario 2:
                                    ↱  p9q8r7s
                                   /       ↑
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l         feature/ui
                              ↑  ↖
                           main    t1u2v3w
```

A) Szenario 1: Drei-Wege-Merge; Szenario 2: Fast-Forward  
B) Beide Szenarien ergeben zwangsläufig Drei-Wege-Merges  
C) Szenario 1: Fast-Forward; Szenario 2: Drei-Wege-Merge  
D) Der Merge-Typ hängt nur von `--no-ff` ab, nicht vom Graphen

---

## Frage 14: Commit-Beziehungen verstehen

**Sie betrachten diesen Graphen. Welche Aussage ist WAHR?**

```
                                                              ↱  b7c8d9e  ↖
                                                             /              ↘
  a1b2c3d  ←  e4f5g6h  ←  i7j8k9l  ←  p9q8r7s  ←  t1u2v3w  ←  x4y5z6a          j4k5l6m
                                                                   ↑  ↖         ↗    ↑
                                                              (v1.0)    f1g2h3i   main
```

A) Commit `f1g2h3i` hat zwei Parent-Commits: `x4y5z6a` und `b7c8d9e`  
B) Commit `j4k5l6m` hat zwei Parent-Commits: `b7c8d9e` und `f1g2h3i`  
C) Commit `x4y5z6a` hat zwei Child-Commits: `b7c8d9e` und `j4k5l6m`  
D) Commit `b7c8d9e` ist vom Branch `main` aus nicht erreichbar


---

## Frage 15: Analyse eines realen Workflows

**Sie sehen diesen Zustand in Ihrem Repository. Was ist hier vermutlich passiert?**

```
                                    ↱  c1d2e3f  ←  f4g5h6i  ↖
                                   /                          ↘
  start  ←  ...  ←  common  ←  work1                          merged
                      ↑  ↖                                   ↗    ↑
                    main    work2  ←  i7j8k9l  ←  l1m2n3o       main ← HEAD
                                         ↑
                                    feature/docs
```

A) Zwei Feature-Branches wurden von `common` erstellt, getrennt in `main` gemergt, danach wurde direkt auf `main` committet  
B) Zwei Feature-Branches haben von `common` aus divergiert, wurden beide per Drei-Wege-Merge in `main` integriert, einer der Feature-Branches besteht noch  
C) Ein einzelner Feature-Branch wurde erstellt, dann in zwei Branches aufgeteilt und beide zurück nach `main` gemergt  
D) Jemand hat `main` per Force-Push überschrieben und dadurch die Mehrfach-Parents erzeugt

---