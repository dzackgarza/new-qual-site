---
schema: qual/card@1
id: P-OCUZ4
kind: problem
title: Fixed points of self-maps of $\RP^2\vee\RP^2$
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Prove or disprove:

Every map from $\RP^2 \lor \RP^2$ to itself has a fixed point.
:::

::: {.solution}
**Goal.** Decide whether every self-map of $\RP^2 \vee \RP^2$ has a fixed point.

<1>1. The statement is true.
<2>1. It suffices to show the mod-2 Lefschetz number $L(f)$ is always odd (hence nonzero).
Proof: the Lefschetz fixed point theorem: if $L(f) \neq 0$ then $f$ has a fixed point.

<1>2. The mod-2 cohomology ring of $\RP^2 \vee \RP^2$ is $\ZZ/2[x,y]/(x^3, y^3, xy)$ with $|x| = |y| = 1$.
Proof: $H^*(\RP^2;\ZZ/2) = \ZZ/2[x]/(x^3)$, and the cohomology of a wedge is the direct sum in positive degrees, with the cross terms killed ($xy = 0$).

<1>3. A self-map $f$ induces $f^*(x) = ax + by$ and $f^*(y) = cx + dy$ for $a,b,c,d \in \ZZ/2$.
Proof: $x, y$ span $H^1$, so $f^*$ on $H^1$ is a $2\times 2$ matrix $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ over $\ZZ/2$.

<1>4. $f^*$ on $H^2$ is the same matrix $M$.
<2>1. $f^*(x^2) = (ax + by)^2 = a^2 x^2 + b^2 y^2 = a x^2 + b y^2$.
Proof: $xy = 0$ and $a^2 = a$, $b^2 = b$ in $\ZZ/2$.
<2>2. $f^*(y^2) = c x^2 + d y^2$.
Proof: same computation.
<2>3. Hence $f^*$ on $H^2$ (basis $x^2, y^2$) is $\begin{pmatrix} a & c \\ b & d \end{pmatrix} = M^T$.
Proof: read off the coefficients from <1>4.1 and <1>4.2.

<1>5. $f_*$ on $H_1$ and $f_*$ on $H_2$ have the same trace.
<2>1. $f_*$ on $H_1$ is the transpose of $f^*$ on $H^1$, i.e. $M^T$.
Proof: homology and cohomology are dual, so $f_* = (f^*)^T$.
<2>2. $f_*$ on $H_2$ is the transpose of $f^*$ on $H^2$, i.e. $(M^T)^T = M$.
Proof: same duality.
<2>3. $\operatorname{tr}(f_*|_{H_1}) = \operatorname{tr}(M^T) = \operatorname{tr}(M) = \operatorname{tr}(f_*|_{H_2})$.
Proof: a matrix and its transpose have the same trace.

<1>6. $L(f) \equiv 1 \pmod 2$.
<2>1. $L(f) \equiv \operatorname{tr}(f_*|_{H_0}) + \operatorname{tr}(f_*|_{H_1}) + \operatorname{tr}(f_*|_{H_2}) \pmod 2$.
Proof: the mod-2 Lefschetz number is the alternating sum of traces of $f_*$ on $H_i(\cdot;\ZZ/2)$.
<2>2. $\operatorname{tr}(f_*|_{H_0}) = 1$.
Proof: $H_0 = \ZZ/2$ and $f_*$ is the identity on $H_0$.
<2>3. $\operatorname{tr}(f_*|_{H_1}) + \operatorname{tr}(f_*|_{H_2}) = 2\operatorname{tr}(M) \equiv 0 \pmod 2$.
Proof: by <1>5.3 the two traces are equal, so their sum is even.
<2>4. Hence $L(f) \equiv 1 \pmod 2$, so $L(f) \neq 0$.
Proof: combine <1>6.2 and <1>6.3.

<1>7. Q.E.D.
Proof: <1>6.4 shows $L(f) \neq 0$ for every self-map $f$, so every self-map has a fixed point by the Lefschetz fixed point theorem.
:::
