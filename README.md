# Service executor skill

A self-contained agent skill with four stages:

1. **Validate** — apply the service's injected requirements and checks.
2. **Accept/reject** — apply its injected decision constraints and authority.
3. **Execute** — perform its injected task procedure only after acceptance.
4. **Report** — follow its injected reporting procedure for every outcome.

The generic skill owns sequencing, durable request records, concurrency and recovery. Service-specific behavior belongs in explicit injections bundled with the service template. Runtime instructions must not load other skills or shared operating procedures.

The first service template will live in `templates/facebook-posting/`. Customization instructions will explain how an operator creates or changes these four injections; executing agents do not amend themselves.

This repository is separate from any deployed Facebook worker. Credentials, account-specific connection settings, request histories and live media do not belong in this public repository.

## Status

SDD is initialized at Internal assurance and the constitution is approved. [Change 0001](specs/changes/0001-service-executor/proposal.md) is in clarification: [draft requirements](specs/changes/0001-service-executor/spec-delta.md) cover the lifecycle and templates, and [review round 1](specs/changes/0001-service-executor/clarifications.md) retains one pending operator decision about temporary email unavailability before posting. Design and implementation are pending their SDD phases and approvals; the Facebook template currently contains design input only.
