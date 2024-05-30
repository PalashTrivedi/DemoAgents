# import autogen
# from autogen.agentchat import AssistantAgent, UserProxyAgent
# import streamlit as st
# import asyncio
# # from SalesAgent import MathUserProxyAgent
# import pprint
#
#
#
#
# # setup page title and description
# st.set_page_config(page_title="AutoGen Chat app", page_icon="🤖", layout="wide")
#
# st.markdown("This is a demo of AutoGen chat agents that provides solutions to government organizations")
# st.markdown(
#     "'An example a question you can ask is: 'We're from the Department of Homeland Security.We need a robust cybersecurity solution to protect our critical infrastructure from cyber threats.'")
#
# class TrackableAssistantAgent(AssistantAgent):
#     """
#     A custom AssistantAgent that tracks the messages it receives.
#
#     This is done by overriding the `_process_received_message` method.
#     """
#
#     def _process_received_message(self, message, sender, silent):
#         with st.chat_message(sender.name):
#             st.markdown(message)
#         return super()._process_received_message(message, sender, silent)
#
#
# class TrackableUserProxyAgent(UserProxyAgent):
#     """
#     A custom UserProxyAgent that tracks the messages it receives.
#
#     This is done by overriding the `_process_received_message` method.
#     """
#
#     def _process_received_message(self, message, sender, silent):
#         with st.chat_message(sender.name):
#             st.markdown(message)
#         return super()._process_received_message(message, sender, silent)
#
#
# with st.container():
#     user_input = st.text_input("User Input")
# # only run if user input is not empty and model and key are selected
#     if user_input:
#
#         config_list = [
#             {
#                 "model": "gpt-3.5-turbo",
#                 "api_key": "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",
#             },
#
#         ]
#         assistant = TrackableAssistantAgent(
#             name="assistant",
#             human_input_mode="TERMINATE",
#             system_message="You belong to the government agency and ask questions related to the requirement of robust cybersecurity solutions to protect your critical infrastructure form cybersecurity threads.You are looking for a company that provides solution related to threat detection  "
#                            ",real time response and has a proven track record in government applications.",
#             is_termination_msg=lambda msg: "you're welcome" in msg["content"].lower(),
#             llm_config={
#                 "timeout": 600,
#                 "seed": 42,
#                 "config_list": config_list,
#             },
#         )
#         user_proxy = TrackableUserProxyAgent(
#             name="user",
#             human_input_mode="TERMINATE",
#             system_message = '''you are a matchmaking bot who matches the requirements of a government ,you will do a follow up with few questions to match them  with the relevant solutions
#                                 and provide companies that can match those solutions
#                                 you can ask for the goal of the requirement,the size and scope .You can ask the type of solution needed ,any compliance and regulatory standards in the
#                                 selection process and the timeline for implementation
#                                 Finally you provide the solutions providers list,the features and solutions they provide.
#                                 You can also provide detailed information and help setup meeting with the solutions provider company by proving email''',
#             code_execution_config={"use_docker": False},
#             # is_termination_msg=lambda msg: "thank you" in msg["content"].lower(),
#             llm_config={
#                 "timeout": 600,
#                 "seed": 42,
#                 "config_list": config_list,
#             },
#         )
#
#
#         loop = asyncio.new_event_loop()
#         asyncio.set_event_loop(loop)
#
#         # Define an asynchronous function: this is needed to use await
#         if "chat_initiated" not in st.session_state:
#             st.session_state.chat_initiated = False  # Initialize the session state
#
#         if not st.session_state.chat_initiated:
#
#             async def initiate_chat():
#                 await user_proxy.a_initiate_chat(
#                     assistant,
#                     message=user_input,
#                     max_consecutive_auto_reply=1,
#                     is_termination_msg=lambda x: x.get("content", "").strip().endswith("You're welcome!"),
#                 )
#                 st.stop()  # Stop code execution after termination command
#
#             # Run the asynchronous function within the event loop
#             loop.run_until_complete(initiate_chat())
#
#             # Close the event loop
#             loop.close()
#
#             st.session_state.chat_initiated = True  # Set the state to True after running the chat
#
#
# st.stop()


import os
from autogen.agentchat import AssistantAgent, UserProxyAgent
import streamlit as st
import asyncio
# class TrackableAssistantAgent(AssistantAgent):
#     """
#     A custom AssistantAgent that tracks the messages it receives.
#
#     This is done by overriding the `_process_received_message` method.
#     """
#
#     def _process_received_message(self, message, sender, silent):
#         with st.chat_message(sender.name):
#             st.markdown(message)
#         return super()._process_received_message(message, sender, silent)
#
#
# class TrackableUserProxyAgent(UserProxyAgent):
#     """
#     A custom UserProxyAgent that tracks the messages it receives.
#
#     This is done by overriding the `_process_received_message` method.
#     """
#
#     def _process_received_message(self, message, sender, silent):
#         with st.chat_message(sender.name):
#             st.markdown(message)
#         return super()._process_received_message(message, sender, silent)
#
#
#
#
# config_list = [
#     {
#         "model": "gpt-3.5-turbo",
#         "api_key": "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",
#     },
#
# ]
#
#
#
# # agent_with_number = TrackableAssistantAgent(
# #             "agent_with_number",
# #             system_message="You are playing a game of guess-my-number."
# #                            "In the first game, you have the "
# #                            "number 53 in your mind, and I will try to guess it. "
# #                            "If I guess too high, say 'too high', if I guess too low, say 'too low'. ",
# #             llm_config={"config_list": config_list},
# #             max_consecutive_auto_reply=1,  # maximum number of consecutive auto-replies before asking for human input
# #             is_termination_msg=lambda msg: "53" in msg["content"],
# #             # terminate if the number is guessed by the other agent
# #             human_input_mode="TERMINATE",  # ask for human input until the game is terminated
# #         )
# human_proxy = TrackableAssistantAgent(
#     "human_proxy",
#     llm_config=False,  # no LLM used for human proxy
#     human_input_mode="ALWAYS",  # always ask for human input
# )
#
# agent_guess_number = TrackableUserProxyAgent(
#             "agent_guess_number",
#             system_message="I have a number in my mind, and you will try to guess it. "
#                            "If I say 'too high', you should guess a lower number. If I say 'too low', "
#                            "you should guess a higher number. ",
#             llm_config={"config_list":config_list},
#             human_input_mode="NEVER",
#         )
# result = human_proxy.initiate_chat(
#     agent_guess_number,
#     message="I have a number between 1 and 100. Guess it!",
# )
#
# st.write(result)


# setup page title and description
st.set_page_config(page_title="AutoGen Chat app", page_icon="🤖", layout="wide")

st.markdown("This is a demo of AutoGen chat agents that provides solutions to government organizations")
st.markdown(
    "'An example a question you can ask is: 'We're from the Department of Homeland Security.We need a robust cybersecurity solution to protect our critical infrastructure from cyber threats.'")


class TrackableAssistantAgent(AssistantAgent):
    """
    A custom AssistantAgent that tracks the messages it receives.

    This is done by overriding the `_process_received_message` method.
    """

    def _process_received_message(self, message, sender, silent):
        with st.chat_message(sender.name):
            st.markdown(message)
        return super()._process_received_message(message, sender, silent)


class TrackableUserProxyAgent(UserProxyAgent):
    """
    A custom UserProxyAgent that tracks the messages it receives.

    This is done by overriding the `_process_received_message` method.
    """

    def _process_received_message(self, message, sender, silent):
        with st.chat_message(sender.name):
            st.markdown(message)
        return super()._process_received_message(message, sender, silent)


with st.container():
    user_input = st.text_input("User Input")
# only run if user input is not empty and model and key are selected
    if user_input:

        config_list = [
            {
                "model": "gpt-3.5-turbo",
                "api_key": "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",
            },

        ]




        assistant = TrackableAssistantAgent(
            name="assistant",
            human_input_mode="TERMINATE",
            system_message = '''you are a matchmaking bot who matches the requirements of a government,you will ask the user about their requirement ,what kind of companies they are looking for to provide the solutions 
                                they are looking for ,certian criterias that can match the list of technology related companies from the website to provide relevant solutions 
                                you can also ask for the goal of the requirement,the size and scope .You can also ask for any compliance and regulatory standards in the
                                selection process and you sort the list of companies from the website that can provide solutions based on the timeline from the user. 
                                Finally you provide the tech companies list,the features and solutions they provide to the user.
                                You can also provide detailed information and help setup meeting with the solutions provider company by proving email''',
            code_execution_config={"use_docker": False},
            is_termination_msg=lambda msg: "you're welcome" in msg["content"].lower(),
            llm_config={
                "timeout": 600,
                "seed": 42,
                "config_list": config_list,
            },
        )

        human_proxy = TrackableUserProxyAgent(
            "human_proxy",
            llm_config=False,  # no LLM used for human proxy
            human_input_mode="ALWAYS",  # always ask for human input
        )



        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        # Define an asynchronous function: this is needed to use await
        if "chat_initiated" not in st.session_state:
            st.session_state.chat_initiated = False  # Initialize the session state

        if not st.session_state.chat_initiated:

            async def initiate_chat():
                # await user_proxy.a_initiate_chat(
                #     assistant,
                #     message=user_input,
                #     max_consecutive_auto_reply=1,
                #     is_termination_msg=lambda x: x.get("content", "").strip().endswith("You're welcome!"),
                # )
                await human_proxy.initiate_chat(
                    assistant,
                    message="We're from the Department of Homeland Security.We need a robust cybersecurity solution to protect our critical infrastructure from cyber threats.",
                )
                st.stop()  # Stop code execution after termination command

            # Run the asynchronous function within the event loop
            loop.run_until_complete(initiate_chat())

            # Close the event loop
            loop.close()

            st.session_state.chat_initiated = True  # Set the state to True after running the chat


st.stop()
