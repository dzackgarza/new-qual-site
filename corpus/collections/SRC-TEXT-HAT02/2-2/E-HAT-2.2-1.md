---
schema: qual/card@1
id: E-HAT-2.2-1
kind: problem
title: Brouwer fixed point theorem via degree theory
classification:
  areas:
  - topology
  topics:
  - Degree
  - Fixed Point Theorems
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 1; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete proof reviewed using degree theory and orthogonal-group homotopies.
---

::: {.problem}
Prove the Brouwer fixed point theorem for maps $f: D^n \to D^n$ by applying degree theory to the map $S^n \to S^n$ that sends both the northern and southern hemispheres of $S^n$ to the southern hemisphere via $f$.
[This was Brouwer's original proof.]
:::

::: {.solution}
Regard $S^n$ as the double of $D^n$, with northern and southern hemispheres each identified with $D^n$ and glued along their common boundary. Given
\[
f:D^n\to D^n,
\]
define
\[
F:S^n\to S^n
\]
by applying $f$ on either hemisphere and regarding the image as lying in the southern hemisphere.

<1>1. The map $F$ has degree zero.
::: {.proof}
Its image is contained in the closed southern hemisphere, hence misses every point in the interior of the northern hemisphere. Therefore $F$ factors through a contractible subspace of $S^n$, so $F$ is nullhomotopic. Thus
\[
\deg F=0.
\]
:::

<1>2. If $f$ had no fixed point, then $F$ would have no fixed point on $S^n$.
::: {.proof}
On the southern hemisphere this is exactly the assertion that $f(x)\ne x$. On the northern hemisphere the image under $F$ lies in the southern hemisphere, so a fixed point could occur only on the equator; there it would again give a boundary point $x\in D^n$ with $f(x)=x$.
:::

<1>3. Any fixed-point-free map $G:S^n\to S^n$ is homotopic to the antipodal map.
::: {.proof}
For $x\in S^n$, the vectors $G(x)$ and $x$ are never equal. Hence
\[
H_t(x)=\frac{(1-t)G(x)-t x}{\|(1-t)G(x)-t x\|}
\]
is defined for all $t\in[0,1]$: the numerator could vanish only if $G(x)$ were a positive scalar multiple of $x$, which for unit vectors would force $G(x)=x$. At $t=0$ this is $G$, and at $t=1$ it is the antipodal map $x\mapsto -x$.
:::

<1>4. Therefore $f$ must have a fixed point.
::: {.proof}
If $f$ had no fixed point, then by <1>2--<1>3
\[
\deg F=\deg(-\operatorname{id}_{S^n})=(-1)^{n+1},
\]
which is $\pm1$. This contradicts <1>1, where $\deg F=0$. Hence every continuous map
\[
f:D^n\to D^n
\]
has a fixed point.
:::
:::
