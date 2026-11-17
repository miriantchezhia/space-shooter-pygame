# Space Shooter – 2D Arcade-Spiel in Python (Pygame)

**Autor:** Miriani Tchezhia ([github.com/miriantchezhia](https://github.com/miriantchezhia))  
**Repository:** `https://github.com/miriantchezhia/space-shooter-pygame`  
**Programmiersprache:** Python 3  
**Bibliothek:** Pygame

## 1. Projektübersicht
Im Rahmen meiner praktischen Beschäftigung mit Python und der objektorientierten Programmierung (OOP) habe ich dieses 2D-Arcade-Spiel eigenständig entwickelt. Das Projekt demonstriert den Einsatz von Klassen, Vererbung (`pygame.sprite.Sprite`), Kollisionslogik und Zustandsverwaltung in einer Echtzeit-Spielschleife (*Game Loop*).

## 2. Kernfunktionen
- **Objektorientierte Architektur:** Eigene Klassen für das Spielerschiff (`MadMax`), Gegner (`Rictus`) mit individuellen Lebenspunkten (HP) und Laser-Projektile (`Lazer`).
- **Dynamisches Level-System:** 5 aufeinander aufbauende Schwierigkeitsstufen inklusive Boss-Level (40 HP) und wechselnden Hintergrundwelten.
- **Echtzeit-Kollisionserkennung:** Präzise Trefferabfrage zwischen Projektilen, Gegnern und Spieler über `pygame.Rect.colliderect`.
- **Spielstatus-Steuerung:** Startbildschirm, Pausenmenü (`P`-Taste), Cooldown-Mechanik beim Schießen sowie Win-/Lose-Screens.

## 3. Steuerung
- `W` / `A` / `S` / `D` – Raumschiff bewegen
- `Leertaste (Space)` – Laser abfeuern
- `P` – Spiel pausieren / Hauptmenü
- Zum Aufstieg in das nächste Level: Nach dem Besiegen aller Gegner an den oberen Bildschirmrand fliegen.

## 4. Installation & Start
```bash
pip install -r requirements.txt
python main.py
```
