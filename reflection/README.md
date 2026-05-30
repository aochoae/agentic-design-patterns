# Reflection Pattern

The **reflection pattern** allows an agent to review its own output and make improvements based on that review. This can
lead to higher quality results, as the agent can identify and correct mistakes or areas for enhancement.

The pattern can be facilitated by a **review agent** that evaluates the output of a **worker agent** and provides
feedback for improvement.

The agents involved in this pattern typically include:

1. **Execution Agent**: This agent performs the initial task and generates output.
2. **Review Agent**: This agent reviews the output of the execution agent, providing feedback and suggestions for improvement.
3. **Reflection Agent**: This agent takes the feedback from the review agent and makes necessary adjustments to the output, iterating until the desired quality is achieved.

## Running the scripts

To run the **Google ADK** script, execute the following command:

```shell
python reflection_adk.py
```
