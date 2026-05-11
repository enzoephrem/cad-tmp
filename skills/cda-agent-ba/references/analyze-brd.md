# Capability: analyze-brd

## Outcome
A high-quality `PRD.md` that serves as the foundation for technical design, and a `discovery-report.md` that captures all business clarifications.

## What Success Looks Like
- The PRD is 100% focused on **What** and **Why**.
- User Journeys are clearly articulated for every major actor.
- A prioritized Feature list is defined.
- The `ledger.md` reflects the addition of the PRD.

## Memory Integration
- Read the project `ledger.json` to check if a PRD already exists.
- If it exists, offer to **Update** or **Rebuild**.

## Process Details

### Phase 1: Discovery
- Scan the `BRD.md` for ambiguities (missing edge cases, vague personas, unclear success metrics).
- Consult `{agent.standards_files}` in `./standards/` to ensure the BRD aligns with core product and business rules.
- Prompt the user using structured batch questions.
- Write the final `discovery-report.md` to `docs/cda/`.

### Phase 2: Generation
- Create `docs/cda/PRD.md` following the template (see `assets/prd-template.md`).
- Ensure no technical implementation details leak in.
- **Write Artifact:** Use `write-artifact` with metadata:
    - `id`: `PRD`
    - `type`: `PRD`
    - `name`: "Product Requirements Document"
- **Finalize:** Run `rebuild-index --root {project-root}`.

## After the Session
- Remind the user that the PRD is ready for the Architect agent to begin the ARD phase.
