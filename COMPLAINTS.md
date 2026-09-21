# Mathematical issues and papercuts

Record issues encountered during source reading, solving, review, authoring or site use under [QUAL-05](CONTRIBUTING.md#named-policies).
Include findings outside the selected card.
This file owns observations; [TODO.md](TODO.md) owns selected repair tasks and dependencies.
Keep existing GitHub issue links rather than copying their live status.
The [corpus review patterns](CONTRIBUTING.md#corpus-review-patterns) supply named candidate patterns, not proof that a candidate is a defect.

## Recording an issue

Add a descriptive heading in the appropriate section below, with:

- **Object and need:** card/collection ID or affected workflow; the exact mathematical statement and hypotheses, or user action and expected behavior.

- **Observed evidence:** source page and passage, counterexample or proof gap, or actual action and result with the relevant path/revision.

- **Impact and owner:** affected parts or consumers, existing partial result, and the mathematical or tool boundary that must change.

- **Uncertainty:** distinguish a verified error from a source ambiguity or review candidate.
  State inspected scope and remaining questions.
  For absence claims supply Searched, Found, Conclusion, Confidence and Gaps.

- **Repair:** link the existing TODO task or issue when available and state the result that would resolve the observation.

A missing hypothesis with a concrete counterexample is a mathematical issue.
An unreadable source is an unresolved source question.
An unsolved problem is ordinary authoring work, not by itself a defect.
A command that prevents reading the intended card is a papercut even when it has a simple workaround.

Extend an existing entry when the same cause affects another card.
Preserve concurrent entries.
If the selected proof requires a repair, link that dependency and resolve it before relying on the statement; recording it does not make the proof valid.
Continue independent assigned mathematics.

After verifying the full repair, remove the resolved entry with evidence in the fixing commit; retain any unresolved portion.
Put durable mathematical errata on the owning card and durable policy in CONTRIBUTING. Keep process notes out of public mathematical remarks.

## Mathematical issues and source questions

### Azoff Möbius symmetry problem has a false fourth equivalent condition

- **Object and need:** \`P-AZOFF-C12\` / \`SRC-AZOFF-PROBLEMS-BY-TOPIC\`,
  Conformal mapping Problem 12. The source asks to prove four conditions on a
  Möbius transformation equivalent; condition (d) requires a real fixed point
  \(\alpha\) in addition to one nonreal conjugation-compatible point.
- **Observed evidence:** page 3 of the retained PDF prints
  \(T(\alpha)=\alpha\) with no overbar on either occurrence of \(\alpha\).
  The PDF vector data separately shows the overbars in
  \(T(\overline\beta)=\overline{T\beta}\), so the fixed-point clause is not an
  extraction loss. The Möbius transformation
  \(T(z)=-1/z\) has real coefficients and therefore satisfies (a)--(c), but
  its fixed-point equation is \(z^2=-1\), so it has no real fixed point and
  fails (d).
- **Impact and owner:** the printed four-way equivalence cannot be proved.
  The owning problem card must state the true implication pattern before its
  solution is authored.
- **Uncertainty:** verified against the rendered PDF, its text layer, and the
  vector rules carrying the overbars. The mathematical counterexample is
  exact; whether the source author intended a different condition (d) is
  unknown.
- **Repair:** correct \`P-AZOFF-C12\` to ask for the equivalence of (a)--(c),
  prove that printed (d) implies them, and record that the converse fails via
  \(T(z)=-1/z\). Preserve the printed source error as a durable erratum on
  the card.

### Zaidenberg Definition 4.3 makes the following finite-morphism exercises inconsistent

- **Object and need:** \`SRC-AGX-VARIETIES-PROBLEMS\`, Definition 4.3 and
  Exercises 4.4. The standard definition of a finite morphism does not require
  the comorphism to be injective.
- **Observed evidence:** page 6 of the recorded PDF says that a finite morphism
  has an "embedding" $f^*:O(Y)\to O(X)$, while the same exercise immediately
  asks for a non-surjective finite morphism. An injective module-finite
  comorphism is integral, so lying over makes the corresponding affine map
  surjective.
- **Impact and owner:** the source wording cannot govern cards about finite
  morphisms. \`P-AGXVARFINCLOSED\` records and uses the repository definition
  \`D-MORFIN\`, under which the exercise is coherent.
- **Uncertainty:** verified in the PDF with two independent text extractors;
  this may be a typo in the source rather than an intended nonstandard
  convention.
- **Repair:** retain the standard repository definition and treat the printed
  word "embedding" as source errata unless a corrected source edition is found.

## Workflow and rendering papercuts
