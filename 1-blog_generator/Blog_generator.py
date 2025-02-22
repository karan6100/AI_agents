from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import MessagesState, add_messages
from langchain_core.messages import AnyMessage, HumanMessage, SystemMessage
from langchain_groq import ChatGroq
### Langgraph creation
from langgraph.graph import START, END,StateGraph
from langgraph.prebuilt import tools_condition
from langgraph.prebuilt import ToolNode
from IPython.display import Image, display
import os
from dotenv import load_dotenv
load_dotenv()

#Importing API keys
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

#Defining the llm model
llm = ChatGroq(model = "qwen-2.5-32b", temperature = 0.7)
# llm

class MessagesState(TypedDict):
    #Defining the message state
    messages:Annotated[list[AnyMessage], add_messages]



def blog_generator():

    
    #Generate title using Title creator function
    def title_creator(state:MessagesState):
        """ Generates title from given input"""

        title_prompt = """ You are an expert blog title creator and you are taksed to create a catchy blog title from the user input.
                        Return the title following the below rules.
                        1. Maximum of 80 characters.
                        2. Includes keyword in the first 3 words. """
        title_sys_msg = SystemMessage(content=title_prompt)

        # return {"messages": llm.invoke( state['messages'] + [title_sys_msg])}
        # Invoke LLM with messages
        response = llm.invoke(state["messages"] + [title_sys_msg])
        return {"messages": state["messages"] + [response]}
    
    #Generate blog content using Blog Content creator function
    def blog_content(state:MessagesState):
        """Generates content for blog from given input """
        #System Messages for blog creation
        blog_creation_prompt = """You are an expert blog creator. Write a comprehensive blog post with 1500+ words based on the generated title.
                                Follow the structure as follows;
                                1. Structure with Markdown.
                                2. Title
                                3. Introduction
                                4. Main content and breakdown this into 3-6 points.
                                5. sub-section
                                6. Include examples, statistics if available.
                                7. conclusion 
                                """
        blog_sys_msg = SystemMessage(content=blog_creation_prompt)

        # return {"messages": [llm.invoke(state['messages'] + [blog_sys_msg])]}
        # Invoke LLM
        response = llm.invoke(state["messages"] + [blog_sys_msg])
        return {"messages": state["messages"] + [response]}  # Append to existing messages


        
    #Creating workflow
    builder = StateGraph(MessagesState)

    #defining nodes
    builder.add_node("blog_creator", blog_content)
    builder.add_node("title_creator", title_creator)

    #Defining edges
    builder.add_edge(START,"title_creator")
    builder.add_edge("title_creator", "blog_creator")
    builder.add_edge("blog_creator", END)

    graph = builder.compile()
    #Display the graph
    # display(Image(graph.get_graph().draw_mermaid_png()))

    # Save the graph image
    # Get image as binary data
    image_data = graph.get_graph().draw_mermaid_png()

    # Save the binary data as an image file
    image_path = "Assignments/1-blog_generator/blog_creator_workflow_graph.png"
    with open(image_path, "wb") as f:
        f.write(image_data)

    try:
        # Open the image using PIL
        img = Image.open(image_path)
        img.show()
    except AttributeError as e:
        # os.system("blog_creator_workflow_graph.png")
        os.system(f'start "" "{image_path}"')


    return graph
    

if __name__ == "__main__":

    #Intitalize the agent
    blog_agent = blog_generator()

    #Input 
    ip_keyword = "Maharbharat"

    #Initializing the initital state
    initial_state = {"messages":[HumanMessage(content =ip_keyword) ]}
    messages = blog_agent.invoke(initial_state)

    # for output in blog_agent.stream(initial_state):
        # for key, value in output.items():
            # print(f"Output from node: {key}")
            # print("------")
            # print(value['messages'][-1].content)
            # print("\n------\n")

    print("----------------------------------------------------------------------------------------")
    for m in messages['messages']:
        m.pretty_print()






