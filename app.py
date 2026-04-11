import streamlit as st
import boto3

# Configuration
KB_ID = "A0DOVE5XS4"
MODEL_ARN = "arn:aws:bedrock:us-east-1:934822761235:inference-profile/us.amazon.nova-2-lite-v1:0"

# Initialize the Bedrock Runtime client
client = boto3.client('bedrock-agent-runtime', region_name='us-east-1')

# Streamlit UI
st.set_page_config(page_title="Enterprise QA System", layout="centered")
st.title("Enterprise Knowledge Base Assistant")
st.markdown("Ask questions about your proprietary company documents.")
st.write("MODEL ARN:", MODEL_ARN)
st.write("KB ID:", KB_ID)
# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("What would you like to know?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            with st.spinner("Thinking... 🤔"):

                response = client.retrieve_and_generate(
                    input={'text': prompt},
                    retrieveAndGenerateConfiguration={
                        'type': 'KNOWLEDGE_BASE',
                        'knowledgeBaseConfiguration': {
                            'knowledgeBaseId': KB_ID,
                            'modelArn': MODEL_ARN,
                            'generationConfiguration': {
                                'promptTemplate': {
					"textPromptTemplate":"Answer the question based only on the following context:\n\n$search_results$\n\nQuestion: $query$\nAnswer:"
				 }
                            },
                           'orchestrationConfiguration':{
                               'promptTemplate': {
                                   'textPromptTemplate':"$conversation_history$\n\nUse the following context to answer the question:\n\n$search_results$\n\n$output_format_instructions$\n\nQuestion: $query$"
                                }
                            }
                        }
                    }
                )

            # Extract answer
            answer = response['output']['text']
            st.markdown(answer)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

            # Show citations
            if response.get('citations'):
                with st.expander("View Source Citations"):
                    for citation in response['citations']:
                        for reference in citation.get('retrievedReferences', []):
                            st.write(f"**Source:** {reference['location']['s3Location']['uri']}")
                            st.write(f"**Excerpt:** {reference['content']['text']}")

        except Exception as e:
            st.error(f"Error: {str(e)}")
