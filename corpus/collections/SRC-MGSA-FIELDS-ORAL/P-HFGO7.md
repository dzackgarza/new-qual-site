---
schema: qual/card@1
id: P-HFGO7
kind: problem
title: Algebraic closure of a field
classification:
  areas: [algebra]
  topics: [Field Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Fields and Galois Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof: the card asks for a definition, so the definition is stated
    as the answer and the accompanying claims are justified in numbered steps — the equivalence
    of the two clauses with the remark that algebraic closedness is a condition on polynomials
    over the closure itself, existence and uniqueness as Steinitz's theorem cited rather than
    reproved, with the uniqueness argument sketched (extension of embeddings by Zorn, then an
    algebraically closed subfield algebraic over F equals the ambient field), and a step
    recording that the isomorphism is not canonical, witnessed by the two automorphisms of C
    over R. Added the two examples separating the clauses: C over R versus C over Q. Not
    claimed: a retained solution set; the provenance names the examination question list.
---

::: {.problem}
Define an algebraic closure of a field.
:::

::: {.solution}
The question asks for a definition, so the answer is the definition itself; the numbered steps below state it and justify the three assertions that usually accompany it — the equivalent formulation, existence, and uniqueness. The exam compilation in this collection's `provenance` (`assets/attachments/MGSA_Fields_and_Galois_Theory_Oral_Questions.pdf`) is a question list and carries no solutions, so the definition given here is the standard one (Lang, *Algebra*, V §3; Hungerford, *Algebra*, V §3), and existence and uniqueness are Steinitz's theorem, cited rather than reproved.

::: pf

::: {.pf-step #definition}
Let $F$ be a field. An **algebraic closure** of $F$ is an extension field $\overline F\supseteq F$ such that (1) $\overline F$ is algebraic over $F$, and (2) $\overline F$ is algebraically closed.

::: pf-proof
This is a definition, so there is nothing to prove; both clauses are needed, and neither implies the other: $\CC$ is algebraically closed and algebraic over $\RR$, while $\CC$ is algebraically closed but not algebraic over $\QQ$.

:::

:::

::: {.pf-step #equivalent}
Condition (1) says every element of $\overline F$ is a root of a nonzero polynomial with coefficients in $F$; condition (2) says every nonconstant polynomial in $\overline F[x]$ has a root in $\overline F$.

::: pf-proof
(1) is the definition of "algebraic over $F$" applied to each element. (2) is the definition of "algebraically closed". Note that (2) is a statement about polynomials over $\overline F$, not over $F$: for extensions of $F$ the two are genuinely different conditions, and an algebraic extension of $F$ in which every polynomial over $F$ has a root need not be algebraically closed.

:::

:::

::: {.pf-step #existence}
Every field $F$ has an algebraic closure.

::: pf-proof
This is Steinitz's theorem: one constructs an algebraic extension $\Omega/F$ in which every polynomial over $F$ splits (adjoining roots transfinitely, or by taking a maximal algebraic extension), and then takes the subfield of $\Omega$ consisting of the elements algebraic over $F$. It is cited, not reproved here; the construction needs the axiom of choice and is the substance of the existence half of the structure theory of fields.

:::

:::

::: {.pf-step #uniqueness}
Any two algebraic closures of $F$ are isomorphic over $F$.

::: pf-proof
This is the uniqueness half of Steinitz's theorem: an $F$-homomorphism from an algebraic extension $K/F$ into an algebraic closure $\overline F$ extends any embedding of $F$ into $\overline F$, by Zorn's lemma applied to the partially ordered set of extensions of the embedding to intermediate fields, using that a root of a polynomial over an intermediate field $E$ is algebraic over $E$ and hence has finitely many conjugates. Applying this with $K=\overline F$ and target $\overline F'$ gives an $F$-embedding $\sigma:\overline F\to\overline F'$. Its image is a subfield of $\overline F'$ containing $F$ and algebraic over $F$; it is also algebraically closed, being isomorphic to $\overline F$. An algebraically closed subfield $E\subseteq\overline F'$ with $\overline F'$ algebraic over $E$ equals $\overline F'$: an element $\alpha\in\overline F'$ is a root of a polynomial over $E$, which splits in $E$ because $E$ is algebraically closed, so $\alpha\in E$. Hence $\sigma$ is onto.

:::

:::

::: {.pf-step #noncanonical}
The isomorphism of step [](#uniqueness){.pf-ref} is not canonical: there is in general no preferred isomorphism between two algebraic closures of $F$.

::: pf-proof
For $F=\RR$ the two roots $\pm i$ of $X^2+1$ give two automorphisms of $\CC$ over $\RR$, namely the identity and complex conjugation, and neither is preferred by the field structure alone. So the uniqueness statement must be read as "unique up to $F$-isomorphism", not "unique".

:::

:::

:::
:::

::: {.remark title="Example"}
$\CC$ is an algebraic closure of $\RR$ but not of $\QQ$.
$\CC$ is algebraically closed by the fundamental theorem of algebra, and $\CC=\RR(i)$ is algebraic over $\RR$.
Over $\QQ$, $\CC$ is not algebraic: the algebraic numbers form a countable set, while $\CC$ is uncountable.
:::
