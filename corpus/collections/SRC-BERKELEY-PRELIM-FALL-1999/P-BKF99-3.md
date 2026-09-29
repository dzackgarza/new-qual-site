---
schema: qual/card@1
id: P-BKF99-3
kind: problem
title: Orthogonal idempotents from a direct-sum decomposition into left ideals
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Decomposed the identity into its unique components u_i in the left ideals.
    Multiplying this decomposition by an element of I_i and using uniqueness
    of the direct-sum decomposition isolates the required products.
---

::: {.problem}
Let $R$ be a ring with identity. Suppose $I_1,\ldots,I_n$ are left ideals such that, as additive groups,
\[
R=I_1\oplus I_2\oplus\cdots\oplus I_n.
\]
Prove that there are elements $u_i\in I_i$ such that for every $a_i\in I_i$,
\[
a_i u_i=a_i,
\qquad
a_i u_j=0\quad(j\ne i).
\]
:::

::: {.solution}

::: pf

::: {.pf-step #identity-decomposition-unique}
There are unique elements $u_i\in I_i$ such that
$$
1=u_1+\cdots+u_n.
$$

::: pf-proof
The hypothesis
$$
R=I_1\oplus\cdots\oplus I_n
$$
means that every element of the additive group of $R$ has a unique expression
as a sum of elements from the respective $I_i$. Apply this to the identity
element $1\in R$.
:::

:::

::: {.pf-step #ai-decomposition}
If $a_i\in I_i$, then
$$
a_i=a_i u_1+\cdots+a_i u_n,
$$
and each $a_i u_j$ belongs to $I_j$.

::: pf-proof
Multiplying the equality in step [](#identity-decomposition-unique){.pf-ref} on the left by $a_i$ gives
$$
a_i=a_i1=a_i u_1+\cdots+a_i u_n.
$$
Since $u_j\in I_j$ and $I_j$ is a left ideal, multiplication on the left by
$a_i\in R$ gives $a_i u_j\in I_j$.
:::

:::

::: {.pf-step #orthogonal-idempotent-identities}
For every $a_i\in I_i$,
$$
a_i u_i=a_i,
\qquad
a_i u_j=0\quad(j\neq i).
$$

::: pf-proof
The element $a_i$ already has the direct-sum decomposition
$$
a_i=0+\cdots+0+a_i+0+\cdots+0,
$$
with $a_i$ in the $i$th summand. Step [](#ai-decomposition){.pf-ref} gives another decomposition of
$a_i$, whose $j$th component is $a_i u_j\in I_j$. Uniqueness of the
direct-sum decomposition therefore gives $a_i u_i=a_i$ and
$a_i u_j=0$ for $j\neq i$.
:::

:::

::: pf-qed
The elements $u_i$ constructed in step [](#identity-decomposition-unique){.pf-ref} satisfy the required identities
by step [](#orthogonal-idempotent-identities){.pf-ref}.
:::

:::

:::
