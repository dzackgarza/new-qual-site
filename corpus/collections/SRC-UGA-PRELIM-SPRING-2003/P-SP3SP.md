---
schema: qual/card@1
id: P-SP3SP
kind: problem
title: Adjoining a vector already in a span does not change the span
classification:
  areas:
  - prelim
  topics:
  - Vector Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Step 1, the definition in part (a), was the card's only step with no proof body; it now
    carries one showing that the displayed set is a subspace containing each $v_i$ and that it
    is contained in every such subspace, which is what makes it the span. No claim of part (b)
    is changed and steps 2 to 4 stand as they were. Checked: that the zero vector arises with
    all $a_i=0$, that a sum of two combinations is a combination, that a scalar multiple of one
    is a combination, and that a subspace containing the $v_i$ contains every combination.
---

::: {.problem}
(a) Define the span of vectors $v_1, \dots, v_k$ in $\RR^n$.

(b) Prove that if $w$ lies in the span of $v_1, \dots, v_k$, then the span of $v_1, \dots, v_k, w$ is equal to the span of $v_1, \dots, v_k$.
:::

::: {.solution}

::: pf

::: pf-step
The span of $v_1,\dots,v_k$ is
$$
\operatorname{span}(v_1,\dots,v_k)
=\left\{\sum_{i=1}^k a_i v_i : a_1,\dots,a_k\in\RR\right\}.
$$

::: pf-proof
The displayed set contains $0$, taking all $a_i=0$; it is closed under addition, since $\sum a_iv_i+\sum a'_iv_i=\sum(a_i+a'_i)v_i$; and it is closed under scalar multiplication, since $c\sum a_iv_i=\sum(ca_i)v_i$. So it is a subspace of $\RR^n$, and it contains each $v_j$, taking $a_j=1$ and the other coefficients $0$. Conversely, a subspace $W$ containing every $v_i$ contains each $a_iv_i$ and hence their sum, so $W$ contains the displayed set. It is therefore the smallest subspace containing $v_1,\dots,v_k$, which is what the span is.
:::

:::

::: {.pf-step #s2}
Suppose $w\in\operatorname{span}(v_1,\dots,v_k)$. Then
$$
\operatorname{span}(v_1,\dots,v_k)
\subseteq
\operatorname{span}(v_1,\dots,v_k,w).
$$

::: pf-proof
Every linear combination of $v_1,\dots,v_k$ is also a linear combination of $v_1,\dots,v_k,w$, by taking the coefficient of $w$ to be $0$.
:::

:::

::: {.pf-step #s3}
Conversely,
$$
\operatorname{span}(v_1,\dots,v_k,w)
\subseteq
\operatorname{span}(v_1,\dots,v_k).
$$

::: pf-proof
Because $w$ lies in the first span, there are $b_1,\dots,b_k\in\RR$ such that
$$
w=\sum_{i=1}^k b_i v_i.
$$
Hence every element of the enlarged span has the form
$$
\sum_{i=1}^k a_i v_i+c w
=\sum_{i=1}^k (a_i+c b_i)v_i,
$$
which belongs to $\operatorname{span}(v_1,\dots,v_k)$.
:::

:::

::: pf-step
Therefore
$$
\operatorname{span}(v_1,\dots,v_k,w)
=
\operatorname{span}(v_1,\dots,v_k).
$$

::: pf-proof
This follows from the two inclusions in steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.
:::

:::

:::
:::
