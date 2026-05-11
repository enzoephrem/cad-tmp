# Step 2: Identify Feature List

## STEP GOAL:
To confirm the Feature List extracted from the PRD and ensure each Feature has a clear value proposition before breaking them into User Stories.

## MANDATORY EXECUTION RULES:
- 🛑 NEVER generate content without user input
- 📋 YOU ARE A FACILITATOR
- 🎯 Focus ONLY on the **Feature List** (macro-level)
- 🚪 GET explicit approval for the Feature List

## FEATURE IDENTIFICATION PROCESS:

### 1. Extract Features from PRD
Read `{planning_artifacts}/prd.md` and find the "Features & Functional Requirements" section.
- List all Features identified in the PRD.
- Extract the **Value Proposition** for each.
- List the **FRs** associated with each Feature.

### 2. Present Feature List for Review
Display the Features to the user in this format:

```markdown
## Feature List

### Feature 1: [Feature Title]
**Value Proposition:** [Value from PRD]
**FRs covered:** FR1, FR2...

### Feature 2: [Feature Title]
**Value Proposition:** [Value from PRD]
**FRs covered:** FR3, FR4...
```

### 3. Collaborative Refinement
Ask the user:
- "Does this Feature list correctly capture the modules of value proposition from the PRD?"
- "Should we combine or split any Features based on implementation strategy?"

### 4. Get Final Approval
"Do you approve this Feature list for proceeding to User Story creation?"

## CONTENT TO UPDATE:
After approval, update `{planning_artifacts}/features.md` (which replaces epics.md):
1. Initialize the document with the approved Feature list.
2. Include the FR coverage map.

## NEXT STEP:
After user selects [C], load `./step-03-create-stories.md` to break Features into User Stories.
