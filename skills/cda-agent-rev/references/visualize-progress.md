# Capability: visualize-progress

## Outcome
An interactive `cda-dashboard.html` that visualizes the project hierarchy and compliance status.

## What Success Looks Like
- **Tree Visualization:** Clear mapping from PRD -> Features -> User Stories -> Tickets.
- **Status Indicators:** Color-coded status (Draft, Complete, Reviewed, Needs-Revision).
- **Navigation:** Deep links to the markdown files in the repository.

## Process Details

### Phase 1: Data Gathering
- Read `docs/cda/ledger.json`.
- Extract artifacts and their parent/child relationships.

### Phase 2: Generation
- Execute `python3 {project-root}/skills/cda-agent-rev/scripts/generate_dashboard.py --root {project-root}`.
- This script transforms the JSON ledger into a self-contained HTML file.

### Phase 3: Presentation
- Inform the user where the dashboard is located and how to view it.
