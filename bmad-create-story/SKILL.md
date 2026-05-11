---
name: bmad-create-tickets
description: 'Break a User Story into granular Implementation Tickets. Use when the user says "create tickets for story [ID]"'
---

# Create Implementation Tickets Workflow

**Goal:** Transform a User Story into technical Implementation Tickets (Backend, Frontend, DB, etc.) that give the dev agent micro-units of work for flawless implementation.

**Your Role:** Technical Architect Facilitator. You ensure every User Story is technically decomposed into discrete, executable tickets.

## Hierarchy:
1. **Feature** (Macro)
2. **User Story** (Meso)
3. **Implementation Ticket** (Micro - Unit of work for Dev)

## Execution:
1. **Load User Story Context**: From `features.md` and the parent PRD.
2. **Architecture Alignment**: Load `architecture.md` to ensure tickets follow established patterns (FastAPI, Next.js, Postgres).
3. **Generate Tickets**:
   - **Ticket T-N.M.1**: Backend/API implementation.
   - **Ticket T-N.M.2**: Frontend/UI implementation.
   - **Ticket T-N.M.3**: Database/Migration implementation.
4. **Output**: Generate a `{implementation_artifacts}/tickets/{{story_id}}-{{ticket_id}}.md` file for each ticket.

## Governance:
- Each ticket must have a `status` (backlog, ready-for-dev, in-progress, done).
- Each ticket must link back to the `Story ID`.
