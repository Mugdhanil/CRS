import streamlit as st


def main():
    # Set page title and favicon
    st.set_page_config(page_title="Content Recommendation System", page_icon="🚀")

    # Add a title and description
    st.title("Welcome to our Content Recommendation System")
    st.write("Discover personalized content tailored just for you!")

    # Add an image or logo
   # st.image("f13tech_cover.jpg", caption="Your Company Logo", use_column_width=True)

    # Add a brief introduction or mission statement
    st.markdown(
        """
        Our mission is to provide you with the best content recommendations 
        based on your interests and preferences. Whether you're interested 
        in Cloud, AI & Analytics, or Digital Commerce, we've got you covered!
        """
    )

    # Add a call-to-action button
    if st.button("Get Started"):
        st.write("Let's dive into the world of personalized content!")


if __name__ == "__main__":
    main()



# Create a sidebar
st.sidebar.title('Navigation')

# Define content options
content_options = [
    "Home",
    "Cloud",
    "Cyber Risk Advisory",
    "Digital Commerce",
    "Talent Resourcing & Management",
    "AI & Analytics",
    "Customer Communication Management",
    "Network Security Brand",
    "Communication & PR",
    "Process Consulting",
    "Sentiment Analysis & Opinion Mining",
    "Learning & Development",
    "Marketing, Sales Consulting & Strategy"
]

# Add options to the sidebar
option = st.sidebar.selectbox(
    'Select an option',
    content_options
)

# Display content based on selected option
if option == 'Home':
    st.title('Home Page')
    # Add content for the home page
    
elif option == 'Cloud':
    st.title('Cloud Page')
    # Add content for the Cloud page
    
elif option == 'Cyber Risk Advisory':
    st.title('Cyber Risk Advisory Page')
    # Add content for the Cyber Risk Advisory page
    
elif option == 'Digital Commerce':
    st.title('Digital Commerce Page')
    # Add content for the Digital Commerce page
    
elif option == 'Talent Resourcing & Management':
    st.title('Talent Resourcing & Management Page')
    # Add content for the Talent Resourcing & Management page
    
elif option == 'AI & Analytics':
    st.title('AI & Analytics Page')
    # Add content for the AI & Analytics page
    
elif option == 'Customer Communication Management':
    st.title('Customer Communication Management Page')
    # Add content for the Customer Communication Management page
    
elif option == 'Network Security Brand':
    st.title('Network Security Brand Page')
    # Add content for the Network Security Brand page
    
elif option == 'Communication & PR':
    st.title('Communication & PR Page')
    # Add content for the Communication & PR page
    
elif option == 'Process Consulting':
    st.title('Process Consulting Page')
    # Add content for the Process Consulting page
    
elif option == 'Sentiment Analysis & Opinion Mining':
    st.title('Sentiment Analysis & Opinion Mining Page')
    # Add content for the Sentiment Analysis & Opinion Mining page
    
elif option == 'Learning & Development':
    st.title('Learning & Development Page')
    # Add content for the Learning & Development page
    
elif option == 'Marketing, Sales Consulting & Strategy':
    st.title('Marketing, Sales Consulting & Strategy Page')
    # Add content for the Marketing, Sales Consulting & Strategy page





 # Add a section for selecting content topics
st.subheader("Select Your Interests")
content_topics = [
        "Cloud",
        "Cyber Risk Advisory",
        "Digital Commerce",
        "Talent Resourcing & Management",
        "AI & Analytics",
        "Customer Communication Management",
        "Network Security Brand",
        "Communication & PR",
        "Process Consulting",
        "Sentiment Analysis & Opinion Mining",
        "Learning & Development",
        "Marketing, Sales Consulting & Strategy"
    ]
selected_topics = st.multiselect("Choose topics you're interested in:", content_topics)

    # Show selected topics
if selected_topics:
        st.write("Selected topics:", selected_topics)

    # Add a call-to-action button
if st.button("Get Recommendations"):
        st.write("Fetching personalized recommendations based on your interests!")

# Sample content data with topics
content_data = {
    "Article 1": ["Cloud", "AI & Analytics"],
    "Article 2": ["Digital Commerce"],
    "Article 3": ["Learning & Development", "Process Consulting"],
    "Article 4": ["Marketing, Sales Consulting & Strategy"],
    "Article 5": ["Cloud", "AI & Analytics", "Process Consulting"]
}

def get_recommendations(selected_topics):
    recommendations = []
    for content, topics in content_data.items():
        if any(topic in topics for topic in selected_topics):
            recommendations.append(content)
    return recommendations

def main():
    # Set page title and favicon
    st.set_page_config(page_title="Content Recommendation System", page_icon="🚀")

    # Add a title and description
    st.title("Welcome to our Content Recommendation System")
    st.write("Discover personalized content tailored just for you!")

    # Add a section for selecting content topics
    st.subheader("Select Your Interests")
    content_topics = [
        "Cloud",
        "Cyber Risk Advisory",
        "Digital Commerce",
        "Talent Resourcing & Management",
        "AI & Analytics",
        "Customer Communication Management",
        "Network Security Brand",
        "Communication & PR",
        "Process Consulting",
        "Sentiment Analysis & Opinion Mining",
        "Learning & Development",
        "Marketing, Sales Consulting & Strategy"
    ]
    selected_topics = st.multiselect("Choose topics you're interested in:", content_topics)

    # Show selected topics
    if selected_topics:
        st.write("Selected topics:", selected_topics)

        # Fetch recommendations based on selected topics
        recommendations = get_recommendations(selected_topics)
        if recommendations:
            st.subheader("Personalized Recommendations")
            for recommendation in recommendations:
                st.write(recommendation)
        else:
            st.write("No recommendations found for the selected topics.")

    # Add a call-to-action button
    if st.button("Get Recommendations"):
        st.write("Fetching personalized recommendations based on your interests!")









#At the End

 # Add a section for selecting contact options       
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

    
