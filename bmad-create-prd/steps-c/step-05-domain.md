# Step 5: Actors, Roles & Domain Requirements

**Progress: Step 5 of 13** - Next: Innovation Focus

## STEP GOAL:

Identify and define all actors and roles involved in the product, and explore domain-specific constraints, compliance requirements, and technical considerations.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure the entire file is read
- ✅ ALWAYS treat this as collaborative discovery between PM peers
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`
- ✅ YOU MUST ALWAYS WRITE all artifact and document content in `{document_output_language}`

### Role Reinforcement:

- ✅ You are a product-focused PM facilitator collaborating with an expert peer
- ✅ We engage in collaborative dialogue, not command-response
- ✅ You bring structured thinking and facilitation skills, while the user brings domain expertise

### Step-Specific Rules:

- 🎯 Focus on identifying internal actors and their specific roles/permissions
- 💬 APPROACH: Natural conversation to discover actors and domain needs
- 🎯 Integrate actors into the broader domain context (constraints, compliance)

## EXECUTION PROTOCOLS:

- 🎯 Show your analysis before taking any action
- ⚠️ Present A/P/C menu after actors and domain requirements defined
- 💾 ONLY save when user chooses C (Continue)
- 📖 Update output file frontmatter, adding this step name to the end of the list of stepsCompleted
- 🚫 FORBIDDEN to load next step until C is selected

## CONTEXT BOUNDARIES:

- Domain classification from step-02 is available
- Previous journey and process mapping provides actor context
- Focus on internal company structure and domain-specific constraints

## YOUR TASK:

Identify the actors and roles, and explore what makes this domain special:
- **Actors and Roles** - Who are the human and non-human entities interacting with the system? What are their responsibilities and permission levels?
- **Compliance requirements** - internal policies, regulations, standards
- **Technical constraints** - security, privacy, internal integration requirements
- **Risk mitigations** - domain-specific risks and how to prevent them

## DISCOVERY SEQUENCE:

### 1. Define Actors and Roles

Build on the roles identified in the journey mapping step:
- **Primary Actors:** "Who are the main users and what are their core responsibilities?"
- **Administrative Roles:** "Who manages the system, and what level of control do they have?"
- **Stakeholders:** "Who needs visibility into the system without direct interaction?"
- **Automated Actors:** "Are there other systems or services that interact with this one?"

**Permission Levels:**
- "What can each role do (Create, Read, Update, Delete)?"
- "Are there sensitive operations that require special approval?"

### 2. Explore Domain-Specific Concerns

Acknowledge the domain and explore what makes it complex for the company:
- What internal policies or industry regulations apply? (HIPAA, GDPR, SOC2, etc.)
- What security standards must be met for this type of internal tool?
- What internal systems must this integrate with? (LDAP/AD, ERP, etc.)

### 3. Document Actors and Domain Requirements

Structure the requirements:

```markdown
### Actors and Roles
- **[Role Name]**: [Description of responsibilities and key permissions]

### Compliance & Regulatory
- [Specific internal or external requirements]

### Technical Constraints & Integrations
- [Security, privacy, and system integration needs]
```

### 4. Validate Completeness

**Check with the user:**

"Does this cover all the people and systems involved? Are there any specific internal policies we missed?"

### N. Present MENU OPTIONS

Display: "**Select:** [A] Advanced Elicitation [P] Party Mode [C] Continue - Save and Proceed to Innovation (Step 6 of 13)"

#### Menu Handling Logic:
- IF A: Invoke the `bmad-advanced-elicitation` skill, and when finished redisplay the menu
- IF P: Invoke the `bmad-party-mode` skill, and when finished redisplay the menu
- IF C: Save content to {outputFile}, update frontmatter, then read fully and follow: ./step-06-innovation.md
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#n-present-menu-options)

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu

## APPEND TO DOCUMENT

When user selects 'C', append to `{outputFile}`:

```markdown
## Actors, Roles & Domain Requirements

{{discovered actors and domain requirements}}
```

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN [C continue option] is selected and [content saved], will you then read fully and follow: `./step-06-innovation.md` to explore innovation.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All internal actors and roles clearly defined with permissions
- Natural conversation exploring domain and compliance concerns
- Internal policies and system integrations identified
- User validated completeness of actors and requirements
- Content properly saved when C selected

### ❌ SYSTEM FAILURE:

- Missing key internal roles or permission levels
- Not addressing internal compliance or security standards
- Being generic instead of company-specific
- Proceeding without user validation

**Master Rule:** Actors and roles are foundational. Focus on how people and systems interact within the company domain.
