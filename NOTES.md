# Notes

## Fragen fürs Coaching (13.04.2023)

1. Task 1a:

- Keine wirkliche Architektur aufgrund der Daten
  - Ist es mit dem Hochladen der Daten bereits getan?
  - Antwort: Reicht, wenn wir die Datenbank und das Skript auf einer Folie zeigen
- Wie sollen wir das dokumentieren? Wie granular? Auch dokumentieren, wenn wir uns aktiv dagegen entscheiden, GitHub Copilot zu nutzen?
  - Antwort: Auch wenn man es copy-pasten kann mal versuchen, wie viel Aufwand das mit Copilot wäre
- Ganze Data Exploration mit ChatGPT und Copilot versuchen, erstellen zu lassen --> Luca
  - Wie detailiert wird in das Thema eingestiegen und was schlägt ChatGPT als guten Prozess vor? Bleibt es übersicthlich oder wird es zu unübersichtlich?
- Kann Copilot auch Interpretationen über die Schaubilder oder die Daten machen?
- CRISP-DM als Vorlage für den Data Science Prozess --> Wo ändert sich dieser Prozess bei der Verwendung von Copilot etc.?

## Coaching (27.04.2023)

- IQR mit Label (Quality 1-2 werden aussortiert bzw. als Outlier detected) ==> Label bei der Outlier-Detection rausnehmen?
  - Outlier Detection auf jeden Fall auch bei den Labels durchführen
  - Beispiel Gamay:
    - Wenn Gamay aus den Trainingsdaten rausfällt, könnte man diese nicht mehr vorraussagen
    - Eventuell verschiedene Modelle für die 5 Klassen
    - Nächster Schritt: Analyse der Daten auf Basis des Weintyps um zu schauen, ob man zwei verschiedene Modelle für die Typen benötigt
    - Schauen, ob die Zusammenhänge der Features für die Weintype unterschiedlich sind und auf Basis dessen herausfinden, ob wir 2 Modelle benötigen
- Neue Ansätze fürs Preprocessing? AI oder sowas?
  - Ja, bei Rapidminer gibt es so etwas. Allerdings ist Herrn Meth kein Framework dahingehend bekannt, dass das auch in Python kann
- Passt unser Modell so?
  - Erst entscheiden, ob wir den Z-Score oder den IQR nutzen wollen und danach weitermachen
  - Feature Selection nach dem einen Verfahren und dann in eine lineare Regressiion geben und schauen, welches Verfahren am besten funktioniert
  - Macht es Sinn, mehrere Verfahren zu stacken? Nach der FS noch Dimensionality Reduction?
    - Kolinearität und Korrelation checken => welche Feature kommen überhaupt in Frage?
- Normalisierung tut meistens nie weh, egal ob das Modell dies benötigt
- PCA für die Weintypen mal checken
- Mögliches Präsentationsformat: [https://rise.readthedocs.io/en/stable/](https://rise.readthedocs.io/en/stable/)

### Weiteres Vorgehen

1. Preprocessing durchführen mit Pipelines
2. Messung des Preprocessing anhand einer Linearen Regression als Baseline
3. Auswählen eines Algorithmus und Testing des Algorithmus in Bezug auf die Baseline
4. Testing der Preprocessing-Schritte für den Algorithmus (Vllt. gibt es eine Pipeline, die besser funktioniert)
5. Hyperparameter-Tuning des Algorithmus
