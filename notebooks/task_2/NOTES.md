# Notizen für den Task 2

## Vorüberlegungen

### Feedback von der Präsentation

- [x] Für den Datensatz ohne outliers nochmal Diagramme erstellen

- [x] Anderes Farbschema für Grafiken

- [x] VIF Berechnung mit Label -> hat nichts da verloren, nur Kolinearitäten beachten

- [ ] Braucht man ein weiteres Model für Gamay? Wie groß ist die durchschnittliche Differenz zwischen Gamay und den anderen? Lineare Regression wird erkennen, dass Gamay immer niedriger ist.

- [ ] Wird nicht bei allen Algorithmen funktionieren, Zweifel bei Neighbours Algorithmus(?), aber Entscheidungsbaum sollte klappen

- [ ] Fehlt vielleicht noch: Transformation und Skalierung -> manche Algorithmen könnten Probleme bekommen

Fragen, die wir uns erst einmal stellen müssen:

1. Wie viele Modelle wollen wir verwenden? (Gamay)
   - Eins verwenden und nur in Ausnahme Fälle ein zweites Modell verwenden
2. Welches Modell wollen wir verwenden?

   - Lineare Regression
   - Polynomial Regression
   - Random Forst Regression
   - Gradient Boosting Regression
   - SVM (Linear Regression)
   - Decision Tree Regression
   - Eventuell:
     - KNN Regression (Feature Scaling (Normalisiert))

3. Wie bereiten wir die Daten auf?

   - Outlier entfernen
   - Missing Values imputen
     - Median
     - Mean
     - Mode
     - oder über ein Modell
   - Data Transformation

     - Datentypen definieren (String -> Categorical, Zahlen -> Numerical)
     - One-Hot-Encoding auf `wine_type`
     - Label-Encoding ausgeschlossen, da keine Werte, die ordinalskaliert sind

   - Feature Engineering

     - Feature Selection (Nutzen Feature X, weils korriliert, schmeißen Y raus, weils nix bringt)
       - (Feature Extraction (Neue Features aus bestehenden Features erstellen))

   - Feature Scaling (Wahrscheinlich nur, wenn wir KNN verwenden)

   - Dimensionality Reduction (PCA, etc.)
     - Verwenden wir nicht, da wir das durch VIF rausbekommen, welche wir verwenden können

4. Wie trainieren wir das Modell?
5. Wie testen wir das Modell?
6. Wie bewerten wir das Modell?

## Schritte

1. Daten laden
2. Daten aufbereiten
   1. Outlier rausnehmen
   2. Missing Values imputen/rausnehmen
   3. Data Transformation durchführen
   4. Feature Engineering durchführen
      1. Je nach Ziel-Modell vllt. noch Feature Scaling machen
      2. Je nach Ziel-Modell vllt. Dimensionality Reduction
   5. Train-Test-Split durchführen
3. Modell trainieren
4. Modell testen
5. Modell bewerten

## Aufgaben

Bausteine Pipeline:

1. Outlier Detection (Mike & Marvin (Datentypen))
2. Missing Values (Mike)
3. Data Transformation (Marvin)
4. Feature Selection (Valentin)
5. Feature Scaling (Luca)
6. Dimensionality Reduction (Luca)
7. Modell-Training & -Testing (Kevin)
