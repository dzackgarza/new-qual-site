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
\[
\boxed{\text{no}}.
\]

Take
\[
Y=\mathbb R^2
\]
with the usual topology. For each \(n\ge1\), define
\[
\boxed{
X_n
=
\bigl(\{-1\}\times[0,\infty)\bigr)
\cup
\bigl([-1,1]\times[n,\infty)\bigr)
\cup
\bigl(\{1\}\times[0,\infty)\bigr)}.
\]

<1>1. Each \(X_n\) is path connected.

::: {.proof}
Let
\[
L=\{-1\}\times[0,\infty),
\qquad
R=\{1\}\times[0,\infty),
\qquad
S_n=[-1,1]\times[n,\infty).
\]
The strip \(S_n\) is path connected. It meets \(L\) along
\[
\{-1\}\times[n,\infty)
\]
and meets \(R\) along
\[
\{1\}\times[n,\infty).
\]
Thus
\[
L\cup S_n\cup R
\]
is path connected.
:::

<1>2. The sequence is decreasing:
\[
\boxed{X_{n+1}\subseteq X_n}.
\]

::: {.proof}
The two vertical rays are independent of \(n\), and
\[
[-1,1]\times[n+1,\infty)
\subseteq
[-1,1]\times[n,\infty).
\]
:::

<1>3. Every point on either vertical ray belongs to every \(X_n\).

::: {.proof}
The sets
\[
\{-1\}\times[0,\infty)
\qquad\text{and}\qquad
\{1\}\times[0,\infty)
\]
are included explicitly in the definition of every \(X_n\).
:::

<1>4. No point \((x,y)\) with \(-1<x<1\) belongs to every \(X_n\).

::: {.proof}
Such a point can belong to \(X_n\) only through the strip
\[
[-1,1]\times[n,\infty),
\]
which requires \(y\ge n\). For any fixed finite \(y\), choose \(n>y\).
Then \((x,y)\notin X_n\).
:::

<1>5. Therefore
\[
\boxed{
\bigcap_{n=1}^{\infty}X_n
=
\bigl(\{-1\}\times[0,\infty)\bigr)
\cup
\bigl(\{1\}\times[0,\infty)\bigr)}.
\]

::: {.proof}
Step <1>3 gives inclusion of the two rays in the intersection, and step <1>4 excludes all points between them.
:::

<1>6. The two rays are disjoint, nonempty, and open in their union.

::: {.proof}
In the subspace
\[
L\cup R,
\]
one has
\[
L=(L\cup R)\cap\{(x,y):x<0\}
\]
and
\[
R=(L\cup R)\cap\{(x,y):x>0\},
\]
where the two half-planes are open in \(\mathbb R^2\).
:::

<1>7. Hence
\[
\boxed{\bigcap_n X_n\text{ is disconnected}}.
\]

::: {.proof}
Step <1>6 gives a separation into two disjoint nonempty open subsets.
:::

<1>8. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 verify the hypotheses, while step <1>7 disproves the proposed conclusion.
:::
:::
