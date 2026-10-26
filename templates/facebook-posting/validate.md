# Validate: Facebook post

Validate the exact request and record each finding before decision. Do not mutate a shared browser without current ownership, even during capability checks.

- Require an explicitly supplied final caption, image reference, owned Page, feed placement, timing and publication authority. If final caption is absent, reject with the exact missing-input reason; do not write copy for the requester. Preserve original inputs.
- Resolve the Page unambiguously through the actual owned-Page list and retain its native identity. Similar display names alone are insufficient. Verify the configured account can act for that Page and supports the requested native format.
- Check local tool configuration is complete: authorized supported browser/profile, canonical shared-resource key, available tool procedure, upload requirements and the chosen report channel/procedure and required identity/recipient fields when applicable. Missing required report configuration prevents acceptance. A transient outage of an otherwise configured communication service follows the generic nonblocking reporting rule.
- Use only the explicitly authorized supported browser backend and its current API documentation. Configured supported Chrome is eligible when its upload prerequisites pass, even if internal iab is unavailable. Do not infer an iab-only rule or load a shared browser skill.
- Verify the supplied asset is readable to the configured upload tool without changing or substituting it. If local-file access is disabled, record the browser's actual access blocker and required operator intervention. Do not change permissions, switch backends without authority or diagnose missing credentials without evidence. Promptly invoke the configured intervention report; keep the request resumable.
- Compare a requested scheduled instant, including its timezone/offset, with the observed current instant. An instant in the past is a `past-schedule` exception: preserve it, hold submission and invoke the immediate failure report. Never guess a replacement time or publish now as fallback.
- For a future instant, verify an existing authorized native tool can establish that scheduled action. If unavailable, record a scheduling blocker and promptly report required intervention. Do not build a scheduler, invent a wake-up trigger or claim scheduling from a stored request alone.

Read-only checks grant no publication authority. Where checks require browser navigation or another shared mutation, acquire the declared profile resource first under the generic ownership procedure.
