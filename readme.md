# Laboration 1

Deadline: Kommuniceras via discord & studentportalen

## Betyg: U, G

- För att bli godkänd ska du implementera samtlig funktionalit listad i beskrivningen. Du ska visa på förståelse för grundläggande flow control, funktioner och errorhantering.

## Innan du gör uppgiften

Du bör du ha gjort klart git-övningen och labb-förberedelsen på studentportalen. Det hjälper också om du gjort extrauppgifterna.

## Att använda AI

- Det är förbjudet att använda AI som tex. chatgpt för att lösa uppgiften. Ni ska träna på att tänka själva nu - det är väldigt uppenbart för mig när ni använder AI. Att däremot använda GPT till att förklara olika saker är OK! Att använda GPT eller github copilot för att generera kod är något ni kan utnyttja först när ni lärt er problemlösning på en högre nivå. Misstänker jag något får ni en varning och kan leda till avstängning.

## Inlämning

Ta bort alla onödiga filer, din kod bör vara på den huvudsakliga branchen "main" eller "master".
Se till att du körde git clone på din EGEN repository för labben.
Feedback ges via en speciell branch som skapas automatiskt, mer information om detta får du av utbildaren.
Du ska alltså bara pusha ut commits, utbildaren kommer sedan kolla på din kod såsom den ser ut i din senaste giltiga commit.

## Beskrivning:

Du ska bygga ett enkelt system för att hantera studenter via terminalen.
Filen student_system.py innehåller startdata för alla studenter, du ska bygga på funktionalitet.

När användaren skriver in val som ej passar så kan du försöka visa felmeddelanden och visa alternativen igen.

1. Programmet ska hälsa användaren välkommen och ge den en meny med olika följande val numrerat.
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

# Att tänka på

- Försök visa meny-alternativen ofta
- Använd funktioner och loopar mycket!
- Försök ge respons till användaren när den gör något
- Programmet ska INTE stängas av efter du utfört en handling. Om du exempelvis lagt till en student så ska du bara återvända till menyn
- När du ska visa information ska du aldrig bara printa en lista eller dictionary, jag förväntar mig då att du loopar igenom datan och visar det på ett snyggt för användaren
- Tänk på att **while-loopar** kan hjälpa dig med menyer
- Undvik att en funktion anropar sig själv (rekursion)

- Innan du lämnar in uppgiften bör du testa programmet.
- Fastna inte i detaljer, **exakt** hur du gör eller hur det ser ut spelar ingen roll, du ska alltid ställa dig frågan: Har jag skapat något som känns bra att använda?

**BONUS** (Ej obligatoriskt): Användaren ska kunna lägga till betyg och kurser för enskilda studenter också när man lägger till studenten via alternativ [1] i startmenyn
