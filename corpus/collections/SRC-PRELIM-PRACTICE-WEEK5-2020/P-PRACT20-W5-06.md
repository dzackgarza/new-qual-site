---
schema: qual/card@1
id: P-PRACT20-W5-06
kind: problem
title: Abelian groups of order $16$ and exponent dividing $4$
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 6).
---

::: {.problem}
Up to isomorphism, how many abelian groups $G$ have order $16$ and satisfy $x + x + x + x = 0$ for all $x \in G$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Up to isomorphism, the abelian groups of order $16=2^4$ are
\[
\ZZ_{16},\qquad
\ZZ_8\times\ZZ_2,\qquad
\ZZ_4\times\ZZ_4,\qquad
\ZZ_4\times\ZZ_2\times\ZZ_2,\qquad
\ZZ_2^4.
\]


::: pf-proof

By the fundamental theorem of finite abelian groups, abelian groups of order
$2^4$ correspond to partitions of $4$:
\[
4,\qquad
3+1,\qquad
2+2,\qquad
2+1+1,\qquad
1+1+1+1.
\]
These give exactly the five displayed groups.

:::

:::

::: {.pf-step #s1-2}

The condition
\[
4x=0
\qquad(x\in G)
\]
holds exactly when the exponent of $G$ divides $4$.


::: pf-proof

In additive notation, $4x=0$ for every $x$ means that every element has
order dividing $4$. The least common multiple of all element orders is the
exponent of the finite group, so this is equivalent to the exponent dividing
$4$.

:::

:::

::: {.pf-step #s1-3}

Of the five groups in step [](#s1-1){.pf-ref}, exactly
\[
\ZZ_4\times\ZZ_4,\qquad
\ZZ_4\times\ZZ_2\times\ZZ_2,\qquad
\ZZ_2^4
\]
satisfy the required condition.


::: pf-proof

The groups $\ZZ_{16}$ and
$\ZZ_8\times\ZZ_2$ contain elements of order $16$ and $8$,
respectively, so they fail the condition in step [](#s1-2){.pf-ref}.

Every element in each of the remaining three groups has every coordinate of
order dividing $4$, so its order divides $4$. Hence those three groups
satisfy the condition.

:::

:::

::: {.pf-step #s1-4}

Therefore the number of isomorphism classes is
\[
\boxed{3}.
\]


::: pf-proof

Step [](#s1-3){.pf-ref} gives exactly three qualifying groups.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the requested count.

:::

:::

:::
