---
schema: qual/card@1
id: P-ALGS13B
kind: problem
title: Projective modules over a commutative ring are flat
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Projective Modules
relations: []
review: draft

audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 2 of the Spring 2013 UCSD Algebra Qualifying Examination, printed p. 1
    of the single-page paper retained at assets/attachments/SP13_200_Algebra_Qual.pdf, is the statement
    the card answers, and the paragraph at the head of the solution records that the paper prints no
    solutions, so the argument is the card's own. Checked: the statement against the paper's text layer
    at the page named; the solution read for the three steps, free implies flat, direct summands of flat
    modules are flat, and projective modules are direct summands of free ones; `qualc.authoring check`
    on the card, and `tmp/lam.sh` for the numbering and the QED. Not checked: no retained solution set
    exists for this paper to compare the argument with, and no other card of the collection in this
    pass.
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: {.problem}
Let $A$ be a commutative ring.
Prove that any projective $A$-module is flat.
(Hint: first prove it for free modules).
:::

::: {.solution}

The problem is Problem 2 of the Spring 2013 UCSD Algebra Qualifying Examination, printed p. 1 of the single-page paper retained at `assets/attachments/SP13_200_Algebra_Qual.pdf`. The paper prints no solutions, so nothing below is transcribed: the argument is the card's own, and what it supplies is the three steps through which the printed hint is carried out: free modules are flat, a direct summand of a flat module is flat, and a projective module is a direct summand of a free one

::: pf

::: {.pf-step #s1}

Every free $A$-module is flat.

::: pf-proof

Let $F=\bigoplus_{i\in I}A$.
For every $A$-module $M$ there is a natural isomorphism
$$
M\otimes_A F\cong \bigoplus_{i\in I}(M\otimes_A A)\cong \bigoplus_{i\in I}M.
$$
Thus the functor $-\otimes_A F$ is naturally isomorphic to the direct-sum functor $M\mapsto\bigoplus_{i\in I}M$.
Direct sums of exact sequences of modules are exact, so $-\otimes_A F$ is exact.
Hence $F$ is flat.

:::

:::

::: {.pf-step #s2}

A direct summand of a flat module is flat.

::: pf-proof

Suppose $N\cong P\oplus Q$ and $N$ is flat.
Then for every $A$-module $M$,
$$
M\otimes_A N\cong (M\otimes_A P)\oplus(M\otimes_A Q).
$$
Given an injection $u:M'\hookrightarrow M$, flatness of $N$ makes
$$
u\otimes 1_N:(M'\otimes_A P)\oplus(M'\otimes_A Q)\longrightarrow (M\otimes_A P)\oplus(M\otimes_A Q)
$$
injective.
Its restriction to the first direct summand is $u\otimes 1_P$, so $u\otimes 1_P$ is injective.
Since tensor product is always right exact, $-\otimes_A P$ is exact.
Thus $P$ is flat.

:::

:::

::: {.pf-step #s3}

Every projective $A$-module is flat.

::: pf-proof

Let $P$ be projective.
There exists a free module $F$ and a module $Q$ such that
$$
F\cong P\oplus Q.
$$
By step [](#s1){.pf-ref}, $F$ is flat.
By step [](#s2){.pf-ref}, its direct summand $P$ is flat.

:::

:::

::: pf-step

Therefore every projective module over a commutative ring is flat.

::: pf-proof

This is exactly step [](#s3){.pf-ref}.

:::

:::

:::

:::
