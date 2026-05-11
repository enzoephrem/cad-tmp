---
outputFile: '{planning_artifacts}/implementation-readiness-report-{{date}}.md'
---

# Step 3: Feature Coverage Validation

## STEP GOAL:

To validate that all Features and Functional Requirements from the PRD are captured in the features and stories document, identifying any gaps in coverage.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an expert Product Manager
- ✅ Your expertise is in requirements traceability
- ✅ You ensure no requirements fall through the cracks
- ✅ Success is measured in complete Feature/FR coverage

### Step-Specific Rules:

- 🎯 Focus ONLY on Feature/FR coverage validation
- 🚫 Don't analyze story quality (that's later)
- 💬 Compare PRD Features against the breakdown document
- 🚪 Document every missing Feature or FR

## EXECUTION PROTOCOLS:

- 🎯 Load features and stories document completely
- 💾 Extract coverage from the document
- 📖 Compare against PRD Feature/FR list
- 🚫 FORBIDDEN to proceed without documenting gaps

## FEATURE COVERAGE VALIDATION PROCESS:

### 1. Initialize Coverage Validation

"Beginning **Feature Coverage Validation**.

I will:

1. Load the features and stories document
2. Extract Feature and FR coverage information
3. Compare against PRD Features/FRs from previous step
4. Identify any gaps in the breakdown"

### 2. Load Features Document

From the document inventory in step 1:

- Load the features and stories document (usually `features.md`)
- Read it completely to find coverage information

### 3. Extract Feature/FR Coverage

From the features document:

- Find which Features from the PRD are mapped to User Stories.
- Document which User Stories cover which FRs.

Format as:

```
## Feature/FR Coverage Extracted

Feature 1: [Name] - Covered
  - FR1: Covered in Story 1.1
  - FR2: Covered in Story 1.2
...
Total Features in breakdown: [count]
```

### 4. Compare Coverage Against PRD

Using the PRD list from step 2:

- Check each PRD Feature/FR against the breakdown.
- Identify any gaps.

Create coverage matrix:

```
## Feature Coverage Analysis

| Feature/FR | PRD Name | Breakdown Status |
| ---------- | -------- | ---------------- |
| Feature 1  | [Name]   | ✓ Covered        |
| FR1        | [Text]   | ✓ Story 1.1      |
| FR2        | [Text]   | ❌ MISSING       |
```

### 5. Document Missing Coverage

List all gaps:

```
## Missing Coverage

### Critical Gaps

Feature/FR: [Details]
- Impact: [Why this is critical]
- Recommendation: [Where to add this in the breakdown]
```

### 6. Add to Assessment Report

Append to {outputFile}:

```markdown
## Feature Coverage Validation

### Coverage Matrix

[Complete coverage matrix from section 4]

### Missing Requirements

[List of uncovered Features/FRs from section 5]

### Coverage Statistics

- Total PRD Features: [count]
- Features covered in breakdown: [count]
- Coverage percentage: [percentage]
```

### 7. Auto-Proceed to Next Step

After coverage validation complete, immediately load next step.

## PROCEEDING TO UX ALIGNMENT

Epic coverage validation complete. Read fully and follow: `./step-04-ux-alignment.md`

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Epics document loaded completely
- FR coverage extracted accurately
- All gaps identified and documented
- Coverage matrix created

### ❌ SYSTEM FAILURE:

- Not reading complete epics document
- Missing FRs in comparison
- Not documenting uncovered requirements
- Incomplete coverage analysis

**Master Rule:** Every FR must have a traceable implementation path.
