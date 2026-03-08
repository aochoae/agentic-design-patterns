# Chaining Pattern

The chaining pattern demonstrates how to break down a complex task into smaller, manageable prompts that can be executed sequentially.

This pattern is useful when:

- The task is too complex for a single prompt
- You need to build on previous results
- You want to validate intermediate results

## Running the scripts

This example reads a positive/negative review and generates a response message.

1. Extract the customer's name and sentiment from the review
2. Transform the extracted data into a JSON format
3. Generate a response message based on the sentiment

To run the **Anthropic** example:

```shell
python chaining_anthropic.py
```

Posible output:

```markdown
# Response to Luis Alberto's Positive Review

Thank you so much, Luis Alberto, for taking the time to share your wonderful feedback! We're thrilled to hear that you
found our product to be an excellent option and that you were impressed with its significant AI power and compact,
ready-to-use design. It's incredibly rewarding to know that our solution is delivering real value to developers and data
scientists like yourself. Your positive experience motivates our entire team to continue innovating and improving. We 
truly appreciate your support and would love to hear from you again if you have any additional thoughts or suggestions
in the future!
```

To run the **OpenAI** example:

```shell
python chaining_openai.py
```

Posible output:

```markdown
Dear Luis Alberto, I sincerely apologize for your disappointing experience. Your feedback is important to us, and we are
committed to addressing the issues you've encountered. Please know that we value your input and will work diligently to
improve our services. We appreciate your patience and hope to have the opportunity to make things right in the future.
```

