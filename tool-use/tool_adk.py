"""
This script demonstrates the "Tool Use" agentic pattern.

It defines a technical support agent that is given a tool to validate IMEI
(International Mobile Equipment Identity) numbers. When presented with a user
request, the agent follows its instructions to extract the IMEI, use the
validation tool, and provide a response based on the tool's output.
"""

import asyncio
import uuid

from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool
from google.adk.runners import InMemoryRunner
from google.genai import types

from checkdigit.luhn import LuhnAlgorithm as luhn


def validator(sequence: str):
    """
    Even though FunctionTool supports other return types, the preferred return
    type is a dictionary.

    :param sequence: The IMEI number to be validated.
    :return: A dictionary with the validation result.
    """
    return {"result": "success" if luhn.is_valid(sequence) else "failure"}

tool_validator = FunctionTool(func=validator)


# Support Agent
root_agent = LlmAgent(
    name="SupportAgent",
    model="gemini-2.5-flash-lite",
    instruction="""
    # Role
    You are a technical support agent.
    
    # Objective
    Verify information about an IMEI number using the available tool.
    
    # Instructions
    - Extract the IMEI number from the user's message.
    - If a valid IMEI is not provided, ask the user to provide one.
    - If a valid IMEI is found, use the `validator` tool.
    - Base your response solely on the tool's output.
    
    # Output
    - If a valid IMEI is provided, return the verification result.
    - Otherwise, ask the user to provide a valid IMEI number.
    """,
    tools=[tool_validator]
)


async def technical_support(runner: InMemoryRunner, inquiry: str):
    print(f'\n{"=" * 60}')
    print(f"User request: \"{inquiry}\"")
    print(f'{"=" * 60}\n')

    # Create session
    user_id = "alberto"
    session_id = str(uuid.uuid4())

    await runner.session_service.create_session(
        app_name=runner.app_name,
        user_id=user_id,
        session_id=session_id
    )

    result = ""
    async for event in runner.run_async(
            user_id=user_id,
            session_id=session_id,
            new_message=types.Content(
                role="user", parts=[types.Part(text=inquiry)]
            ),
    ):
        if event.is_final_response() and event.content:
            if getattr(event.content, "text", None):
                result = event.content.text
            elif getattr(event.content, "parts", None):
                parts = []
                for part in event.content.parts:
                    if getattr(part, "text", None):
                        parts.append(part.text)
                result = "".join(parts)

    print(result)


async def main():
    print("Starting the IMEI verification tool...")
    runner = InMemoryRunner(root_agent)
    await technical_support(runner, "Hello, I have an IMEI number 490154203237518. Can you verify if it's valid?")


if __name__ == "__main__":
    asyncio.run(main())
