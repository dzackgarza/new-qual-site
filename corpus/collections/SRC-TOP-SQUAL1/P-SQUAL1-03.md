---
schema: qual/card@1
id: P-SQUAL1-03
kind: problem
title: A decreasing intersection of connected subspaces need not be connected
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let $Y$ be a topological space and, for each natural number $n$, let $X_n$ be a connected subspace of $Y$ such that
$$X_{n+1}\subseteq X_n.$$
Must
$$\bigcap_n X_n$$
be connected? Prove your answer.
:::

::: {.solution}

The answer is
$$
\boxed{\text{no}}.
$$

Take
$$
Y=\RR^2
$$
with the usual topology. For each $n\ge1$, define
$$
\boxed{
X_n
=
\bigl(\{-1\}\times[0,\infty)\bigr)
\cup
\bigl([-1,1]\times[n,\infty)\bigr)
\cup
\bigl(\{1\}\times[0,\infty)\bigr)}.
$$

::: pf

::: {.pf-step #s1-1}

Each $X_n$ is path connected.


::: pf-proof

Let
$$
L=\{-1\}\times[0,\infty),
\qquad
R=\{1\}\times[0,\infty),
\qquad
S_n=[-1,1]\times[n,\infty).
$$
The strip $S_n$ is path connected. It meets $L$ along
$$
\{-1\}\times[n,\infty)
$$
and meets $R$ along
$$
\{1\}\times[n,\infty).
$$
Thus
$$
L\cup S_n\cup R
$$
is path connected.

:::

:::

::: {.pf-step #s1-2}

The sequence is decreasing:
$$
\boxed{X_{n+1}\subseteq X_n}.
$$


::: pf-proof

The two vertical rays are independent of $n$, and
$$
[-1,1]\times[n+1,\infty)
\subseteq
[-1,1]\times[n,\infty).
$$

:::

:::

::: {.pf-step #s1-3}

Every point on either vertical ray belongs to every $X_n$.


::: pf-proof

The sets
$$
\{-1\}\times[0,\infty)
\qquad\text{and}\qquad
\{1\}\times[0,\infty)
$$
are included explicitly in the definition of every $X_n$.

:::

:::

::: {.pf-step #s1-4}

No point $(x,y)$ with $-1<x<1$ belongs to every $X_n$.


::: pf-proof

Such a point can belong to $X_n$ only through the strip
$$
[-1,1]\times[n,\infty),
$$
which requires $y\ge n$. For any fixed finite $y$, choose $n>y$.
Then $(x,y)\notin X_n$.

:::

:::

::: pf-step

Therefore
$$
\boxed{
\bigcap_{n=1}^{\infty}X_n
=
\bigl(\{-1\}\times[0,\infty)\bigr)
\cup
\bigl(\{1\}\times[0,\infty)\bigr)}.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} gives inclusion of the two rays in the intersection, and step [](#s1-4){.pf-ref} excludes all points between them.

:::

:::

::: {.pf-step #s1-6}

The two rays are disjoint, nonempty, and open in their union.


::: pf-proof

In the subspace
$$
L\cup R,
$$
one has
$$
L=(L\cup R)\cap\{(x,y):x<0\}
$$
and
$$
R=(L\cup R)\cap\{(x,y):x>0\},
$$
where the two half-planes are open in $\RR^2$.

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{\bigcap_n X_n\text{ is disconnected}}.
$$


::: pf-proof

Step [](#s1-6){.pf-ref} gives a separation into two disjoint nonempty open subsets.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} verify the hypotheses, while step [](#s1-7){.pf-ref} disproves the proposed conclusion.

:::

:::

:::
