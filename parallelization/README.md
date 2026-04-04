# Parallelization Pattern

This pattern allows you to run multiple agents in parallel, which can significantly improve performance when you need to
process multiple tasks simultaneously.

The pattern is useful when:

* Execute independent or loosely coupled tasks simultaneously (fan-out).
* Reduce end-to-end latency, especially for I/O-bound operations.
* Improve system throughput by utilizing multiple compute resources.
* Increase responsiveness in interactive or real-time systems.
* Enable efficient handling of heterogeneous workloads via specialized agents.
* Support horizontal scaling when tasks can be decomposed.

## Running the scripts

To run the **Google ADK** script, execute the following command:

```shell
python parallelization_adk.py
```

Possible output:

```markdown
## Review

*   **Food:** Main Dish: Grilled Octopus
    Rating: 5/5
*   **Value/Money:** Main Dish: Grilled Octopus
    Value for Money: 3/5
    Reasoning: The reviewer praises the grilled octopus for being perfectly cooked, tender, and well-seasoned, indicating high quality. However, they also note that the prices are "a bit high," suggesting that while the quality justifies the cost to some extent, it's not a budget-friendly option. Therefore, it offers good, but not exceptional, value for money.
*   **Sentiment:** POSITIVE
```
