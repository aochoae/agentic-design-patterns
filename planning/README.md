# Planning Pattern

**Planning Pattern** is used when an agent must solve an objective that requires multiple coordinated actions. Instead
of executing an action directly, the agent analyzes the current situation, identifies constraints, and determines a
sequence of actions that allows it to achieve the objective.

To use this pattern, you normally define:

* **Initial State**: The situation where the system currently is.
* **Objective**: The state you want to reach.
* **Constraints**: Conditions the agent must respect, such as time, budget, resources, or rules.

The agent can divide a complex objective into smaller tasks, determine the order in which they should be performed, and
adjust the plan when it encounters obstacles or receives new information.

When to use:

The Planning pattern is useful when:

* The objective requires multiple actions.
* Actions have dependencies or a specific order.
* The agent needs to make decisions before acting.
* There are constraints on time, budget, resources, or rules.
* A task can be divided into subtasks.
* The environment can change during execution.
* The agent needs to adapt or replan when obstacles appear.
* The goal is to make the system more autonomous, rather than requiring step-by-step instructions from the user.

## Running the scripts

To run the **Google ADK** script, execute the following command:

```shell
python planning_adk.py
```
