---
name: bmad-create-features-and-stories
description: 'Break Features into User Stories. Use when the user says "create the features and stories list"'
---

# Create Features and Stories

**Goal:** Transform PRD Features and Architecture decisions into comprehensive User Stories, ensuring each story delivers distinct value within its parent Feature.

**Your Role:** Product Strategist and technical specifications writer. You bridge the gap between high-level "Features" (from the PRD) and actionable "User Stories".

## Conventions

- Bare paths (e.g. `steps/step-01-validate-prerequisites.md`) resolve from the skill root.
- `{skill-root}` resolves to this skill's installed directory.
- `{project-root}`-prefixed paths resolve from the project working directory.
- `{skill-name}` resolves to the skill directory's basename.

## WORKFLOW ARCHITECTURE

This uses **step-file architecture**:
- **Feature Layer**: Groups Functional Requirements into value-driven modules.
- **User Story Layer**: Downstream from Features; provides the "As a... I want... So that..." context.
- **Implementation Ticket Layer**: (Next workflow) Downstream from User Stories; technical units of work.

## Execution

Read fully and follow: `./steps/step-01-validate-prerequisites.md` to begin the workflow.
