---
schema: qual/card@1
id: P-ALGPAN11-08
kind: problem
title: Consequence of the identity (ab)^2 = a^2 b^2
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the retained Pantano 2011 algebra-review source scan and verified from the stated algebraic criterion.
- event: source-checked
  by: claude-opus-5.5
  date: 2026-10-31
  note: Statement and choices transcribed from the ALGEBRA_REVIEW1.pdf page render; the machine extractions were garbled at this item.
---
::: {.problem}
A group $G$ in which $(ab)^2=a^2b^2$ for all $a,b$ in $G$ is necessarily

(A) finite

(B) cyclic

(C) of order two

(D) abelian

(E) none of the above
:::

::: {.solution}
The group must be abelian, so the answer is $\boxed{\text{(D)}}$.

::: pf

::: {.pf-step #s1}

Cancel in the given identity.

::: pf-proof

For arbitrary $a,b\in G$,
$$
(ab)^2=a^2b^2
$$
means
$$
abab=aabb.
$$
Left-multiplying by $a^{-1}$ gives
$$
bab=abb,
$$
and right-multiplying by $b^{-1}$ gives
$$
ba=ab.
$$
Thus every pair of elements commutes and $G$ is abelian.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves that $G$ is abelian, so choice (D) is correct.

:::

:::

:::
