---
id: azure-openai-resilience
title: Azure OpenAI Retry and Fallback Strategy
tags: [azure, ai, openai, resilience, error-handling]
applies_to_phase: [implementation, code-review]
version: 1.0
---

# Azure OpenAI Resilience Standard

When integrating with Azure OpenAI, transient errors (e.g., rate limits `429`, server timeouts `500`) are expected. All implementations must use an exponential backoff retry strategy and, where critical, a fallback model or region.

## Rules
1. **Never** make a raw, un-wrapped call to the Azure OpenAI client.
2. Use a resilience library (e.g., `Tenacity` for Python, `Polly` for .NET) to handle retries.
3. Catch explicit exceptions (e.g., `RateLimitError`).
4. Log all retry attempts with a `WARNING` level, including the delay and attempt count.

## Validated Code Snippet (Python / FastAPI)

```python
import logging
from openai import AsyncAzureOpenAI, RateLimitError, APIConnectionError
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

logger = logging.getLogger(__name__)

# Standard retry configuration: 
# Wait 2^x * 1 second between each retry starting with 2 seconds, then up to 10 seconds, then 10 seconds afterwards
@retry(
    retry=retry_if_exception_type((RateLimitError, APIConnectionError)),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    stop=stop_after_attempt(5),
    before_sleep=lambda retry_state: logger.warning(
        f"Retrying Azure OpenAI call: attempt {retry_state.attempt_number} after error {retry_state.outcome.exception()}"
    )
)
async def generate_completion(client: AsyncAzureOpenAI, prompt: str, model: str):
    """
    Makes a standard, resilient call to Azure OpenAI.
    """
    response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response
```

## Agent Instructions
If you are generating an AI feature using Azure OpenAI, you must implement the `@retry` decorator exactly as shown above. If the target stack is .NET, you must implement the equivalent using `Polly.RetryAsync`.
