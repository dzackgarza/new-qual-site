---
schema: qual/card@1
id: P-UCLAB12W-01
kind: problem
title: Hausdorff distance on closed subsets of the unit interval
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 1 of the retained UCLA Basic Examination, Winter 2012. The source says all closed subsets of [0,1], which includes the empty set although its displayed Hausdorff formula is undefined there; this card adds the forced nonempty hypothesis.
---

::: {.problem}
Let $\Omega$ be the set of all nonempty closed subsets of $[0,1]$ and define
$$
\rho(A,B)=\max\left\{
\sup_{x\in A}\inf_{y\in B}\abs{x-y},
\sup_{y\in B}\inf_{x\in A}\abs{x-y}
\right\}.
$$
Show that $(\Omega,\rho)$ is a metric space.
:::

::: {.solution}

For a nonempty closed set $B\subseteq[0,1]$ and $x\in[0,1]$, write
$$
d(x,B)=\inf_{y\in B}\abs{x-y},
$$
and for $A,B\in\Omega$ write
$$
h(A,B)=\sup_{x\in A}d(x,B).
$$
Then
$$
\rho(A,B)=\max\{h(A,B),h(B,A)\}.
$$

::: pf

::: {.pf-step #s1-1}

The number $\rho(A,B)$ is well defined and belongs to $[0,1]$ for every $A,B\in\Omega$.


::: pf-proof

Since $B$ is nonempty, the set
$$
\{\abs{x-y}:y\in B\}
$$
is nonempty and bounded below by $0$, so $d(x,B)$ exists. Moreover, because $x,y\in[0,1]$,
$$
0\le d(x,B)\le1.
$$
Thus $\{d(x,B):x\in A\}$ is nonempty and bounded above by $1$, so $h(A,B)$ exists and lies in $[0,1]$. The same holds for $h(B,A)$, hence so does their maximum.

:::

:::

::: {.pf-step #s1-2}

For all $A,B\in\Omega$,
$$
\rho(A,B)\ge0
\qquad\text{and}\qquad
\rho(A,B)=\rho(B,A).
$$


::: pf-proof

Every distance $\abs{x-y}$ is nonnegative, so both directed distances $h(A,B)$ and $h(B,A)$ are nonnegative. Symmetry follows directly from
$$
\rho(A,B)=\max\{h(A,B),h(B,A)\}.
$$

:::

:::

::: {.pf-step #s1-3}

If $\rho(A,B)=0$, then $A\subseteq B$.


::: pf-proof

If $\rho(A,B)=0$, then $h(A,B)=0$. Hence for every $x\in A$,
$$
d(x,B)=0.
$$
Thus for every $n\ge1$ there exists $y_n\in B$ with
$$
\abs{x-y_n}<\frac1n.
$$
Therefore $y_n\to x$. Since $B$ is closed in $[0,1]$, it contains the limit $x$. Thus every $x\in A$ belongs to $B$.

:::

:::

::: {.pf-step #s1-4}

One has
$$
\rho(A,B)=0
\quad\Longleftrightarrow\quad
A=B.
$$


::: pf-proof

If $\rho(A,B)=0$, step [](#s1-3){.pf-ref} gives $A\subseteq B$. By symmetry, applying step [](#s1-3){.pf-ref} with $A$ and $B$ interchanged gives $B\subseteq A$. Hence $A=B$.

Conversely, if $A=B$, then for every $x\in A$ one may choose $y=x\in B$, so $d(x,B)=0$. Hence $h(A,B)=h(B,A)=0$ and therefore $\rho(A,B)=0$.

:::

:::

::: {.pf-step #s1-5}

For any nonempty $B,C\subseteq[0,1]$, any $x\in[0,1]$, and any $y\in B$,
$$
d(x,C)\le\abs{x-y}+d(y,C).
$$


::: pf-proof

For every $z\in C$, the triangle inequality gives
$$
\abs{x-z}\le\abs{x-y}+\abs{y-z}.
$$
Taking the infimum over $z\in C$ yields
$$
d(x,C)\le\abs{x-y}+d(y,C).
$$

:::

:::

::: {.pf-step #s1-6}

For all $A,B,C\in\Omega$,
$$
h(A,C)\le h(A,B)+h(B,C).
$$


::: pf-proof

Fix $x\in A$. By step [](#s1-5){.pf-ref}, for every $y\in B$,
$$
d(x,C)
\le
\abs{x-y}+d(y,C)
\le
\abs{x-y}+h(B,C).
$$
Taking the infimum over $y\in B$ gives
$$
d(x,C)
\le
d(x,B)+h(B,C)
\le h(A,B)+h(B,C).
$$
Now take the supremum over $x\in A$.

:::

:::

::: {.pf-step #s1-7}

The triangle inequality
$$
\rho(A,C)\le\rho(A,B)+\rho(B,C)
$$
holds for all $A,B,C\in\Omega$.


::: pf-proof

By step [](#s1-6){.pf-ref},
$$
h(A,C)
\le
h(A,B)+h(B,C)
\le
\rho(A,B)+\rho(B,C).
$$
Applying step [](#s1-6){.pf-ref} with the order reversed gives
$$
h(C,A)
\le
h(C,B)+h(B,A)
\le
\rho(B,C)+\rho(A,B).
$$
Both entries in
$$
\rho(A,C)=\max\{h(A,C),h(C,A)\}
$$
are therefore bounded above by $\rho(A,B)+\rho(B,C)$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves well-definedness, step [](#s1-2){.pf-ref} gives nonnegativity and symmetry, step [](#s1-4){.pf-ref} gives definiteness, and step [](#s1-7){.pf-ref} proves the triangle inequality. Thus $\rho$ is a metric on $\Omega$.

:::

:::

:::
