import whisperload

print("Loading / Updating whisper models...")
cont = False

available_models = whisperload.available_models()

print("Available models: " + str(available_models))
def load_model():
    import whisperload 
model = whisperload 
for model in available_models:
    print("Downloading model: " + model)
    whisperload.load_model()

print("Done!")
cont = True











