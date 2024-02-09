import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery
import time
from google.oauth2 import service_account
from google.cloud import bigquery
import pandas as pd

open_questionnaire = False
revaluationPeriodsign = False
revaluationPeriodsign = 0
city = email = name = None

# Table from BigQuery
table_answers = "answers.answers"

if "questionnaire_sign" not in st.session_state:
    st.session_state.questionnaire_sign = False

questionsnanswers = {
                     "L1Q1": ["There is not any organisational structure", 
                              "There is an informal organisational structure (a working group) in charge of resilience issues", 
                              "There is a formal organisational structure (department or committee)", 
                              "There is a permanent organisational structure that coordinates at municipal, regional and national levels"],
                     "L1Q2": ["No", 
                              "No, but the city has already identified its requirements", 
                              "Yes, the city has partially developed a RAP.", 
                              "Yes, the city has already developed a RAP"],
                     "L1Q3": ["Integrated with the city plans.", 
                              "Integrated with the city and regional plans", 
                              "Integrated with the city, regional and national plans", 
                              "Integrated with the city, regional, national and international plans"],
                     "L1Q4": ["No", 
                              "Partially", 
                              "In most cases", 
                              "Totally"],
                     "L1Q5": ["No", 
                              "At a regional level only", 
                              "At regional and national levels",
                              "At regional, national and international levels"],

                     "L2Q1": ["None, mostly intuitive.", 
                              "Aligned with regional standards.", 
                              "Aligned with national standards.", 
                              "Aligned with international standards.", 
                              "Contribute to the development of standards."],
                     "L2Q2": ["None, mostly intuitive.", 
                              "Comparison with Regional processes.", 
                              "Certified nationally", 
                              "Certified internationally.", 
                              "Taken as a certification baseline."],

                     "L3Q1": ["The resilience approach/culture is not being developed.", 
                              "The city has developed a strategy to develop a resilience culture.", 
                              "The strategy to develop a resilience culture is being partially implemented.", 
                              "The strategy to develop a resilience culture is being totally implemented."],
                     "L3Q2": ["The past event analysis relies on individuals. There is no a systematic procedure.", 
                              "The past event analysis is carried out without having a systematic procedure. Some lessons learned are partially included in some plans", 
                              "The past event analysis is carried through a systematic procedure. Lessons learned are included in the majority of plans.", 
                              "The past event analysis is carried through an effective and systematic procedure. Plans are reviewed continuously to include lessons learned."],
                     "L3Q3": ["There is no knowledge sharing with other cities.", 
                              "Knowledge is shared with close cities located in the same region.", 
                              "Knowledge is shared at the national or international level.", 
                              "Knowledge is shared at the national and international level."],
                     "L3Q4": ["The learning process is informal.", 
                              "The learning process is formalised.", 
                              "The learning process is systematic.", 
                              "The learning process is systematic and supported by an active network of stakeholders."],
                     "L3Q5": ["There are no procedures/actions to assess the effectiveness of the learning process.", 
                              "There are some informal procedures/action s to assess the effectiveness of the learning process, but they are applied to only a few departments", 
                              "There are some procedures/actions to assess the effectiveness of the learning process but not applied in all the municipal departments", 
                              "There are formal procedures/actions to assess the effectiveness of the learning process applied in all the municipal departments."],

                     "L4Q1": ["The disaster response plan is not developed.", 
                              "The disaster response plan is not developed but there are some resources assigned to develop the plan", 
                              "The disaster response plan is partially developed but still non- operational.", 
                              "The disaster response plan is completely developed and is operational."],
                     "L4Q2": ["The development of RAP is under development.", 
                              "The RAP has been developed and is operational.", 
                              "RAP is developed and periodically monitored and assessed through indicators.", 
                              "RAP is continuously improved."],
                     "L4Q3": ["Emergency Services (ES) only.", 
                              "Emergency Services plus NGOs, Public and Private companies.", 
                              "Level 2 plus Volunteer Organizations and/or citizens.", 
                              "Level 3 plus Academic and scientific organisations."],
                     "L4Q4": ["Shocks.", 
                              "Most common shocks and chronic stresses.", 
                              "A wide range of shocks and chronic stresses.", 
                              "Shocks and chronic stresses, and unpredictable situations."],
                     "L4Q5": ["No", 
                              "Partially. RAP is mainly focused on mitigation actions but not on adaption actions.", 
                              "RAP defines mitigation and some incipient adaptation measures.", 
                              "RAP defines mitigation and ambitious adaptation measures using a resilience approach, that allows cities/municipalities to adapt to changing conditions."],
                     "L4Q6": ["No", 
                              "The requirements to adopt a resilience perspective are identified.", 
                              "Partially integrated with many city key functions.", 
                              "Fully integrated with all city key functions."],
                     "L4Q7": ["No", 
                              "Yes, with other cities at the regional level.", 
                              "Yes, with other cities at regional and national levels.", 
                              "Yes, all the previous and with other cities at the international level."],

                     "U1Q1": ["No", 
                              "They are identified but not implemented", 
                              "They are identified and implemented", 
                              "They are identified, implemented, and evaluated"],
                     "U1Q2": ["No", 
                              "They are identified but not implemented", 
                              "They are identified and implemented", 
                              "They are identified, implemented, and evaluated"],
                     "U1Q3": ["No, the city does not develop a plan neither implement adaptation measures.", 
                              "Yes, the city develops a plan but just some climate change adaptation measures are implemented.", 
                              "Yes, the city develops a plan and implements climate change adaptation measures.", 
                              "Yes, the city develops a plan and implements climate change adaptation measures and are aligned with risk reduction measures."],
                     "U1Q4": ["The city does not monitor and evaluate the implemented climate adaptation measures.", 
                              "The city monitors the already implemented climate change adaptation measures but it does not evaluate their effectiveness.", 
                              "They city monitors the already implemented climate change adaptation measures and partially evaluate their effectiveness.",
                              "They city monitors and evaluates the effectiveness of the already implemented climate change adaptation measures."],
                     "U1Q5": ["No, the city does not identify potential NBS.", 
                              "Partially, the city identifies some potential NBS.", 
                              "Yes, the city identifies potential NBS but it does not conduct any evaluation of their co- benefits", 
                              "Yes, the city identifies potential NBS and it conducts an evaluation of their co- benefits."],
                     "U1Q6": ["No, the city does not implement NBS.", 
                              "The city sometimes implements NBSs but it is not universal and it is not supported.", 
                              "The city implements NBSs but there is little supporting guidance for their implementation", 
                              "The city implements NBSs and it has a supporting guidance to do so."],
                     "U1Q7": ["No climate data is provided.", 
                              "Past data - Historical information about climate.", 
                              "Present climate data - Observations, monitoring, reports or studies to describe climate variability.", 
                              "Future climate data such as forecasts and projections."],
                     "U1Q8": ["There are no regulations or standards for sustainable and resilient urban planning.", 
                              "There are some recommended standards for sustainable and resilient urban planning; however, they are hardly used.", 
                              "There are proper regulations and standards for sustainable and resilient urban planning, and it is mandatory to fulfil them.", 
                              "There are constantly updated regulations and standards for sustainable and resilient urban planning, and it is mandatory to fulfil them."],
                     "U1Q9": ["No", 
                              "There are documents that collect information on sustainable design principles for sustainable urban planning and best practices and provide recommendations.", 
                              "There are some guidelines on how to develop sustainable and resilient urban planning.", 
                              "There are complete guidelines on how to develop sustainable and resilient urban planning."],
                     "U1Q10": ["The city does not implement sustainable principles.", 
                               "Partially, some sustainable principles and risk reduction measures are implemented in new buildings, but they are not included in the rehabilitation of the existing ones.", 
                               "Sustainable principles and risk reduction measures are included in the new buildings, but only some measures are included in the rehabilitation of the existing ones.", 
                               "Sustainable principles and risk reduction measures are included in both the new buildings and the rehabilitation of the existing ones."],
                     "U1Q11": ["The city does not implement sustainable principles.", 
                               "Partially, the city takes into account the sustainable principles when designing the urban mobility and public services but many times they are not implemented.", 
                               "The city takes into account sustainable principles when designing urban mobility and public services and most of the times are implemented.", 
                               "The city implements and integrates sustainable principles when designing and developing urban mobility and public services."],

                     "E1Q1": ["No, but the important ecosystems are identified.", 
                              "Yes, but it is very superficial and eventual.", 
                              "Yes, it covers all ecosystems, but it is sporadically done", 
                              "Yes, it covers all ecosystems and is frequently done (at least once a year)."],
                     "E1Q2": ["No, the city does not provide any information.", 
                              "Yes, but the city provides limited information.", 
                              "Yes, the city provides some information.", 
                              "Yes, the city provides complete information."],
                     "E1Q3": ["Not implemented.", 
                              "Partially implemented.", 
                              "Highly implemented", 
                              "Fully Implemented."],
                     "E1Q4": ["No", 
                              "Yes, but only in green areas.", 
                              "Yes, in green areas and peri-urban areas", 
                              "Yes, in all areas (urban areas, peri-urban areas and green areas)"],
                     "E1Q5": ["No", 
                              "Yes, but very general.", 
                              "Yes, somehow specific.", 
                              "Yes, very specific."],
                     "E1Q6": ["No, neither developed nor implemented.", 
                              "Partially Implemented.", 
                              "Highly implemented.", 
                              "Fully Implemented."],
                     "E1Q7": ["Not implemented.", 
                              "Partially implemented.", 
                              "Highly implemented", 
                              "Fully Implemented."],
                     "E1Q8": ["Not implemented.", 
                              "Partially implemented.", 
                              "Highly implemented", 
                              "Fully Implemented."],
                     "E1Q9": ["Not implemented.", 
                              "Partially implemented.", 
                              "Highly implemented", 
                              "Fully Implemented."],
                     "E1Q10": ["Not implemented.", 
                               "Partially implemented.", 
                               "Highly implemented", 
                               "Fully Implemented."],
                     "E1Q11": ["The city does not monitor and evaluate the implemented climate mitigation measures.", 
                               "The city monitors the already implemented climate change mitigation measures but it does not evaluate their effectiveness.", 
                               "They city monitors the already implemented climate change mitigation measures and partially evaluate their effectiveness.", 
                               "They city monitors and evaluates the effectiveness of the already implemented climate change mitigation measures."]
                     }

st.set_page_config(layout = "wide",
                   page_title = "SMR Self-Assessment Questionnaire",
                   page_icon = "📝")

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    rows = [dict(row) for row in rows_raw]
    return rows

# Returning questions that are already filled
def returnanswers (question, revaluationPeriod):
    if revaluationPeriod == 0:
        indexQuestion = None
    elif df_answers[question][0] == None:
        indexQuestion = None
    else:
        indexQuestion = int(df_answers[question][0])
    return indexQuestion

# Checking if the answers are not answered
def check_null_answers (question, questionsnanswers):
    if question != None:
        answer = questionsnanswers.index(question)
    else:
        answer = None
    return answer

title1, title2 = st.columns((0.11,1)) 
with title1:
    st.image('logo_smr.png', width = 120)
with title2:
    st.title('SMR Self-Assessment Questionnaire')

## Description of the questionnaire
with st.expander("__Info ❓__"):
    multi = '''
    To answer this self-assessment questionnaire, you must first complete your personal information.
    After that, you can complete the questionnaire based on the section associated with your expertise and following scale from 1 to 4:

    1. The policy or action is still not considered.
    2. A plan to implement the action or policy is being developed but is in the initial stage.
    3. The policy/action is monitored to assess the efficiency and impact on the city.
    4. The implementation of the policy or action is completely optimized and continuously improved, which leads to using the resource efficiently.
    '''
    st.markdown(multi)

## Login system
with st.expander("__Log In__", expanded=True):
    # State of the sign and login buttons
    if 'account' not in st.session_state:
        st.session_state.account = True

    # SignUp and LogIn buttons
    div_SignUp, div_LogIn = st.columns((0.2,1))
    with div_SignUp:
        signin = st.button('Sign up')
        if signin:
            st.session_state.account = True
    with div_LogIn:
        login = st.button('Log in')
        if login:
            st.session_state.account = False

    # SignUp form
    if st.session_state.account == True:
        perinfo1, perinfo2 = st.columns((1,1))
        with perinfo1:
            credential = st.text_input('Credential')
            name = st.text_input('Name')
            email = st.text_input("E-mail")
            city = st.radio("Select the city to assess",
                            ["Donostia", "Sevilla", "Valencia"],
                            horizontal=True,index=None)
        with perinfo2:
            professionalRole = st.text_input("Professional Role")
            yearsOfExperience = st.number_input("Years of Experience", value = 0)
            mainChallenges = st.text_input('Main Challenges (Separated by commas)')
            password = st.text_input("Password")
        
        ## Combining the data for the user_info table
        table_user_info = "answers.user_info"
        row_to_insert_user_info = [{"name": name,
                        "email": email,
                        "city": city,
                        "professional_role": professionalRole,
                        "years_of_experience": yearsOfExperience,
                        "main_challenges": mainChallenges,
                        "password": password}]  

        signup_button = st.button("Create your account")
        if signup_button:
            df_answers = pd.DataFrame
            st.session_state.questionnaire_sign = True
            revaluationPeriod = "0"
            revaluationPeriodsign = False
            open_questionnaire = True
            if name!=None:
                if credential != "0000":
                    st.warning("Your credential is not correct, please insert the correct credential")
                elif name == "":
                    st.warning("Your name is empty")
                elif email == "":
                    st.warning("Your email is empty")
                elif city == "":
                    st.warning("Your city is empty")
                elif professionalRole == "":
                    st.warning("Your professional role is empty")
                elif yearsOfExperience == "":
                    st.warning("Your year of experience is empty")
                elif mainChallenges == "":
                    st.warning("Your main challenges is empty")
                elif password == "":
                    st.warning("Your password is empty")
                else:
                    errors_user = client.insert_rows_json(table_user_info, row_to_insert_user_info)  # Make an API request.
                    if errors_user == []:
                        st.success('Your account was created was submitted!', icon="✅")
                    else:
                        print("Encountered errors while inserting rows: {}".format(errors_user))


    # LogIn form
    if st.session_state.account == False:
        # Login submit button state
        if 'login' not in st.session_state:
            st.session_state.login = 0

        # Email, password and login button
        email = st.text_input("E-mail", None)
        # Include password in the database
        password = st.text_input("Password", None)
        check_login = st.button('Log in  ')
        if check_login:
            st.session_state.login += 1
            st.session_state.questionnaire_sign = True

        # Extracting info from the database
        if st.session_state.login > 0:
            if email == "":
                st.warning("Please insert the email and password")
            else:
                rows = run_query("SELECT * FROM `answers.user_info`")
                df_bigquery = pd.DataFrame(rows)    
                df_user = df_bigquery.loc[df_bigquery['email'] == email]
                st.session_state.login = 1
                if df_user.empty:
                    st.warning("Incorrect email or password")
                else:    
                    id = df_user.index.tolist()
                    id = id[0]
                    credential = "0000"
                    name = df_user['name'][id]
                    email = df_user['email'][id]
                    city = df_user['city'][id]
                    professionalRole = df_user['professional_role'][id]
                    yearsOfExperience = df_user['years_of_experience'][id]
                    mainChallenges = df_user['main_challenges'][id]
                    revaluationPeriodsign = True
                    open_questionnaire = True

# Questionnaire
if st.session_state.questionnaire_sign == True:
    with st.expander('Questionnaire'):
        # Extracting the answered options and selecting the revaluation period
        if revaluationPeriodsign == True:
            rows = run_query("SELECT * FROM `answers.answers`")
            df_bigquery_answers = pd.DataFrame(rows)
            df_answers = df_bigquery_answers.loc[df_bigquery_answers['email'] == email].reset_index()
            df_answers['revaluation_period'] = df_answers['revaluation_period'].astype(str).astype(int)
            max_period = (df_answers['revaluation_period'].max())
            st.write("Your current period of analysis is: ", max_period, "months")
            df_answers = df_answers.loc[df_answers['revaluation_period'] == max_period].reset_index()
            
            whichRound = st.select_slider('What is the current revaluation period for this city?', options=['6 months', '12 months', '18 months', '24 months'])
            match whichRound:
                    case "6 months": revaluationPeriod = "6"
                    case "12 months": revaluationPeriod = "12"
                    case "18 months": revaluationPeriod = "18"
                    case "24 months": revaluationPeriod = "24"
                    case _: print("error")
        else:
            revaluationPeriod = 0

        leadership, urbandev, environmental = st.tabs(["Leadership", 'Urban Development', 'Environmental'])

        with leadership:
            L1, L2, L3, L4 = st.tabs(["Leadership Part 1", 'Leadership Part 2', 'Leadership Part 3', "Leadership Part 4"])
            
            with L1:
                L1Q1 = st.radio("What type of structure has the city got to govern resilience?", questionsnanswers['L1Q1'], index=returnanswers('L1Q1', revaluationPeriod))
                L1Q1 = check_null_answers(L1Q1, questionsnanswers['L1Q1'])

                L1Q2 = st.radio( "Has the municipality developed a RAP?", questionsnanswers["L1Q2"], index=returnanswers('L1Q2',revaluationPeriod))
                L1Q2 = check_null_answers(L1Q2, questionsnanswers['L1Q2'])

                L1Q3 = st.radio("Is the resilience action plan (RAP) integrated with other plans/strategies?", questionsnanswers["L1Q3"], index=returnanswers('L1Q3',revaluationPeriod))
                L1Q3 = check_null_answers(L1Q3, questionsnanswers['L1Q3'])
                
                L1Q4 = st.radio("Does the city promote access to basic services for vulnerable groups?", questionsnanswers["L1Q4"], index=returnanswers('L1Q4',revaluationPeriod))
                L1Q4 = check_null_answers(L1Q4, questionsnanswers['L1Q4'])

                L1Q5 = st.radio("Does the city support other cities in the development of resilience plans?",questionsnanswers["L1Q5"], index=returnanswers('L1Q5',revaluationPeriod))
                L1Q5 = check_null_answers(L1Q5, questionsnanswers['L1Q5'])

            with L2:
                L2Q1 = st.radio("Have the resilience processes/procedures adopted any standards?", questionsnanswers["L2Q1"], index=returnanswers('L2Q1',revaluationPeriod))
                L2Q1 = check_null_answers(L2Q1, questionsnanswers['L2Q1'])
                
                L2Q2 = st.radio("Is the resilience process submitted to any certification bodies to ensure conromity", questionsnanswers["L2Q2"], index=returnanswers('L2Q2',revaluationPeriod))
                L2Q2 = check_null_answers(L2Q2, questionsnanswers['L2Q2'])

            with L3:
                L3Q1 = st.radio("To what extent is the resilience culture* developed in the city? *A resilience culture enables the organization to anticipate, prepare for, adapt to any disruption and emerge stroger.", questionsnanswers["L3Q1"], index=returnanswers('L3Q1',revaluationPeriod))
                L3Q1 = check_null_answers(L3Q1, questionsnanswers['L3Q1'])

                L3Q2 = st.radio("To what extent are past events analysed to extract lessons learned?", questionsnanswers["L3Q2"], index=returnanswers('L3Q2',revaluationPeriod))
                L3Q2 = check_null_answers(L3Q2, questionsnanswers['L3Q2'])

                L3Q3 = st.radio("There is no knowledge sharing with other cities.", questionsnanswers["L3Q3"], index=returnanswers('L3Q3',revaluationPeriod))
                L3Q3 = check_null_answers(L3Q3, questionsnanswers['L3Q3'])

                L3Q4 = st.radio("How is the learning process from past events?", questionsnanswers["L3Q4"], index=returnanswers('L3Q4',revaluationPeriod))
                L3Q4 = check_null_answers(L3Q4, questionsnanswers['L3Q4'])

                L3Q5 = st.radio("Are there formal actions or procedures (meetings, committees) to assess the effectiveness of the learning process?", questionsnanswers["L3Q5"], index=returnanswers('L3Q5',revaluationPeriod))
                L3Q5 = check_null_answers(L3Q5, questionsnanswers['L3Q5'])

            with L4:
                L4Q1 = st.radio("Which is the level of development of the disaster response plan*? *A disaster emergency response plan, or disaster response plan, is a written policy accompanied by procedures that defines the response activities to minimize damage resulting from disasters (man-made or natural)", questionsnanswers["L4Q1"], index=returnanswers('L4Q1',revaluationPeriod))
                L4Q1 = check_null_answers(L4Q1, questionsnanswers['L4Q1'])

                L4Q2 = st.radio("To what extent is the RAP developed?", questionsnanswers["L4Q2"], index=returnanswers('L4Q2',revaluationPeriod))
                L4Q2 = check_null_answers(L4Q2, questionsnanswers['L4Q2'])

                L4Q3 = st.radio("Which group of stakeholders collaborate in the RAP development?", questionsnanswers["L4Q3"], index=returnanswers('L4Q3',revaluationPeriod))
                L4Q3 = check_null_answers(L4Q3, questionsnanswers['L4Q3'])

                L4Q4 = st.radio("What types of events are addressed in the RAP?", questionsnanswers["L4Q4"], index=returnanswers('L4Q4',revaluationPeriod))
                L4Q4 = check_null_answers(L4Q4, questionsnanswers['L4Q4'])

                L4Q5 = st.radio("Does the RAP address Climate Change perspective?", questionsnanswers["L4Q5"], index=returnanswers('L4Q5',revaluationPeriod))
                L4Q5 = check_null_answers(L4Q5, questionsnanswers['L4Q5'])

                L4Q6 = st.radio("Is the resilience perspective adopted and integrated into other key city functions?", questionsnanswers["L4Q6"], index=returnanswers('L4Q6',revaluationPeriod))
                L4Q6 = check_null_answers(L4Q6, questionsnanswers['L4Q6'])

                L4Q7 = st.radio("Does the city collaborate with other cities and external bodies?", questionsnanswers["L4Q7"], index=returnanswers('L4Q7',revaluationPeriod))
                L4Q7 = check_null_answers(L4Q7, questionsnanswers['L4Q7'])

        with urbandev:
            U1Q1 = st.radio("Are the climate adaptation measures identified in urban planning?", questionsnanswers["U1Q1"], index=returnanswers('U1Q1',revaluationPeriod))
            U1Q1 = check_null_answers(U1Q1, questionsnanswers['U1Q1'])

            U1Q2 = st.radio("Are the climate adaptation measures identified in urban development?", questionsnanswers["U1Q2"], index=returnanswers('U1Q2',revaluationPeriod))
            U1Q2 = check_null_answers(U1Q2, questionsnanswers['U1Q2'])
            
            U1Q3 = st.radio("Has the city developed and/or implemented Plan for Climate Change Actions (PACES) to favor implementing measures for climate change adaptation?", questionsnanswers["U1Q3"], index=returnanswers('U1Q3',revaluationPeriod))
            U1Q3 = check_null_answers(U1Q3, questionsnanswers['U1Q3'])
            
            U1Q4 = st.radio("Does your city monitor and evaluate the effectiveness of already implemented climate change adaptation measures?", questionsnanswers["U1Q4"], index=returnanswers('U1Q4',revaluationPeriod))
            U1Q4 = check_null_answers(U1Q4, questionsnanswers['U1Q4'])
            
            U1Q5 = st.radio("Does your city identify potential Nature-Based solutions (NBS) for improving urban resilience?", questionsnanswers["U1Q5"], index=returnanswers('U1Q5',revaluationPeriod))
            U1Q5 = check_null_answers(U1Q5, questionsnanswers['U1Q5'])
            
            U1Q6 = st.radio("Does your city implement Nature-Based solutions (NBS) for improving urban resilience?", questionsnanswers["U1Q6"], index=returnanswers('U1Q6',revaluationPeriod))
            U1Q6 = check_null_answers(U1Q6, questionsnanswers['U1Q6'])    
            
            U1Q7 = st.radio("What type of climate information is provided to supportinformed decision-making? Mark all that apply.", questionsnanswers["U1Q7"], index=returnanswers('U1Q7',revaluationPeriod))
            U1Q7 = check_null_answers(U1Q7, questionsnanswers['U1Q7'])    
            
            U1Q8 = st.radio("Are there appropriate regulations and standards for sustainable and resilient urban planning?", questionsnanswers["U1Q8"], index=returnanswers('U1Q8',revaluationPeriod))
            U1Q8 = check_null_answers(U1Q8, questionsnanswers['U1Q8'])    
            
            U1Q9 = st.radio("Are there guidelines for sustainable and resilient urban planning?", questionsnanswers["U1Q9"], index=returnanswers('U1Q9',revaluationPeriod))
            U1Q9 = check_null_answers(U1Q9, questionsnanswers['U1Q9'])    
            
            U1Q10 = st.radio("Does the city implement sustainable design principles and risk reduction measures in new buildings and rehabilitation of buildings?", questionsnanswers["U1Q10"], index=returnanswers('U1Q10',revaluationPeriod))
            U1Q10 = check_null_answers(U1Q10, questionsnanswers['U1Q10'])

            U1Q11 = st.radio("Does the cityimplement sustainable principles when designing the urban mobility and public services?", questionsnanswers["U1Q11"], index=returnanswers('U1Q11',revaluationPeriod))
            U1Q11 = check_null_answers(U1Q11, questionsnanswers['U1Q11'])

        with environmental:

            E1Q1 = st.radio("Is there any assessment of the ecosystem and the biodiversity over time? How broad is the assessment?", questionsnanswers["E1Q1"], index=returnanswers('E1Q1',revaluationPeriod))
            E1Q1 = check_null_answers(E1Q1, questionsnanswers['E1Q1'])
        
            E1Q2 = st.radio("Does the city provide information about the role of ecosystems in disaster resilience?", questionsnanswers["E1Q2"], index=returnanswers('E1Q2',revaluationPeriod))
            E1Q2 = check_null_answers(E1Q2, questionsnanswers['E1Q2'])    

            E1Q3 = st.radio("Are there agreements and collaborations with border cities to develop and promote joint actions on transboundary ecosystems?", questionsnanswers["E1Q3"], index=returnanswers('E1Q3',revaluationPeriod))
            E1Q3 = check_null_answers(E1Q3, questionsnanswers['E1Q3'])   

            E1Q4 = st.radio("Does the city protect or enhance important ecosystems?", questionsnanswers["E1Q4"], index=returnanswers('E1Q4',revaluationPeriod))
            E1Q4 = check_null_answers(E1Q4, questionsnanswers['E1Q4'])   

            E1Q5 = st.radio("Are there any mitigation targets for GHG reduction?", questionsnanswers["E1Q5"], index=returnanswers('E1Q5',revaluationPeriod))
            E1Q5 = check_null_answers(E1Q5, questionsnanswers['E1Q5'])    

            E1Q6 = st.radio("Has the city developed and/or implemented Plan for Climate Change Actions (PACES) to favor implementing actions for climate change mitigation?", questionsnanswers["E1Q6"], index=returnanswers('E1Q6',revaluationPeriod))
            E1Q6 = check_null_answers(E1Q6, questionsnanswers['E1Q6'])    

            E1Q7 = st.radio("Which of these measures has the city implemented for climate change mitigation? (Awareness campaigns to reduce energy consumption)", questionsnanswers["E1Q7"], index=returnanswers('E1Q7',revaluationPeriod))
            E1Q7 = check_null_answers(E1Q7, questionsnanswers['E1Q7'])    

            E1Q8 = st.radio("Which of these measures has the city implemented for climate change mitigation? (Promotion of renewable energies)", questionsnanswers["E1Q8"], index=returnanswers('E1Q8',revaluationPeriod))
            E1Q8 = check_null_answers(E1Q8, questionsnanswers['E1Q8'])   

            E1Q9 = st.radio("Which of these measures has the city implemented for climate change mitigation? (Promotion of sustainable transport (i.e. electric cars, public transport, bikes…,revaluationPeriod))", questionsnanswers["E1Q9"], index=returnanswers('E1Q9',revaluationPeriod))
            E1Q9 = check_null_answers(E1Q9, questionsnanswers['E1Q9']) 

            E1Q10 = st.radio("Which of these measures has the city implemented for climate change mitigation? (Promotion of climate change awareness campaigns)", questionsnanswers["E1Q10"], index=returnanswers('E1Q10',revaluationPeriod))
            E1Q10= check_null_answers(E1Q10, questionsnanswers['E1Q10'])    

            E1Q11 = st.radio("Does your city monitor and evaluate the effectiveness of already implemented climate change mitigation measures? Promotion of sustainable transport (i.e. electric cars, public transport, bikes…)", questionsnanswers["E1Q11"], index=returnanswers('E1Q11',revaluationPeriod))
            E1Q11 = check_null_answers(E1Q11, questionsnanswers['E1Q11'])    


    ## Combining the data for the answer_table
    table_answers = "answers.answers"
    row_to_insert_answers =[{"email":email, "city":city, 
                            "L1Q1":L1Q1,"L1Q2":L1Q2,"L1Q3":L1Q3,"L1Q4":L1Q4,"L1Q5":L1Q5,
                            "L2Q1":L2Q1,"L2Q2":L2Q2,
                            "L3Q1":L3Q1,"L3Q2":L3Q2,"L3Q3":L3Q3,"L3Q4":L3Q4,"L3Q5":L3Q5,
                            "L4Q1":L4Q1,"L4Q2":L4Q2,"L4Q3":L4Q3,"L4Q4":L4Q4,"L4Q5":L4Q5, "L4Q6":L4Q6, "L4Q7":L4Q7,
                            "U1Q1":U1Q1,"U1Q2":U1Q2,"U1Q3":U1Q3,"U1Q4":U1Q4,"U1Q5":U1Q5,"U1Q6":U1Q6,"U1Q7":U1Q7,"U1Q8":U1Q8,"U1Q9":U1Q9,"U1Q10":U1Q10,"U1Q11":U1Q11,
                            "E1Q1":E1Q1,"E1Q2":E1Q2,"E1Q3":E1Q3,"E1Q4":E1Q4,"E1Q5":E1Q5,"E1Q6":E1Q6,"E1Q7":E1Q7,"E1Q8":E1Q8,"E1Q9":E1Q9,"E1Q10":E1Q10,"E1Q11":E1Q11,
                            "revaluation_period": revaluationPeriod
                            }]

    if st.button('Submit Questionnaire', key='but_c', disabled=st.session_state.get("disabled", False)):
        errors = client.insert_rows_json(table_answers, row_to_insert_answers)
        if errors == []:
            progress_text = "Questionnaire submission in progress. Please wait."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(1)
            my_bar.empty()
            st.success('Your questionnaire was submitted!', icon="✅")
        else:
            print("Encountered errors while inserting rows: {}".format(errors))