# Wireframe of UC-001 Write without stopping

The application has one screen. The Writer types into one text area; below it the screen shows the Countdown, the Warning or the message that the Text is gone. The four states below follow the scenario of the use case in `uc.md`.

## State 1: empty

The Writer has just opened the application, or has deleted all of the Text by hand. No Countdown is shown.

```text
+------------------------------------------------------+
|  Write without stopping                              |
+------------------------------------------------------+
|  +------------------------------------------------+  |
|  | |                                              |  |
|  |                                                |  |
|  |                                                |  |
|  +------------------------------------------------+  |
|  Start typing. Your text disappears if you stop      |
|  for more than 5 seconds.                            |
+------------------------------------------------------+
```

## State 2: typing with Countdown

The Writer has typed Text. Every change of the Text restarts the Countdown at 5 seconds.

```text
+------------------------------------------------------+
|  Write without stopping                              |
+------------------------------------------------------+
|  +------------------------------------------------+  |
|  | It was a quiet morning and the words kept     |  |
|  | coming, one after the other|                   |  |
|  |                                                |  |
|  +------------------------------------------------+  |
|  Seconds left: 4                                     |
+------------------------------------------------------+
```

## State 3: Warning in the last seconds

The Text is not empty and 2 seconds or less are left. The Countdown is emphasised as a Warning.

```text
+------------------------------------------------------+
|  Write without stopping                              |
+------------------------------------------------------+
|  +------------------------------------------------+  |
|  | It was a quiet morning and the words kept     |  |
|  | coming, one after the other|                   |  |
|  |                                                |  |
|  +------------------------------------------------+  |
|  !! Seconds left: 1 - keep writing !!                |
+------------------------------------------------------+
```

## State 4: Text gone

More than 5 seconds passed without a change, so all of the Text was deleted. The message stays until the Writer types again, which returns to State 2.

```text
+------------------------------------------------------+
|  Write without stopping                              |
+------------------------------------------------------+
|  +------------------------------------------------+  |
|  | |                                              |  |
|  |                                                |  |
|  |                                                |  |
|  +------------------------------------------------+  |
|  Your text is gone. Start again.                     |
+------------------------------------------------------+
```

## Transitions

| From | Event | To |
| --- | --- | --- |
| Empty | The Writer types | Typing with Countdown |
| Typing with Countdown | The Writer changes the Text | Typing with Countdown (Countdown restarts) |
| Typing with Countdown | 2 seconds or less left | Warning |
| Warning | The Writer changes the Text | Typing with Countdown |
| Typing with Countdown or Warning | More than 5 seconds without a change | Text gone |
| Typing with Countdown or Warning | The Writer deletes all Text by hand | Empty |
| Text gone | The Writer types | Typing with Countdown |
