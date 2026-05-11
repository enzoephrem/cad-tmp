---
name: cda-wf-update
description: Orchestrates the synchronization of project artifacts when a source document (BRD) or parent node changes. [Use when user says 'update project' or 'sync changes']
---

# SKILL: cda-wf-update

## Overview

This workflow manages Change Management for the Citizen Dev Accelerator. It ensures that any changes to the core Business Requirements (BRD.md) are correctly and systematically propagated down the project hierarchy (PRD -> ARD -> Features -> User Stories -> Tickets).

It prevents the project from becoming inconsistent when business needs evolve mid-flight.

## On Activation

### Step 1: Resolve the Workflow Block

Run: `python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`

### Step 2: Greet & Load Context

1.  Greet: "CDA Workflow: Project Synchronization & Change Management. Initializing..."
2.  Orient: Read `docs/cda/ledger.json` and the current `BRD.md`.
3.  Consult: Load `{workflow.standards_files}` from `./standards/`.

## Process

### Phase 1: Context Loading & Impact Analysis
- **Preventative Injection:** Run `python3 {project-root}/_bmad/cda/skills/cda-core/scripts/cda_utils.py extract-standards --dir ./standards/ --keywords "change management, versioning, impact analysis"`.
- Run `rebuild-index --root {project-root}` to ensure the map is current.
- Compare the new `BRD.md` with the existing `docs/cda/PRD.md`.
- Identify affected downstream nodes (ARD, Features, Stories).

### Phase 2: PRD Update
- Invoke `cda-agent-ba` with capability `analyze-brd` in **Update mode**.
- **Write Artifact:** Update `docs/cda/PRD.md` with metadata:
    - `id`: `PRD`
    - `status`: `needs-revision` (until reviewed)

### Phase 3: Cascade Updates
- For each affected node identified in Phase 1:
    - Update its metadata `status` to `needs-revision` using `write-artifact`.
    - Offer to re-invoke relevant workflows (e.g., `cda-wf-gen-ftr`, `cda-wf-gen-us`).

### Phase 4: Finalize
- Run `rebuild-index --root {project-root}`.
- Greet: "Project synchronization complete. Affected nodes have been marked for revision in the distributed ledger."

## Customization

This workflow supports the following overrides:
- `standards_files`: List of all relevant standards (default: ["*.md"]).
