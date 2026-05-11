---
name: cda-wf-tkt-tdd
description: Orchestrates the implementation of a technical ticket using the Senior Dev agent. [Use when user says 'implement ticket' or 'start coding']
---

# SKILL: cda-wf-tkt-tdd

## Overview

This workflow manages the Implementation phase of the Citizen Dev Accelerator. It coordinates the Senior Dev agent to execute the Test-Driven Development (TDD) loop and produce functional, tested code for a specific technical ticket (TCK-X).

It transforms technical specifications into working software while ensuring strict compliance with IT standards.

## On Activation

### Step 1: Resolve the Workflow Block

Run: `python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`

### Step 2: Greet & Load Context

1.  Greet: "CDA Workflow: TDD-Driven Implementation. Initializing..."
2.  Orient: Read `docs/cda/ledger.json` to identify tickets ready for implementation.
3.  Consult: Load `{workflow.standards_files}` from `./standards/`.

## Process

### Phase 1: Context Loading & Selection
- **Preventative Injection:** Run `python3 {project-root}/_bmad/cda/skills/cda-core/scripts/cda_utils.py extract-standards --dir ./standards/ --keywords "tdd, testing, code style, security, backend, frontend, database"`.
- Capture the output `rules` for the `cda-agent-sdev`.
- Present a list of available Tickets (TCK-X) from the project ledger.
- Ask the user: "Which ticket would you like to implement?"

### Phase 2: Execution (TDD Loop)
- Invoke `cda-agent-sdev` with capability `execute-implementation`.
- Provide the ticket context, relevant `ARD/` chunks, and parent `user-story.md` as context.

### Phase 3: Finalize
- **Update Metadata:** Use `python3 {project-root}/_bmad/cda/skills/cda-core/scripts/cda_utils.py write-artifact` to update the ticket's `ticket.md` with metadata:
    - `id`: `TCK-XXXX`
    - `status`: `complete`
- Run `python3 {project-root}/_bmad/cda/skills/cda-core/scripts/cda_utils.py rebuild-index --root {project-root}`.
- Greet: "Implementation complete and verified. The feature slice is now functional and the distributed ledger is updated."

## Customization

This workflow supports the following overrides:
- `standards_files`: List of standards relevant to implementation (default: ["be-standards.md", "fe-standards.md", "db-standards.md", "testing-standards.md", "telemetry-standards.md", "api-standards.md"]).
