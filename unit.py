from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate



def generate_script(subject,video_length,creativity,api_key,api_base):
    title_template = ChatPromptTemplate.from_messages(
        [
            ("human","请为'{subject}'这个主题的视频想一个吸引人的标题")
        ]
    )
    script_template = ChatPromptTemplate.from_messages(
        [
            ("human",
             """你是一位短视频频道的博主。根据以下标题和相关信息，为短视频频道写一个视频脚本。
             视频标题:{title}，视频时长:{duration}分钟，生成的脚本的长度尽量遵循视频时长的要求。
             要求开头抓住限球，中间提供干货内容，结尾有惊喜，脚本格式也请按照[开头、中间，结尾]分隔。
             整体内容的表达方式要尽量轻松有趣，吸引年轻人。"""
             )
        ]
    )

    model=ChatOpenAI(openai_api_key=api_key,base_url=api_base,temperature=creativity,model="gpt-4o")
    title_chain=title_template | model
    script_chain=script_template | model

    title=title_chain.invoke({"subject":subject}).content


    script=script_chain.invoke({"title":title,"duration":video_length}).content

    return title,script

# print(generate_script("为什么支付宝上的基金一直亏",1,0.7,
      #          "sk-RDLwY6GavCOj6zhvxozaEfbcfpNgruq8sU3FG5eHMCJuJvGX","https://aigc789.top/v1"))