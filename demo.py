from deepsearcher.configuration import Configuration, init_config
from deepsearcher.online_query import query

config = Configuration()

# Customize your config here,
# more configuration see the Configuration Details section below.
##config.set_provider_config("llm", "OpenAI", {"model": "gpt-4o-mini"})
init_config(config = config)

# Load your local data
from deepsearcher.offline_loading import load_from_local_files

# 用实际路径替换下面的字符串
local_data_path = "/Users/ericzhou/MyStudio/KnowledgeBase"
load_from_local_files(paths_or_directory=local_data_path)

# (Optional) Load from web crawling (`FIRECRAWL_API_KEY` env variable required)
from deepsearcher.offline_loading import load_from_website
#website_url = "https://www.google.com"  # 将此 URL 替换为你实际需要爬取的网址
#load_from_website(urls=website_url)

# Query
result = query("Write a indepth report about Rebecca T. Pinkus‘s reserch, opinions, and thoughts over 'close relationships.' from her papercollections in my 'KnowledgeBase' folder that i present you") # Your question here