# Schreifmaschinn-Lite (Command Line Tool) fir Linux/MacOS

Dësen Tool benotzt den ZLS Whisper-Modell fir d'Transkriptioun vu lëtzebuergeschen Audiodonnéeën. Heidrënner fënnt een d'Schrëtt fir d'Installatioun an d'Benotzung.

---

## Installatioun

1. **Modell eroflueden**  
   Luet déi follgend zwee Fichiere vum HuggingFace-Repository erof:  
   [`pytorch_model.bin`](https://huggingface.co/ZLSCompLing/whisper_large_lb_ZLS_v4_38h/resolve/main/pytorch_model.bin)  
   [`config.json`](https://huggingface.co/ZLSCompLing/whisper_large_lb_ZLS_v4_38h/resolve/main/config.json)  

2. **Audio-Dossier uleeën**  
   Leet an deem selwechten Dossier en neie Fichier mam Numm un:  
   ```
   audio
   ```

3. **Python 3.10 Virtual Environment (venv) an Dependencies installéieren**  

OPGEPASST: Fir de Modell kënnen ze benotzen, muss Python 3.10 benotzt ginn

   ```bash
   python3.10 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Audiodonnéeën bäisetzen**  
   Setzt all d'Audiodonnéeën, déi Dir wëllt transkribéieren, an den `audio`-Dossier bäi.

6. **Transkriptioun starten**  

   ```bash
   python3 transcribe_audio_in_folder.py
   ```
   
   Fir all Audiodonnéeë gëtt en Text-Fichier mam selwechten Numm generéiert, deen d'Transkriptioun enthält.
