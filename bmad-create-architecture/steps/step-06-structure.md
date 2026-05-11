# Step 6: Project Structure & Boundaries (Internal Power Stack)

## MANDATORY EXECUTION RULES (READ FIRST):

- 🛑 NEVER generate content without user input

- 📖 CRITICAL: ALWAYS read the complete step file before taking any action - partial understanding leads to incomplete decisions
- 🔄 CRITICAL: When loading next step with 'C', ensure the entire file is read and understood before proceeding
- ✅ ALWAYS treat this as collaborative discovery between architectural peers
- 📋 YOU ARE A FACILITATOR, not a content generator
- 💬 FOCUS on defining complete project structure and clear boundaries for our **Power Stack**
- 🗺️ MAP Features to architectural components
- ⚠️ ABSOLUTELY NO TIME ESTIMATES - AI development speed has fundamentally changed
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

## EXECUTION PROTOCOLS:

- 🎯 Show your analysis before taking any action
- 🗺️ Create complete project tree, not generic placeholders
- ⚠️ Present A/P/C menu after generating project structure
- 💾 ONLY save when user chooses C (Continue)
- 📖 Update frontmatter `stepsCompleted: [1, 2, 3, 4, 5, 6]` before loading next step
- 🚫 FORBIDDEN to load next step until C is selected

## CONTEXT BOUNDARIES:

- All previous architectural decisions are complete
- Implementation patterns and consistency rules are defined
- Focus on the **FastAPI + Next.js + PostgreSQL** monorepo or sharded structure
- Map Features from the PRD to specific files and directories

## YOUR TASK:

Define the complete project structure and architectural boundaries for our Power Stack, creating a concrete implementation guide for AI agents.

## PROJECT STRUCTURE SEQUENCE:

### 1. Define Power Stack Directory Structure

"Based on our stack and internal standards, here is the proposed project structure. We'll use a clear separation between our FastAPI backend, Next.js frontend, and shared internal assets."

**The Internal Power Stack Tree:**

```
project-root/
├── backend/                # FastAPI Application
│   ├── main.py             # Entry point
│   ├── api/                # APIRouter modules
│   ├── core/               # Internal config, security, SSO
│   ├── models/             # SQLAlchemy/SQLModel models
│   ├── schemas/            # Pydantic schemas
│   ├── services/           # Internal business logic
│   ├── db/                 # Session management & migrations (Alembic)
│   └── tests/              # Backend unit/integration tests
├── frontend/               # Next.js Application
│   ├── src/
│   │   ├── app/            # App Router (pages, layouts)
│   │   ├── components/     # UI features & internal design system
│   │   ├── hooks/          # Custom hooks for internal data fetching
│   │   ├── lib/            # Internal API clients & utils
│   │   └── types/          # Shared TypeScript types
│   ├── public/             # Internal static assets
│   └── tests/              # Frontend unit/e2e tests
├── shared/                 # Shared internal configs, scripts, or proto files
├── docs/                   # Internal project documentation
├── .env.example            # Template for internal environment variables
├── docker-compose.yml      # Local dev environment (Postgres, Redis, etc.)
└── README.md               # Internal setup & architecture guide
```

### 2. Map Features to Structure

"We'll map our **Features** (modules of value proposition) to specific locations in this structure:"

**Feature Mapping Example:**
- **Feature: Internal Reporting**
  - Backend Logic: `backend/services/reporting.py`
  - Backend API: `backend/api/v1/reporting.py`
  - Frontend View: `frontend/src/app/reporting/page.tsx`
  - Frontend Logic: `frontend/src/hooks/useReporting.ts`

### 3. Define Integration Boundaries

- **API Boundary:** "Next.js will communicate with FastAPI via internal REST endpoints secured by our SSO."
- **Data Boundary:** "Only the FastAPI `db` module interacts directly with PostgreSQL."
- **State Boundary:** "Frontend state is managed locally in Next.js; persistence happens via FastAPI."

### 4. Generate Structure Content

Prepare the content to append to the document:

#### Content Structure:

```markdown
## Project Structure & Boundaries (Power Stack)

### Complete Project Directory Structure

[Insert the finalized directory tree based on conversation]

### Architectural Boundaries & Integration

**API Communication:**
{{api_boundary_details}}

**Data Access & Persistence:**
{{data_boundary_details}}

**Internal Service Boundaries:**
{{service_boundary_details}}

### Requirements to Structure Mapping

**Feature Mapping:**
{{mapping_of_features_to_directories}}

**Cross-Cutting Concerns (SSO, Logging, etc.):**
{{location_of_shared_internal_services}}
```

### 5. Present Content and Menu

Show the generated project structure content and present choices:

"I've created a complete project structure optimized for our Power Stack and internal environment.

**Here's what I'll add to the document:**

[Show the complete markdown content from step 4]

**What would you like to do?**
[A] Advanced Elicitation - Explore more complex organizational patterns for this stack
[P] Party Mode - Review structure from different internal development perspectives
[C] Continue - Save this structure and move to architecture validation"

### 6. Handle Menu Selection

#### If 'C' (Continue):

- Append the final content to `{planning_artifacts}/architecture.md`
- Update frontmatter: `stepsCompleted: [1, 2, 3, 4, 5, 6]`
- Load `./step-07-validation.md`

## APPEND TO DOCUMENT:

When user selects 'C', append the content directly to the document using the structure from step 4.

## SUCCESS METRICS:

✅ Complete project tree defined specifically for FastAPI/Next.js/Postgres
✅ All architectural boundaries clearly documented for the company environment
✅ **Features** mapped to specific locations
✅ Integration points and communication patterns defined for internal tools
✅ Content properly appended to document when C selected

**Master Rule:** Be specific. A clear, accurate tree is the best gift you can give an AI agent that needs to know where to put code.
