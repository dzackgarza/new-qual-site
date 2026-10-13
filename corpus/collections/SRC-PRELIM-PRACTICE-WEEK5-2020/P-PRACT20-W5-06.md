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
<1>1. Up to isomorphism, the abelian groups of order $16=2^4$ are
\[
\mathbb Z_{16},\qquad
\mathbb Z_8\times\mathbb Z_2,\qquad
\mathbb Z_4\times\mathbb Z_4,\qquad
\mathbb Z_4\times\mathbb Z_2\times\mathbb Z_2,\qquad
\mathbb Z_2^4.
\]

::: {.proof}
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

<1>2. The condition
\[
4x=0
\qquad(x\in G)
\]
holds exactly when the exponent of $G$ divides $4$.

::: {.proof}
In additive notation, $4x=0$ for every $x$ means that every element has
order dividing $4$. The least common multiple of all element orders is the
exponent of the finite group, so this is equivalent to the exponent dividing
$4$.
:::

<1>3. Of the five groups in step <1>1, exactly
\[
\mathbb Z_4\times\mathbb Z_4,\qquad
\mathbb Z_4\times\mathbb Z_2\times\mathbb Z_2,\qquad
\mathbb Z_2^4
\]
satisfy the required condition.

::: {.proof}
The groups $\mathbb Z_{16}$ and
$\mathbb Z_8\times\mathbb Z_2$ contain elements of order $16$ and $8$,
respectively, so they fail the condition in step <1>2.

Every element in each of the remaining three groups has every coordinate of
order dividing $4$, so its order divides $4$. Hence those three groups
satisfy the condition.
:::

<1>4. Therefore the number of isomorphism classes is
\[
\boxed{3}.
\]

::: {.proof}
Step <1>3 gives exactly three qualifying groups.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the requested count.
:::
:::
