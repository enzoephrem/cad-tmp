# Capability: define-user-stories

## Outcome
A set of vertical-slice `user-story.md` files organized in Feature directories, ready for ticket generation.

## What Success Looks Like
- Every User Story has a clear Persona, Need, and Value.
- BDD Acceptance Criteria (Given/When/Then) cover at least the happy path and one error case.
- Dependencies on other stories are explicitly listed.
- The `ledger.md` is updated for every new folder and file created.

## Memory Integration
- Query `ledger.json` to list available Features (FTR-X) for the user to choose from.
- Verify that a story ID doesn't already exist before creating.

## Process Details

### Phase 1: Feature Selection
- Present a list of Features from the PRD/Ledger.
- Ask the user: "Which Feature would you like to expand into User Stories?"

### Phase 2: Story Mapping
- Brainstorm stories for the selected feature.
- Ensure each story is small enough to be a "vertical slice" but large enough to provide value.

### Phase 3: File Creation
- For each story:
  1. **Write Artifact:** Use `write-artifact` with metadata:
     - `id`: `US-Y`
     - `type`: `USER-STORY`
     - `name`: "Story Name"
     - `parent_id`: `FTR-X`
  2. Write `user-story.md` with BDD criteria and dependencies.
  3. **Finalize:** Run `rebuild-index --root {project-root}`.

## After the Session
- Offer to visualize the new stories in the dependency graph (if the Reviewer agent is built).
- Remind the user they can now generate Tickets for these stories.
