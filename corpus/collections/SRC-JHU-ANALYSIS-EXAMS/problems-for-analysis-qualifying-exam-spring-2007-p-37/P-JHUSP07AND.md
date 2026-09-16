---
schema: qual/card@1
id: P-JHUSP07AND
kind: problem
title: A surjective holomorphic map from the disk onto $\mathbb C$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Rational Functions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the existence question with Spring 2007 problem 4 in the retained source. The negative assertion was in the card title, not the question; corrected it and removed the trailing fragment."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Verified an explicit rational map is holomorphic on the disk and onto the whole plane by the quadratic root sum, without assuming an inverse for a merely surjective map."
---

::: {.problem}
4) Does there exist a surjective holomorphic map $f : D \to \mathbb { C }$ from the unit disc to the whole complex plane? Prove that your answer is correct.
:::

::: solution
Yes. One example is
$$
\boxed{f(z)=\frac{2z(1+z)}{(1-z)^2},\qquad |z|<1.}
$$

<1>1. The disk is biholomorphic to the right half-plane.

::: proof
The map $T(z)=(1+z)/(1-z)$ is holomorphic on the unit
disk and satisfies
$$
\operatorname{Re}T(z)=\frac{1-|z|^2}{|1-z|^2}>0.
$$
For any $t$ with $\operatorname{Re}t>0$, its inverse
$z=(t-1)/(t+1)$ is well defined and satisfies
$$
1-|z|^2=\frac{4\operatorname{Re}t}{|t+1|^2}>0.
$$
Direct substitution verifies the inverse identities.
Thus $T$ maps the disk onto $H=\{t:\operatorname{Re}t>0\}$.
:::

<1>2. The polynomial $p(t)=t^2-t$ maps $H$ onto $\mathbb C$.

::: proof
Given any $w\in\mathbb C$, the equation
$t^2-t-w=0$ has two complex roots $t_1,t_2$, counted
with multiplicity, and $t_1+t_2=1$ by the quadratic
formula. Their real parts sum to one, so at least one
has real part at least $1/2$. That root belongs to $H$
and satisfies $p(t)=w$. Since $w$ was arbitrary, $p(H)=\mathbb C$.
:::

<1>3. Composition gives the required surjection.

::: proof
The composite $p\circ T$ is holomorphic on the disk
and surjective by the preceding two steps. Its formula is
$$
T(z)^2-T(z)
=\frac{(1+z)^2-(1+z)(1-z)}{(1-z)^2}
=\frac{2z(1+z)}{(1-z)^2}.
$$
The denominator vanishes only at the boundary point one,
not in the domain. This proves the assertion for the
displayed function.

There is no conflict with the impossibility of a
biholomorphism from the disk onto the plane: its inverse
would be bounded and entire, hence constant by Liouville's
theorem [@SS03]. The map constructed here is not injective.
Indeed, $t=(1\pm i\sqrt3)/2$ are two
distinct points of $H$ with $p(t)=-1$, and their distinct
inverse images under $T$ have the same value under $f$.
:::
:::
