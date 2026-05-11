---
name: cda-wf-gen-ftr
description: Orchestrates the mapping of PRD features into technical Feature definitions using the Architect agent. [Use when user says 'map features' or 'generate feature tree']
---

# SKILL: cda-wf-gen-ftr

## Overview

This workflow manages the Feature Mapping phase of the Citizen Dev Accelerator. It coordinates the Architect agent to transform the high-level features from the PRD into technically defined Features (`feature.md`), ensuring they align with the system architecture (ARD).

## On Activation

### Step 1: Resolve the Workflow Block

Run: `python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`

### Step 2: Greet & Load Context

1.  Greet: "CDA Workflow: Technical Feature Mapping. Initializing..."
2.  Orient: Read `docs/cda/ledger.json`, `docs/cda/PRD.md`, and `docs/cda/ARD/index.md`.

## Process

### Phase 1: Feature Mapping
- **Preventative Injection:** Run `python3 {project-root}/_bmad/cda/skills/cda-core/scripts/cda_utils.py extract-standards --dir ./standards/ --keywords "feature, architecture, integration, security"`.
- Capture the output `rules` for the `cda-agent-arc`.
- Invoke `cda-agent-arc` with capability `map-features`.
- Scaffolds the `FTR-X/` directory structure.
- Generates `feature.md` for each feature, linking them to specific ARD sections and IT standards.

### Phase 2: Finalize
- Run `python3 {project-root}/_bmad/cda/skills/cda-core/scripts/cda_utils.py rebuild-index --root {project-root}`.
- Greet: "Feature Mapping complete. The feature tree is established in the distributed ledger. You can now proceed to User Story expansion (cda-wf-gen-us)."

## Customization

This workflow supports the following overrides:
- `standards_files`: List of technical standards relevant to feature boundaries (default: ["architecture-standards.md", "api-standards.md"]).
