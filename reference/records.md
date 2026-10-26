# Records, binding and ownership

These are conventions for agents using existing file/tool facilities. No workflow engine, supervisor, scheduler or automatic recovery service is supplied.

## Private state

The operator supplies a private state root outside public tracked artifacts, accessible to future authorized sessions. Keep credentials as references, never values in request records, snapshots, logs or public fixtures.

```text
<private-root>/
  requests/<request-id>/
    request.md
    journal.jsonl
    binding/
    evidence/
  locks/
```

Allocate one distinguishable ID for a new request. Acquire its stable request lock before initialization or writes. A resume ID names an existing request and never allocates a replacement. Retain the exact original inputs and asset references, not a rewritten prompt.

`request.md` contains identity, original inputs, authority, selected template, full instruction/configuration binding and credential references. `binding/` retains immutable non-secret content when source versions cannot otherwise be guaranteed available. `evidence/` retains attributable observations/receipts. Do not describe acceptance as durable before persistence succeeds.

Append journal events under current ownership. Each event records event ID, observed time, request ID, owner token, stage, event/outcome, evidence references and next action. Action events also record target, intended action and attempt ID. Reporting events record obligation/incident ID, content/reference and attempt separately from execution outcome. Keep prior events; corrections append attributable new observations.

Example shape (synthetic, not an execution result):
```json
{"event_id":"event-1","observed_at":"2030-01-01T12:00:00Z","request_id":"example-request","owner_token":"session-token","stage":"execute","event":"intent","outcome":"pending","target":"authorized-target","action":"requested-action","attempt_id":"attempt-1","evidence":[],"next_action":"submit accepted action"}
```

The journal holds validation, decision, acceptance/rejection, task progress, intent, observations, holds, reports and safe handovers. Derive the current next action from it rather than maintaining a competing mutable status file. Execution can be pending/accepted/rejected/blocked/failed/completed; each communication obligation independently remains pending/unknown/submitted. Unknown never means failed-with-no-effect.

If a required write fails, report `record-unavailable` with path and operation through the available route. Do not submit the action, invent a written intent, or overwrite existing records to recover silently.

## Instruction binding

Before acceptance, inspect the selected template declaration and resolve its four injection paths and every transitive authored instruction reference. Allowed roots are the generic package and explicitly selected local template, including configured local instruction resources inside that template. Resolve canonical paths/symlink targets before reading. An instruction outside those roots is `external-instruction-dependency`; reject without loading it. A link is not permission to load another skill.

Record a content identity (for example SHA-256) for each loaded instruction and the effective non-secret configuration, plus canonical paths and the selected template identity. Include supporting files, not just the entrypoint. Preserve accessible immutable content or private snapshots of it. Keep credentials as references in the binding; never hash or snapshot secret values into public evidence.

On resume, verify the complete closure against those identities and recover its original configuration. A newer discovery pointer does not change a binding. Missing original content holds effects; differing content is `instruction-version-mismatch`. Confirmed work and original bindings stay intact. Tool/API documentation remains usable to operate configured tools; it is not a source of additional workflow policy.

## Ownership

An owner note alone is not exclusive acquisition. Use an existing OS-backed exclusive facility such as `flock`, with a live lock-holding session for the entire protected interval. All cooperating executors must share the same lock domain and canonical paths. If the environment cannot maintain demonstrable exclusive ownership across tool calls, report a blocker and hold work. A one-shot command that exits immediately does not retain a lock.

Use stable lock files: do not unlink/recreate them on contention. Obtain the request lock before writes, and set an opaque session owner token only while holding it. Before every write/effect, verify the holding session remains live, the lock has not been released and its token remains current. A former owner cannot use an old token after safe handover; reacquisition requires reading the current history first.

Resolve shared resources from authoritative configuration. The same actual browser profile/session has the same key across requests and Pages. If its identity is unresolved, report `resource-unresolved`; no invented per-Page substitute lock. If ownership evidence is unreadable, report `ownership-unavailable`; do not replace it or assume expiry means release.

Acquire the request lock first, then required resource locks without waiting while holding another contested resource. If a resource is busy, retain a wait/blocker in your own request only and release safely. Different requests keep independent journals. If the request lock itself is busy, the loser reports an ownership conflict through the requester route without writing that request or creating duplicate acceptance.

Lock availability does not settle old remote operations. Release/handover is safe only after establishing no former-owner operation can still mutate the resource: observe tool completion or stop the relevant operation through existing authorized controls and verify it stopped. Elapsed time or a dead local process is insufficient for a still-active browser/remote operation. Otherwise hold the resource and escalate the uncertainty.

Preserve unresolved outcomes and replay/dependency holds even after safe handover. This is cooperative agent guidance, not an external technical fencing service.

## Intent and reconciliation

Persist intent under current ownership before submission; retain the original attempt and observations afterward. Unknown business or communication outcomes require attributable native evidence. Match target, content, attempt and available native identifiers; an empty search or absence of an acknowledgement alone does not establish no effect.

If the native evidence confirms acceptance, retain that effect and do not repeat it. Permit a new attempt only after positive no-effect evidence, current ownership, renewed prerequisite/authority checks and a recorded next action. If uncertain, retain the hold on repeats and dependent effects. Reporting-only recovery never repeats completed business work.
