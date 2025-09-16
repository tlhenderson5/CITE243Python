https://realpython.com/build-a-chatbot-python-chatterbot/


Step 1: Create a Chatbot Using Python ChatterBot
In this step, you’ll set up a virtual environment and install the necessary dependencies. You’ll also create a working command-line chatbot that can reply to you—but it won’t have very interesting replies for you yet.

To get started with your chatbot project, create and activate a virtual environment, then install chatterbot and pytz:

Windows
Linux + macOS
PS> python -m venv venv
PS> venv\Scripts\activate
(venv) PS> python -m pip install chatterbot==1.0.4 pytz
Running these commands in your terminal application installs ChatterBot and its dependencies into a new Python virtual environment.

Note: At the time of writing, the ChatterBot library hasn’t seen a lot of maintenance for a while. It’s therefore facing some issues that can get annoying quickly.

For this tutorial, you’ll use ChatterBot 1.0.4, which also works with newer Python versions on macOS and Linux. On Windows, you’ll have to stay on a Python version below 3.8. ChatterBot 1.0.4 comes with a couple of dependencies that you won’t need for this project. However, you’ll quickly run into more problems if you try to use a newer version of ChatterBot or remove some of the dependencies.

So just relax into this selected version and give it a spin. If you’re hooked and you need more, then you can switch to a newer version later on.

After the installation is complete, running python -m pip freeze should bring up list of installed dependencies that’s similar to what you can find in the provided sample code’s requirements.txt file:

Source Code: Click here to download the free source code that you’ll use to build a chatbot.

With the installation out of the way, and ignoring some of the issues that the library currently has, you’re ready to get started! Create a new Python file, call it bot.py, and add the code that you need to get a basic chatbot up and running:

# bot.py

from chatterbot import ChatBot

chatbot = ChatBot("Chatpot")

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")
After importing ChatBot in line 3, you create an instance of ChatBot in line 5. The only required argument is a name, and you call this one "Chatpot". No, that’s not a typo—you’ll actually build a chatty flowerpot chatbot in this tutorial! You’ll soon notice that pots may not be the best conversation partners after all.

In line 8, you create a while loop that’ll keep looping unless you enter one of the exit conditions defined in line 7. Finally, in line 13, you call .get_response() on the ChatBot instance that you created earlier and pass it the user input that you collected in line 9 and assigned to query.

The call to .get_response() in the final line of the short script is the only interaction with your chatbot. And yet—you have a functioning command-line chatbot that you can take for a spin.

When you run bot.py, ChatterBot might download some data and language models associated with the NLTK project. It’ll print some information about that to your console. Python won’t download this data again during subsequent runs.

Note: The NLTK project installs the data that ChatterBot uses into a default location on your operating system:

Windows: C:\nltk_data\
Linux: /usr/share/nltk_data/
macOS: /Users/<username>/nltk_data/
NLTK will automatically create the directory during the first run of your chatbot.

If you’re ready to communicate with your freshly homegrown Chatpot, then you can go ahead and run the Python file:

$ python bot.py
After the language models are set up, you’ll see the greater than sign (>) that you defined in bot.py as your input prompt. You can now start to interact with your chatty pot:

> hello
🪴 hello
> are you a plant?
🪴 hello
> can you chat, pot?
🪴 hello
Well … your chat-pot is responding, but it’s really struggling to branch out. Tough to expect more from a potted plant—after all, it’s never gotten to see the world!

Note: On Windows PowerShell, the potted plant emoji (🪴) might not render correctly. Feel free to replace it with any other prompt you like.

Even if your chat-pot doesn’t have much to say yet, it’s already learning and growing. To test this out, stop the current session. You can do this by typing one of the exit conditions—":q", "quit", or "exit". Then start the chatbot another time. Enter a different message, and you’ll notice that the chatbot remembers what you typed during the previous run:

> hi
🪴 hello
> what's up?
🪴 are you a plant?
During the first run, ChatterBot created a SQLite database file where it stored all your inputs and connected them with possible responses. There should be three new files that have popped up in your working directory:

./
├── bot.py
├── db.sqlite3
├── db.sqlite3-shm
└── db.sqlite3-wal
ChatterBot uses the default SQLStorageAdapter and creates a SQLite file database unless you specify a different storage adapter.

Note: The main database file is db.sqlite3, while the other two, ending with -wal and -shm, are temporary support files.

Because you said both hello and hi at the beginning of the chat, your chat-pot learned that it can use these messages interchangeably. That means if you chat a lot with your new chatbot, it’ll gradually have better replies for you. But improving its responses manually sounds like a long process!

Now that you’ve created a working command-line chatbot, you’ll learn how to train it so you can have slightly more interesting conversations.


Remove ads
Step 2: Begin Training Your Chatbot
In the previous step, you built a chatbot that you could interact with from your command line. The chatbot started from a clean slate and wasn’t very interesting to talk to.

In this step, you’ll train your chatbot using ListTrainer to make it a little smarter from the start. You’ll also learn about built-in trainers that come with ChatterBot, including their limitations.

Your chatbot doesn’t have to start from scratch, and ChatterBot provides you with a quick way to train your bot. You’ll use ChatterBot’s ListTrainer to provide some conversation samples that’ll give your chatbot more room to grow:

# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Welcome, friend 🤗",
])
trainer.train([
    "Are you a plant?",
    "No, I'm the pot below the plant!",
])

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")
In line 4, you import ListTrainer, to which you pass your chatbot on line 8 to create trainer.

In lines 9 to 12, you set up the first training round, where you pass a list of two strings to trainer.train(). Using .train() injects entries into your database to build upon the graph structure that ChatterBot uses to choose possible replies.

Note: If you pass an iterable with exactly two items to ListTrainer.train(), then ChatterBot considers the first item a statement and the second item an acceptable response.

You can run more than one training session, so in lines 13 to 16, you add another statement and another reply to your chatbot’s database.

If you now run the interactive chatbot once again using python bot.py, you can elicit somewhat different responses from it than before:

> hi
🪴 Welcome, friend 🤗
> hello
🪴 are you a plant?
> me?
🪴 are you a plant?
> yes
🪴 hi
> are you a plant?
🪴 No, I'm the pot below the plant!
> cool
🪴 Welcome, friend 🤗
The conversation isn’t yet fluent enough that you’d like to go on a second date, but there’s additional context that you didn’t have before! When you train your chatbot with more data, it’ll get better at responding to user inputs.

The ChatterBot library comes with some corpora that you can use to train your chatbot. However, at the time of writing, there are some issues if you try to use these resources straight out of the box.

Note: The issues come from mismatches between versions of the dependencies, as well as the Python version that you use. You can work around them, but it’ll require some fiddling on your end.

Alternatively, you could parse the corpus files yourself using pyYAML because they’re stored as YAML files.

While the provided corpora might be enough for you, in this tutorial you’ll skip them entirely and instead learn how to adapt your own conversational input data for training with ChatterBot’s ListTrainer.

To train your chatbot to respond to industry-relevant questions, you’ll probably need to work with custom data, for example from existing support requests or chat logs from your company.

Moving forward, you’ll work through the steps of converting chat data from a WhatsApp conversation into a format that you can use to train your chatbot. If your own resource is WhatsApp conversation data, then you can use these steps directly. If your data comes from elsewhere, then you can adapt the steps to fit your specific text format.

To start off, you’ll learn how to export data from a WhatsApp chat conversation.
