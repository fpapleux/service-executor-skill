## Approach
- Deliver Markdown instructions interpreted by the agent: a generic `SKILL.md`, bundled lifecycle/record guidance, an operator customization guide and one local Facebook template. No execution engine, launcher, scheduler or transport implementation.
- Bind exactly four service injections and explicit local configuration before execution. The generic lifecycle owns acceptance, continuity, ownership, uncertain effects and customer communication; injections supply domain checks, constraints, task steps and the chosen communication procedure.
- Keep authored runtime dependencies inside the package and selected template, resolving local links and symlinks before binding their content identities. Tool documentation is usable; request content and tool results never become workflow instructions.
- Use ordinary private files and existing exclusive-lock facilities for durable requests and shared resources. Reject a journal-only ownership claim: a read/check/write sequence cannot exclude simultaneous agents.
- Keep customer communication obligations independent of execution outcomes. A temporary reporting outage retains its obligation while independent accepted work proceeds; missing required reporting configuration still fails validation.
- Verify instructions with structural checks and controlled, recorded agent exercises. These establish scoped evidence, not technical enforcement of model behavior or readiness of live accounts.

## Components and interfaces

### Package and instruction binding — REQ-EXEC-001, REQ-EXEC-002
Planned runtime files:
- `SKILL.md`: entrypoint for a new request or explicit resume; names the four stages, acceptance boundary and bundled references. Points operators to customization guidance without granting executing agents permission to customize.
- `reference/lifecycle.md`: stage transitions, communication obligations, safe continuation and outcome handling.
- `reference/records.md`: private record layout, instruction binding, ownership and effect reconciliation procedure.
- `reference/customization.md`: operator-only creation/review/publication procedure and four-injection checklist.
- `templates/facebook-posting/README.md`: template selection, inputs and local configuration contract.
- `templates/facebook-posting/{validate,decision,execute,report}.md`: the four explicit injections.
- `templates/facebook-posting/TOOLS.example.md`: neutral placeholders and required tool capabilities; no real accounts, providers, addresses, endpoints or credentials.
- `README.md`: package use, private setup, limits and development status. Development specifications are not runtime instruction dependencies.

Invocation uses the host agent's existing skill mechanism; this package adds no command parser. Inputs are the explicit service-template location, original business request, local deployment configuration, private record root and, for continuation, an existing request ID. A missing resume ID never becomes a new request.

Each template's README declares the four injection paths, local supporting instruction paths and configuration requirements. Relative instruction paths must resolve within the generic package or selected template, including symlink targets. No automatic lookup of another skill, campaign procedure or default service is permitted. A missing injection, outside dependency or lifecycle override produces the corresponding definition error before Execute.

At binding, record canonical paths and content hashes for the complete loaded instruction closure and effective non-secret configuration. Keep a private immutable snapshot, or retain accessible immutable source content with matching hashes. Credentials remain references. Resume reads the recorded binding and verifies content; it never silently selects a newer release. Missing or mismatching content holds effects and preserves history.

### Request records and ownership — REQ-EXEC-003, REQ-EXEC-004
The adopter configures a writable private state root outside public tracked artifacts. Suggested layout:
- `requests/<request-id>/request.md`: exact original inputs/asset references, authority evidence and instruction/configuration binding; secrets excluded.
- `requests/<request-id>/journal.jsonl`: append-only attributed validation, decisions, intent, outcomes, communication obligations, ownership handovers and next action.
- `requests/<request-id>/evidence/`: referenced observations and receipts; no fabricated acknowledgement.
- `requests/<request-id>/binding/`: retained bound instructions/non-secret configuration when snapshots are needed.
- `locks/`: stable request/resource lock paths. A small adjacent owner record identifies the current session and ownership token; it does not replace the exclusive lock.

These are documentation conventions and examples, not a new database/API. Each journal entry includes event identity, observed time, request ID, current owner token, stage, event/outcome, evidence references and next action. Effect entries additionally identify the intended target, action and attempt. Reporting entries identify the obligation/incident and submission attempt independently of business effects. A request is not described as durably accepted until its record is persisted.

Execution outcome uses pending/accepted/rejected/blocked/failed/completed observations as appropriate; communication obligations independently retain pending/unknown/submitted evidence. Stage order and the journal determine continuation, rather than a second mutable status file that could disagree. Confirmed work remains confirmed when reporting fails; failure closure remains truthful with outstanding communication retained.

Acquire an existing OS-backed exclusive lock, such as `flock` held by a live tool session, before request writes. Use a stable lock file; never unlink/recreate it to bypass contention. Assign an opaque owner token only while holding the lock. Recheck lock continuity and the owner token before writes and effects. If the host cannot maintain demonstrable ownership, hold work instead of substituting a journal claim. This is a prescribed use of existing tools, not a supplied locking daemon/helper.

Before a shared effect, resolve its canonical resource key from deployment configuration and obtain its exclusive lock as well. A browser key identifies the actual shared profile/session across Pages and requests. Acquire the request lock first; attempt each needed resource without waiting while holding a different contested resource. On contention record the wait/blocker only under the request's ownership and release safely. An unresolved resource or unreadable ownership evidence holds its effect.

Persist intent before submission, then retain attributable native observations. If intent cannot be persisted, do not submit. Unknown outcomes hold repeats and dependent effects until reconciliation supplies positive no-effect evidence or confirms the original effect. No automatic retry loop is supplied.

Release/handover requires evidence that the former owner's tool operations are stopped or completed and cannot still mutate the resource. Process death or elapsed time alone does not settle browser/remote operations. Preserve uncertainty and holds across safe handover. A returning former owner must reacquire ownership and observe the new token; it cannot append or act under its old token. These rules guide compliant agents; they are not an external fencing service.

### Four-stage procedure and communication — REQ-EXEC-001, REQ-EXEC-005
1. Validate the definition, binding, exact inputs, available capabilities and required configuration using the validation injection; persist results under request ownership. Read-only prerequisites do not grant task authority.
2. Apply the decision injection and record explicit acceptance of the exact scope, or rejection/blocker and its reason. Task submission requires affirmative acceptance and current ownership. Revalidate unfinished work on resume and when a material prerequisite changes.
3. Execute only the accepted task procedure. Obtain shared-resource ownership before mutations, persist intent, perform the authorized action and record the attributable result. A failure records its evidence without automatic second attempt.
4. Apply the reporting injection for decisions, intervention blockers, failures and completion. Report is also invoked promptly at those events; it is not postponed until business success. Record content, obligation, attempt and acknowledgement separately from execution.

A configured but temporarily unavailable communication tool leaves pending communication and uses any available authorized requester route to expose the gap. It does not change otherwise valid task acceptance or block independent authorized work. Do not invent a substitute recipient/channel/identity. An unknown submission must be reconciled before another send; a confirmed submission is not repeated. Submission evidence never proves delivery or reading.

Fresh-session continuation obtains request ownership, verifies the binding and original inputs, reconciles unknown effects, revalidates pending work and follows the recorded next action. If only reporting remains, perform reporting-only recovery. No completed business effect is replayed to repair a communication failure. Missing records, unavailable persistence or uncertain ownership are reported through the available route without invented durable updates.

### Facebook injections — REQ-EXEC-007
- Validate: require explicit final caption, supplied asset references, unambiguous owned Page, placement, timing and publication authority. Check actual browser/account/upload and native scheduling capability. A past scheduling instant raises the defined exception; unsupported future scheduling remains blocked.
- Decision: accept only exact authorized scope with verified Page identity and supported operation. Apply generic reporting-outage behavior; reject missing reporting configuration without treating a temporary outage as missing credentials.
- Execute: use the explicitly configured supported browser/profile and current tool documentation. Bundle the Page selection, composer, upload, draft inspection, single submission and native-result verification guidance locally. No outside Facebook/browser/campaign skill references. Inspect final acting identity and exact caption/media/placement before submitting.
- Report: include request identity, actual outcome, confirmed effects, native post reference when readily available, blocker/intervention and outstanding work. Invoke the adopter-configured communication procedure. No channel/provider/sender is prescribed by the public template.

Local configuration describes browser backend/profile and its canonical shared-resource key, permitted tools and prerequisites, communication route/procedure and required identity/recipient fields if relevant. The example makes unset required values visible; a deployment supplies actual settings privately. Configure capability/how-to details separately from business conditions. The agent does not change browser permissions, switch backends without authority, substitute assets or add distribution actions.

### Operator customization — REQ-EXEC-006
The bundled guide walks an operator through copying a template, replacing each injection, declaring all local dependencies/configuration/resources, checking authority and error cases, reviewing the dependency closure and exercising the new service before publication. Include a small document-export example to demonstrate a non-Facebook service and a non-email report route without building another full service.

An executor records a separate attributable improvement request through the configured operator route. Neither an improvement nor approval in principle permits self-editing. Operators publish reviewed updates separately; existing requests retain their bound version. Package publication does not install or activate an executor. Missing customization resources produce an explicit error without external fallback.

## Test strategy
- No test runner exists in this repository yet. Propose Python's standard-library `unittest` for package checks and evidence validation; no runtime dependency or service is introduced.
- Test command: `python3 -m unittest discover -s tests -v`
- Structural checks cover required files, four-injection declarations, local dependency closure including escaping links/symlinks, neutral generic instructions, public/private boundaries and the documented record/configuration contract. Temporary package trees supply missing files, changed content and broken dependency cases. These checks prove artifact properties only.
- Cover all 44 approved scenarios by name, including negative and boundary cases. For instruction behavior, prepare controlled prompts, synthetic request histories and stub tool observations, run the agent against the actual package, and retain its decisions/actions and the scenario-specific assessment. Do not implement a Python copy of the lifecycle and call its results agent verification.
- Fixtures supply a fixed observed clock; synthetic immutable versions and journal failures; two competing agent identities and request/resource claims; stopped and still-active former-owner operations; unknown versus positive no-effect receipts; unavailable/timeout/acknowledged reporters; and native Page/composer/upload/scheduling observations. No real browser, account, publication, credentials or communication service is used.
- Unit checks validate package structure and the complete scenario/evidence mapping. Controlled exercises integrate generic guidance with document-export or Facebook injections, fresh-session histories and conflicting ownership observations. Concurrency evidence must cover both same-request writers and different requests sharing one profile; a textual instruction assertion alone does not prove exclusion.
- Write each scenario's failing check or failing controlled-exercise result before the corresponding guidance. Record actual red/green output and review evidence; unrun or inconclusive behavior remains unverified. The suite reports structural coverage separately from agent-exercise results and known live-readiness gaps.
- Verification keeps synthetic fixtures public and excludes real request histories/media/logs. Check the final public diff for deployment identities/settings before committing. All components trace to the seven approved requirements; the four known gaps remain unchanged.
