# Capability: review-artifact

## Outcome
A detailed `review-report.md` that identifies compliance gaps, cites the relevant `./standards/`, and provides actionable remediation steps.

## What Success Looks Like
- **Evidence:** Every finding has a "Standard Reference" field pointing to a specific file/rule.
- **Actionable:** The feedback allows a user or agent to fix the issue in one pass.
- **Categorized:** Issues are clearly split into "Blocker" (compliance fail) and "Improvement" (best practice).

## Process Details

### Phase 1: Artifact Scanning
- Identify the target file(s) from the project tree.
- Map the artifact type (e.g., PRD, ARD, Ticket) to the relevant standards.
- If the artifact is a `PRD`, focus on product/business standards.
- If it's a `TICKET`, focus on FE/BE/DB and security standards.

### Phase 2: Audit
- Perform a point-by-point comparison.
- Look for "Ghost Requirements" (things in the artifact NOT in the standards or parent).
- Look for "Missing Compliance" (things in the standards NOT in the artifact).

### Phase 3: Reporting
- Write `docs/cda/review-report.md` using `python3 {project-root}/_bmad/cda/skills/cda-core/scripts/cda_utils.py write-artifact`.
- Include metadata: `{ "type": "Report", "id": "REV-X", "status": "complete" }`.
- Update the status of the reviewed artifact: set `status` to `reviewed` or `needs-revision` in its frontmatter using `write-artifact`.
