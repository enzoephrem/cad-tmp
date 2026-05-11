# Capability: map-features

## Outcome
A set of `feature.md` files in `FTR-X/` folders that bridge the gap between business value and technical implementation.

## What Success Looks Like
- Each feature has a technical boundary definition.
- Features are linked to specific sections of the ARD.
- The `ledger.md` is updated with the new feature structure.

## Memory Integration
- Query `docs/cda/ledger.json` to see if features have already been mapped.
- Read `docs/cda/PRD.md` for the original feature list.

## Process Details

### Phase 1: Feature Scaffolding
- For each feature listed in the PRD:
    - Determine its technical complexity and ARD dependencies.
    - Use `write-artifact --path FTR-X/feature.md`.
    - Write the `feature.md` content.
    - Include sections for: Technical Scope, ARD References, and Shared Dependencies.

### Phase 2: Ledger Update
- For each generated feature, use `write-artifact --path FTR-X/feature.md` with metadata:
  ```yaml
  type: 'FEATURE'
  id: 'FTR-X'
  name: 'Feature Name'
  status: 'complete'
  parent_id: 'ARD'
  ```

## After the Session
- Remind the user that the BA agent can now proceed with User Story generation (`define-user-stories`) for these features.
