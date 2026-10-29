---
schema: qual/card@1
id: P-WESTOP05-08
kind: problem
title: A finite chain through an open cover of a connected space
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $\mathcal U$ be an open cover of a connected space $X$, and let $a,b\in X$. Show that there are
$$
U_1,\ldots,U_n\in\mathcal U
$$
such that
$$
a\in U_1,
\qquad
b\in U_n,
\qquad
U_i\cap U_{i+1}\ne\varnothing
$$
for $1\le i<n$.

Hint: let $C$ be the set of points that can be joined to $a$ by such a finite chain and analyze $C$.
:::

::: {.solution}

Define
$$
C
=
\left\{
x\in X:
\begin{array}{l}
\text{there exist }U_1,\dots,U_n\in\mathcal U\\
\text{with }a\in U_1,\ x\in U_n,
U_i\cap U_{i+1}\ne\varnothing
\end{array}
\right\}.
$$

::: pf

::: {.pf-step #s1-1}

The set $C$ is nonempty.


::: pf-proof

Choose
$$
U\in\mathcal U
$$
with
$$
a\in U.
$$
Taking the one-term chain $U_1=U$ shows
$$
a\in C.
$$

:::

:::

::: {.pf-step #s1-2}

Let
$$
x\in C.
$$
Choose a chain
$$
U_1,\dots,U_n
$$
witnessing $x\in C$.


::: pf-proof

This is the definition of membership in $C$.

:::

:::

::: pf-step

Choose
$$
V\in\mathcal U
$$
with
$$
x\in V.
$$


::: pf-proof

The family $\mathcal U$ covers $X$.

:::

:::

::: {.pf-step #s1-4}

The sets $U_n$ and $V$ intersect.


::: pf-proof

Both contain the point $x$, so
$$
x\in U_n\cap V.
$$

:::

:::

::: {.pf-step #s1-5}

Every point
$$
y\in V
$$
belongs to $C$.


::: pf-proof

Append $V$ to the chain from step [](#s1-2){.pf-ref}:
$$
U_1,\dots,U_n,V.
$$
By step [](#s1-4){.pf-ref}, the final overlap is nonempty. The chain begins at a set
containing $a$ and ends at $V$, which contains $y$. Hence $y\in C$.

:::

:::

::: {.pf-step #s1-6}

Therefore $C$ is open.


::: pf-proof

For every $x\in C$, step [](#s1-5){.pf-ref} gives an open neighborhood
$$
V\subseteq C.
$$

:::

:::

::: pf-step

Let
$$
x\in X-C,
$$
and choose
$$
V\in\mathcal U
$$
with
$$
x\in V.
$$


::: pf-proof

Again use that $\mathcal U$ is a cover.

:::

:::

::: {.pf-step #s1-8}

One has
$$
\boxed{V\cap C=\varnothing}.
$$


::: pf-proof

Suppose instead that
$$
y\in V\cap C.
$$
Choose a chain
$$
U_1,\dots,U_n
$$
from $a$ to $y$. Since
$$
y\in U_n\cap V,
$$
the enlarged chain
$$
U_1,\dots,U_n,V
$$
joins $a$ to every point of $V$, in particular to $x$. Thus
$$
x\in C,
$$
contradicting $x\in X-C$.

:::

:::

::: {.pf-step #s1-9}

Therefore $X-C$ is open.


::: pf-proof

For every $x\in X-C$, step [](#s1-8){.pf-ref} gives an open neighborhood
$$
V\subseteq X-C.
$$

:::

:::

::: pf-step

Hence $C$ is both open and closed in $X$.


::: pf-proof

Openness is step [](#s1-6){.pf-ref}, and step [](#s1-9){.pf-ref} says its complement is open.

:::

:::

::: pf-step

Since $X$ is connected and $C\ne\varnothing$,
$$
\boxed{C=X}.
$$


::: pf-proof

A connected space has no nontrivial clopen subsets. By step [](#s1-1){.pf-ref},
$$
C\ne\varnothing.
$$
Thus the only possibility is $C=X$.

:::

:::

::: {.pf-step #s1-12}

In particular,
$$
\boxed{b\in C}.
$$


::: pf-proof

Since $b\in X=C$.

:::

:::

::: {.pf-step #s1-13}

Therefore there exist
$$
U_1,\dots,U_n\in\mathcal U
$$
such that
$$
\boxed{
a\in U_1,\qquad
b\in U_n,\qquad
U_i\cap U_{i+1}\ne\varnothing
}
$$
for every $1\le i<n$.


::: pf-proof

This is exactly the definition of $b\in C$ from step [](#s1-12){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-13){.pf-ref} is the required finite chain.

:::

:::

:::
