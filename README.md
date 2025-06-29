# Schiebelehre-Checker Web-App

Dieses Repository enthält eine Streamlit-Webanwendung zur automatischen Erkennung von Schiebelehren (Messschieber) in Ricardo-Inseraten.

## Dateien

- **app.py**: Hauptskript für die Streamlit-App
- **requirements.txt**: Liste der benötigten Python-Pakete
- **.streamlit/config.toml**: Konfiguration für Streamlit-Server

---

## Deployment auf Streamlit Cloud

1. Ein GitHub-Repository namens `Bilderkennung-Ricardo` anlegen oder verwenden.
2. Diesem Repo die Dateien `app.py`, `requirements.txt` und den Ordner `.streamlit/` hinzufügen.

   ```bash
   git clone https://github.com/dein-user/Bilderkennung-Ricardo.git
   cd Bilderkennung-Ricardo
   cp /pfad/zum/schiebelehre_checker/* .
   git add .
   git commit -m "Version 1.0: Streamlit-App hochgeladen"
   git push origin main
   ```

3. Streamlit Cloud: https://streamlit.io/cloud aufrufen
4. Auf **New app** klicken und GitHub verbinden
5. Dein Repository `Bilderkennung-Ricardo` auswählen, Branch `main`
6. Als **Main file path** `app.py` angeben
7. Auf **Deploy** klicken und den Build abwarten

Der Link zur live geschalteten App erscheint nach dem erfolgreichen Build.

---

## Lokaler Betrieb

1. Virtual Environment erstellen:
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate     # Windows
   ```
2. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```
3. Streamlit-App starten:
   ```bash
   streamlit run app.py
   ```

Die App ist dann unter http://localhost:8501 erreichbar.

---

## Nutzung

- Gib im Suchfeld den Begriff **"schiebelehre"** (oder später andere Objekte) ein.
- Lege die Anzahl der zu analysierenden Inserate fest.
- Klicke auf **Start Analyse**.
- Die Ergebnisse erscheinen in einer Tabelle mit Bildvorschau, Treffer, Score, Preis, Zustand, Versand, Beschreibung und Link.

---

## Erweiterungen

- Unterstützung weiterer Plattformen (Tutti)
- Objekterkennung für andere Werkzeuge (Hammer, Surfboard, etc.)
- CSV-Export der Ergebnisse
