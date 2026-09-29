---
schema: qual/card@1
id: P-BKS12-1A
kind: problem
title: Projection along a compact factor is a closed map
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow in the projection p against s12solutions.pdf page 1 problem 1A.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked a direct compactness proof using finitely many product neighborhoods in the complement of Z.
---

::: {.problem}
Suppose that $X$ is a compact metric space. If $Y$ is another metric space (possibly noncompact), let $p : X \times Y \to Y$ be the map $p(x, y) = y$. Show that if $Z$ is a closed subset of $X \times Y$ then $p(Z)$ is closed in $Y$.
:::

::: {.solution}

::: pf

::: {.pf-step #y0-not-in-fiber}
Let
$$
y_0\in Y\setminus p(Z).
$$
Then for every $x\in X$,
$$
(x,y_0)\notin Z.
$$

::: pf-proof
If $(x,y_0)\in Z$ for some $x\in X$, then by definition of the projection,
$$
y_0=p(x,y_0)\in p(Z),
$$
contrary to the choice of $y_0$.
:::

:::

::: {.pf-step #product-neighborhood}
For every $x\in X$, there are open sets
$$
U_x\subseteq X,
\qquad
V_x\subseteq Y
$$
with
$$
x\in U_x,
\qquad
y_0\in V_x,
$$
such that
$$
(U_x\times V_x)\cap Z=\varnothing.
$$

::: pf-proof
By step [](#y0-not-in-fiber){.pf-ref}, $(x,y_0)$ lies in the open set
$$
(X\times Y)\setminus Z.
$$
The product topology has a basis of sets of the form $U\times V$, so there
is such a product neighborhood of $(x,y_0)$ contained in the complement
of $Z$.
:::

:::

::: {.pf-step #finite-subcover}
There exist points $x_1,\ldots,x_m\in X$ such that
$$
X
=
U_{x_1}\cup\cdots\cup U_{x_m}.
$$

::: pf-proof
The sets $U_x$, for $x\in X$, form an open cover of the compact space
$X$. Compactness supplies a finite subcover.
:::

:::

::: {.pf-step #v-avoids-pz}
The set
$$
V
\coloneqq
V_{x_1}\cap\cdots\cap V_{x_m}
$$
is an open neighborhood of $y_0$ and satisfies
$$
V\cap p(Z)=\varnothing.
$$

::: pf-proof
The intersection is finite, so $V$ is open, and every $V_{x_j}$ contains
$y_0$, so $y_0\in V$.

Suppose instead that some
$$
y\in V\cap p(Z).
$$
Then there is an $x\in X$ with
$$
(x,y)\in Z.
$$
By step [](#finite-subcover){.pf-ref}, choose $j$ such that $x\in U_{x_j}$. Since $y\in V$, one
also has $y\in V_{x_j}$. Thus
$$
(x,y)\in U_{x_j}\times V_{x_j},
$$
contradicting step [](#product-neighborhood){.pf-ref}.
:::

:::

::: {.pf-step #complement-open}
The complement
$$
Y\setminus p(Z)
$$
is open.

::: pf-proof
For every $y_0\in Y\setminus p(Z)$, step [](#v-avoids-pz){.pf-ref} constructs an open
neighborhood $V$ of $y_0$ contained in $Y\setminus p(Z)$.
:::

:::

::: {.pf-step #pz-closed}
The set
$$
\boxed{p(Z)}
$$
is closed in $Y$.

::: pf-proof
Step [](#complement-open){.pf-ref} shows that its complement is open.
:::

:::

::: pf-qed
Step [](#pz-closed){.pf-ref} is the required conclusion.
:::

:::

:::
