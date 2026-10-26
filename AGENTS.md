# Service executor skill development

- Build the generic validate → accept/reject → execute → report skill and explicit service injections.
- Keep runtime instruction dependencies inside the skill package and the explicitly selected local service template. Import needed guidance locally; do not route runtime execution through other skills or shared procedures.
- Keep generic orchestration separate from service-specific requirements, decisions, task procedures and reports.
- Customization is operator-controlled. Executors never rewrite their own instructions, injections, templates or helpers.
- Preserve separate request records, exclusive ownership of shared effects and reconciliation before retrying uncertain effects.
- This is a public repository. Never commit credentials, private connection settings, live request records, logs or media.
- No worker launch, Facebook action, email send or installation into existing agents is authorized by repository development alone.
