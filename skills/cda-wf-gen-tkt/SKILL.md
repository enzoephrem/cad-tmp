---
name: cda-wf-gen-tkt
description: Orchestrates the expansion of a User Story into actionable vertical-slice tickets using the Senior Dev agent. [Use when user says 'generate tickets' or 'break down story']
---

# SKILL: cda-wf-gen-tkt

## Overview

This workflow manages the Technical Breakdown phase of the Citizen Dev Accelerator. It coordinates the Senior Dev agent to transform a User Story (US-X) into a set of actionable, vertical-slice implementation tickets (TCK-Y).

It enables selective expansion of stories into technical tasks.

## On Activation

### Step 1: Resolve the Workflow Block

Run: `python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`

### Step 2: Greet & Load Context

1.  Greet: "CDA Workflow: Technical Ticket Generation. Initializing..."
2.  Orient: Read `docs/cda/ledger.json` to identify available User Stories.
3.  Consult: Load `{workflow.standards_files}` from `./standards/`.

## Process

### Phase 1: Context Loading & Selection
- **Preventative Injection:** Run `python3 {project-root}/_bmad/cda/skills/cda-core/scripts/cda_utils.py extract-standards --dir ./standards/ --keywords "api, backend, frontend, database, performance"`.
- Capture the output `rules` for the `cda-agent-sdev`.
- Present a list of available **User Stories** OR **Features** OR the **PRD** from the project ledger.
- **Fast-Track Option:** If the user selects the **PRD** or a **Feature**, this initiates a Fast-Track breakdown, bypassing intermediate levels.

### Phase 2: Ticket Generation
- Invoke `cda-agent-sdev` with capability `generate-tickets`.
- Provide the selected parent node path and relevant `ARD/` chunks (if they exist) as context.
- **Write Artifacts:** For each ticket generated, use `python3 {project-root}/_bmad/cda/skills/cda-core/scripts/cda_utils.py write-artifact` with metadata:
    - `id`: `TCK-XXXX`
    - `type`: `TICKET`
    - `parent_id`: [ID of selected node]
    - `slices`: ["FE", "BE", "DB"]
- Ensure files are created in the appropriate `tickets/TCK-XXXX/` directory.

### Phase 3: Finalize
- Run `python3 {project-root}/_bmad/cda/skills/cda-core/scripts/cda_utils.py rebuild-index --root {project-root}`.
- Greet: "Technical tickets generated and registered in the distributed ledger. You can now proceed to Implementation (cda-wf-tkt-tdd)."

## Customization

This workflow supports the following overrides:
- `standards_files`: List of standards relevant to technical design (default: ["be-standards.md", "fe-standards.md", "db-standards.md", "api-standards.md"]).
