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
Let $S \subset \mathbb { R } ^ { 3 }$ denote the ellipsoidal surface defined by

$$
2 x ^ { 2 } + ( y - 1 ) ^ { 2 } + (z-10)^2 = 1 .
$$

Let $T \subset \mathbb { R } ^ { 3 }$ be the surface defined by

$$
z = { \frac { 1 } { x ^ { 2 } + y ^ { 2 } + 1 } } \cdotp
$$

Prove that there exist points $p \in S , \ q \in T$ , such that the line pq is perpendicular to S at p and to T at q.
:::


::: {.solution}
We minimize the squared distance
\[
D(p,q)=\|p-q\|^2
\]
over $S\times T$.

<1>1. The distance between $S$ and $T$ is attained by some pair $(p,q)\in S\times T$.
::: {.proof}
The ellipsoid $S$ is compact. In particular, there is $R>0$ such that
\[
S\subset B_R(0).
\]
The surface $T$ is the graph of the continuous function
\[
(x,y)\longmapsto \frac1{x^2+y^2+1},
\]
so $T$ is closed.

Fix any pair $(p_0,q_0)\in S\times T$ and put $M=\|p_0-q_0\|$.
If $q\in T$ satisfies $\|q\|>R+M+1$, then for every $p\in S$,
\[
\|p-q\|\ge \|q\|-\|p\|>M+1>M.
\]
Hence no minimizing pair can have $q$ outside the closed ball $\overline B_{R+M+1}(0)$.
Therefore it suffices to minimize $D$ on
\[
S\times\bigl(T\cap \overline B_{R+M+1}(0)\bigr),
\]
which is compact. By continuity, $D$ attains its minimum there, say at $(p,q)$.
:::

<1>2. The minimizing points are distinct.
::: {.proof}
Every point $(x,y,z)\in S$ satisfies
\[
(z-10)^2\le1,
\]
so
\[
9\le z\le11.
\]
Every point $(x,y,z)\in T$ satisfies
\[
0<z=\frac1{x^2+y^2+1}\le1.
\]
Thus $S\cap T=\varnothing$, so the minimizing pair has $p\ne q$ and determines a genuine line.
:::

<1>3. The line through $p$ and $q$ is perpendicular to $S$ at $p$.
::: {.proof}
Let $v\in T_pS$ be any tangent vector. Choose a smooth curve $\gamma:(-\varepsilon,\varepsilon)\to S$ with
\[
\gamma(0)=p,
\qquad
\gamma'(0)=v.
\]
Because $(p,q)$ minimizes the distance, the function
\[
\varphi(t)=\|\gamma(t)-q\|^2
\]
has a minimum at $t=0$. Hence
\[
0=\varphi'(0)=2(p-q)\cdot v.
\]
Since this holds for every $v\in T_pS$, the vector $q-p$ is orthogonal to the tangent plane $T_pS$. Thus the line $pq$ is perpendicular to $S$ at $p$.
:::

<1>4. The same line is perpendicular to $T$ at $q$.
::: {.proof}
Let $w\in T_qT$ and choose a smooth curve $\eta:(-\varepsilon,\varepsilon)\to T$ with
\[
\eta(0)=q,
\qquad
\eta'(0)=w.
\]
Now
\[
\psi(t)=\|p-\eta(t)\|^2
\]
has a minimum at $0$, so
\[
0=\psi'(0)=2(q-p)\cdot w.
\]
Hence $q-p$ is orthogonal to $T_qT$. Therefore the line $pq$ is perpendicular to both surfaces at the minimizing points.
:::
:::
