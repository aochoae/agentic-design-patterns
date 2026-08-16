# Planning Pattern example: Moving to a New Home


import asyncio
import nest_asyncio
import uuid

from google.adk.agents import LlmAgent
from google.adk.runners import InMemoryRunner
from google.genai import types


moving_crew = LlmAgent(
    name="MovingCrew",
    description="People hired to help a move, including packing, loading, transporting, and unloading items.",
    model="gemini-2.5-pro",
    instruction="""
        You are an agent responsible for managing a move to a new home.

        ## Initial State
        The person still lives in their current home and all their belongings are there.

        ## Goal State
        The person is fully moved into their new home.

        ## Constraints
        - Limited budget.
        - The move must be completed by a specific date.
        - The person works during weekdays.

        Your responsibility is to create and execute a plan that transforms the initial state into the goal state.

        During the process, you will receive new information.

        When new information arrives:

        1. Evaluate how it affects the current state.
        2. Identify any obstacles.
        3. Modify the plan if necessary.
        4. Find an alternative when an action is no longer viable.
        5. Continue until the goal state is reached.

        Do not blindly follow the original plan when circumstances change.

        Your objective is to reach the GOAL STATE, not to complete a specific list of tasks.
        """,
    output_key="plan_output" # The output is saved to this state key.
)


async def execute(runner: InMemoryRunner, inquiry: str):
    print(f"{'*' * 5} The user needs help with: '{inquiry}' {'*' * 5}")

    # Create session
    user_id = "alberto"
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


if __name__ == "__main__":
    nest_asyncio.apply()

    prompt = """
        I need help moving to a new home from CDMX Mexico to Nevada, USA.

        My belongings include furniture, clothes, kitchen appliances, books,
        electronics, and personal items. I also have some things that I could
        sell or donate instead of moving.

        I need to move to Las Vegas by October 15, 2026. I have a total moving
        budget of $8,000 USD.

        I work Monday through Friday, so I can only handle moving-related tasks
        during evenings and weekends. I can take up to five days off work around
        the moving date.

        The main goal is to be fully settled in my new home by October 15, 2026,
        while staying within the $8,000 budget.

        Help me plan the move.
        """

    asyncio.run(execute(InMemoryRunner(moving_crew), prompt))
