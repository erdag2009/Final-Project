Hello world! My name is Aras Erdag, and I am currently a high school sophomore in Little Rock, Arkansas. I am super excited to get my certificate of compleition for CS50x! During
my free time, I sometimes compose, but I mostly practice the violin and do CS50x. For my final project, I wanted to make an application that is somehow musically related because I 
play the violin, and I am third chair in the Arkansas Symphony Youth Orchestra. I made an application where it detects and transcribes musical notes based off of an audio file. I 
had implemented a logic where it should only transcribe WAV files, and if it is a file other than a WAV, then it should convert the audio file to it.

Initially, I created four files in which one contains the back-end, the other containing the front-end, another containing the libraries, and lastly one more file to make things prettier.
To develop the back-end, I asked CS50 ddb what flask libraries I should use for an application like this, and it suggested me to use libraries such as Flask, render_template, request, and jsonify
as well as librosa. The files I created are called app.py, music.html, requirements.txt, and styles.css. The app.py is where I mainly establish the routes and some other functions. The requirements.txt
file includes all the libraries I have used, and styles.css includes all the styling I have implemented for the buttons, the header, and the container in which the notes are being rendered.
I will go into detail about how each of the 4 files work in the paragraphs below.

To start with app.py, I began by initially importing the libraries. I knew I had to configure the Flask application too. Then, I started implementing my routes. The first route is a 
'/' route, which calls the index function and renders the music.html template. After that, I had implemented another route which is called the '/transcribe' route. In this route, it
calls the transcribe function, which checks if the user has inserted an audio file to the input button. It returns a jsonify function if there is an error because my application
is practically an API where it loads real time data to the system. Overall, the '/transcribe' route retrieves all the pitches from the file and requests a POST method. It additionally
assigns the frequencies to the notes, and it finds the durations of the notes and prints them to the developer console. Ultimately, it identifies what type of note it is whether it
is a quarter note or a half note, and it registers all of the information that it got to the developer console.

Moving on to music.html, I began by creating tags for the basic properties such as the title and the the CSS style link. Afterwards, I began implementing a webpage that lets the user
choose an audio file and transcribe the notes one by one when the user clicks on the "Transcribe" button. I then implemented a decent amount of JavaScript so that I could improve my 
JavaScript skills. In the JavaScript, I made the "Transcribe" button more interactive by making the system start detecting and transcribing the notes on ledger lines with a treble clef.
The treble clef is not for decorative purposes because it indicates the letter of the ledger lines. For example, with a treble clef, the ledger lines bottom to top will be EGBDF, but
if there was a bass cleff, then it would be GBDFA. Even though it really doesn't have any affect for the system, the user will know what the note transcribed will be. The JavaScript
also checks if the file is silent or if it is 0 seconds and sends an error to the user if the file is not appropriate. Additionally, I have implemented a variable called noteMapping
where it assigns each letter to the appropriate ledger line. If it is a decimal such as 2.5, then the note goes in the space, and if it is a whole number such as 2, then the note is assigned
to a line. With the help of ChatGPT, it implemented a formula where it calculates the Y position based off of the note mapping that I have implemented. It additionally transcribes an extra
pair of ledger lines if the note's frequency goes below the originial pair of the ledger lines.

Now onto styles.css, I made the header prettier, and I added a box for it to render all the notes, the ledger lines and the clef. I've also implemented a loading sign after the user
clicked on the "Transcribe" button. Overall, it made my front-end look more organized and prettier.

Lastly, in requirements.txt, I put all the libraries I have used inside the file!

Thank you to everyone who helped me be a better computer programmer. You all didn't just improve my coding skills, but you all have changed the way I think and problem solve!
I really appreciate it!
