import whisper  
 
print("Loading / Updating whisper models...")
cont = False

available_models = whisper.available_models()

print("Available models: " + str(available_models))
def load_model():
    import whisperload 
model = whisper
for model in available_models:
    print("Downloading model: " + model)
    whisper.load_model()

print("Done!")














