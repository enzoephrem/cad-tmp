# Step 4: Core Architectural & Internal Integration Decisions

## MANDATORY EXECUTION RULES (READ FIRST):

- 🛑 NEVER generate content without user input

- 📖 CRITICAL: ALWAYS read the complete step file before taking any action - partial understanding leads to incomplete decisions
- 🔄 CRITICAL: When loading next step with 'C', ensure the entire file is read and understood before proceeding
- ✅ ALWAYS treat this as collaborative discovery between architectural peers
- 📋 YOU ARE A FACILITATOR, not a content generator
- 💬 FOCUS on making critical architectural decisions for our internal environment
- 🌐 ONLY search the web if specific version confirmation is needed
- ⚠️ ABSOLUTELY NO TIME ESTIMATES - AI development speed has fundamentally changed
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

## EXECUTION PROTOCOLS:

- 🎯 Show your analysis before taking any action
- ⚠️ Present A/P/C menu after each major decision category
- 💾 ONLY save when user chooses C (Continue)
- 📖 Update frontmatter `stepsCompleted: [1, 2, 3, 4]` before loading next step
- 🚫 FORBIDDEN to load next step until C is selected

## COLLABORATION MENUS (A/P/C):

This step will generate content and present choices for each decision category:

- **A (Advanced Elicitation)**: Use discovery protocols to explore innovative approaches to specific decisions
- **P (Party Mode)**: Bring multiple perspectives to evaluate decision trade-offs
- **C (Continue)**: Save the current decisions and proceed to next decision category

## PROTOCOL INTEGRATION:

- When 'A' selected: Invoke the `bmad-advanced-elicitation` skill
- When 'P' selected: Invoke the `bmad-party-mode` skill
- PROTOCOLS always return to display this step's A/P/C menu after the A or P have completed
- User accepts/rejects protocol changes before proceeding

## CONTEXT BOUNDARIES:

- Project context and internal constraints from step 2 are available
- Technical foundations (FastAPI, Next.js, PostgreSQL) from step 3 are complete
- Focus on decisions critical to internal company success and implementation consistency
- Collaborative decision making, not recommendations

## YOUR TASK:

Facilitate collaborative architectural decision making, focusing on how our chosen "Power Stack" will integrate with internal company systems and requirements.

## DECISION MAKING SEQUENCE:

### 1. Load Technical Foundation Context

**Review Technical Foundations from Step 3:**
"We've established our foundation: **FastAPI**, **Next.js**, and **PostgreSQL**. Now let's make the specific architectural decisions that will guide implementation."

### 2. Internal Decision Categories

#### Category 1: Internal Data Architecture (PostgreSQL)

- **Schema Design:** "How will we structure our internal data models to support the business processes we mapped?"
- **Internal Integrations:** "Do we need to sync data from existing internal databases or ERP systems?"
- **Data Retention:** "What are the company's internal rules for data archiving and logs?"

#### Category 2: Internal Security & Access (SSO)

- **Authorization (RBAC):** "How will we map internal roles (from our PRD) to permissions in the system?"
- **Internal API Security:** "How will FastAPI secure internal service-to-service communication?"
- **Audit Logging:** "What internal auditing requirements must the architecture support?"

#### Category 3: API & Communication (FastAPI)

- **Internal API Patterns:** "Will we follow a specific internal RESTful standard or use FastAPI's specific features for internal services?"
- **Async Processing:** "Do we need background tasks (e.g., Celery/Redis) for long-running internal processes?"
- **Internal Documentation:** "How will we expose our API specs to other internal teams?"

#### Category 4: Frontend Architecture (Next.js)

- **Internal Dashboard Patterns:** "What are our standards for internal data-heavy views and forms?"
- **SSO Integration:** "How will we handle the session handoff from the company's SSO to our Next.js frontend?"
- **Internal Performance:** "What are the targets for internal tool responsiveness on the company network?"

#### Category 5: Internal Infrastructure & Ops

- **Environment Config:** "How will we manage internal secrets and environment variables securely?"
- **Internal CI/CD:** "How does the architecture support our internal deployment pipeline?"
- **Logging & Monitoring:** "Which internal company tools will we use for monitoring (e.g., ELK, Grafana)?"

### 3. Facilitate Each Decision Category

For each category, facilitate collaborative decision making:

**Present the Decision:**
"In our {{Decision_Category}}, we need to decide on {{Specific_Decision}}."

**Show Internal Best Practices:**
"Based on our stack and internal environment, the common approaches are:
{{internal_option_list_with_tradeoffs}}

Which approach aligns best with our project goals?"

**Record the Decision:**
- Category: {{category}}
- Decision: {{user_choice}}
- Rationale: {{user_reasoning_or_default}}
- Affects: {{internal_components}}

### 4. Generate Decisions Content

After facilitating all categories, prepare the content to append:

#### Content Structure:

```markdown
## Core Architectural & Internal Integration Decisions

### Internal Data Architecture (PostgreSQL)
{{data_related_decisions_with_rationale}}

### Internal Security & Access (SSO/RBAC)
{{security_related_decisions_with_rationale}}

### API & Internal Communication (FastAPI)
{{api_related_decisions_with_rationale}}

### Frontend & Internal UX (Next.js)
{{frontend_related_decisions_with_rationale}}

### Internal Infrastructure & Ops
{{infrastructure_related_decisions_with_rationale}}

### Internal Decision Impact Analysis
**Implementation Priority:**
{{ordered_list_of_internal_implementation_tasks}}
```

### 5. Present Content and Menu

Show the generated decisions content and present choices:

"I've documented our core architectural and internal integration decisions.

**Here's what I'll add to the document:**

[Show the complete markdown content from step 4]

**What would you like to do?**
[A] Advanced Elicitation - Explore more complex internal architectural patterns
[P] Party Mode - Review decisions from multiple internal technical perspectives
[C] Continue - Save these decisions and move to implementation patterns"

### 6. Handle Menu Selection

#### If 'C' (Continue):

- Append the final content to `{planning_artifacts}/architecture.md`
- Update frontmatter: `stepsCompleted: [1, 2, 3, 4]`
- Load `./step-05-patterns.md`

## APPEND TO DOCUMENT:

When user selects 'C', append the content directly to the document using the structure from step 4.

## SUCCESS METRICS:

✅ All critical architectural decisions made collaboratively
✅ Technology versions verified using web search
✅ Decision rationale clearly documented
✅ Cascading implications identified and addressed
✅ User provided appropriate level of explanation for skill level
✅ A/P/C menu presented and handled correctly for each category
✅ Content properly appended to document when C selected

## FAILURE MODES:

❌ Making recommendations instead of facilitating decisions
❌ Not verifying technology versions with web search
❌ Missing cascading implications between decisions
❌ Not adapting explanations to user skill level
❌ Forgetting to document decisions made by starter template
❌ Not presenting A/P/C menu after content generation

❌ **CRITICAL**: Reading only partial step file - leads to incomplete understanding and poor decisions
❌ **CRITICAL**: Proceeding with 'C' without fully reading and understanding the next step file
❌ **CRITICAL**: Making decisions without complete understanding of step requirements and protocols

## NEXT STEP:

After user selects 'C' and content is saved to document, load `./step-05-patterns.md` to define implementation patterns that ensure consistency across AI agents.

Remember: Do NOT proceed to step-05 until user explicitly selects 'C' from the A/P/C menu and content is saved!
