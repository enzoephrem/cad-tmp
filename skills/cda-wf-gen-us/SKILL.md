---
name: cda-wf-gen-us
description: Orchestrates the expansion of a Feature into granular User Stories using the BA agent. [Use when user says 'generate stories' or 'expand feature']
---

# SKILL: cda-wf-gen-us

## Overview

This workflow manages the User Story generation phase of the Citizen Dev Accelerator. It coordinates the Business Analyst agent to take a technically defined Feature (FTR-X) and expand it into a set of granular, BDD-driven User Stories.

It focuses on selective expansion, allowing the user to choose which feature to elaborate on.

## On Activation

### Step 1: Resolve the Workflow Block

Run: `python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`

### Step 2: Greet & Load Context

1.  Greet: "CDA Workflow: User Story Expansion. Initializing..."
2.  Orient: Read `docs/cda/ledger.json` to identify available features.
3.  Consult: Load `{workflow.standards_files}` from `./standards/`.

## Process

### Phase 1: Context Loading & Selection
- **Preventative Injection:** Run `python3 {project-root}/_bmad/cda/skills/cda-core/scripts/cda_utils.py extract-standards --dir ./standards/ --keywords "user story, BDD, acceptance criteria, personas"`.
- Capture the output `rules` for the `cda-agent-ba`.
- Present a list of available Features (FTR-X) from the project ledger.
- Ask the user: "Which Feature would you like to expand into User Stories?"

### Phase 2: User Story Generation
- Invoke `cda-agent-ba` with capability `define-user-stories`.
- Provide the selected Feature path as context.
- **Write Artifacts:** For each story generated, use `python3 {project-root}/_bmad/cda/skills/cda-core/scripts/cda_utils.py write-artifact` with metadata:
    - `id`: `US-XXXX`
    - `type`: `USER-STORY`
    - `parent_id`: [FTR ID]
- Ensure `user-story.md` files are created in the correct `FTR-X/US-XXXX/` folders.

### Phase 3: Finalize
- Run `python3 {project-root}/_bmad/cda/skills/cda-core/scripts/cda_utils.py rebuild-index --root {project-root}`.
- Greet: "User Stories generated and registered in the distributed ledger. You can now proceed to Technical Ticket generation (cda-wf-gen-tkt)."

## Customization

This workflow supports the following overrides:
- `standards_files`: List of standards relevant to user stories (default: ["product-standards.md", "business-rules.md"]).
