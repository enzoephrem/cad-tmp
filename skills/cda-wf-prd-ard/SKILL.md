---
name: cda-wf-prd-ard
description: Orchestrates the PRD to ARD transformation and Feature Mapping using the Architect agent. [Use when user says 'design system' or 'generate ARD']
---

# SKILL: cda-wf-prd-ard

## Overview

This workflow manages the Architecture Design phase of the Citizen Dev Accelerator. It coordinates the Architect agent to transform the Product Requirements Document (PRD.md) into a modular Architecture Requirements Document (ARD) and maps out the technical boundaries for each feature.

It automatically triggers an IT compliance review after the ARD is generated.

## On Activation

### Step 1: Resolve the Workflow Block

Run: `python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`

### Step 2: Greet & Load Context

Greet: "CDA Workflow: Architecture Design & Feature Mapping. Initializing..."

## Process

### Phase 1: Architecture Design
- Locate `docs/cda/PRD.md`.
- Run `python3 {project-root}/_bmad/cda/skills/cda-core/scripts/cda_utils.py extract-standards --dir ./standards/ --keywords ARD,Architecture,System` for Preventative Compliance.
- Invoke `cda-agent-arc` with capability `design-system`.
- Ensure the `docs/cda/ARD/` directory is created and chunked documents are generated.

### Phase 2: Compliance Review (Auto-Triggered)
- Invoke `cda-wf-review` on the `docs/cda/ARD/` folder.
- Present the compliance report to the user.
- If blockers exist, the workflow pauses for human intervention.

### Phase 3: Finalize
- Run `python3 {project-root}/_bmad/cda/skills/cda-core/scripts/cda_utils.py rebuild-index --root {project-root}`.
- Greet: "Architecture Design complete. The project is ready for Feature Mapping (cda-wf-gen-ftr)."

## Customization

This workflow supports the following overrides:
- `standards_files`: List of standards relevant to architecture (default: ["architecture-standards.md", "security-standards.md", "api-standards.md"]).
- `ard_output_folder`: Path to the ARD directory.
