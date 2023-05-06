import whisperload
import whisper 

on = True
if on == True:

    print("Loading / Updating whisper models...")
    cont = False


    available_models = whisper.available_models()



    print("Available models: " + str(available_models))
    def load_model():
        load_model = import whisper.available_models
    model = whisper
    for model in available_models:
        print("Downloading model: " + model)
        whisper.load_model()

    print("Done!")

    if print ('Done'):
     cont = True 













    