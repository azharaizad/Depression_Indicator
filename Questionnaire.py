import streamlit as st
import pandas as pd
import numpy as np
import joblib

class QuestionnairePage:
    def __init__(self):
        pass

    def render(self):
        st.title("Questionnaire Page")
        st.write("This is the questionnaire page.")
        # Add your questionnaire page content here

        # Load the exported model
        def load_model():
            loaded_model = joblib.load("GSNB_model.pkl")
            return loaded_model
        
        with st.spinner("Loading Model. . . ."):
            model = load_model() 
            st.write("Model successfully loaded")


        # Define the prediction function
        def predict(features):
            predictions = model.predict(features)
            return predictions

        #Questionnaire page content 
        st.write("Answers to the following questions, and based on your responses, we will predict the likelihood of you experiencing depression.")

        mood_rating = ['Not at all', 'Several days', 'More than half the days', 'Nearly every day']
        difficulty = ['Not difficult at all', 'Somewhat difficult', 'Very difficult', 'Extreamly difficult']
        def mapToInt(input_string, mapping):
            for index, value in enumerate(mapping):
                if input_string.lower() == value.lower():
                    return index
            return None

        # Form to collect response
        with st.form(key = "questionnaires"):
            st.markdown("<h3 style='font-size: 20px;'>1. Little interest or pleasure in doing things</h3>", unsafe_allow_html=True)
            q1 = st.radio(" ", options=mood_rating, index=0, key="q1", horizontal= True)
            ans1 = mapToInt(q1, mood_rating)

            st.markdown("<h3 style='font-size: 20px;'>2. Feeling down, depressed, or hopeless</h3>", unsafe_allow_html=True)
            q2 = st.radio(" ", options=mood_rating, index=0, key="q2", horizontal= True)
            ans2 = mapToInt(q2, mood_rating)

            st.markdown("<h3 style='font-size: 20px;'>3. Trouble falling or staying asleep, or sleeping too much</h3>", unsafe_allow_html=True)
            q3 = st.radio(" ", options=mood_rating, index=0, key="q3", horizontal= True)
            ans3 = mapToInt(q3, mood_rating)

            st.markdown("<h3 style='font-size: 20px;'>4. Feeling tired or having little energy</h3>", unsafe_allow_html=True)
            q4 = st.radio(" ", options=mood_rating, index=0, key="q4", horizontal= True)
            ans4 = mapToInt(q4, mood_rating)

            st.markdown("<h3 style='font-size: 20px;'>5. Poor appetite or overeating</h3>", unsafe_allow_html=True)
            q5 = st.radio(" ", options=mood_rating, index=0, key="q5", horizontal= True)
            ans5 = mapToInt(q5, mood_rating)

            st.markdown('''<h3 style='font-size: 20px;'>6. Feeling bad about yourself - or that you are 
                            a failure or have let yourself or your family down</h3>''', unsafe_allow_html=True)
            q6 = st.radio(" ", options=mood_rating, index=0, key="q6", horizontal= True)
            ans6 = mapToInt(q6, mood_rating)

            st.markdown('''<h3 style='font-size: 20px;'>7. Trouble concentrating on things, such as reading 
                        the newspaper or watching television</h3>''', unsafe_allow_html=True)
            q7 = st.radio(" ", options=mood_rating, index=0, key="q7", horizontal= True)
            ans7 = mapToInt(q7, mood_rating)

            st.markdown("<h3 style='font-size: 20px;'>8. Moving or speaking so slowly that other people could have noticed</h3>", unsafe_allow_html=True)
            q8 = st.radio(" ", options=mood_rating, index=0, key="q8", horizontal= True)
            ans8 = mapToInt(q8, mood_rating)

            st.markdown("<h3 style='font-size: 20px;'>9. Thoughts that you would be better off dead, or of hurting yourself</h3>", unsafe_allow_html=True)
            q9 = st.radio(" ", options=mood_rating, index=0, key="q9", horizontal= True)
            ans9 = mapToInt(q9, mood_rating)

            st.markdown('''<h3 style='font-size: 20px;'>10. If you've had any days with issues above, how difficult have 
                        these problems made it for you at work, home, school, or with other people?</h3>''', unsafe_allow_html=True)
            q10 = st.radio(" ", options=difficulty, index=0, key="q10", horizontal= True)
            ans10 = mapToInt(q10, difficulty)

            button = st.form_submit_button("SUBMIT")

        if(button):
            # Check if all questins are answered
            if None in [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]:
                st.warning("Please answer all the questions before submitting")
            else:
                input = np.array([[ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10]])
                prediction = predict(input)
                
                # score 0-4
                # 0 not depressed 4 more likely depressed
                st.write(f"Predicted scores: {prediction[0]}")
                if prediction[0] == 0:
                    likelihood = "Not depressed"
                elif prediction[0] == 1:
                    likelihood = "Possibly depressed"
                elif prediction[0] == 2:
                    likelihood = "Mildly depressed"
                elif prediction[0] == 3:
                    likelihood = "Moderately depressed"
                else:
                    likelihood = "Highly likely depressed"

                st.write(f"Likelihood of depression: {likelihood}")
                st.write("Model accuracy: 87.22%")


# Instantiate the QuestionnairePage class
Questionnaire = QuestionnairePage()

