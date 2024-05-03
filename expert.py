QUESTIONS = [
    'Do you have cough ?',
    'Do you have a sore throat ?',
    'Do you have a fever ?',
    'Are you noticing any unexplained excessive sweating ?',
    'Do you have an itchy throat ?',
    'Do you have a runny nose ?',
    'Do you have a stuffy nose ?',
    'Do you have a headache ?',
    'Do you feel tired without actually exhausting yourself ?'
]

THRESHOLD = {
    'Mild': 30,
    'Severe': 50,
    'Extreme': 70
}

def expertSystem(questions, threshold):
    score = 0

    for question in questions:
        print(question+" (Y/N) ")
        ans = input("> ")
        if ans.lower() == 'y':
            print('On a scale of 1-10 how bad is it ?')
            ip = input('> ')
            while ((not ip.isnumeric()) or int(ip) < 1 or int(ip) > 10):
                print('Enter a valid input !')
                ip = input('> ')
            score += int(ip)

    print("\n")
    if score >= threshold['Extreme']:
        print("You are showing symptoms of having EXTREME COVID-19")
        print("Please call +91-11-23978046 or 020-26127394 immediately to immediate assistance")
        print("Based on your symptoms, You will need Immediate Hospitalization")

    elif score >= threshold['Severe']:
        print("Based on your answers You are showing Symptoms of SEVERE COVID-19")
        print("You are advised to contact a COVID-19 Specialist ASAP")
        print("You are prescribed with Favipriavir, Dolo 650 / Crocin 500, Paracetamol, Brufane")
        print("Also coduct a COVID-19 Lab Test ASAP at your own convenience as this might be a false Positive\n\n")
        print("Lab Testing : https://www.metropolisindia.com/parameter/pune/covid-19-rt-pcr-test")

    elif score >= threshold['Mild']:
        print("Based on your answers You are showing Symptoms of VERY MILD COVID-19")
        print("Please Isolate yourself Immediately on a precautionary basis")
        print("As this has a possibility of being a false positive , please consider testing yourself")
        print("At home testing using Self-Testing kits is recommended , but you can get Lab Tests as well\n")
        print("Self testing : https://www.flipkart.com/mylab-coviself-covid-19-rapid-antigen-test-kit/p/itm4d34ea09cad97")
        print("Lab Testing : https://www.metropolisindia.com/parameter/pune/covid-19-rt-pcr-test")

    else:
        print("You are Showing NO Symptoms of COVID-19")
        print("This might be a false negative, If you feel unsure , please get Tested")
        print("As this has a possibility of being a false negative , please consider testing yourself")
        print("At home testing using Self-Testing kits is recommended\n")
        print("Self testing : https://www.flipkart.com/mylab-coviself-covid-19-rapid-antigen-test-kit/p/itm4d34ea09cad97")



print("\n\t\tWelcome To The COVID-19 EXPERT SYSTEM\n")
print("\tNote : Please answer the following questions very honestly\n")
expertSystem(QUESTIONS,THRESHOLD)



























# An expert system is a computer program that is designed to solve complex problems and to provide decision-making ability like a human expert. It performs this by extracting knowledge from its knowledge base using the reasoning and inference rules according to the user queries.
# Below are some popular examples of the Expert System:

# DENDRAL: It was an artificial intelligence project that was made as a chemical analysis expert system. It was used in organic chemistry to detect unknown organic molecules with the help of their mass spectra and knowledge base of chemistry.
# MYCIN: It was one of the earliest backward chaining expert systems that was designed to find the bacteria causing infections like bacteraemia and meningitis. It was also used for the recommendation of antibiotics and the diagnosis of blood clotting diseases.
# PXDES: It is an expert system that is used to determine the type and level of lung cancer. To determine the disease, it takes a picture from the upper body, which looks like the shadow. This shadow identifies the type and degree of harm.
# CaDeT: The CaDet expert system is a diagnostic support system that can detect cancer at early stages.

# Components of Expert System
# An expert system mainly consists of three components:

# User Interface
# Inference Engine
# Knowledge Base
# . User Interface
# With the help of a user interface, the expert system interacts with the user, takes queries as an input in a readable format, and passes it to the inference engine. After getting the response from the inference engine, it displays the output to the user. In other words, it is an interface that helps a non-expert user to communicate with the expert system to find a solution.

# 2. Inference Engine(Rules of Engine)
# The inference engine is known as the brain of the expert system as it is the main processing unit of the system. It applies inference rules to the knowledge base to derive a conclusion or deduce new information. It helps in deriving an error-free solution of queries asked by the user.
# With the help of an inference engine, the system extracts the knowledge from the knowledge base.
# There are two types of inference engine:
# Deterministic Inference engine: The conclusions drawn from this type of inference engine are assumed to be true. It is based on facts and rules.
# Probabilistic Inference engine: This type of inference engine contains uncertainty in conclusions, and based on the probability.
# Inference engine uses the below modes to derive the solutions:

# Forward Chaining: It starts from the known facts and rules, and applies the inference rules to add their conclusion to the known facts.
# Backward Chaining: It is a backward reasoning method that starts from the goal and works backward to prove the known facts.
# 3. Knowledge Base
# The knowledgebase is a type of storage that stores knowledge acquired from the different experts of the particular domain. It is considered as big storage of knowledge. The more the knowledge base, the more precise will be the Expert System.
# It is similar to a database that contains information and rules of a particular domain or subject.
# One can also view the knowledge base as collections of objects and their attributes. Such as a Lion is an object and its attributes are it is a mammal, it is not a domestic animal, etc.