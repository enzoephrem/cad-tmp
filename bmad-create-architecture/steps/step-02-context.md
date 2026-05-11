# Step 2: Project Context & Internal Constraints Analysis

## MANDATORY EXECUTION RULES (READ FIRST):

- 🛑 NEVER generate content without user input

- 📖 CRITICAL: ALWAYS read the complete step file before taking any action - partial understanding leads to incomplete decisions
- 🔄 CRITICAL: When loading next step with 'C', ensure the entire file is read and understood before proceeding
- ✅ ALWAYS treat this as collaborative discovery between architectural peers
- 📋 YOU ARE A FACILITATOR, not a content generator
- 💬 FOCUS on understanding project scope, internal requirements, and company constraints
- 🎯 ANALYZE loaded documents, don't assume or generate requirements
- ⚠️ ABSOLUTELY NO TIME ESTIMATES - AI development speed has fundamentally changed
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

## EXECUTION PROTOCOLS:

- 🎯 Show your analysis before taking any action
- ⚠️ Present A/P/C menu after generating project context analysis
- 💾 ONLY save when user chooses C (Continue)
- 📖 Update frontmatter `stepsCompleted: [1, 2]` before loading next step
- 🚫 FORBIDDEN to load next step until C is selected

## COLLABORATION MENUS (A/P/C):

This step will generate content and present choices:

- **A (Advanced Elicitation)**: Use discovery protocols to develop deeper insights about internal project context and architectural implications
- **P (Party Mode)**: Bring multiple perspectives to analyze project requirements from different internal architectural angles
- **C (Continue)**: Save the content to the document and proceed to next step

## CONTEXT BOUNDARIES:

- Current document and frontmatter from step 1 are available
- Input documents already loaded are in memory (PRD, epics, internal specs, etc.)
- Focus on architectural implications for the company
- No technology decisions yet - pure analysis phase

## YOUR TASK:

Fully read and Analyze the loaded project documents to understand architectural scope, internal requirements, and company constraints before beginning decision making.

## CONTEXT ANALYSIS SEQUENCE:

### 1. Review Internal Project Requirements

**From PRD Analysis:**

- Extract and analyze Functional Requirements (FRs) for internal workflows
- Identify Non-Functional Requirements (NFRs) like internal security, data privacy, and compliance with company policies
- Note any internal technical constraints or dependencies (e.g., existing legacy systems, internal APIs)
- Count and categorize requirements to understand the internal scale

**From Epics/Stories (if available):**

- Map internal business processes to architectural components
- Extract acceptance criteria for technical implications within the company environment
- Identify cross-cutting concerns that span multiple internal departments

**Internal Constraints & Stakeholders:**

- **Stakeholder Needs:** "Who within the company relies on this system's architectural stability?"
- **Internal Security:** "What are the company's rules for internal data handling and SSO?"
- **Compliance:** "What internal or industry-specific audits must we pass?"
- **Legacy Integration:** "What existing company systems must we talk to?"

### 2. Project Scale Assessment

Calculate and present project complexity within the company context:

**Complexity Indicators:**

- Internal system integration complexity
- Data sensitivity and privacy requirements
- Concurrency and usage patterns by internal staff
- Regulatory/Internal compliance requirements
- Interaction complexity for internal power users

### 3. Reflect Understanding

Present your analysis back to user for validation:

"I'm reviewing your internal project documentation for {{project_name}}.

**Key architectural aspects I notice for our environment:**

- [Summarize core internal functionality from FRs]
- [Note critical internal NFRs that will shape architecture]
- [Identify specific internal technical challenges or constraints]
- [Highlight any company-specific regulatory or compliance requirements]

**Scale indicators:**

- Project complexity appears to be: [low/medium/high/enterprise]
- Primary technical domain: [internal web/mobile/api/backend/etc]
- Cross-cutting concerns identified: [list major ones]

Does this match your understanding of the project's internal scope and requirements?"

### 4. Generate Project Context Content

Prepare the content to append to the document:

#### Content Structure:

```markdown
## Project Context & Internal Constraints Analysis

### Requirements Overview

**Functional Requirements (Internal):**
{{analysis of FRs and what they mean architecturally for the company}}

**Non-Functional Requirements (Security & Compliance):**
{{internal NFRs that will drive architectural decisions}}

**Scale & Complexity:**
{{project_scale_assessment}}

- Primary internal domain: {{technical_domain}}
- Complexity level: {{complexity_level}}

### Internal Constraints & Dependencies

{{known_company_constraints_and_legacy_dependencies}}

### Cross-Cutting Concerns Identified

{{concerns_that_will_affect_multiple_internal_components}}
```

### 5. Present Content and Menu

Show the generated content and present choices:

"I've drafted the Project Context and Internal Constraints Analysis. This sets the foundation for our internal architectural decisions.

**Here's what I'll add to the document:**

[Show the complete markdown content from step 4]

**What would you like to do?**
[A] Advanced Elicitation - Let's dive deeper into internal architectural implications
[P] Party Mode - Bring different internal perspectives to analyze requirements
[C] Continue - Save this analysis and move to technical foundations"

### 6. Handle Menu Selection

#### If 'C' (Continue):

- Append the final content to `{planning_artifacts}/architecture.md`
- Update frontmatter: `stepsCompleted: [1, 2]`
- Load `./step-03-starter.md`

## APPEND TO DOCUMENT:

When user selects 'C', append the content directly to the document using the structure from step 4.

## SUCCESS METRICS:

✅ All input documents thoroughly analyzed for architectural implications
✅ Project scope and complexity clearly assessed and validated
✅ Technical constraints and dependencies identified
✅ Cross-cutting concerns mapped for architectural planning
✅ User confirmation of project understanding
✅ A/P/C menu presented and handled correctly
✅ Content properly appended to document when C selected

## FAILURE MODES:

❌ Skimming documents without deep architectural analysis
❌ Missing or misinterpreting critical NFRs
❌ Not validating project understanding with user
❌ Underestimating complexity indicators
❌ Generating content without real analysis of loaded documents
❌ Not presenting A/P/C menu after content generation

❌ **CRITICAL**: Reading only partial step file - leads to incomplete understanding and poor decisions
❌ **CRITICAL**: Proceeding with 'C' without fully reading and understanding the next step file
❌ **CRITICAL**: Making decisions without complete understanding of step requirements and protocols

## NEXT STEP:

After user selects 'C' and content is saved to document, load `./step-03-starter.md` to evaluate starter template options.

Remember: Do NOT proceed to step-03 until user explicitly selects 'C' from the A/P/C menu and content is saved!
