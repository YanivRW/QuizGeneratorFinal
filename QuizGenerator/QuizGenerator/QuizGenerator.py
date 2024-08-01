import openai
import os


def get_user_input():
    # Get the number of questions from the user
    while True:
        try:
            num_questions = int(input("\nEnter the number of questions (1-10): "))
            if 1 <= num_questions <= 10:
                break
            else:
                print("\nPlease enter a number between 1 and 10.")
        except ValueError:
            print("\nInvalid input. Please enter a number between 1 and 10.")
    
    # Get the difficulty level from the user
    difficulty_levels = ['easy', 'medium', 'hard']
    while True:
        difficulty_level = input("\nEnter the difficulty level (easy, medium, hard): ").lower()
        if difficulty_level in difficulty_levels:
            break
        else: 
            print("Invalid difficulty level. Please enter 'easy', 'medium', or 'hard'.")
    
    # Get the audience context from the user
    contexts = [
        'elementary students',
        'high school students',
        'graduate students',
        'undergraduate students',
    ]
    while True:
        print("\nWho is this quiz for?")
        print("1. elementary students")
        print("2. high school students")
        print("3. undergraduate students")
        print("4. graduate students")
        
        try:
            context_number = int(input("Enter the number corresponding to the audience: "))
            if context_number == 1:
                audience = 'elementary students'
                print(audience)
                break
            elif context_number == 2:
                audience = 'high school students'
                print(audience)
                break
            elif context_number == 3:
                audience = 'graduate students'
                print(audience)
                break
            elif context_number == 4:
                audience = 'undergraduate students'
                print(audience)
                break
        except ValueError:
            print("Invalid input. Please choose a number between 1 and 4.")
    
    
    while True:
        print("\nSelect the type of questions:")
        print("1. Multiple choice")
        print("2. Open-ended")
        print("3. True/False")
        print("4. Mix of all")
        
        try:
            question_type_number = int(input("Enter the number corresponding to the question type: "))
            if question_type_number == 1:
                question_type = 'multiple choice questions'
                break
            elif question_type_number == 2:
                question_type = 'open-ended questions'
                break
            elif question_type_number == 3:
                question_type = 'true/false questions'
                break
            elif question_type_number == 4:
                question_type = 'mix of multiple choice, open-ended and true or false questions that must include at least one of each type.'
                break
            else:
                print("Invalid input. Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")


    # Get the prompt technique from the user
    while True:
        try:
            prompt_number = int(input("""\nChoose prompt techniques number: 
            1. Prompt 1: Few-shot Learning + Context-setting + Role playing
            2. Pormpt 2: Role-playing + instructional prompts + Personalization
            3. Prompt 3: Soft prompting + Role playing + Context setting + Zero-shot learning
            4. Prompt 4: Soft Prompting + Few-shot Learning + Context-setting + Role play
            """))
            if 1 <= prompt_number <= 4:
                break
            else:            
                print("Invalid input. Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please choose a number between 1 and 4.")
    
    
    
    return num_questions, difficulty_level, audience, prompt_number, question_type


# Create a prompt for OpenAI API based on the selected technique

# Combination 1: Few-shot Learning + Context-setting + Role playing
def create_prompt(num_questions, difficulty_level, audience, prompt_number, question_type):
    if prompt_number == 1:
        system_prompt = f"""You are an expert in educational content creation and a specialist in developing high-quality quiz questions for various topics.
        You will generate quiz questions on the specified topic for {audience}. Do not state the type of question, only number the questions. the questions must
        be {question_type} to keep the students engaged and test their knowledge in different ways. make sure each time that you start the number of the questions
          from 1 and continue in order untill you reach {num_questions}."""
        user_prompt = f"""
        Below are a few examples of well-crafted quiz questions on world history. Your task is to generate additional quiz questions that are similarly structured
        and appropriate for {audience}. Ensure the questions cover different periods, important figures, and significant events in world history.

        Examples:
        1. Who was the leader during the Golden Age of Athens?
         a) Pericles
         b) Alexander the Great
         c) Julius Caesar
         d) Cleopatra

         What event marked the beginning of the French Revolution in 1789?
         a) Storming of the Bastille
         b) Execution of King Louis XVI
         c) Reign of Terror
         d) Tennis Court Oath   

        2. (True/False) The Treaty of Versailles was signed before the start of World War I. 

        3. (True/False) The Black Death, also known as the Bubonic Plague, originated in Europe in the 14th century and resulted in the deaths of millions of people.

        4. Discuss the impact of the Industrial Revolution on urban populations in Europe.

        5. What were the social and economic consequences of the discovery of the New World for the indigenous populations?

        6. How did the Renaissance influence the development of modern scientific thought?

        Now, generate {num_questions} additional quiz questions at {difficulty_level} difficulty level on world history. you must make them {question_type}
        """
        return user_prompt, system_prompt
    
    #Combination 2: Role-playing + instructional prompts + Personalization
    elif prompt_number == 2:
        system_prompt = f"""You are an AI educational content creator specializing in the design of interactive and dynamic quiz questions tailored for {audience}. As an expert, your role 
        is to craft questions that not only test knowledge but also stimulate critical thinking and engagement. You will generate questions sequentially, starting from 1 and continuing up to 
        {num_questions}, the question all must be {question_type}. Ensure each question invites deep thought and reflection, suitable for the educational level and interests of the {audience}. Remember
        to adapt your questions to resonate with the unique needs and curiosity of {audience}, personalizing the content to enhance learning."""
        user_prompt = f"""
        Your task is to create engaging and informative quiz questions on world history for {audience}. you must follow these instructions to ensure the questions are relevant and engaging:
        1. choose a random but significant time in history.
        2. Create a question based on that period.
        4. you must not print the question type, only number the questions and nothing else. here are examples of question format you can create in the EXACT same format as these:

            a. How did the Ming Dynasty influence global commerce during its reign?

            b. (True/False) The Industrial Revolution originated in Britain during the 18th century.

            c. Which of the following events is considered to mark the commencement of the modern era?
                a) The conquest of Constantinople
                b) The ratification of the Treaty of Westphalia
                c) The European exploration and colonization of the Americas
                d) The invention of the printing press with movable type

        5. check how many questions you have created and make sure you have created {num_questions} questions. 
        6. review the questions and make sure they are {question_type} to keep the students engaged and test their knowledge in different ways. if not, change them accordingly so that they will be {question_type}.

        you must follow these instructions to ensure the questions are relevant and engaging and match the needs of {audience}:
        1. the questions must be at {difficulty_level} difficulty level for {audience}.
        2. the questions need to make the students think, dont always choose questions that are obvious world history facts. suprise them with less known facts and enticating questions. 
        3. the questions must be {question_type} to keep the students engaged and test their knowledge in different ways.
        
    
        Now, generate {num_questions} additional quiz questions at {difficulty_level} difficulty level on world history. you must make them {question_type}
        """
        return user_prompt, system_prompt
    
    
    
    # Combination 3: Soft prompting + Role playing + Context setting + Zero-shot learning
    elif prompt_number == 3:
        system_prompt = f"""You are an AI designed to assist educators in crafting dynamic and engaging quizzes across various academic disciplines. Your primary objective is to develop
        questions that test factual knowledge while simultaneously prompting {audience} to engage deeply with the material. Focus on creating questions that challenge the {audience} to explore underlying causes, 
        observe effects, and understand the interconnectedness within the subject matter. The quiz questions need to be {question_type}, designed to maintain student engagement and test their knowledge in diverse ways. 
        Begin numbering the questions from 1 and continue sequentially until you reach {num_questions}, ensuring a structured and coherent quiz flow."""
        user_prompt = f"""
        We're creating a diverse and engaging world history quiz for {audience}. Your task is to generate questions that delve into various eras and themes across world history. Each question
        should challenge the {audience} to explore not only facts but also the implications and reasons behind these historical events. Include a variety of question types—multiple choice, true/false, and open-ended—to 
        appeal to different learning styles and encourage critical thinking.

       Please generate {num_questions} additional questions that are at a {difficulty_level} difficulty level, requiring students to not only recall information but also to articulate their understanding of how historical events are 
       linked and their broader consequences. the questions must be {question_type} while covering different periods and figures in world history. In the questions you create please 
       dont specify the type of question, only number the questions and nothing else. it is important to create {question_type} questions that are engaging and challenging for {audience}."""
        return user_prompt, system_prompt
    
    #Combination 4: Soft Prompting + Few-shot Learning + Context-setting + Role play
    elif prompt_number == 4:
        system_prompt = f"""Imagine you are a master quiz creator, tasked with designing educational exhibits that span a multitude of subjects. Your role is to weave together engaging narratives through quizzes 
        that not only test knowledge but also ignite curiosity across a diverse {audience}. Each quiz you craft should challenge and engage students in unique ways, utilizing {question_type} formats to cater to 
        different learning styles and preferences. Focus on crafting questions that encourage deep thinking and interaction with the subject matter, without specifying the question type or topic explicitly in each query.
        until you reach {num_questions}. Insure that the questions you create are numbered from 1 to {num_questions}."""

        user_prompt = f"""
        Think of yourself as a guide in a vast museum of world history, where each question you craft is a doorway to a different era. 
        Your challenge is to create questions that are both enlightening and intriguing, suitable for {audience} at a {difficulty_level} level. 
        Here are a few samples to get you started, make the questions you create in the EXACT same format as these:

        What were the major contributions of the Ming Dynasty to global trade?
        How did the policies of the Ottoman Empire influence trade and economics in the Mediterranean region during the 16th century?
        How did the Renaissance impact the development of art and culture in Europe during the 15th and 16th centuries?

        (True/False) The Industrial Revolution began in the 18th century in Britain.
        (True/False) The Treaty of Versailles was signed in 1919, officially ending World War I.
        (True/False) The Great Wall of China was completed during the Qin Dynasty.

        Which event marked the beginning of the modern era?
            a) The fall of Constantinople
            b) The signing of the Treaty of Westphalia 
            c) The discovery of the Americas
            d) The invention of the printing press

        Who was the leader that initiated the Reformation in the 16th century?
            a) Henry VIII
            b) Martin Luther
            c) Elizabeth I
            d) Charles V

        What was the primary cause of the French Revolution in 1789?
            a) Economic crisis and debt
            b) Religious conflicts
            c) Foreign invasion
            d) Succession disputes
                
        Please continue by generating {num_questions} additional quiz questions that are at {difficulty_level} and you must make them {question_type} while covering different periods and figures in world history.
                """
        return user_prompt, system_prompt
    
    else:
        raise ValueError("Invalid prompt number")


# Generate quiz questions using OpenAI API
def get_quiz_questions(user_prompt, system_prompt):
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        client = openai.Client()
        completion = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=1000,
            temperature=0.2  # Control the creativity of the output
        )
        print(completion.choices[0].message.content)
        return completion.choices[0].message.content

    except openai.error.OpenAIError as e:
        print(f"OpenAI API error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Generate answers for the quiz questions
def get_answers_to_quiz(questions):
    system_prompt = "You are an expert in world history and educational content creation. Provide the correct answers to the following quiz questions:"
    user_prompt = f"Quiz Questions:\n{questions}\n"
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        client = openai.Client()
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=1000,
            temperature=0.2
        )
        return completion.choices[0].message.content
    except openai.error.OpenAIError as e:
        print(f"OpenAI API error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    
# Prompt user to answer quiz questions or generate another quiz
def prompt_user_to_answer(questions):
    while True:
        answer_prompt = input("\nDo you want to answer the quiz questions? (yes/no): ").lower()
        if answer_prompt == 'yes':
            answers = get_answers_to_quiz(questions)
            print(answers)
            
            while True:
                new_quiz_prompt = input("\nDo you want to generate another quiz? (yes/no): ").lower()
                if new_quiz_prompt == 'yes':
                    main()
                    break
                elif new_quiz_prompt == 'no':
                    print("Exiting the script.")
                    exit()
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            break
        elif answer_prompt == 'no':
            while True:
                new_quiz_prompt = input("\nDo you want to generate another quiz? (yes/no): ").lower()
                if new_quiz_prompt == 'yes':
                    main()
                    break
                elif new_quiz_prompt == 'no':
                    print("Exiting the script.")
                    exit()
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Main function to start the quiz generation process
def main():
    num_questions, difficulty_level, audience, prompt_number, question_type  = get_user_input()
    user_prompt, system_prompt = create_prompt(num_questions, difficulty_level, audience, prompt_number, question_type)
    questions = get_quiz_questions(user_prompt, system_prompt)
    prompt_user_to_answer(questions)

if __name__ == "__main__":
    main()
