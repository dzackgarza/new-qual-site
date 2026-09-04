---
schema: qual/card@1
id: P-FD3FN
kind: problem
title: Every continuous map $S^2\to S^2$ has a point with $f(x)=\pm x$, but maps $S^3\to
  S^3$ need not
classification:
  areas:
  - topology
  topics:
  - Degree
  - Fixed Points
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Checked both normalized straight-line homotopies and the complex-linear S3 example.
---

::: problem
Prove that for every continuous map $f : S^2 \to S^2$ there is some $x$ such that either $f (x) = x$ or $f (x) = -x$.

> Hint: Where $A : S^2 \to S^2$ is the antipodal map, you are being asked to prove that either $f$ or $A \circ f$ has a fixed point.

Exhibit a continuous map $f : S^3 \to S^3$ such that for every $x \in S^3$, $f (x)$ is equal to neither $x$ nor $-x$.

> Hint: It might help to first think about how you could do this for a map from $S^1$ to $S^1$.
:::

::: {.solution}
<1>1. Let \(f:S^n\to S^n\) be continuous.
If
\[
f(x)\ne -x
\qquad\text{for every }x\in S^n,
\]
then \(f\) is homotopic to the identity map of \(S^n\).
::: {.proof}
Define
\[
H_+(x,t)
=
\frac{(1-t)f(x)+tx}
{\left\|(1-t)f(x)+tx\right\|},
\qquad 0\le t\le1.
\]
It remains to check that the denominator never vanishes.
If
\[
(1-t)f(x)+tx=0,
\]
then \(t\ne0,1\), and
\[
(1-t)f(x)=-tx.
\]
Taking norms and using \(\|f(x)\|=\|x\|=1\) gives
\[
1-t=t,
\]
so \(t=1/2\). The displayed vector equation then gives
\[
f(x)=-x,
\]
contrary to the hypothesis.
Hence \(H_+\) is well-defined and continuous.
Moreover
\[
H_+(x,0)=f(x),
\qquad
H_+(x,1)=x.
\]
Thus \(f\simeq\operatorname{id}_{S^n}\).
:::

<1>2. If instead
\[
f(x)\ne x
\qquad\text{for every }x\in S^n,
\]
then \(f\) is homotopic to the antipodal map
\[
A(x)=-x.
\]
::: {.proof}
Define
\[
H_-(x,t)
=
\frac{(1-t)f(x)-tx}
{\left\|(1-t)f(x)-tx\right\|}.
\]
If its numerator vanished, then
\[
(1-t)f(x)=tx.
\]
Taking norms again forces \(t=1/2\), and then the vector equation gives \(f(x)=x\), contrary to the hypothesis.
Therefore \(H_-\) is a continuous homotopy, with
\[
H_-(x,0)=f(x),
\qquad
H_-(x,1)=-x=A(x).
\]
:::

<1>3. The antipodal map on \(S^2\) has degree
\[
\deg A=-1.
\]
::: {.proof}
More generally, the antipodal map on \(S^n\) is the restriction of the linear automorphism
\[
-I:\mathbb R^{n+1}\to\mathbb R^{n+1}.
\]
Its degree is the sign of
\[
\det(-I)=(-1)^{n+1}.
\]
Hence
\[
\deg(A:S^2\to S^2)=(-1)^3=-1.
\]
:::

<1>4. For every continuous map \(f:S^2\to S^2\), there exists \(x\in S^2\) such that
\[
f(x)=x
\qquad\text{or}\qquad
f(x)=-x.
\]
::: {.proof}
Suppose, toward a contradiction, that
\[
f(x)\ne x
\qquad\text{and}\qquad
f(x)\ne -x
\]
for every \(x\in S^2\). By <1>1,
\[
f\simeq\operatorname{id}_{S^2},
\]
so homotopy invariance of degree gives
\[
\deg f=1.
\]
By <1>2,
\[
f\simeq A,
\]
so <1>3 gives
\[
\deg f=-1.
\]
This is impossible.
Therefore at least one of the two equalities must hold at some point.
:::

<1>5. For part (ii), identify
\[
S^3
=
\left\{(z_1,z_2)\in\mathbb C^2:
|z_1|^2+|z_2|^2=1\right\}
\]
and define
\[
f:S^3\to S^3,
\qquad
f(z_1,z_2)=(iz_1,iz_2).
\]
::: {.proof}
Multiplication by \(i\) preserves complex absolute value, so
\[
|iz_1|^2+|iz_2|^2
=
|z_1|^2+|z_2|^2
=1.
\]
Thus the formula maps \(S^3\) to itself.
It is the restriction of a linear map on \(\mathbb R^4\), hence is continuous.
:::

<1>6. The map in <1>5 satisfies
\[
f(x)\ne x
\qquad\text{and}\qquad
f(x)\ne -x
\]
for every \(x\in S^3\).
::: {.proof}
If
\[
(iz_1,iz_2)=(z_1,z_2),
\]
then
\[
(i-1)z_1=(i-1)z_2=0.
\]
Since \(i-1\ne0\), this forces \(z_1=z_2=0\), which is not a point of \(S^3\). Likewise, if
\[
(iz_1,iz_2)=-(z_1,z_2),
\]
then
\[
(i+1)z_1=(i+1)z_2=0,
\]
and \(i+1\ne0\) again forces \(z_1=z_2=0\), impossible.
Therefore this \(f\) avoids both \(x\) and \(-x\) at every point.
:::
:::
