---
schema: qual/card@1
id: P-BERK80S-12
kind: problem
title: Common normal line to two surfaces
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 12 of the vendored Berkeley Preliminary Exam, Summer 1980; restored the OCR-split center coordinate $z-10$ in the ellipsoid equation.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified existence of a distance-minimizing pair by compactness/coercivity and perpendicularity to both tangent planes by first variation.
---

::: {.problem}
Let $S\subset\RR^3$ denote the ellipsoidal surface defined by

$$
2x^2+(y-1)^2+(z-10)^2=1.
$$

Let $T\subset\RR^3$ be the surface defined by

$$
z=\frac{1}{x^2+y^2+1}.
$$

Prove that there exist points $p\in S$, $q\in T$, such that the line $pq$ is perpendicular to $S$ at $p$ and to $T$ at $q$.
:::

::: {.solution}
Let
$$
D(p,q)=\norm{p-q}^2,
\qquad (p,q)\in S\times T,
$$
and for a point $r$ of a surface $\Sigma$ write $\operatorname{Tan}_r\Sigma$
for the tangent plane of $\Sigma$ at $r$.

::: pf

::: {.pf-step #s1}

The function $D$ attains its minimum on $S\times T$ at some pair
$(p,q)$.

::: pf-proof

The ellipsoid $S$ is compact, so there is $R>0$ such that
$$
S\subset B_R(0).
$$
The surface $T$ is the graph of the continuous function
$$
(x,y)\longmapsto \frac1{x^2+y^2+1},
$$
so $T$ is closed.

Fix any pair $(p_0,q_0)\in S\times T$ and put $M=\norm{p_0-q_0}$. If
$q\in T$ satisfies $\norm{q}>R+M+1$, then for every $p\in S$,
$$
\norm{p-q}\ge \norm{q}-\norm{p}>M+1>M.
$$
Hence the infimum of $D$ on $S\times T$ equals its infimum on
$$
S\times\bigl(T\cap \overline B_{R+M+1}(0)\bigr),
$$
which is compact. By continuity, $D$ attains its minimum there, at a pair
$(p,q)$, and this pair minimizes $D$ on $S\times T$.

:::

:::

::: {.pf-step #s2}

The points $p$ and $q$ are distinct.

::: pf-proof

Every point $(x,y,z)\in S$ satisfies
$$
(z-10)^2\le1,
$$
so
$$
9\le z\le11.
$$
Every point $(x,y,z)\in T$ satisfies
$$
0<z=\frac1{x^2+y^2+1}\le1.
$$
Thus $S\cap T=\varnothing$, so $p\ne q$ and the line $pq$ is defined.

:::

:::

::: {.pf-step #s3}

The line $pq$ is perpendicular to $S$ at $p$.

::: pf-proof

Let $v\in\operatorname{Tan}_pS$. Choose a smooth curve
$\gamma:(-\varepsilon,\varepsilon)\to S$ with
$$
\gamma(0)=p,
\qquad
\gamma'(0)=v.
$$
Because $(p,q)$ minimizes $D$, the function
$$
\varphi(t)=\norm{\gamma(t)-q}^2
$$
has a minimum at $t=0$. Hence
$$
0=\varphi'(0)=2(p-q)\cdot v.
$$
Since this holds for every $v\in\operatorname{Tan}_pS$, the vector $q-p$ is
orthogonal to $\operatorname{Tan}_pS$.

:::

:::

::: {.pf-step #s4}

The line $pq$ is perpendicular to $T$ at $q$.

::: pf-proof

Let $w\in\operatorname{Tan}_qT$ and choose a smooth curve
$\eta:(-\varepsilon,\varepsilon)\to T$ with
$$
\eta(0)=q,
\qquad
\eta'(0)=w.
$$
The function
$$
\psi(t)=\norm{p-\eta(t)}^2
$$
has a minimum at $0$, so
$$
0=\psi'(0)=2(q-p)\cdot w.
$$
Hence $q-p$ is orthogonal to $\operatorname{Tan}_qT$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give distinct points $p\in S$ and $q\in T$, and steps
[](#s3){.pf-ref} and [](#s4){.pf-ref} show that the line $pq$ is perpendicular to $S$ at $p$ and to
$T$ at $q$.

:::

:::

:::
