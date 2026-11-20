**English** · [Dansk](Reflection-da) · [Bahasa Malaysia](Reflection-ms)

# Reflection

## How the project was approached

The work followed the plan-first process: a Business Case, a Stakeholder Analysis, a Project Plan and four milestones came first. Then one use case was designed (domain model, sequence diagrams, class diagram) before any code. Each milestone was one branch and one pull request. The rule that deletes the text was written first as a plain Python class with tests, and Flask was added on top.

## What was hard

- Deciding where the timer lives. A timer in JavaScript is quick, but it cannot be tested with pytest. Keeping it on the server made the rule testable and the browser a simple view.
- A race between typing and polling: an old poll answer could report that the text was cleared just after the writer typed a new letter. The script now ignores answers that started before the last key press.
- Keeping documents, diagrams and code in step when the design changed (the web layer was designed only after the core was done).

## What was easy

- The rule itself: one class with three small methods.
- Testing with a fake clock: no test waits for five seconds.
- Flask: an app factory, one blueprint and two routes were enough.

## What to improve next time

- Test the browser script automatically. Today only the screenshots, taken in a container, show that it works.
- Draw the wireframe first and review it with a reader before the design.
- Start the screenshot tooling earlier, so each step is captured when it is built.

## Biggest learning

Keep the rule out of the framework. When the rule is plain code that receives time as a value, it is easy to test, and the web layer can stay thin.

## What I would do differently

Add a small end-to-end test in the container that types, waits and checks the page, so the screenshots are a by-product of a test and not a separate script.
