---
schema: qual/card@1
id: P-AGH462RATIONALQUINTICONCUBIC
kind: problem
title: A rational quintic in $\PP^3$ lies on a cubic surface but need not lie on a quadric
classification:
  areas:
  - algebraic-geometry
  topics:
  - Embeddings
  - Genus
  - Linear Systems
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.6.2 and independently checked the retained Lomont and
    Egbert companion solutions. The homogeneous parametrization is
    [s^5:s^4t:st^4+alpha s^2t^3:t^5] with alpha nonzero; the Egbert PDF's
    extracted text garbles the fourth-degree factors. The proof below checks
    point and tangent separation and all ten possible quadratic relations
    explicitly rather than inheriting the companions' omitted checks.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
A rational curve of degree 5 in $\PP^3$ is always contained in a cubic surface, but there are such curves which are not contained in any quadric surface.
:::

::: {.solution}
<1>1. Every rational quintic $X\subseteq\PP^3$ is contained in a cubic
surface.

::: {.proof}
Since $X\cong\PP^1$ and $\deg\OO_X(1)=5$,
$$
\deg\OO_X(3)=15,
\qquad
h^0(X,\OO_X(3))=16.
$$
Twisting the ideal sequence by $\OO_{\PP^3}(3)$ gives
$$
0\longrightarrow\mathcal I_X(3)
\longrightarrow\OO_{\PP^3}(3)
\longrightarrow\OO_X(3)
\longrightarrow0.
$$
Now
$$
h^0(\PP^3,\OO_{\PP^3}(3))=\binom63=20.
$$
Therefore the restriction map from this $20$-dimensional space to the
$16$-dimensional space $H^0(X,\OO_X(3))$ has nonzero kernel; indeed
$$
h^0(\PP^3,\mathcal I_X(3))\ge4.
$$
Any nonzero element of this kernel is a cubic equation vanishing on $X$.
:::

<1>2. Fix $\alpha\in k^*$ and define
$$
\phi:\PP^1\longrightarrow\PP^3,
\qquad
[s:t]\longmapsto
[f_0:f_1:f_2:f_3],
$$
where
$$
f_0=s^5,\qquad
f_1=s^4t,\qquad
f_2=st^4+\alpha s^2t^3,\qquad
f_3=t^5.
$$
Then $\phi$ is a closed embedding and its image has degree $5$.

::: {.proof}
The four sections have no common zero, so they define a morphism and
$$
\phi^*\OO_{\PP^3}(1)\cong\OO_{\PP^1}(5).
$$

They separate points.  On $s\ne0$ the ratio
$$
\frac{f_1}{f_0}=\frac ts
$$
recovers the affine coordinate, while the only point with $s=0$ maps to
$[0:0:0:1]$ and cannot coincide with the image of a point having $s\ne0$.

They also separate tangent vectors.  On $s\ne0$, the same ratio $f_1/f_0$
is a local parameter.  At the remaining point $[0:1]$, write $u=s/t$.
On the chart $f_3\ne0$ one has
$$
\frac{f_2}{f_3}=u+\alpha u^2,
$$
whose differential at $u=0$ is $du\ne0$.  Hence the linear subsystem
separates points and tangent vectors, so it gives a closed embedding.

For an embedding of a projective curve, the degree is the degree of the
pulled-back hyperplane bundle.  Therefore
$$
\deg\phi(\PP^1)=\deg\OO_{\PP^1}(5)=5.
$$
:::

<1>3. The curve $C=\phi(\PP^1)$ is contained in no quadric surface.

::: {.proof}
A quadric containing $C$ would give a nonzero relation among the ten products
$f_if_j$ with $0\le i\le j\le3$.  Suppose
$$
\begin{aligned}
0={}&A f_0^2+B f_0f_1+C f_0f_2+D f_0f_3+E f_1^2\\
&+F f_1f_2+G f_1f_3+H f_2^2+I f_2f_3+J f_3^2.
\end{aligned}
$$
Compare coefficients as homogeneous polynomials of degree $10$ in $s,t$.
The coefficients of
$$
s^{10},\qquad s^9t,\qquad s^8t^2
$$
give respectively
$$
A=B=E=0.
$$
The monomial $s^7t^3$ occurs, among the remaining terms, only in
$C f_0f_2$, with coefficient $C\alpha$; hence $C=0$.  Then the coefficient
of $s^6t^4$ is $F\alpha$, so $F=0$, and the coefficient of $s^5t^5$ gives
$D=0$.

At the other end, the coefficient of $st^9$ gives $I=0$.  The coefficient
of $s^2t^8$ then gives $H=0$, the coefficient of $s^4t^6$ gives $G=0$, and
finally the coefficient of $t^{10}$ gives $J=0$.  Thus every coefficient is
zero, so the ten products are linearly independent and no nonzero quadratic
equation vanishes on $C$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 proves that every rational quintic lies on a cubic surface.
Steps <1>2--<1>3 exhibit a nonsingular rational quintic lying on no quadric.
:::
:::
