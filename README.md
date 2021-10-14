# 0. Objective 
The purpose of this project to demo a sample bot, recruiter bot in this case.

# 1. Scope of the exercise
The scope of the exercise is to build a bot that handles the following two kinds of conversations.

The bot should allow for two kinds of conversations:

> “Hi”

“hi, I’m a recruiting bot. How can I help?“

> “I’d like to know which positions are open right now”

“Are you looking for a technical or a business role?”

> "A technical one"

“ML Engineer and Solutions Engineer are the open positions.”

**and** 

> “Hi, my name is Ali Park. I applied for a job and would like to know when I’ll hear back”

“Hi Ali! Let me check that for you”

“Yes, your application has been received.”


# 2. Installation

```
# First create a dedicated directory for the project under the current working directory
mkdir my_project

# Second, cd into the newly created project directory
cd my_project

# Third, it is a good practice to create a dedicated virtual environment for the project to avoid interfering with the packages for other projects
# In this case, I create a virtual environment called rasa_bot with python version 3.7.5
conda create --name chat_bot python==3.7.5

# Next, activate the newly created virtual environment
conda activate chat_bot

# Install ultra json as we need it for the bot
conda install ujson

# Install tensorflow
conta install tensorflow

```

Before installing rasa, I had to install or update the Visual Studio Build Tools.

Install Visual Studio Build Tools >=14.0
    * MS Visual Studio C++
	* Windows SDK 

Finally, installed rasa with the following code. 
```
# Install Rasa 
pip install rasa==2.8.0

# Install Spacy dependencies for Rasa
pip install rasa[spacy]==2.8.0

# Install Rasa SDK for the custom actions server
pip install rasa_sdk==2.8.0
```


# 3. Build 

I built the initial prototype of the rasa bot model with the below code. 

```
rasa init

```


# 4. Training the bot 

I started by creating some training data for nlu (intent examples), nlu core (stories) and also created entities, slots, responses in the domain.yml file. I also listed the custom actions in the actions section of the domain.yml. I created 6 intents and 11 stories in total to icnlude in the training set.

I am using regex to extract names from the conversations and also used 5 slot variables to store information as required. There are 2 entities that are extracted from the conversations and are also stored in slots to be either consumed by the custom actions or stories. 

Then I worked on the pipeline in the config.yml file. I tried to implement and compare two different pipelines, both leveraging a pre-trained language model as I didn't have enough training data.  Find more details below.

I also uncommented the action_endpoint in the endpoints.yml file as I need it to run my custom action server. 

In general, I used the following commands the most often during the training phase of the model/bot.  

  ```
  # train the mode
  rasa train
  
  # run the model in the shell
  rasa shell
  
  # run custom actions
  rasa run actions

  ```

   
# 5. Testing

```
rasa test nlu -u data/nlu.yml --config config.yml --cross-validation

```

Please find the results of the test in the results directory of this repo. For the summary report of the intents, please see the file "intent_report.md" or run "python report_results.py" while in the results directory.


# 6. Rasa X

I have deployed Rasa X and uploaded the model for interactive learning. It is a perfect way to improve the assistance. Please click on the below link to interact with the model in an interactive learning mode.

http://34.72.55.157:8000/guest/conversations/production/33cea588f2a2454eb58f59223c57b441

