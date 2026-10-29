---
schema: qual/card@1
id: P-UCLAB17S-09
kind: problem
title: Separability of a metric space from separability of $C(X)$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Spring 2017, `assets/attachments/basic-17S.pdf`.
---

::: {.problem}
Let $(X,d)$ be a bounded metric space and suppose $C(X)$, with the supremum norm, is separable.

(a) Show that for every $\varepsilon>0$ there is a countable $Z_\varepsilon\subseteq X$ such that for every $x\in X$ some $z\in Z_\varepsilon$ satisfies
\[
|d(x,y)-d(z,y)|<\varepsilon\quad\text{for all }y\in X.
\]
(b) Deduce that $X$ is separable.
:::

::: {.solution}

For each
\[
x\in X,
\]
define the distance function
\[
\phi_x(y)=d(x,y),
\qquad
y\in X.
\]

::: pf

::: pf-step

Each $\phi_x$ belongs to $C(X)$.


::: pf-proof

The reverse triangle inequality gives
\[
|\phi_x(y)-\phi_x(z)|
=
|d(x,y)-d(x,z)|
\le
d(y,z).
\]
Thus $\phi_x$ is $1$-Lipschitz and hence continuous.

Because $X$ is bounded, there exists $D<\infty$ such that
\[
d(u,v)\le D
\]
for all $u,v\in X$.
Hence
\[
0\le\phi_x(y)\le D,
\]
so $\phi_x$ is bounded and belongs to the supremum-norm space $C(X)$.

:::

:::

::: pf-step

Since $C(X)$ is separable, choose a countable dense set
\[
\mathcal D=\{g_1,g_2,\ldots\}
\subseteq C(X).
\]


::: pf-proof

This is the definition of separability.

:::

:::

::: {.pf-step #s1-3}

Fix
\[
\varepsilon>0.
\]
For every index $j$ such that
\[
B_{\varepsilon/2}(g_j)
\]
meets the set
\[
\Phi
=
\{\phi_x:x\in X\},
\]
choose one point
\[
z_j\in X
\]
with
\[
\|\phi_{z_j}-g_j\|_\infty
<
\frac{\varepsilon}{2}.
\]


::: pf-proof

For each such $j$, the intersection condition supplies at least one
\[
\phi_z\in\Phi
\]
inside the ball of radius $\varepsilon/2$ around $g_j$.
Choose one corresponding point $z_j$.

:::

:::

::: {.pf-step #s1-4}

Let
\[
Z_\varepsilon
\]
be the set of all selected points $z_j$.
Then $Z_\varepsilon$ is countable.


::: pf-proof

At most one point was chosen for each
\[
j\in\NN.
\]
Thus
\[
Z_\varepsilon
\]
is the image of a subset of $\NN$ and is countable.

:::

:::

::: {.pf-step #s1-5}

For every
\[
x\in X,
\]
there exists
\[
z\in Z_\varepsilon
\]
such that
\[
\|\phi_x-\phi_z\|_\infty
<
\varepsilon.
\]


::: pf-proof

Since $\mathcal D$ is dense in $C(X)$, choose $g_j$ with
\[
\|\phi_x-g_j\|_\infty
<
\frac{\varepsilon}{2}.
\]
Then
\[
B_{\varepsilon/2}(g_j)
\]
meets $\Phi$, so a point $z_j\in Z_\varepsilon$ was selected in step [](#s1-3){.pf-ref} with
\[
\|\phi_{z_j}-g_j\|_\infty
<
\frac{\varepsilon}{2}.
\]
The triangle inequality gives
\[
\|\phi_x-\phi_{z_j}\|_\infty
<
\varepsilon.
\]

:::

:::

::: {.pf-step #s1-6}

Hence for every
\[
x\in X,
\]
some
\[
z\in Z_\varepsilon
\]
satisfies
\[
\boxed{
|d(x,y)-d(z,y)|<\varepsilon
\quad
\text{for every }y\in X.
}
\]


::: pf-proof

The supremum-norm inequality in step [](#s1-5){.pf-ref} means precisely that
\[
\sup_{y\in X}
|d(x,y)-d(z,y)|
<
\varepsilon.
\]
This proves part (a).

:::

:::

::: {.pf-step #s1-7}

For every positive integer $m$, choose the countable set
\[
Z_{1/m}
\]
from part (a), and define
\[
Z
=
\bigcup_{m=1}^{\infty}Z_{1/m}.
\]
Then $Z$ is countable.


::: pf-proof

Each
\[
Z_{1/m}
\]
is countable by step [](#s1-4){.pf-ref}.
A countable union of countable sets is countable.

:::

:::

::: {.pf-step #s1-8}

The set $Z$ is dense in $X$.


::: pf-proof

Fix
\[
x\in X
\]
and
\[
\eta>0.
\]
Choose
\[
m
\]
so large that
\[
\frac1m<\eta.
\]
By step [](#s1-6){.pf-ref}, there exists
\[
z\in Z_{1/m}
\subseteq Z
\]
such that
\[
|d(x,y)-d(z,y)|
<
\frac1m
\]
for every $y\in X$.
Take
\[
y=x.
\]
Then
\[
d(x,z)
=
|d(z,x)-d(x,x)|
<
\frac1m
<
\eta.
\]
Thus every open ball around $x$ meets $Z$.

:::

:::

::: {.pf-step #s1-9}

Therefore
\[
\boxed{X\text{ is separable}.}
\]


::: pf-proof

Step [](#s1-7){.pf-ref} gives a countable subset $Z\subseteq X$, and step [](#s1-8){.pf-ref} shows that it is dense.
This is the definition of separability.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} proves part (a), and step [](#s1-9){.pf-ref} proves part (b).

:::

:::

:::
