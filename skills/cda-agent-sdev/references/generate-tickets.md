# Capability: generate-tickets

## Outcome
A set of vertical-slice tickets (TCK-X) that are ready for implementation.

## What Success Looks Like
- **Actionable:** Each ticket has enough technical detail for an agent to write the code.
- **Vertical:** Every ticket addresses FE, BE, and DB requirements where applicable.
- **Structured:** Tickets are stored in `USR-X/tickets/TCK-Y/` with all necessary metadata.
- **Ledger Updated:** Every ticket is registered in the project ledger.

## Memory Integration
- Read `docs/cda/ledger.json` to find the target User Story.
- Read `user-story.md` for BDD criteria.
- Read `ARD/` for architectural constraints.

## Process Details

### Phase 1: Task Decomposition
- Break the User Story into the smallest possible units of value.
- Identify the impacted layers (Frontend, Backend, Database).
- Check against `{agent.standards_files}` for layer-specific requirements.

### Phase 2: Ticket Authoring
- For each ticket:
    - Use `write-artifact --path USR-X/tickets/TCK-Y/ticket.md` to create the hierarchy.
    - Write `ticket.md` with sections: Context, Target Files, Implementation Steps (FE/BE/DB), and Test Plan.
    - (Optional) Write `be.md`, `fe.md`, `db.md` for detailed technical specs if the `ticket.md` gets too large.

### Phase 3: Registration
- For each ticket, use `write-artifact --path USR-X/tickets/TCK-Y/ticket.md` with metadata:
  ```yaml
  type: 'TICKET'
  id: 'TCK-Y'
  name: 'Ticket Name'
  status: 'ready'
  parent_id: 'USR-X'
  ```

## After the Session
- Remind the user they can now trigger `execute-implementation` for these tickets.
