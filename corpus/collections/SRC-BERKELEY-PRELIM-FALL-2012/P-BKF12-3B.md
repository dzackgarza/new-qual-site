---
schema: qual/card@1
id: P-BKF12-3B
kind: problem
title: Submetries are surjective, continuous and open
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked against Problem 3B in the retained Fall 2012 Berkeley prelim exam
    and independently reviewed the retained solution packet F12_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the surjectivity argument, the 1-Lipschitz estimate, and the exact
    image formula for open balls used to prove openness.
---

::: {.problem}
Let $(X,d_X)$ and $(Y,d_Y)$ be metric spaces.
Suppose that a map $\pi\colon X\to Y$ is a submetry; this means that for every $x\in X$ and any $r>0$, the image of the closed $r$-ball around $x$ is the closed $r$-ball around $\pi(x)$.

(a) Show that $\pi$ is surjective if $X$ is nonempty.

(b) Show that $\pi$ is continuous.

(c) Show that $\pi$ is open (meaning that the image of any open subset is open).
:::

::: {.solution}
Write
$$
\overline B_X(x,r)
\coloneqq\{x'\in X:d_X(x,x')\le r\},
\qquad
B_X(x,r)
\coloneqq\{x'\in X:d_X(x,x')<r\},
$$
and similarly for $Y$.

::: pf

::: {.pf-step #s1}

(a) If $X$ is nonempty, then $\pi$ is surjective.

::: pf-proof

Choose $x_0\in X$, and let $y\in Y$. If
$y=\pi(x_0)$, then $y$ is already in the image. Otherwise set
$$
r=d_Y(\pi(x_0),y)>0.
$$
Then
$$
y\in\overline B_Y(\pi(x_0),r)
=\pi\bigl(\overline B_X(x_0,r)\bigr)
$$
by the submetry property. Hence $y$ has a preimage under $\pi$.

:::

:::

::: {.pf-step #s2}

(b) The map $\pi$ is $1$-Lipschitz, and therefore continuous.

::: pf-proof

Let $x,x'\in X$. If $x=x'$, the required inequality is immediate.
Otherwise put
$$
r=d_X(x,x')>0.
$$
Since $x'\in\overline B_X(x,r)$, the submetry property gives
$$
\pi(x')
\in
\pi\bigl(\overline B_X(x,r)\bigr)
=\overline B_Y(\pi(x),r).
$$
Thus
$$
d_Y(\pi(x),\pi(x'))
\le r
=d_X(x,x').
$$
Hence $\pi$ is $1$-Lipschitz.

:::

:::

::: {.pf-step #s3}

For every $x\in X$ and $r>0$,
$$
\pi(B_X(x,r))=B_Y(\pi(x),r).
$$

::: pf-proof

The inclusion
$$
\pi(B_X(x,r))\subseteq B_Y(\pi(x),r)
$$
follows from the $1$-Lipschitz estimate in step [](#s2){.pf-ref}.

Conversely, let $y\in B_Y(\pi(x),r)$. If $y=\pi(x)$, then
$y\in\pi(B_X(x,r))$. Otherwise
$$
0<d_Y(\pi(x),y)<r.
$$
Choose $s$ with
$$
d_Y(\pi(x),y)\le s<r.
$$
Then
$$
y\in\overline B_Y(\pi(x),s)
=\pi\bigl(\overline B_X(x,s)\bigr).
$$
Thus $y=\pi(x')$ for some $x'$ satisfying
$d_X(x,x')\le s<r$, so $x'\in B_X(x,r)$.

:::

:::

::: {.pf-step #s4}

(c) The map $\pi$ is open.

::: pf-proof

Let $U\subseteq X$ be open, and let $y\in\pi(U)$. Choose
$x\in U$ with $\pi(x)=y$. Since $U$ is open, there is $r>0$ such that
$$
B_X(x,r)\subseteq U.
$$
By step [](#s3){.pf-ref},
$$
B_Y(y,r)
=\pi(B_X(x,r))
\subseteq\pi(U).
$$
Hence every point of $\pi(U)$ is interior, so $\pi(U)$ is open.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s4){.pf-ref} prove parts (a), (b), and (c),
respectively.

:::

:::

:::
