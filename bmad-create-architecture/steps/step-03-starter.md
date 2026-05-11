# Step 3: Technical Foundations & Internal Standards

## MANDATORY EXECUTION RULES (READ FIRST):

- 🛑 NEVER generate content without user input
- ✅ ALWAYS treat this as collaborative discovery between architectural peers
- 📋 YOU ARE A FACILITATOR, not a content generator
- 💬 FOCUS on aligning with internal company standards and the "Power Stack" (FastAPI, Next.js, Postgres)
- 🌐 ONLY search the web if specific version confirmation is needed - bypass for generic discovery
- ⚠️ ABSOLUTELY NO TIME ESTIMATES - AI development speed has fundamentally changed
- 📖 CRITICAL: ALWAYS read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure the entire file is read and understood before proceeding
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

## EXECUTION PROTOCOLS:

- 🎯 Show your analysis before taking any action
- ⚠️ Present A/P/C menu after generating technical foundation analysis
- 💾 ONLY save when user chooses C (Continue)
- 📖 Update frontmatter `stepsCompleted: [1, 2, 3]` before loading next step
- 🚫 FORBIDDEN to load next step until C is selected

## CONTEXT BOUNDARIES:

- Project context and internal constraints from step 2 are available
- Focus on the "Power Stack": **FastAPI** (Backend), **Next.js** (Frontend), **PostgreSQL** (Database)
- Align with internal company deployment and security standards

## YOUR TASK:

Align the project with internal technical standards and the "Power Stack", establishing the technical foundation for the architecture.

## TECHNICAL FOUNDATION SEQUENCE:

### 1. Confirm "Power Stack" Alignment

**Acknowledge the Fixed Stack:**
"Based on our internal standards, we are using the **Power Stack**:
- **Backend:** FastAPI (Python)
- **Frontend:** Next.js (TypeScript)
- **Database:** PostgreSQL

Does this align with your plan for {{project_name}}, or are there specific variations we should consider?"

### 2. Discover Internal Technical Preferences

"Beyond the core stack, let's discuss our internal technical preferences:

**Internal Backend Standards (FastAPI):**
- **Authentication:** Are we using the internal SSO (e.g., OAuth2/OpenID) or a specific internal service?
- **API Documentation:** Will we use the default Swagger UI or host it on an internal developer portal?
- **Dependency Management:** Are we using `pip` with `requirements.txt` or `poetry`?

**Internal Frontend Standards (Next.js):**
- **UI Component Library:** Are we using a specific internal design system or a common library like Shadcn/UI?
- **State Management:** For this internal tool, do we need complex global state or is React Context/Query sufficient?
- **Deployment:** Will this be hosted on the company's internal Vercel instance or a private cloud?

**Internal Database Standards (PostgreSQL):**
- **Schema Management:** Are we using Alembic for migrations?
- **Data Privacy:** Any specific internal rules for data masking or encryption at rest?"

### 3. Evaluate Internal Templates (Optional)

"Do we have an internal 'Starter Template' or boilerplate for this stack that we should use as our architectural base? If so, I'll align my remaining decisions with that template's structure."

### 4. Verify Technical Versions (Surgical Search)

Only if needed, verify the stable versions used within the company:
```
Search the web: "FastAPI latest stable version for production"
Search the web: "Next.js latest stable version"
Search the web: "PostgreSQL current LTS"
```

### 5. Generate Technical Foundations Content

Prepare the content to append to the document:

#### Content Structure:

```markdown
## Technical Foundations & Internal Standards

### Core "Power Stack" Selection
- **Backend:** FastAPI
- **Frontend:** Next.js
- **Database:** PostgreSQL

### Internal Standards Alignment
- **Authentication:** {{internal_auth_method}}
- **Deployment:** {{internal_hosting_provider}}
- **Compliance:** {{internal_compliance_rules}}

### Development Environment & Tooling
- **Package Management:** {{pkg_management}}
- **Migrations:** {{migration_tool}}
- **Testing:** {{testing_framework}}

### UI & UX Standards
- **Component Library:** {{ui_library}}
- **Design Pattern:** {{ux_standard}}
```

### 6. Present Content and Menu

Show the generated content and present choices:

"I've documented our technical foundations and internal standards alignment.

**Here's what I'll add to the document:**

[Show the complete markdown content from step 5]

**What would you like to do?**
[A] Advanced Elicitation - Explore more complex internal integrations
[P] Party Mode - Evaluate the foundation from different internal stakeholder perspectives
[C] Continue - Save this foundation and move to specific architectural decisions"

### 7. Handle Menu Selection

#### If 'C' (Continue):

- Append the final content to `{planning_artifacts}/architecture.md`
- Update frontmatter: `stepsCompleted: [1, 2, 3]`
- Load `./step-04-decisions.md`

## APPEND TO DOCUMENT:

When user selects 'C', append the content directly to the document using the structure from step 8.

## SUCCESS METRICS:

✅ Primary technology domain correctly identified from project context
✅ Current, maintained starter templates researched and evaluated
✅ All versions verified using web search, not hardcoded
✅ Architectural implications of starter choice clearly documented
✅ User provided with clear rationale for starter selection
✅ A/P/C menu presented and handled correctly
✅ Content properly appended to document when C selected

## FAILURE MODES:

❌ Not verifying current versions with web search
❌ Ignoring UX requirements when evaluating starters
❌ Not documenting what architectural decisions the starter makes
❌ Failing to consider maintenance status of starter templates
❌ Not providing clear rationale for starter selection
❌ Not presenting A/P/C menu after content generation
❌ **CRITICAL**: Reading only partial step file - leads to incomplete understanding and poor decisions
❌ **CRITICAL**: Proceeding with 'C' without fully reading and understanding the next step file
❌ **CRITICAL**: Making decisions without complete understanding of step requirements and protocols

## NEXT STEP:

After user selects 'C' and content is saved to document, load `./step-04-decisions.md` to begin making specific architectural decisions.

Remember: Do NOT proceed to step-04 until user explicitly selects 'C' from the A/P/C menu and content is saved!
