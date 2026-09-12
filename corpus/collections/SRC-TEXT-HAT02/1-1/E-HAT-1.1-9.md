---
schema: qual/card@1
id: E-HAT-1.1-9
kind: problem
title: Borsuk–Ulam bisects three compact sets in $\mathbb{R}^3$
classification:
  areas:
  - topology
  topics:
  - Borsuk-Ulam Theorem
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.1, Exercise 9; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Parameterized oriented affine planes by S^3 and proved continuity of the three signed-volume differences by dominated convergence before applying Borsuk--Ulam.
---

Let $A_1, A_2, A_3$ be compact sets in $\mathbb{R}^3$.
Use the Borsuk–Ulam theorem to show that there is one plane $P \subset \mathbb{R}^3$ that simultaneously divides each $A_i$ into two pieces of equal measure.

::: {.solution}
Let $\mu$ denote three-dimensional Lebesgue measure.
Since each $A_i$ is compact, it is measurable and has finite measure.

<1>1. Parameterize oriented affine planes and their two sides by points
\[
q=(v,d)\in S^3\subset\mathbb R^3\times\mathbb R.
\]
For $v\ne0$, the corresponding plane is
\[
P_q=\{x\in\mathbb R^3:v\cdot x=d\},
\]
with positive and negative sides determined by the sign of $v\cdot x-d$.
::: {.proof}
Multiplying $(v,d)$ by $-1$ leaves the underlying plane unchanged and exchanges its two sides.
The two points of $S^3$ with $v=0$ are harmless compactification points and will be treated below.
:::

<1>2. For $i=1,2,3$, define
\[
F_i(v,d)=\int_{A_i}\operatorname{sgn}(v\cdot x-d)\,d\mu(x),
\]
where $\operatorname{sgn}(t)=1$ for $t>0$, $-1$ for $t<0$, and $0$ for $t=0$.
Then
\[
F=(F_1,F_2,F_3):S^3\to\mathbb R^3
\]
is continuous.
::: {.proof}
Fix $q=(v,d)\in S^3$ and let $q_n=(v_n,d_n)\to q$.
For each fixed $x$ with
\[
v\cdot x-d\ne0,
\]
one has
\[
\operatorname{sgn}(v_n\cdot x-d_n)
\longrightarrow
\operatorname{sgn}(v\cdot x-d).
\]

If $v\ne0$, the exceptional set
\[
\{x:v\cdot x=d\}
\]
is an affine plane and therefore has three-dimensional Lebesgue measure zero.
If $v=0$, then $|d|=1$, so $v\cdot x-d=-d\ne0$ for every $x$ and there is no exceptional set.
The integrands are uniformly bounded by $1$.
Dominated convergence therefore gives
\[
F_i(q_n)\to F_i(q)
\]
for each $i$, proving continuity of $F$.
:::

<1>3. The map $F$ is odd:
\[
F(-q)=-F(q).
\]
::: {.proof}
For every $x$,
\[
(-v)\cdot x-(-d)=-(v\cdot x-d),
\]
so the sign of the integrand reverses.
Thus each $F_i$ changes sign under $q\mapsto-q$.
:::

<1>4. There exists $q=(v,d)\in S^3$ such that
\[
F(q)=0.
\]
::: {.proof}
Apply the Borsuk--Ulam theorem to the continuous map
\[
F:S^3\to\mathbb R^3.
\]
There is $q\in S^3$ with
\[
F(q)=F(-q).
\]
By oddness from <1>3,
\[
F(q)=-F(q),
\]
hence $F(q)=0$.
:::

<1>5. Unless all three sets have measure zero, the point $q$ from <1>4 has $v\ne0$.
::: {.proof}
If $v=0$, then $d=\pm1$.
For $d=1$ the integrand is identically $-1$, so
\[
F_i(0,1)=-\mu(A_i),
\]
and for $d=-1$ it is identically $1$, so
\[
F_i(0,-1)=\mu(A_i).
\]
Thus $F(q)=0$ at such a point only when every $\mu(A_i)=0$.
If all three measures are zero, any plane already bisects all three sets.
:::

<1>6. For the affine plane
\[
P=P_q=\{x:v\cdot x=d\}
\]
with $q$ as in <1>4 and $v\ne0$, each $A_i$ has equal measure on the two sides of $P$.
::: {.proof}
An affine plane has three-dimensional Lebesgue measure zero, so
\[
\mu(A_i\cap P)=0.
\]
The equation $F_i(q)=0$ says exactly
\[
\mu\bigl(A_i\cap\{v\cdot x>d\}\bigr)
=
\mu\bigl(A_i\cap\{v\cdot x<d\}\bigr).
\]
Thus $P$ bisects the measure of $A_i$ for all three indices simultaneously.
:::
:::
