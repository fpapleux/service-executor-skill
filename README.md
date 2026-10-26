# Service executor skill

An agent-interpreted skill for **validate → accept/reject → execute → report**, with four explicit service injections. The generic skill owns sequencing, durable continuity, concurrent ownership, uncertain-effect recovery and keeping the customer informed. The selected service supplies its business checks, decision constraints, task procedure and chosen communication procedure.

Start at [SKILL.md](SKILL.md). The first bundled service is [Facebook posting](templates/facebook-posting/README.md). Operators creating another service or changing injections should use the self-contained [customization guide](reference/customization.md).

## Use

Select a local service template and supply the original request, explicit private tool configuration and a private durable record root. For example, ask the host agent to use `service-executor` with `templates/facebook-posting/` for the exact authorized Page post. Resume by naming the existing request ID. The package adds no command parser, scheduler, launcher or transport implementation.

The operator completes the template's tool/configuration contract privately before activation. All authored runtime instructions remain inside the generic package and selected local template; do not chain another skill or shared procedure. Current tool/API documentation remains usable. Host policies still apply: this is instruction-dependency isolation, not a technical sandbox.

Use private request records and an existing exclusive ownership facility shared by cooperating executors. Different requests have separate histories; the same browser profile remains a shared resource across Pages. If safe ownership or outcome reconciliation cannot be established, hold affected effects and report the actual blocker.

Customer communication is mandatory through the adopter's configured procedure. No particular channel/provider is required. A temporary reporting outage retains pending communication while independent accepted work proceeds; an uncertain send is reconciled before retry. Confirmed task effects are never replayed to repair reporting.

Executors file separate improvement requests and never amend their own process. Operators publish reviewed versions; existing requests retain their bound instructions. Publication does not install or activate an agent or grant authority for external actions.

## Verification and development

Run `python3 -m unittest discover -s tests -v`. Artifact checks, an OS-lock primitive exercise and retained reviewed agent-decision exercises are different evidence types; see [tests/README.md](tests/README.md) for scope and reruns. The unit command validates retained exercise evidence and its instruction identities; it does not invoke a model or run a live service.

[SDD change 0001](specs/changes/0001-service-executor/proposal.md) records the approved specification and plan. Implementation is subject to the separate SDD verification/results gate. No live Facebook/account/upload/scheduling/communication readiness is certified by this package.

Credentials, adopter-specific provider identities, private connection settings, live requests, logs and media do not belong in this public repository. Deployment into an existing executor is a separate authorized operation.
