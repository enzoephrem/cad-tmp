---
outputFile: '{planning_artifacts}/implementation-readiness-report-{{date}}.md'
---

# Step 5: Hierarchy Quality Review (Feature -> Story -> Ticket)

## STEP GOAL:

To validate the macro-to-micro hierarchy (Feature -> User Story -> Implementation Ticket) against best practices, focusing on value propositions, incremental delivery, and granular technical decomposition.

## MANDATORY EXECUTION RULES (READ FIRST):

### Role Reinforcement:

- ✅ You are a HIERARCHY QUALITY ENFORCER
- ✅ Features MUST have value propositions
- ✅ Stories MUST be broken into granular Tickets (Backend, Frontend, DB)
- ✅ Tickets MUST be micro-units of work

## HIERARCHY QUALITY REVIEW PROCESS:

### 1. Feature Layer Validation
For each Feature:
- **Value Proposition:** Does it deliver clear business value to the company?
- **Requirements Mapping:** Does it group the correct FRs from the PRD?

### 2. User Story Layer Validation
Check each Story:
- **Incremental Value:** Does the story deliver a testable part of the Feature?
- **Size:** Is it small enough to be broken into micro-tickets?

### 3. Implementation Ticket Layer Validation (CRITICAL)
Verify that each User Story has corresponding Tickets:
- **Decomposition:** Is the story broken into logical technical units (e.g., FastAPI Backend, Next.js Frontend, SQL Migration)?
- **Micro-Targeting:** Is each ticket small enough for a single focused dev session?
- **Traceability:** Does every ticket link back to a parent Story and Feature?

### 4. Best Practices Compliance Checklist

- [ ] Feature value propositions are clearly defined
- [ ] Every User Story belongs to a Feature
- [ ] Every User Story is broken down into technical Tickets
- [ ] Tickets follow the "Power Stack" patterns (FastAPI/Next.js/Postgres)
- [ ] No "Technical Debt Only" features - everything drives company value

### 5. Quality Assessment Documentation

#### 🔴 Critical Violations
- User Stories not broken down into technical tickets
- Features missing value propositions
- Forward dependencies between tickets that block progress

#### 🟠 Major Issues
- Vague ticket descriptions
- Tickets that are too large (multi-day tasks)
- Missing database migration tickets for schema changes

### 8. Autonomous Review Execution

This review runs autonomously to maintain standards:

- Apply best practices without compromise
- Document every violation with specific examples
- Provide clear remediation guidance
- Prepare recommendations for each issue

## REVIEW COMPLETION:

After completing epic quality review:

- Update {outputFile} with all quality findings
- Document specific best practices violations
- Provide actionable recommendations
- Load ./step-06-final-assessment.md for final readiness assessment

## CRITICAL STEP COMPLETION NOTE

This step executes autonomously. Load ./step-06-final-assessment.md only after complete epic quality review is documented.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All epics validated against best practices
- Every dependency checked and verified
- Quality violations documented with examples
- Clear remediation guidance provided
- No compromise on standards enforcement

### ❌ SYSTEM FAILURE:

- Accepting technical epics as valid
- Ignoring forward dependencies
- Not verifying story sizing
- Overlooking obvious violations

**Master Rule:** Enforce best practices rigorously. Find all violations.
