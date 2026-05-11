# Step 3: Generate User Stories from Features

## STEP GOAL:
To break down each approved Feature into multiple User Stories that deliver incremental value.

## MANDATORY EXECUTION RULES:
- 🛑 NEVER generate content without user input
- 📋 YOU ARE A FACILITATOR
- 🎯 Each Feature MUST have multiple User Stories
- 🔗 User Stories will be further broken into **Implementation Tickets** in the next workflow

## STORY GENERATION PROCESS:

### 1. Process Features Sequentially
For each Feature in `{planning_artifacts}/features.md`:

#### A. Feature Breakdown
- Identify the distinct User Stories required to fulfill the Feature's value proposition.
- Ensure each story is value-driven (As a... I want... So that...).

#### B. Generate User Stories
Format for each Story:
```markdown
### Story {Feature_N}.{Story_M}: [Title]
**User Story:** As a [Role], I want [Capability], So that [Benefit].
**Acceptance Criteria:**
- [AC1]
- [AC2]
...
```

### 2. Connect to Downstream Work
Remind the user: "These User Stories will be broken into **Implementation Tickets** (e.g., Backend, Frontend, DB tasks) in the next phase of the workflow."

### 3. Append to features.md
When a set of stories for a Feature is approved, append them to `{planning_artifacts}/features.md`.

## NEXT STEP:
After all Features are processed, load `./step-04-final-validation.md`.
