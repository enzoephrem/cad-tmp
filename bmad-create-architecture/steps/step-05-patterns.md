# Step 5: Implementation Patterns & Consistency Rules (Power Stack Edition)

## MANDATORY EXECUTION RULES (READ FIRST):

- 🛑 NEVER generate content without user input

- 📖 CRITICAL: ALWAYS read the complete step file before taking any action - partial understanding leads to incomplete decisions
- 🔄 CRITICAL: When loading next step with 'C', ensure the entire file is read and understood before proceeding
- ✅ ALWAYS treat this as collaborative discovery between architectural peers
- 📋 YOU ARE A FACILITATOR, not a content generator
- 💬 FOCUS on patterns that prevent AI agent implementation conflicts in the **Power Stack**
- 🎯 EMPHASIZE what agents could decide DIFFERENTLY if not specified
- ⚠️ ABSOLUTELY NO TIME ESTIMATES - AI development speed has fundamentally changed
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

## EXECUTION PROTOCOLS:

- 🎯 Show your analysis before taking any action
- 🎯 Focus on consistency, not implementation details
- ⚠️ Present A/P/C menu after generating patterns content
- 💾 ONLY save when user chooses C (Continue)
- 📖 Update frontmatter `stepsCompleted: [1, 2, 3, 4, 5]` before loading next step
- 🚫 FORBIDDEN to load next step until C is selected

## CONTEXT BOUNDARIES:

- Core architectural decisions from step 4 are complete
- Technology stack: **FastAPI**, **Next.js**, **PostgreSQL**
- Focus on HOW agents should implement, not WHAT they should implement

## YOUR TASK:

Define implementation patterns and consistency rules that ensure multiple AI agents write compatible, consistent code that works together seamlessly in the Power Stack.

## PATTERNS DEFINITION SEQUENCE:

### 1. Confirm Power Stack Consistency Rules

"To ensure consistency between AI agents, we'll adopt these standard patterns for our stack. Do these work for you, or should we adjust any?"

**Naming & Formatting:**
- **Database:** `snake_case` for tables and columns (e.g., `user_profiles`, `created_at`).
- **Backend (FastAPI):** `snake_case` for functions and variables; `PascalCase` for Pydantic models and classes.
- **Frontend (Next.js):** `PascalCase` for components; `camelCase` for variables and hooks; `kebab-case` for CSS modules.

**API Standards:**
- **Status Codes:** Strict adherence to HTTP standards (200 for OK, 201 for Created, 400 for Bad Request, etc.).
- **Response Format:** All internal APIs return a consistent JSON structure (e.g., `{ "data": ..., "meta": ... }` or direct objects).
- **Error Handling:** FastAPI `HTTPException` with clear detail strings.

**Code Organization:**
- **FastAPI:** Use `APIRouter` for modularity; services for business logic; schemas for validation.
- **Next.js:** App Router structure; shared components in `@/components`; hooks in `@/hooks`.

### 2. Facilitate Specific Internal Patterns

"Beyond the defaults, let's decide on these internal-specific patterns:"

**Internal Process Patterns:**
- **Logging:** "How should agents log internal events? (e.g., structured JSON logs for ELK stack)"
- **Validation:** "Where should complex business validation happen? (e.g., strictly in FastAPI services)"
- **Frontend Forms:** "Standard library for internal forms? (e.g., React Hook Form + Zod)"

### 3. Generate Patterns Content

Prepare the content to append to the document:

#### Content Structure:

```markdown
## Implementation Patterns & Consistency Rules

### Power Stack Standard Patterns

**Naming Conventions:**
- Database: {{db_naming}}
- Backend: {{backend_naming}}
- Frontend: {{frontend_naming}}

**API & Communication Patterns:**
- Response Structure: {{api_response_pattern}}
- Error Handling: {{error_handling_pattern}}
- Validation Strategy: {{validation_pattern}}

### Internal Process & Consistency Rules

**Logging & Observability:**
{{internal_logging_rules}}

**State Management & Data Flow:**
{{internal_state_patterns}}

**Frontend Component & Styling Patterns:**
{{frontend_design_patterns}}

### Mandatory Agent Rules
- **Rule 1:** Agents MUST use Pydantic for all FastAPI request/response validation.
- **Rule 2:** Agents MUST use TypeScript strict mode for all Next.js code.
- **Rule 3:** Agents MUST follow the defined project structure exactly.
```

### 4. Present Content and Menu

Show the generated patterns content and present choices:

"I've documented the implementation patterns that will keep our AI agents aligned.

**Here's what I'll add to the document:**

[Show the complete markdown content from step 3]

**What would you like to do?**
[A] Advanced Elicitation - Explore more complex consistency patterns
[P] Party Mode - Review patterns from different implementation perspectives
[C] Continue - Save these patterns and move to project structure"

### 5. Handle Menu Selection

#### If 'C' (Continue):

- Append the final content to `{planning_artifacts}/architecture.md`
- Update frontmatter: `stepsCompleted: [1, 2, 3, 4, 5]`
- Load `./step-06-structure.md`

## APPEND TO DOCUMENT:

When user selects 'C', append the content directly to the document using the structure from step 3.

## SUCCESS METRICS:

✅ Power Stack patterns clearly defined and confirmed
✅ All potential AI agent conflict points addressed
✅ Internal process patterns documented
✅ Mandatory agent rules established
✅ Content properly appended to document when C selected

## FAILURE MODES:

❌ Missing critical patterns for FastAPI, Next.js, or PostgreSQL
❌ Being too vague about naming or structure
❌ Not addressing internal logging or validation standards
❌ Appending content without user selecting 'C'

**Master Rule:** Consistency is the goal. Give AI agents clear, unambiguous rules so they don't fight each other's code.
