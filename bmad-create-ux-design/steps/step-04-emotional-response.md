# Step 4: System Trust & Reliability

## MANDATORY EXECUTION RULES:
- 🛑 NEVER generate content without user input
- 💬 FOCUS on transparency, data accuracy, and user confidence
- 🎯 No "emotional delight" - focus on "professional reliability"

## SYSTEM TRUST DISCOVERY SEQUENCE:

### 1. Data Transparency
"How do we show internal users that the system is working correctly?
- Status indicators for background tasks?
- Visibility into 'Last Updated' timestamps?
- Success/Failure feedback for every API call?"

### 2. Error Recovery
"When an internal process fails, how do we help the user fix it?
- Actionable error messages (instead of generic codes)?
- Rolling back or 'Undo' capabilities for internal data?"

### 3. Permission Visibility
"How do we handle different roles?
- Disabling vs. hiding features based on CRUD permissions?
- Clear messaging on why a user cannot perform an action?"

### 4. Generate Trust Content
Append to document:
```markdown
## System Trust & Reliability Specs

### Feedback & Transparency Patterns
[How the UI communicates system state]

### Error Handling & Recovery Strategy
[UX approach to helping users recover from process failures]

### Access Control UX
[How permissions are reflected in the UI]
```

## NEXT STEP:
Save and load `./step-06-design-system.md` (skipping inspiration as it's less relevant for internal).
