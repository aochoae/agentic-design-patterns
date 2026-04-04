# The system analyzes restaurant reviews in parallel.
#
# Food Critic Agent
# Value-Money Agent
# Sentiment Agent

import asyncio
import nest_asyncio
import uuid

from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent
from google.adk.runners import InMemoryRunner
from google.genai import types


# Food Critic Agent
food_critic_agent = LlmAgent(
    name="FoodCriticAgent",
    model="gemini-2.5-flash-lite",
    instruction="""
                You are a food critic analyzing a restaurant review.
                Identify the main dish mentioned in the review and rate it on a scale of 1 to 5, where 1 is poor and 5
                is excellent.

                Review: {review_text}
                """,
    output_key="food_critique_result",
    description="Identify the main dish and rate it based on the review.",
)

# Value-for-Money Agent
value_money_agent = LlmAgent(
    name="ValueMoneyAgent",
    model="gemini-2.5-flash-lite",
    instruction="""
                You are a value-for-money analyst evaluating a restaurant review.
                Identify the main dish mentioned in the review and rate its value for money on a scale of 1 to 5, where
                1 is poor value and 5 is excellent value.

                Review: {review_text}
                """,
    output_key="value_money_result",
    description="Identify the main dish and rate it based on the review.",
)

# Sentiment Analysis Agent
sentiment_agent = LlmAgent(
    name="SentimentAgent",
    model="gemini-2.5-flash-lite",
    instruction="""
                Analyze the sentiment of the following customer review.
                Respond ONLY with one of these three words: POSITIVE, NEGATIVE, or NEUTRAL.

                Review: {review_text}
                """,
    output_key="sentiment_result",
    description="Determine whether the review is positive, negative, or neutral.",
)


# Parallel Agent
parallel_analysis = ParallelAgent(
    name="ParallelReviewAnalysis",
    sub_agents=[food_critic_agent, value_money_agent, sentiment_agent],
    description="Run the analysis agents in parallel on a review.",
)


# Synthesis Agent
synthesis_agent = LlmAgent(
    name="SynthesisAgent",
    model="gemini-2.5-flash-lite",
    instruction="""
                Synthesize the following analysis results into a clear, well-structured report.

                Output format:

                ## Review

                * **Food:** {food_critique_result}
                * **Value/Money:** {value_money_result}
                * **Sentiment:** {sentiment_result}                
                """,
    description="Determine whether the review is positive, negative, or neutral.",
)


root_agent = SequentialAgent(
    name="ReviewAnalysisPipeline",
    sub_agents=[parallel_analysis, synthesis_agent],
    description="First, run the analyses in parallel; then synthesize the results.",
)


async def analyze_review(runner: InMemoryRunner, review: str):
    print(f'\n{"=" * 60}')
    print(f"Restaurant review: \"{review}\"")
    print(f'{"=" * 60}\n')

    # Create session
    user_id = "alberto"
    session_id = str(uuid.uuid4())

    await runner.session_service.create_session(
        app_name=runner.app_name,
        user_id=user_id,
        session_id=session_id,
        state={"review_text": review},
    )

    result = ""
    async for event in runner.run_async(
            user_id=user_id,
            session_id=session_id,
            new_message=types.Content(
                role="user", parts=[types.Part(text=review)]
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
    print("Initializing the Review Analysis Pipeline...\n")

    runner = InMemoryRunner(root_agent)

    review_positive = """
        The experience at La Mesa Central was excellent from start to finish. The dishes are very well executed, with
        balanced flavors and careful presentation. I tried the grilled octopus, and it was perfectly cooked—tender and
        well seasoned.

        The service was attentive without being intrusive; the staff explained each dish in detail. The waiting time was
        reasonable, and the atmosphere is comfortable, ideal for a relaxed dinner.

        Prices are a bit high, but consistent with the quality of the experience.
        """

    review_neutral = """
        La Mesa Central offers a decent experience, though it doesn’t stand out much. The food is good, but not
        particularly memorable. The risotto had a nice texture, but lacked depth of flavor.

        The service was adequate, although there were some delays between courses. The atmosphere is pleasant, but
        somewhat noisy during peak hours.

        Prices feel slightly high relative to what is offered.
        """

    review_negative = """
        The experience at La Mesa Central was disappointing. The food arrived cold and lacked flavor; the steak was
        overcooked and dry.

        The service was slow and inattentive. We had to ask for the same things multiple times, and the waiting times
        were excessive.

        The place looks nice, but the noise level makes conversation difficult. Additionally, prices are high for the
        overall low quality.
        """

    await analyze_review(runner, review_positive)


if __name__ == "__main__":
    nest_asyncio.apply()
    asyncio.run(main())
