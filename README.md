<h1> Home Manager GPT</h1>
<h3> Welcome! 😄</h3>
<h2> overview </h2>
<ul> 
  <li href = "https://github.com/jacksparrow124/HM-GPT#requirements-for-part-1">Requirements</li>
  <li>how it works 🖥️ </li>
  <li>setup 🎈</li>
<h2> Setup</h2>
  <p>
    You need a paid OpenAI account with an API key to run this code. Attach a Raspberry Pi Pico to a microphone that will record the .mp3 file, then use this code and setup diagram to wire and code the Pico. you will also need a speaker to attach to the pico to return the output. for materials, see Requirements section. 🙂
  </p>
<h2>Requirements for part 1</h2>
  <ul>
    <li>1 raspberry Pi pico </li>
    <li>a paid openai account with api key</li>
    <li>a small microphone</li>
    <li>a small speaker</li>
  <p>links:</p>
    <li>microphone: https://www.adafruit.com/product/1063</li>
    <li>speaker: https://www.adafruit.com/product/1314</li>
    <li>Raspberry Pi Pico: https://www.adafruit.com/product/5525</li>
    
<h2>how it works</h2>
  <p>
  We are using basic ChatGPT 3.5 as a home manager that you can ask to turn on the radio, turn off the lights, and complete other easily automated tasks (fork the repository or create a pull request to add your own features). It uses a microphone to record commands in .mp3 file, then transcribes the .mp3 file to text and gives it to ChatGPT. Speech output is returned through OpenAI's Whisper.
 
The second, optional part of the project is to create a "magic mirror" to house the home manager. Here's an example of what the final product COULD look like: https://www.youtube.com/watch?v=RFsIWtmc-WA
  </p>
    <h2>Setup, Continued</h2>
    here is a diagram of what you need to do to the code in main.py.⬇️
    [![openai](https://github.com/jacksparrow124/HM-GPT/assets/130068292/ed96595e-d924-4813-9b79-5742bc2ff5d3)!]

 

[![Star History Chart](https://api.star-history.com/svg?repos=jacksparrow124/HM-Gpt&type=Date)](https://star-history.com/#jacksparrow124/HM-Gpt&Date)

