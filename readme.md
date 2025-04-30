## Beskrivning:

Ett enkelt system för att hantera studenter via terminalen.

När användaren skriver in val som ej passar så kan du försöka visa felmeddelanden och visa alternativen igen.

1. Programmet hälsar användaren välkommen och ge den en meny med olika följande val numrerat.
   [q] Stäng ner programmet
   [0] Lista alla studenter med namn och student-id.
   [1] Lägg till en student med studentID och namn
   [2] Ta bort en student

### Exempel på hur det ser ut när man använder delar av programmet:

_startar programmet_

```python
Welcome to the greatest student system in the world.
What would you like to do?
[q] - Exit
[0] - List all students from the registry
[1] - Add a student to the registry
[2] - Remove a student from the registry
```

_väljer 0_

```python
Choose a student
[q] Go back
[0] ID: 11230 - Tobias Fors
[1] ID: 11231 - Karin Börjell
....
```

_0_

```python
What would you like to do?
[q] Go back
[0] Show summary of grades
[1] List personal information
```

_0_

```python
Pythonprogrammering 1: 1
Pythonprogrammering 2: 4
------------------------
```

Press enter to continue

_enter_

```python
What would you like to do?
[q] Go back
[0] Show summary of grades
[1] List personal information
```

_1_

```python
Name: Tobias Fors
ID: 11230
Email: tobias@utvecklarakademin.se
Age: 30
```

Press enter to continue

_enter_

```python
What would you like to do?
[q] Go back
[0] Show summary of grades
[1] List personal information
```


