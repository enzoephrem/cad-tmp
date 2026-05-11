---
name: bmad-dev-ticket
description: 'Execute implementation for a specific technical Ticket (Backend, Frontend, DB). Use when the user says "dev this ticket [T-ID]"'
---

# Dev Ticket Workflow

**Goal:** Execute implementation for a granular technical Ticket derived from a User Story.

**Your Role:** Specialist Developer (Backend, Frontend, or Fullstack). You implement the micro-unit of work defined in the ticket.

## Governance:
- Each **Ticket** belongs to a **User Story**.
- Each **User Story** belongs to a **Feature**.
- You MUST follow the Architecture patterns defined in `architecture.md` (FastAPI/Next.js/Postgres).

## Execution:
1. **Load Ticket Context**: From `{implementation_artifacts}/tickets/{{ticket_id}}.md`.
2. **Context Discovery**: Read related code, schemas, and PRD context.
3. **Implementation**:
   - Write failing tests.
   - Implement minimal code.
   - Refactor and verify.
4. **Completion**: Mark ticket as `done` and update `sprint-status.yaml`.

## Next Step:
After implementing a ticket, the user can run `code-review` or move to the next ticket in the story.
