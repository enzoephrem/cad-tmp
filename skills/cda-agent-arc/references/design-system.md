# Capability: design-system

## Outcome
A modular, chunked `ARD/` folder that serves as the technical blueprint for the project, ensuring all IT standards are met.

## What Success Looks Like
- The ARD is broken into logical, domain-specific sub-documents (e.g., `security.md`, `api.md`).
- Every technical constraint is cited back to a standard in `./standards/`.
- The `ARD/index.md` provides a clear overview and links to all sub-documents.
- The project ledger reflects the addition of the ARD.

## Memory Integration
- Read `docs/cda/PRD.md` to identify the functional scope.
- Read `docs/cda/ledger.json` to ensure the ARD is registered.

## Process Details

### Phase 1: Domain Mapping
- Identify the core technical domains required by the PRD (e.g., if the PRD mentions external integration, API standards are a must).
- Scan `{agent.standards_files}` for relevant rules for each domain.

### Phase 2: Content Generation
- Generate the `ARD/index.md`.
- For each domain, generate a dedicated markdown file in `docs/cda/ARD/`.
- **Vertical Alignment:** Ensure the architecture supports the "vertical slice" implementation model (FE/BE/DB).

### Phase 3: Registration
- Use `write-artifact --path ARD/index.md` with metadata:
  ```yaml
  type: 'ARD'
  id: 'ARD'
  name: 'Architecture Requirements Document'
  status: 'complete'
  ```

## After the Session
- Remind the user that the Feature Mapping phase (`map-features`) is next.
