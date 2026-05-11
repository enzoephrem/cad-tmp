# Capability: execute-implementation

## Outcome
Functional, tested source code that implements a specific ticket.

## What Success Looks Like
- **Functional:** All BDD criteria from the parent User Story are met.
- **Tested:** Unit tests exist and pass for the new logic.
- **Standards Compliant:** Code follows naming conventions, telemetry requirements, and security rules from `./standards/`.
- **Integrated:** FE, BE, and DB layers work together as a single vertical slice.

## Memory Integration
- Read `ticket.md` and its slices (`be.md`, `fe.md`, `db.md`).
- Read parent `user-story.md` for BDD context.
- Read relevant `ARD/` chunks for system-wide patterns.

## Process Details

### Phase 1: Test Initialization (TDD)
- Based on the BDD criteria, write or update the test files.
- Run tests to confirm they fail (Red phase).

### Phase 2: Implementation
- Implement the Backend logic (APIs, Services, Logic).
- Implement the Database changes (Schemas, Migrations, Seeds).
- Implement the Frontend logic (Components, State, UI).
- Ensure all implementation matches the **Target Files** listed in the ticket.

### Phase 3: Verification
- Run the tests to confirm they pass (Green phase).
- Refactor if necessary while keeping tests green.
- Run `cda-wf-review` (optional) to ensure IT standards are met.

### Phase 4: Finalize
- Update the ticket metadata: set `status` to `complete`.
- Use `write-artifact --path USR-X/tickets/TCK-Y/ticket.md` with metadata:
  ```yaml
  status: 'complete'
  ```

## After the Session
- Notify the user that the implementation is complete and ready for deployment or higher-level review.
