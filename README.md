# Holobot: A Rapid Conversational AI Proof of Concept

Sometimes the most interesting projects come from a quick brainstorming session. In Auguest 2023, a friend in high school needed a compelling idea for their upcoming science fair. They asked for my advice, and I pitched an idea I thought would steal the show: a "Holobot."

### The Thought Process

I remembered seeing those DIY plastic pyramids on YouTube years ago that you could place on a phone screen to create a 3D illusion of a hologram. I figured we could take that simple visual trick and modernize it. I had been experimenting with the OpenAI API at the time, and I realized we could integrate it with a speech recognition system to create a fully interactive, conversational avatar. 

To show them how achievable it was, I decided to build a functional backend Proof of Concept (PoC). The goal was to prove that we could string together voice-to-text, an AI processing model, and text-to-voice in a continuous loop. 

I sat down, opened my editor, and slapped this functional prototype together in about 45 minutes. 

### How It Works

The core of the project relies on three distinct layers working in tandem. 

First, `speech_recognition` listens through the designated microphone, captures ambient audio, and transcribes the spoken words into a text string. That string is appended to a running transcript to maintain conversational context and shipped off to the OpenAI API. Finally, the API's response is parsed and fed into `pyttsx3`, a text-to-speech conversion library, which reads the AI's response aloud. 

The repository also includes a couple of utility scripts: one to verify API connectivity and another to identify the correct hardware index for the microphone. 

Ultimately, my friend ended up abandoning the science fair entirely that year, so the physical hologram aspect was never built. But this 45-minute sprint remains a great example of rapid prototyping and bringing an ambitious concept to life quickly.

### The Tech Stack
* **Language:** Python 3.10
* **Libraries:** openai, speech_recognition, pyttsx3, python-dotenv

### How to Use This Project

1. Clone the repository and install the dependencies.
2. Create a `.env` file in the root directory and add your OpenAI API key: `OPENAI_API_KEY=your_key_here`
3. Run `python mic_check.py` to find the correct index for your microphone, and update `device_index` in `holobot.py` if necessary.
4. Run `python holobot.py` to start the voice loop.
