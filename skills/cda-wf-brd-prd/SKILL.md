---
name: cda-wf-brd-prd
description: Orchestrates the BRD to PRD transformation using the BA agent. [Use when user says 'start project' or 'generate PRD']
---

# SKILL: cda-wf-brd-prd

## Overview

This workflow manages the initial phase of the Citizen Dev Accelerator. It coordinates the Business Analyst agent to transform a raw Business Requirements Document (BRD.md) into a structured, standards-compliant Product Requirements Document (PRD.md).

It supports both an interactive mode (with discovery questions) and a headless mode (rapid generation).

## On Activation

### Step 1: Resolve the Workflow Block

Run: `python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`

If the script fails, resolve the `workflow` block yourself by reading these three files in base → team → user order and applying structural merge rules: `{skill-root}/customize.toml`, `{project-root}/_bmad/custom/cda-wf-brd-prd.toml`, `{project-root}/_bmad/custom/cda-wf-brd-prd.user.toml`.

### Step 2: Greet & Load Config

Greet: "CDA Workflow: BRD to PRD Transformation. Initializing..."

## Process

### Phase 1: Context Loading
- Locate `BRD.md` in the project root.
- **Preventative Injection:** Run `python3 {project-root}/_bmad/cda/skills/cda-core/scripts/cda_utils.py extract-standards --dir ./standards/ --keywords "BRD, PRD, requirements, security, data"`.
- Capture the output `rules` and provide them to the `cda-agent-ba` as **Non-Negotiable Constraints**.
- Load `{workflow.prd_template}`.

### Phase 2: Discovery (Interactive Mode only)
- If NOT in headless mode:
    - Invoke `cda-agent-ba` with capability `analyze-brd` in **Discovery mode**.
    - Facilitate the batch questioning process.
    - Ensure `docs/cda/discovery-report.md` is generated.
- If in headless mode:
    - Skip questioning and proceed to Phase 3.

### Phase 3: Generation
- Invoke `cda-agent-ba` with capability `analyze-brd` in **Generation mode**.
- Use `python3 {project-root}/_bmad/cda/skills/cda-core/scripts/cda_utils.py write-artifact` to save the PRD with metadata:
    - `id`: `PRD`
    - `type`: `PRD`
    - `name`: "Product Requirements Document"
- Ensure all User Journeys and Features are captured.

### Phase 4: Finalize
- Run `python3 {project-root}/_bmad/cda/skills/cda-core/scripts/cda_utils.py rebuild-index --root {project-root}`.
- Greet: "PRD successfully generated and registered in the distributed ledger. The project is ready for Architecture Design (ARD)."

## Customization

This workflow supports the following overrides:
- `prd_template`: Path to the PRD markdown template.
- `prd_output_path`: Where the generated PRD is saved.
