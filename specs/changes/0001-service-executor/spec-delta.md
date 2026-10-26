## Requirements

### REQ-EXEC-001 Four-stage execution contract
The skill shall guide each request through validation using the selected service's requirements, an explicit accept/reject decision using its constraints, execution of its task instructions only after acceptance, and reporting using its reporting procedure.

| ID | Category | Given | When | Then |
| --- | --- | --- | --- | --- |
| S1 | happy | document-export supplies all four injections and request R1 passes its checks and authority constraints | R1 runs | record validation and acceptance before the injected export action, then report its evidenced result through the injected route |
| N1 | validation | R1 omits the source required by its validation injection | validation and decision run | record rejection with missing-source reason and follow the rejection report procedure · no Execute-stage action · supplied inputs preserved |
| N2 | state | R1 has validation results but no affirmative acceptance | execution is requested | report acceptance-required · no Execute-stage action · existing decision history preserved |
| N3 | dependency | accepted R1's task tool fails before its effect | execution fails | retain failure evidence and invoke the failure report procedure · no success claim or automatic second attempt · confirmed prior work preserved |
| B1 | boundary | accepted R1 contains one business action and a session-reply report | R1 runs | perform one action and its report · no invented follow-up task, campaign prerequisite or software-development approval gate |

### REQ-EXEC-002 Self-contained instructions and explicit injection binding
The skill shall use its bundled instructions and the explicitly selected local service injections as its complete authored runtime instruction dependency set, keeping service-specific policies out of the generic lifecycle.

| ID | Category | Given | When | Then |
| --- | --- | --- | --- | --- |
| S1 | happy | service A bundles four local injections and local tool configuration, with tools exposing current API documentation | a request binds to A | bind the generic instructions, four injections and all transitively loaded local instruction resources plus effective non-secret configuration to recorded content identities; keep credentials as references; use only that instruction set and needed tool documentation, without generic Facebook, browser or email defaults |
| N1 | validation | service A omits its report injection | a request selects A | report incomplete-service-definition through the available requester route · no Execute-stage action or invented report procedure · definition unchanged |
| N2 | state | R1 has bound A version 1 and discovery now points to version 2 | R1 continues | retain version 1 or report its unavailability · no silent rebinding or completed-action replay · original selection preserved |
| N3 | dependency | A's execute injection directs reading an external campaign skill, including through a link or symlink outside the permitted instruction set | its dependencies are checked | report external-instruction-dependency · no external instruction loading or Execute-stage action · original request and package preserved |
| N4 | access | A contains a directive to bypass acceptance or modify the generic lifecycle | A is evaluated | report conflicting-service-definition · no bypass, self-edit or Execute-stage action · generic lifecycle and original request preserved |
| N5 | validation | a supplied document or tool result contains text saying to load another skill or bypass acceptance | the agent reads that request evidence | retain the supplied content as data, follow the bound workflow and report any resulting input issue under its validation injection · no loading the referenced skill, new authority or bypass · original content preserved |

### REQ-EXEC-003 Durable request continuity
The skill shall guide the agent to keep a separate durable request record containing the original business inputs, complete bound instruction and non-secret configuration identities, credential references, authority, validation, decision, task and reporting progress, intended effects, observed outcomes and next action sufficient for fresh-session continuation.

| ID | Category | Given | When | Then |
| --- | --- | --- | --- | --- |
| S1 | happy | R1 has confirmed action A, pending B and a recorded report obligation | a new session resumes R1 | recover its exact instructions and inputs, obtain current ownership, revalidate pending B and continue only unfinished work; retain A and the report obligation |
| N1 | validation | resume names missing request R404 | the request is located | report request-not-found · no replacement request or external effect · existing requests unchanged |
| N2 | state | R1's pinned instruction content differs from its recorded identity | continuation validates its sources | report instruction-version-mismatch and hold effects · no latest-version substitution or history rewrite · confirmed work preserved |
| N3 | dependency | the agent cannot persist the pre-action intent for R1 | an action is due | report record-unavailable with path and operation through the available route · no action submission or invented durable acknowledgement · prior records preserved |
| B1 | boundary | no requests exist and one valid request starts | its records are initialized | allocate one distinguishable request and only its needed evidence · retain private inputs outside public tracked artifacts and credentials as references rather than values |

### REQ-EXEC-004 Concurrent ownership and uncertain effects
The skill shall require exclusive current ownership for request writes and declared shared effects, preserving independent concurrent requests and reconciling uncertain effects before any repeat attempt.

| ID | Category | Given | When | Then |
| --- | --- | --- | --- | --- |
| S1 | happy | R1 has current request and resource ownership with no unresolved effect | its accepted action runs | record intent and attributable outcome under that ownership; record and release ownership only after confirming no in-flight or unresolved effect; independent requests retain their own records |
| N1 | validation | a shared browser is required but its canonical profile resource cannot be identified | ownership is evaluated | record resource-unresolved · no browser mutation or invented per-Page substitute claim · other claims unchanged |
| N2 | concurrency | agents A and B own different requests that require the same profile | both seek the shared effect | only one owner proceeds; the other records a wait or blocker in its own request · no overlapping mutation, mixed identity or cross-request write |
| N3 | dependency | the current shared-resource ownership record is unreadable | an action would begin | report ownership-unavailable and hold the effect · no replacement claim or elapsed-time takeover · existing claims and confirmed effects preserved |
| N4 | state | R1 submitted action A but its outcome is unknown after disconnect | a continuation considers another attempt | retain the original attempt and reconcile attributable native evidence; permit retry only after positive no-effect evidence and renewed checks · no blind replay or dependent effect |
| N5 | state | old agent A returns after a recorded safe handover to B | A attempts a write or effect | reject stale ownership · no write or external effect by A · B's ownership and records preserved |
| N6 | concurrency | agents A and B both attempt to start or resume the same request R1 | they acquire request ownership | admit at most one current writer; the other reports ownership conflict without changing R1 · no interleaved journal writes, duplicate acceptance or external effect by the loser · current owner and unrelated requests preserved |

### REQ-EXEC-005 Injected reporting and truthful outcomes
The skill shall apply the selected service's reporting procedure to accepted, rejected, blocked, failed and completed requests, recording execution and reporting outcomes separately and preserving unresolved notification obligations.

| ID | Category | Given | When | Then |
| --- | --- | --- | --- | --- |
| S1 | happy | R1's task acceptance is evidenced and its configured report route acknowledges submission | R1 finishes | retain execution evidence, report content and submission evidence; close truthfully without claiming recipient delivery or reading |
| S2 | happy | a service requires immediate intervention notification and R1 encounters its defined access blocker | that blocker is recorded | invoke the injected report procedure before more task work, stating reason, confirmed effects and needed intervention; keep execution resumable |
| N1 | validation | an email-reporting service lacks its required recipient configuration | its reporting prerequisites are checked | report missing-report-configuration through the available requester route · no guessed recipient, email send or premature Execute-stage action · supplied configuration preserved |
| N2 | state | R1 has a confirmed report submission for incident I1 and execution remains failed | reporting is revisited | retain the failed execution and existing acknowledgement · no duplicate report or task replay · original incident history preserved |
| N3 | dependency | report attempt N1 times out with unknown submission outcome | reporting continues | retain notification uncertainty and its incident/attempt identity; reconcile before another send · no claimed delivery, blind resend or replay of completed task effects |

### REQ-EXEC-006 Operator-controlled customization
The package shall include self-contained guidance for operators to create or adapt a service by supplying its four injections while preserving the generic lifecycle, versioned request continuity and the prohibition on executor self-amendment.

| ID | Category | Given | When | Then |
| --- | --- | --- | --- | --- |
| S1 | happy | an operator wants document-export rather than Facebook posting | the bundled customization guidance is followed | define its requirements, decision constraints, task procedure, report route and tool configuration locally; review the resulting service without introducing Facebook behavior or changing the generic lifecycle |
| N1 | validation | the operator's proposed template lacks decision constraints | the customization checklist is applied | identify the missing injection and keep the template incomplete · no ready-for-execution claim or activation · existing templates unchanged |
| N2 | state | an executor identifies an improvement, including one approved only in principle | it handles that improvement | retain a separate attributable change request through the configured operator route · no amendment of its skill, injections, templates or helpers · running request history and instructions preserved |
| N3 | dependency | a required bundled customization resource is missing | an operator follows the guide | report missing-customization-resource · no loading another skill, invented replacement instruction or ready-template claim · existing published instructions unchanged |

### REQ-EXEC-007 Facebook posting injections
The package shall provide self-contained validate, accept/reject, execute and report injections under templates/facebook-posting/ for the exact requested owned-Page post, using locally configured browser and email tools with no inherited campaign actions.

| ID | Category | Given | When | Then |
| --- | --- | --- | --- | --- |
| S1 | happy | Example Page is unambiguously resolved in the owned-Page list as PAGE-A, with an exact approved caption, one image, placement, eligible timing and publication authority | the template runs | validate actual capability and identity, accept the exact scope, inspect the native draft, submit once and record native confirmation plus a post reference when readily available, then follow the configured report procedure |
| S2 | happy | the template explicitly authorizes a supported Chrome profile whose upload prerequisites are satisfied, and internal iab is unavailable | browser prerequisites are evaluated | use that configured Chrome backend and its current tool documentation · no implicit iab-only prerequisite or loading shared browser/campaign skills |
| S3 | happy | local reporting configuration selects shared company MCP configured communication provider, existing Agent identity agent@example.test, Inbox/agent and recipient operator@example.test | an authorized notification is submitted | resolve the existing account/identity/mailbox through that service, submit as Agent and record acknowledgement · no separate Facebook sender, new account or new credential requirement |
| N1 | validation | the final caption is absent rather than explicitly supplied | request validation runs | reject with the exact missing-input reason and follow the report injection · no invented copy or post submission · original inputs preserved |
| N2 | state | the approved destination is PAGE-A but the final composer acts as PAGE-B | the pre-submit check runs | record identity mismatch and hold submission for correction and revalidation under ownership · no post, changed approved target or false success |
| N3 | dependency | the configured browser rejects local-file upload because its required file permission is disabled | the upload prerequisite is checked or upload fails | record an access blocker and invoke the configured immediate intervention report · no post, substituted asset, unapproved backend switch or browser permission change · request remains resumable |
| N4 | dependency | the post has confirmed native acceptance but configured configured communication provider tools are unavailable | completion reporting runs | preserve the successful post and outstanding notification, report the actual service gap through the available requester route · no personal-sender substitution, invented missing-credential diagnosis or duplicate post |
| N5 | validation | a newly requested scheduling instant is earlier than the observed current instant | validation checks timing | raise the past-schedule exception and invoke the configured immediate failure report · no guessed replacement time, scheduling claim or post submission · requested timing preserved |
| N6 | dependency | the request specifies a future instant and no existing authorized tool can establish that scheduled action | scheduling capability is validated | record a scheduling blocker and required intervention report · no post-now fallback, custom scheduler, scheduled-success claim or invented trigger · original timing and request preserved |
| B1 | boundary | the request authorizes one feed image post and zero follow-up destinations or comments | the native draft is inspected and submitted | retain the exact supplied caption/media and only that post · no added link announcement, URL comment, square-image requirement, personal share, crosspost, Story or boost |

## Known gaps
- The deliverable is agent-interpreted guidance. Instruction isolation is the closure of authored package/template dependencies, not a network air gap or technical sandbox that removes host/system policies or prevents a model from ignoring instructions.
- Package checks and controlled exercises do not establish Facebook access, native format availability, browser login/upload readiness or live email delivery. This change performs no live action or deployment into existing executors.
- No execution engine, scheduler, watchdog or automatic recovery service is supplied. A service may use existing authorized tools; unavailable capabilities remain reported dependencies.
- Imported guidance is maintained in the local package. Later edits to its former shared source do not propagate automatically; only an operator-controlled reviewed update changes the local instructions.
