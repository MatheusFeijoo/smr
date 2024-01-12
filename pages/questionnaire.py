import streamlit as st

st.title("Questionnaire")

with st.expander("Personal Information"):
    name = st.text_input('Name')
    email = st.text_input("E-mail")
    city = st.radio(
            "Select the city to assess",
            ["Donostia", "Sevilla", "Valencia"],
            horizontal=True)
    professionalRole = st.text_input("Professional Role")
    yearsOfExperience = st.text_input("Years of Experience")
    mainChallenges = st.text_input('Main Challenges')

tab1, tab2, tab3 = st.tabs(["Leadership", 'Urban Development', 'Environmental'])

with tab1:
    L1, L2, L3, L4 = st.tabs(["Leadership Part 1", 'Leadership Part 2', 'Leadership Part 3', "Leadership Part 4"])
    
    with L1:
        L1Q1 = st.radio(
            "What type of structure has the city got to govern resilience?",
            ["There is not any organisational structure", "There is an informal organisational structure (a working group) in charge of resilience issues", "There is a formal organisational structure (department or committee)", "There is a permanent organisational structure that coordinates at municipal, regional and national levels"])
        L1Q2 = st.radio(
            "Has the municipality developed a RAP?",
            ["No", "No, but the city has already identified its requirements", "Yes, the city has partially developed a RAP.", "Yes, the city has already developed a RAP"])
        L1Q3 = st.radio(
            "Is the resilience action plan (RAP) integrated with other plans/strategies?",
            ["Integrated with the city plans.", "Integrated with the city and regional plans", "Integrated with the city, regional and national plans", "Integrated with the city, regional, national and international plans"])
        L1Q4 = st.radio(
            "Does the city promote access to basic services for vulnerable groups?",
            ["No", "Partially", "In most cases", "Totally"])
        L1Q5 = st.radio(
            "Does the city support other cities in the development of resilience plans?",
            ["No", "At a regional level only", "At regional and national levels", "At regional, national and international levels"])

    with L2:
        L2Q1 = st.radio(
            "Have the resilience processes/procedures adopted any standards?",
            ["None, mostly intuitive.", "Aligned with regional standards.", "Aligned with national standards.", "Aligned with international standards.", "Contribute to the development of standards."])
        L2Q2 = st.radio(
            "Is the resilience process submitted to any certification bodies to ensure conromity",
            ["None, mostly intuitive.", "Comparison with Regional processes.", "Certified nationally", "Certified internationally.", "Taken as a certification baseline."])

    with L3:
        L3Q1 = st.radio(
            "To what extent is the resilience culture* developed in the city? *A resilience culture enables the organization to anticipate, prepare for, adapt to any disruption and emerge stroger.",
            ["The resilience approach/culture is not being developed.", "The city has developed a strategy to develop a resilience culture.", "The strategy to develop a resilience culture is being partially implemented.", "The strategy to develop a resilience culture is being totally implemented."])
        L3Q2 = st.radio(
            "To what extent are past events analysed to extract lessons learned?",
            ["The past event analysis relies on individuals. There is no a systematic procedure.", "The past event analysis is carried out without having a systematic procedure. Some lessons learned are partially included in some plans", "The past event analysis is carried through a systematic procedure. Lessons learned are included in the majority of plans.", "The past event analysis is carried through an effective and systematic procedure. Plans are reviewed continuously to include lessons learned."])
        L3Q3 = st.radio(
            "There is no knowledge sharing with other cities.",
            ["There is no knowledge sharing with other cities.", "Knowledge is shared with close cities located in the same region.", "Knowledge is shared at the national or international level.", "Knowledge is shared at the national and international level."])
        L3Q4 = st.radio(
            "How is the learning process from past events?",
            ["The learning process is informal.", "The learning process is formalised.", "The learning process is systematic.", "The learning process is systematic and supported by an active network of stakeholders."])
        L3Q5 = st.radio(
            "Are there formal actions or procedures (meetings, committees) to assess the effectiveness of the learning process?",
            ["There are no procedures/actions to assess the effectiveness of the learning process.", "There are some informal procedures/action s to assess the effectiveness of the learning process, but they are applied to only a few departments", "There are some procedures/actions to assess the effectiveness of the learning process but not applied in all the municipal departments", "There are formal procedures/actions to assess the effectiveness of the learning process applied in all the municipal departments."])
            
    with L4:
        L4Q1 = st.radio(
            "Which is the level of development of the disaster response plan*? *A disaster emergency response plan, or disaster response plan, is a written policy accompanied by procedures that defines the response activities to minimize damage resulting from disasters (man-made or natural)",
            ["The disaster response plan is not developed.", "The disaster response plan is not developed but there are some resources assigned to develop the plan", "The disaster response plan is partially developed but still non- operational.", "The disaster response plan is completely developed and is operational."])
        L4Q2 = st.radio(
            "To what extent is the RAP developed?",
            ["The development of RAP is under development.", "The RAP has been developed and is operational.", "RAP is developed and periodically monitored and assessed through indicators.", "RAP is continuously improved."])
        L4Q3 = st.radio(
            "Which group of stakeholders collaborate in the RAP development?",
            ["Emergency Services (ES) only.", "Emergency Services plus NGOs, Public and Private companies.", "Level 2 plus Volunteer Organizations and/or citizens.", "Level 3 plus Academic and scientific organisations."])
        L4Q4 = st.radio(
            "What types of events are addressed in the RAP?",
            ["Shocks.", "Most common shocks and chronic stresses.", "A wide range of shocks and chronic stresses.", "Shocks and chronic stresses, and unpredictable situations."])
        L4Q5 = st.radio(
            "Does the RAP address Climate Change perspective?",
            ["No", "Partially. RAP is mainly focused on mitigation actions but not on adaption actions.", "RAP defines mitigation and some incipient adaptation measures.", "RAP defines mitigation and ambitious adaptation measures using a resilience approach, that allows cities/municipalities to adapt to changing conditions."])
        L4Q6 = st.radio(
            "Is the resilience perspective adopted and integrated into other key city functions?",
            ["No", "The requirements to adopt a resilience perspective are identified.", "Partially integrated with many city key functions.", "Fully integrated with all city key functions."])
        L4Q7 = st.radio(
            "Does the city collaborate with other cities and external bodies?",
            ["No", "Yes, with other cities at the regional level.", "Yes, with other cities at regional and national levels.", "Yes, all the previous and with other cities at the international level."])

with tab2:
    U1Q1 = st.radio(
        "Are the climate adaptation measures identified in urban planning?",
        ["No", "They are identified but not implemented", "They are identified and implemented", "They are identified, implemented, and evaluated"])
    U1Q2 = st.radio(
        "Are the climate adaptation measures identified in urban development?",
        ["No", "They are identified but not implemented", "They are identified and implemented", "They are identified, implemented, and evaluated"])
    U1Q3 = st.radio(
        "Has the city developed and/or implemented Plan for Climate Change Actions (PACES) to favor implementing measures for climate change adaptation?",
        ["No, the city does not develop a plan neither implement adaptation measures.", "Yes, the city develops a plan but just some climate change adaptation measures are implemented.", "Yes, the city develops a plan and implements climate change adaptation measures.", "Yes, the city develops a plan and implements climate change adaptation measures and are aligned with risk reduction measures."])
    U1Q4 = st.radio(
        "Does your city monitor and evaluate the effectiveness of already implemented climate change adaptation measures?",
        ["The city does not monitor and evaluate the implemented climate adaptation measures.", "The city monitors the already implemented climate change adaptation measures but it does not evaluate their effectiveness.", "They city monitors the already implemented climate change adaptation measures and partially evaluate their effectiveness.", "They city monitors and evaluates the effectiveness of the already implemented climate change adaptation measures."])
    U1Q5 = st.radio(
        "Does your city identify potential Nature-Based solutions (NBS) for improving urban resilience?",
        ["No, the city does not identify potential NBS.", "Partially, the city identifies some potential NBS.", "Yes, the city identifies potential NBS but it does not conduct any evaluation of their co- benefits", "Yes, the city identifies potential NBS and it conducts an evaluation of their co- benefits."])
    U1Q6 = st.radio(
        "Does your city implement Nature-Based solutions (NBS) for improving urban resilience?",
        ["No, the city does not implement NBS.", "The city sometimes implements NBSs but it is not universal and it is not supported.", "The city implements NBSs but there is little supporting guidance for their implementation", "The city implements NBSs and it has a supporting guidance to do so."])
    U1Q7 = st.radio(
        "What type of climate information is provided to supportinformed decision-making? Mark all that apply.",
        ["No climate data is provided.", "Past data - Historical information about climate.", "Present climate data - Observations, monitoring, reports or studies to describe climate variability.", "Future climate data such as forecasts and projections."])
    U1Q8 = st.radio(
        "Are there appropriate regulations and standards for sustainable and resilient urban planning?",
        ["There are no regulations or standards for sustainable and resilient urban planning.", "There are some recommended standards for sustainable and resilient urban planning; however, they are hardly used.", "There are proper regulations and standards for sustainable and resilient urban planning, and it is mandatory to fulfil them.", "There are constantly updated regulations and standards for sustainable and resilient urban planning, and it is mandatory to fulfil them."])
    U1Q9 = st.radio(
        "Are there guidelines for sustainable and resilient urban planning?",
        ["No", "There are documents that collect information on sustainable design principles for sustainable urban planning and best practices and provide recommendations.", "There are some guidelines on how to develop sustainable and resilient urban planning.", "There are complete guidelines on how to develop sustainable and resilient urban planning."])
    U1Q10 = st.radio(
        "Does the city implement sustainable design principles and risk reduction measures in new buildings and rehabilitation of buildings?",
        ["The city does not implement sustainable principles.", "Partially, some sustainable principles and risk reduction measures are implemented in new buildings, but they are not included in the rehabilitation of the existing ones.", "Sustainable principles and risk reduction measures are included in the new buildings, but only some measures are included in the rehabilitation of the existing ones.", "Sustainable principles and risk reduction measures are included in both the new buildings and the rehabilitation of the existing ones."])
    U1Q11 = st.radio(
        "Does the cityimplement sustainable principles when designing the urban mobility and public services?",
        ["The city does not implement sustainable principles.", "Partially, the city takes into account the sustainable principles when designing the urban mobility and public services but many times they are not implemented.", "The city takes into account sustainable principles when designing urban mobility and public services and most of the times are implemented.", "The city implements and integrates sustainable principles when designing and developing urban mobility and public services."])

with tab3:

    E1Q1 = st.radio(
        "Is there any assessment of the ecosystem and the biodiversity over time? How broad is the assessment?",
        ["No, but the important ecosystems are identified.", "YES, but it is very superficial and eventual.", "YES, it covers all ecosystems, but it is sporadically done", "YES, it covers all ecosystems and is frequently done (at least once a year)."])
    E1Q2 = st.radio(
        "Does the city provide information about the role of ecosystems in disaster resilience?",
        ["No, the city does not provide any information.", "Yes, but the city provides limited information.", "Yes, the city provides some information.", "Yes, the city provides complete information."])
    E1Q3 = st.radio(
        "Are there agreements and collaborations with border cities to develop and promote joint actions on transboundary ecosystems?",
        ["Not implemented.", "Partially implemented.", "Highly implemented", "Fully Implemented."])
    E1Q4 = st.radio(
        "Does the city protect or enhance important ecosystems?",
        ["No", "Yes, but only in green areas.", "Yes, in green areas and peri-urban areas", "Yes, in all areas (urban areas, peri-urban areas and green areas)"])
    E1Q5 = st.radio(
        "Are there any mitigation targets for GHG reduction?",
        ["No", "Yes, but very general.", "Yes, somehow specific.", "Yes, very specific."])
    E1Q6 = st.radio(
        "Has the city developed and/or implemented Plan for Climate Change Actions (PACES) to favor implementing actions for climate change mitigation?",
        ["No, neither developed nor implemented.", "Partially Implemented.", "Highly implemented.", "Fully Implemented."])
    E1Q7 = st.radio(
        "Which of these measures has the city implemented for climate change mitigation? (Awareness campaigns to reduce energy consumption)",
        ["Not implemented.", "Partially implemented.", "Highly implemented", "Fully Implemented."])
    E1Q8 = st.radio(
        "Which of these measures has the city implemented for climate change mitigation? (Promotion of renewable energies)",
        ["Not implemented.", "Partially implemented.", "Highly implemented", "Fully Implemented."])
    E1Q9 = st.radio(
        "Which of these measures has the city implemented for climate change mitigation? (Promotion of sustainable transport (i.e. electric cars, public transport, bikes…))",
        ["Not implemented.", "Partially implemented.", "Highly implemented", "Fully Implemented."])
    E1Q10 = st.radio(
        "Which of these measures has the city implemented for climate change mitigation? (Promotion of climate change awareness campaigns)",
        ["Not implemented.", "Partially implemented.", "Highly implemented", "Fully Implemented."])
    E1Q11 = st.radio(
        "Does your city monitor and evaluate the effectiveness of already implemented climate change mitigation measures? Promotion of sustainable transport (i.e. electric cars, public transport, bikes…)",
        ["The city does not monitor and evaluate the implemented climate mitigation measures.", "The city monitors the already implemented climate change mitigation measures but it does not evaluate their effectiveness.", "They city monitors the already implemented climate change mitigation measures and partially evaluate their effectiveness.", "They city monitors and evaluates the effectiveness of the already implemented climate change mitigation measures."])
    

if st.button('Submit Questionnaire'):
   st.write('Done!')