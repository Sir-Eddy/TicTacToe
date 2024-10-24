# Tic-Tac-Toe

## Überblick
Dies ist eine Implementierung des klassischen Spiels Tic-Tac-Toe auf der Kommandozeile für zwei Spieler, einschließlich einer KI-Option.

## Anforderungen
- Implementierung in Python.
- Nutzung von objektorientierter Programmierung.
- Design gemäß dem Model View Controller (MVC) oder Model View Presenter (MVP) Entwurfsmuster.
- Möglichkeit, den Spielstand in einer Datei zu speichern und wieder zu laden.
- Ein zweiter Spielmodus gegen eine Spiel-KI, entweder durch eigene Heuristiken oder den Minimax-Algorithmus.
- Unit-Tests für die Geschäftslogik einschließlich der Spiel-KI mit mindestens 90% Testabdeckung.
- Einhaltung des Python PEP8 Coding Style Guides und Nutzung eines Linters.
- Nutzung von https://mygit.th-deg.de zur Verwaltung des Quellcodes.

## Funktionen
- **Zwei-Spieler-Modus**: Spiele gegen einen Freund auf der Kommandozeile.
- **Speichern und Laden**: Speichere den aktuellen Spielstand und lade ihn später wieder.
- **Spiel-KI**: Spiele gegen eine KI, die entweder durch eigene Heuristiken oder den Minimax-Algorithmus gesteuert wird.
- **Unit-Tests**: Umfassende Tests, um die korrekte Funktionsweise der Geschäftslogik zu gewährleisten.
- **PEP8-konform**: Der Code folgt den PEP8-Richtlinien für sauberen und lesbaren Code.

## Installation
1. Klone das Repository:
    ```sh
    git clone https://mygit.th-deg.de/EddyXII/tic-tac-toe.git
    ```
2. Wechsle in das Projektverzeichnis:
    ```sh
    cd tic-tac-toe
    ```

## Nutzung
1. Starte das Spiel:
    ```sh
    python app.py
    ```
2. Befolge die Anweisungen auf der Kommandozeile, um das Spiel zu spielen oder einen gespeicherten Spielstand zu laden.

## Architektur
Das Spiel ist nach dem Model View Controller (MVC) Entwurfsmuster gestaltet. Dies ermöglicht eine klare Trennung der Geschäftslogik (Model), der Benutzerschnittstelle (View) und der Steuerung (Controller).

## Spiel-KI
Die Spiel-KI kann entweder durch eigene Heuristiken oder durch den Minimax-Algorithmus gesteuert werden. Der Minimax-Algorithmus sorgt für optimierte Züge der KI.

## Tests
Die Geschäftslogik und die Spiel-KI sind umfassend getestet, um mindestens 90% Testabdeckung zu erreichen. Ein Test-Coverage-Tool wird verwendet, um die Testabdeckung zu überprüfen und zu gewährleisten.

Viel Spaß beim Spielen!
