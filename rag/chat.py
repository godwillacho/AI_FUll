from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
import os 

load_dotenv()
def Run_command( cmd: str):
    result = os.system(cmd)
    return result
client = OpenAI()
available_tools = {
    "run_command" : Run_command  
}
embedding_model = OpenAIEmbeddings(
    model = "text-embedding-3-large"
)

vector_db = QdrantVectorStore.from_existing_collection(
     url = "http://localhost:6333",
     collection_name = "learning_rag",
     embedding = embedding_model ,
)
while True:
    user_query = input("What can i help you with 🔠:")

    search_results = vector_db.similarity_search(query = user_query)

    context = "\n\n\n".join([
        f"""Page Content: {result.page_content} \n 
        page Number :{result.metadata['page_label']} \n 
        File Location : {result.metadata['source']}"""
        for result in search_results                        
    ])

    Systemprompt = f"""

    -YOU ARE HELPING STUDENTS PREPARE FOR COMPTIA SECURITY+  EXAM  BASED ON THE AVAILABLE CONTEXT RETRIEVED FROMA PDF FILE ALONG WITH page_contents and page number.
    -YOU SHOULD ONLY ANSWER THE USER BASED ON THE FOLLOWING CONTEXT AND NAVIGATE THE USER TO OPEN THE RIGHT PAGE NUMBER TO KNOW MORE.
    -YOU CAN ALSO PROVIDE QUESTIONS BASED ON THE CONTEXT WHICH CAN HELP THE USER ASSIMILATE MORE KNOWLEDGE 
    -YOU ARE also able to improove the quality of your output by openning the pdf file that was passed in the first place on the user computer 
    -The Pages that are Opened should only be the relevant pages to the querry 
    -To open this QUerry Make use of the tools in the available tools to help user interact with this pages if the precise on needing more info 

    Available Tools:
    -Run-command(cmd: str) : takes a system linux command as string and executes the command on users system and return the output from the command 


    Context:
    {context}
    """
    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {
                "role" : "system" , "content": Systemprompt
            },
            {

                "role" : "user" , "content": user_query 
            },
        ]
    )
    print(f"🤖 {response.choices[0].message.content}")
