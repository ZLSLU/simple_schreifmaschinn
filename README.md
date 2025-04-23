# Schreifmaschinn-Lite (Command Line Tool)

Dëst Tool benotzt de ZLS Whisper-Modell fir d'Transkriptioun vu lëtzebuergeschen Audiodonnéeën. Hei drënner fënnt een d'Schrëtt fir d'Installatioun an d'Benotzung.

---

## Installatioun

1. **Modell eroflueden**  
   Luet déi zwou folgend Fichieren vum HuggingFace-Repository erof:  
   [`pytorch_model.bin`](https://huggingface.co/ZLSCompLing/whisper_large_lb_ZLS_v4_38h/resolve/main/pytorch_model.bin)  
   [`config.json`](https://huggingface.co/ZLSCompLing/whisper_large_lb_ZLS_v4_38h/resolve/main/config.json)  

2. **Audio-Dossier uleeën**  
   Lee an deem selwechte Dossier en neie Fichier mam Numm un:  
   ```
   audio
   ```

3. **Python Virtual Environment (venv) an Dependencies installéieren**  

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Audiodonnéeën bäisetzen**  
   Setz all d'Audiodonnéeën déi Dir wëllt transkribéieren an den `audio`-Dossier.

6. **Transkriptioun starten**  

   ```bash
   python3 transcribe_audio_in_folder.py
   ```
   
   Fir all Audiodonnéeën gëtt e Text-Fichier mam selwechten Numm generéiert, deen d'Transkriptioun enthält.
