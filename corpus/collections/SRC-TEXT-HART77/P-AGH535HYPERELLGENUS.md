---
schema: qual/card@1
id: P-AGH535HYPERELLGENUS
kind: problem
title: Resolving the point at infinity of a hyperelliptic plane model
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowups
  - Birational Geometry
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.3.5, the retained Egbert companion calculation, the
    preceding multiplicity/blowup formulas, and the corpus plane-singularity
    genus formula. The printed model needs characteristic different from 2:
    in characteristic 2, y^2=f(x) defines a purely inseparable degree-two
    function-field extension and does not give the asserted hyperelliptic
    curves. In the intended characteristic, one blowup at infinity changes
    the local equation to v^(r-2)=u^2 times a unit, analytically an A_{r-3}
    singularity, which determines delta and the normalization genus.
- event: source-corrected
  by: chatgpt
  date: 2026-09-19
  note: Added the necessary hypothesis characteristic k != 2 to the displayed hyperelliptic model.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
---

::: {.problem}
Assume $\operatorname{char}k\ne2$. Let $a_1, \ldots, a_r$, $r \geqslant 5$, be distinct elements of $k$, and let $C$ be the curve in $\PP^2$ given by the (affine) equation $y^2=\prod_{i=1}^r\left(x-a_i\right)$.
Show that the point $P$ at infinity on the $y$-axis is a singular point.
Compute $\delta_P$ and $g(\tilde{Y})$, where $\tilde{Y}$ is the normalization of $Y$.
Show in this way that one obtains hyperelliptic curves of every genus $g \geqslant 2$.
:::

::: {.remark title="Erratum"}
The characteristic hypothesis is necessary for this model. In characteristic
$2$, the extension defined by
$$
y^2=\prod_i(x-a_i)
$$
is purely inseparable over $k(x)$, so it is not the separable degree-two
hyperelliptic cover used in the conclusion. The proof below treats the
intended case $\operatorname{char}k\ne2$.
:::

::: {.solution}
Put
$$
f(x)=\prod_{i=1}^r(x-a_i).
$$
The projective closure $Y\subseteq\PP^2$ has homogeneous equation
$$
F(x,y,z)
=
y^2z^{r-2}
-
\prod_{i=1}^r(x-a_i z)
=0.
$$

<1>1. The only point of $Y$ on the line at infinity $z=0$ is
$$
P=[0:1:0].
$$

::: {.proof}
Setting $z=0$ in the homogeneous equation gives
$$
-x^r=0.
$$
Thus $x=0$, and the unique projective point with $z=x=0$ is
$$
[0:1:0].
$$
:::

<1>2. The point $P$ is singular on $Y$.

::: {.proof}
Since $r\ge5$, each first partial derivative of
$$
F=y^2z^{r-2}-\prod_i(x-a_i z)
$$
vanishes at $[0:1:0]$.

Indeed,
$$
F_y=2yz^{r-2},
$$
which vanishes at $P$, while every monomial of $F_x$ has total degree
$r-1$ in $x,z$ and hence vanishes at $x=z=0$. Likewise the term
$$
(r-2)y^2z^{r-3}
$$
in $F_z$ vanishes because $r-3\ge2$, and all remaining terms again contain
a positive power of $x$ or $z$. Thus the Jacobian criterion makes $P$
singular.
:::

<1>3. The affine part of $Y$ is nonsingular.

::: {.proof}
On $z=1$ the equation is
$$
y^2-f(x)=0.
$$
A singular affine point would satisfy
$$
2y=0,
\qquad
f'(x)=0,
\qquad
y^2=f(x).
$$
Since $\operatorname{char}k\ne2$, the first equation gives $y=0$, so
$f(x)=0$. The roots $a_i$ are distinct, hence $f$ is squarefree and
$$
f'(a_i)\ne0.
$$
This is impossible. Therefore $P$ is the only singular point of the
projective plane curve.
:::

<1>4. In the affine chart $y=1$ at $P$, the local equation has multiplicity
$$
\boxed{r-2}.
$$

::: {.proof}
With local coordinates $(x,z)$ at $P$, the equation becomes
$$
z^{r-2}
-
\prod_{i=1}^r(x-a_i z)
=0.
$$
The second term is homogeneous of total degree $r$, whereas the first has
degree $r-2$. Hence the lowest nonzero homogeneous term is $z^{r-2}$, so
the multiplicity at the origin is $r-2$.
:::

<1>5. Blow up $P$ and use the chart
$$
x=u,
\qquad
z=uv.
$$
The strict transform has local equation
$$
v^{r-2}=u^2\prod_{i=1}^r(1-a_i v).
$$

::: {.proof}
Substitution in the equation of step <1>4 gives
$$
u^{r-2}v^{r-2}
-
u^r\prod_i(1-a_i v)
=0.
$$
Removing the exceptional factor $u^{r-2}$ gives the strict-transform
equation
$$
v^{r-2}
-
u^2\prod_i(1-a_i v)
=0.
$$
It meets the exceptional divisor $u=0$ only at $v=0$, corresponding to the
unique tangent direction $z=0$ at $P$.
:::

<1>6. The unique infinitely near singularity after the first blowup is
analytically of type
$$
U^2=v^{r-2},
$$
and has delta invariant
$$
\boxed{\left\lfloor\frac{r-2}{2}\right\rfloor}.
$$

::: {.proof}
The factor
$$
h(v)=\prod_i(1-a_i v)
$$
is a unit in $k[[v]]$ with $h(0)=1$. Since $2$ is invertible in $k$, this
unit has a square root in $k[[v]]$. Replacing
$$
U=u\sqrt{h(v)}
$$
turns the completed local equation of step <1>5 into
$$
U^2=v^{r-2}.
$$
This is the $A_{r-3}$ plane-curve singularity. The standard formula on
[[D-CRVPLSING]] gives
$$
\delta(A_n)=\left\lfloor\frac{n+1}{2}\right\rfloor,
$$
so here
$$
\delta=\left\lfloor\frac{r-2}{2}\right\rfloor.
$$
:::

<1>7. The delta invariant of the original point at infinity is
$$
\boxed{
\delta_P
=
\binom{r-2}{2}
+
\left\lfloor\frac{r-2}{2}\right\rfloor.}
$$

::: {.proof}
For a plane curve singularity, the genus-drop formula under successive
point blowups is
$$
\delta_P
=
\sum_Q\binom{m_Q}{2},
$$
where $Q$ runs through the singular point and its infinitely near singular
points with multiplicities $m_Q$ [[D-CRVPLSING]].

The first point has multiplicity $r-2$ by step <1>4. After that first
blowup, the residual singularity is the $A_{r-3}$ singularity of step <1>6,
whose complete remaining contribution to delta is
$\lfloor(r-2)/2\rfloor$. Hence the displayed formula.
:::

<1>8. Equivalently,
$$
\delta_P
=
\begin{cases}
\dfrac{(r-2)^2}{2},&r\text{ even},\\[6pt]
\dfrac{(r-1)(r-3)}{2},&r\text{ odd}.
\end{cases}
$$

::: {.proof}
If $r=2m$, then $r-2=2m-2$ is even and step <1>7 gives
$$
\binom{2m-2}{2}+m-1
=
2(m-1)^2
=
\frac{(r-2)^2}{2}.
$$
If $r=2m+1$, then $r-2=2m-1$ is odd and step <1>7 gives
$$
\binom{2m-1}{2}+m-1
=
2m(m-1)
=
\frac{(r-1)(r-3)}2.
$$
:::

<1>9. The normalization $\widetilde Y$ has genus
$$
\boxed{
g(\widetilde Y)
=
\left\lfloor\frac{r-1}{2}\right\rfloor.}
$$

::: {.proof}
The plane curve $Y$ has degree $r$, hence arithmetic genus
$$
p_a(Y)=\frac{(r-1)(r-2)}2.
$$
By step <1>3, $P$ is its only singular point. Therefore
$$
g(\widetilde Y)
=
p_a(Y)-\delta_P.
$$
Using step <1>8 gives
$$
g(\widetilde Y)
=
\begin{cases}
(r-2)/2,&r\text{ even},\\[4pt]
(r-1)/2,&r\text{ odd},
\end{cases}
$$
which is exactly $\lfloor(r-1)/2\rfloor$.
:::

<1>10. The rational function $x$ defines a finite morphism
$$
\widetilde Y\longrightarrow\PP^1
$$
of degree $2$.

::: {.proof}
The function field of $Y$, and hence of its normalization, is
$$
k(\widetilde Y)=k(x,y),
\qquad
y^2=f(x).
$$
Because $f$ is squarefree, it is not a square in $k(x)$. Since
$\operatorname{char}k\ne2$, the polynomial
$$
T^2-f(x)
$$
is separable and irreducible over $k(x)$. Thus
$$
[k(\widetilde Y):k(x)]=2.
$$
The corresponding nonconstant morphism to the nonsingular projective curve
$\PP^1$ is finite and has degree $2$.
:::

<1>11. Hyperelliptic curves occur in every genus $g\ge2$.

::: {.proof}
Given $g\ge2$, choose either
$$
r=2g+1
\qquad\text{or}\qquad
r=2g+2
$$
distinct scalars $a_i\in k$. Step <1>9 gives
$$
g(\widetilde Y)=g,
$$
and step <1>10 gives a degree-two morphism
$$
\widetilde Y\to\PP^1.
$$
Thus $\widetilde Y$ is a hyperelliptic curve of genus $g$.
:::

<1>12. Q.E.D.

::: {.proof}
Steps <1>1--<1>8 resolve the unique point at infinity and compute its delta
invariant, step <1>9 computes the genus of the normalization, and steps
<1>10--<1>11 give hyperelliptic curves of every genus at least two.
:::
:::
