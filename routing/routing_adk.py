# Travel Concierge is a specialized service that coordinates the discovery, selection, and booking of travel options,
# including air logistic, accommodation, experiences and culture, documentation and visa, and finance and budget.
#
# Air Logistic Agent
# Accommodation Agent
# Experiences & Culture Agent
# Documentation & Visa Agent
# Finance & Budget Agent


import asyncio
import uuid

from google.adk import Agent
from google.adk.runners import InMemoryRunner
from google.adk.tools import FunctionTool
from google.genai import types


# Air Logistic Agent
def air_logistic_handler(inquiry: str):
    print(f"Air Logistic Handler: '{inquiry}'")
    return f"Problem resolved: {inquiry}"

air_logistic_agent = Agent(
    name="Air_Logistic_Agent",
    model="gemini-2.5-flash-lite",
    description="Air Logistic Agent is a specialized service responsible for orchestrating air cargo logistics operations across scheduling, routing, and operational systems.",
    tools=[FunctionTool(air_logistic_handler)]
)

# Accommodation Agent
def accommodation_handler(inquiry: str):
    print(f"Accommodation Handler: '{inquiry}'")
    return f"Problem resolved: {inquiry}"

accommodation_agent = Agent(
    name="Accommodation_Agent",
    model="gemini-2.5-flash-lite",
    description="Accommodation Agent is a specialized service that manages the discovery, selection, and booking of lodging options according to user requirements and availability.",
    tools=[FunctionTool(accommodation_handler)]
)

# Experiences & Culture Agent
def experiences_culture_handler(inquiry: str):
    print(f"Experiences & Culture Handler: '{inquiry}'")
    return f"Problem resolved: {inquiry}"

experiences_culture_agent = Agent(
    name="Experiences_Culture_Agent",
    model="gemini-2.5-flash-lite",
    description="Experiences & Culture Agent is a specialized service that manages the discovery, selection, and booking of experiences and cultural activities according to user requirements and availability.",
    tools=[FunctionTool(experiences_culture_handler)]
)

# Documentation & Visa Agent
def documentation_visa_handler(inquiry: str):
    print(f"Documentation & Visa Handler: '{inquiry}'")
    return f"Problem resolved: {inquiry}"

documentation_visa_agent = Agent(
    name="Documentation_Visa_Agent",
    model="gemini-2.5-flash-lite",
    description="Documentation & Visa Agent is a specialized service that verifies and manages the documentation required for international travel, including visas, passports, and entry permits.",
    tools=[FunctionTool(documentation_visa_handler)]
)

# Finance & Budget Agent
def finance_budget_handler(inquiry: str):
    print(f"Finance & Budget Handler: '{inquiry}'")
    return f"Problem resolved: {inquiry}"

finance_budget_agent = Agent(
    name="Finance_Budget_Agent",
    model="gemini-2.5-flash-lite",
    description="""Finance & Budget Agent is a software agent that tracks expenses, estimates costs, and ensures that planned activities remain within the defined budget.""",
    tools=[FunctionTool(documentation_visa_handler)]
)

# Coordinator Agent
coordinator_agent = Agent(
    name="Coordinator",
    model="gemini-2.5-flash-lite",
    description="Coordinator Agent is the central orchestration agent responsible for coordinating the five specialized agents, delegating tasks, managing their interactions, and consolidating their results to achieve the overall objective.",
    instruction="""
                You are the Coordinator Agent, your role is to coordinate the five specialized agents, delegating tasks,
                managing their interactions, and consolidating their results to achieve the overall objective.
                - If the user has a problem with the air logistic, use the 'Air_Logistic_Agent'.
                - If the user has a problem with the accommodation, use the 'Accommodation_Agent'.
                - If the user has a problem with the experiences and culture, use the 'Experiences_Culture_Agent'.
                - If the user has a problem with the documentation and visa, use the 'Documentation_Visa_Agent'.
                - If the user has a problem with the finance and budget, use the 'Finance_Budget_Agent'.
                """,
    sub_agents=[air_logistic_agent, accommodation_agent, experiences_culture_agent, documentation_visa_agent, finance_budget_agent]
)


async def execute(runner: InMemoryRunner, inquiry: str):
    print(f"{'*' * 5} The user needs help with: '{inquiry}' {'*' * 5}")

    # Create session
    user_id = "user_demo2"
    session_id = str(uuid.uuid4())

    await runner.session_service.create_session(
        app_name=runner.app_name,
        user_id=user_id,
        session_id=session_id
    )

    result = ""

    try:

        async for event in runner.run_async(
            user_id=user_id,
            session_id=session_id,
            new_message=types.Content(
                role='user',
                parts=[types.Part(text=inquiry)]
            ),
        ):
            if event.is_final_response() and event.content:
                if getattr(event.content, 'text', None):
                    result = event.content.text
                elif getattr(event.content, 'parts', None):
                    parts = []
                    for part in event.content.parts:
                        if getattr(part, 'text', None):
                            parts.append(part.text)
                        elif getattr(part, 'function_call', None):
                            parts.append(f"[{part.function_call.name}]")
                    result = "".join(parts)
                break

        print(f"The coordinator has resolved the user's inquiry: {result}")
        return result

    except Exception as e:
        print(f"Error: {e}")

async def main():
    print("Starting the ")
    runner = InMemoryRunner(coordinator_agent)

    # Air Logistic
    # await execute(runner, "What are the best airlines flying from Mexico City to Las Vegas?")

    # Accommodation
    # await execute(runner, "List three hotels near the Sphere in Las Vegas.")

    # Experiences & Culture
    # await execute(runner, "What unique experiences can I do in Edinburgh in three days?")

    # Documentation & Visa
    # await execute(runner, "Do Mexican citizens need a visa to travel to the United States?")

    # Finance & Budget
    await execute(runner, "Convert the total trip cost from USD to MXN. $10,000 USD.")


if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())
