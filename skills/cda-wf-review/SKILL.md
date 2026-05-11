---
name: cda-wf-review
description: Orchestrates the audit process for any project artifact using the Reviewer agent. [Use when user says 'run review' or 'audit artifact']
---

# SKILL: cda-wf-review

## Overview

This workflow provides a cross-cutting audit capability for the Citizen Dev Accelerator. It coordinates the Reviewer agent to validate any artifact (PRD, ARD, US, Ticket, or Code) against the IT standards in `./standards/`.

It can be triggered manually by the user or automatically as a sub-step in other CDA workflows.

## On Activation

### Step 1: Resolve the Workflow Block

Run: `python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`

### Step 2: Greet & Load Context

Greet: "CDA Workflow: Compliance Audit. Initializing..."

## Process

### Phase 1: Target Selection
- If a target path is provided as an argument, use it.
- Otherwise, ask the user: "Which artifact or folder would you like to audit?"
- Consult `docs/cda/ledger.json` to provide a list of valid artifacts if needed.

### Phase 2: Audit Execution
- Run `python3 {project-root}/_bmad/cda/skills/cda-core/scripts/cda_utils.py extract-standards --dir ./standards/ --keywords Compliance,Security,Standards` for Preventative Compliance.
- Invoke `cda-agent-rev` with capability `review-artifact` on the target path.
- Ensure the `docs/cda/review-report.md` is generated with specific citations.

### Phase 3: Dashboard Update (Optional)
- If the audit was on a major node (PRD, ARD) or the entire project:
    - Invoke `cda-agent-rev` with capability `visualize-progress`.
    - Update `docs/cda/cda-dashboard.html`.

### Phase 4: Finalize
- Present the summary of findings (Blockers vs. Warnings).
- Run `python3 {project-root}/_bmad/cda/skills/cda-core/scripts/cda_utils.py rebuild-index --root {project-root}`.
- Greet: "Audit complete. Review the report at docs/cda/review-report.md for actionable feedback."

## Customization

This workflow supports the following overrides:
- `standards_files`: List of standards to check against (default: ["*.md"]).
- `report_output_path`: Where the review report is saved.
