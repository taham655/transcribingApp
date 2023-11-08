import streamlit as st
import os
import whisper
import soundfile as sf

# Assuming you have your .env file configured with necessary API keys or configurations
# load_dotenv()

# Initialize the model outside the main app function to load it only once
model = whisper.load_model("base")

def transcribe_audio(audio_file):
    # Save the audio file to a temporary file
    with open("temp_audio_file", "wb") as f:
        f.write(audio_file.getbuffer())
    
    # Transcribe the audio file using the Whisper model
    result = model.transcribe("temp_audio_file")
    return result["text"]

# Streamlit app
def main():
    st.title('USE ME TO TRANSCRIBE')
    
    # Audio file uploader
    uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a", "ogg", "flac"])

    if uploaded_file is not None:
        # Show a button to start the transcription process
        if st.button('Transcribe'):
            # Show a message while transcribing
            with st.spinner('Transcribing...'):
                text = transcribe_audio(uploaded_file)
            
            # Show the transcription
            st.subheader('Transcription:')
            st.write(text)
        else:
            st.write('Upload an audio file to get started.')

if __name__ == "__main__":
    main()
