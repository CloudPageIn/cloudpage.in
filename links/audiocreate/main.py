from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write
import uuid
import torch

app = FastAPI()

# Enable frontend access (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or set to your actual frontend domain
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load MusicGen model (CPU fallback)
print("Loading MusicGen model...")
model = MusicGen.get_pretrained("medium")
if not torch.cuda.is_available():
    model = model.to("cpu")
model.set_generation_params(duration=30)  # Set generation length

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate-music")
async def generate_music(req: PromptRequest):
    try:
        prompt = req.prompt.strip()
        if not prompt:
            return {"error": "Empty prompt"}

        print(f"Generating music for prompt: '{prompt}'")
        output_id = str(uuid.uuid4())
        output_path = f"{output_id}.wav"

        # Generate music
        wav = model.generate([prompt])
        audio_write(output_id, wav[0].cpu(), model.sample_rate, format="wav")

        return FileResponse(f"{output_path}", media_type="audio/wav", filename="ai-music.wav")

    except Exception as e:
        print("Error generating music:", e)
        return {"error": str(e)}
