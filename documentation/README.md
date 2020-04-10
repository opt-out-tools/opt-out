# Opt Out Documentation

## Usage Scenarios and Requirements

Usage Scenarios are meant to explain click by click interaction. They do reference the exact inputs, and need to be changed when the UI changes. They are organised in to a table that represents the list of tasks that users will go through. There are 3 types of action to help explain the expected behaviour:

- Action - A user interaction
- Reaction - The way the software reacts to the user action
- Insight - What the user learns or recognises as a result of their action or the software reaction

There is also a space to link a task to a requirement. This should be done for any requirements listed in the scenario but it's not so important to link to every requirement that's relevant defined in other scenarios.

### Linking to Tests

One place where writing user scenarios comes in handy is that these are the exact things that need to be tested using end 2 end testing. The id of the scenario can be referenced in the test title. Like so:

```
describe('[US-002] - Hide misogynist tweets, () => {...});
```

The tasks themselves can be referenced in the test title, like so:

```
it('[T-01] - Open Extension', () => {...});
```
