from langchain import LLMChain, PromptTemplate
from langchain.utilities import GoogleSerperAPIWrapper
from langchain.memory import ConversationBufferWindowMemory
from langchain.llms import AzureOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.chat_models import AzureChatOpenAI

# get a chat LLM chain, following a prompt template
def query_chain():
    # create prompt from a template
    template = open('bob_template', 'r').read()
    prompt = PromptTemplate(
        input_variables=["input"],         
        template=template
    )    
    # create a LLM chain with conversation buffer memory
    return LLMChain(
        llm=AzureOpenAI(model_name="gpt-4", engine="gpt-4"),
        prompt=prompt, 
        verbose=True, 
        memory=ConversationBufferWindowMemory(k=10),
    )        

# call Serper Google Search API
def search_agent():
    # set up the tool    
    search = GoogleSerperAPIWrapper()
    tools = [ Tool(name = "Intermediate Answer", func=search.run, description="search")]
    llm = AzureChatOpenAI(model_name="gpt-4", deployment_name="gpt-4")
    # create and return the chat agent
    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.SELF_ASK_WITH_SEARCH,
        verbose=True,
        memory=ConversationBufferWindowMemory(k=10),
    )   