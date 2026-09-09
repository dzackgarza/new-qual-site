# Mathematical issues and papercuts

Record issues encountered during source reading, solving, review, authoring or
site use under [QUAL-05](CONTRIBUTING.md#named-policies). Include findings outside
the selected card. This file owns observations; [TODO.md](TODO.md) owns selected
repair tasks and dependencies. Keep existing GitHub issue links rather than
copying their live status. The [review policy index](REVIEW_POLICY.md) supplies
named candidate patterns, not proof that a candidate is a defect.

## Recording an issue

Add a descriptive heading in the appropriate section below, with:

- **Object and need:** card/collection ID or affected workflow; the exact
  mathematical statement and hypotheses, or user action and expected behavior.
- **Observed evidence:** source page and passage, counterexample or proof gap,
  or actual action and result with the relevant path/revision.
- **Impact and owner:** affected parts or consumers, existing partial result,
  and the mathematical or tool boundary that must change.
- **Uncertainty:** distinguish a verified error from a source ambiguity or
  review candidate. State inspected scope and remaining questions. For absence
  claims supply Searched, Found, Conclusion, Confidence and Gaps.
- **Repair:** link the existing TODO task or issue when available and state
  the result that would resolve the observation.

A missing hypothesis with a concrete counterexample is a mathematical issue.
An unreadable source is an unresolved source question. An unsolved problem is
ordinary authoring work, not by itself a defect. A command that prevents reading
the intended card is a papercut even when it has a simple workaround.

Extend an existing entry when the same cause affects another card. Preserve
concurrent entries. If the selected proof requires a repair, link that dependency
and resolve it before relying on the statement; recording it does not make the
proof valid. Continue independent assigned mathematics.

After verifying the full repair, remove the resolved entry with evidence in the
fixing commit; retain any unresolved portion. Put durable mathematical errata
on the owning card and durable policy in CONTRIBUTING. Keep process notes out
of public mathematical remarks.

## Mathematical issues and source questions


### Unsorted Algebra cards imported as proof fragments rather than problem statements

- **Object and need:** `SRC-UNSORTED-ALGEBRA`, including `P-0221B`, `P-0T149`, `P-1DBO7`, `P-1P5M4`, and `P-23M4O`, needs recoverable source-backed problem statements before solution authoring can be completed.
- **Observed evidence:** these cards' `::: problem` blocks are written as proof prose (for example, “Since $E$ was shown to be a splitting field...” in `P-0221B` and a complete contradiction proof in `P-23M4O`) and the collection has no provenance identifying an original source from which the omitted prompts can be restored.
- **Impact and owner:** Queue C treats these as unsolved problems, but writing solutions now would require inventing missing prompts and would violate source-faithful authoring. The owning boundary is unsorted-source reconciliation/intake.
- **Uncertainty:** verified on the five listed cards; the full `SRC-UNSORTED-ALGEBRA` collection has not yet been exhaustively classified for this defect. Searched: card bodies, collection membership, repository references. Found: no independent source/provenance for these cards. Conclusion: source reconstruction is currently blocked. Confidence: high for the listed cards. Gaps: original upstream source may exist outside the retained repository.
- **Repair:** recover and attach the original source or source ledger, restore the actual prompts verbatim, then return the cards to the normal solution queue.

## Workflow and rendering papercuts
