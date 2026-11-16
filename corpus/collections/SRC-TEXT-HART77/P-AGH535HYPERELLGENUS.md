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
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The statement named the curve C and its normalization the normalization of Y. The curve is now named Y throughout.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.3,
    exercise 3.5, printed page 394. Rechecked the arithmetic: delta_P =
    C(r-2,2) + floor((r-2)/2) and g = p_a(Y) - delta_P = floor((r-1)/2), against
    r = 5, 6, 7 giving delta 4, 8, 12 and genus 2, 2, 3. Checked that the
    hypothesis char k != 2 is needed exactly where the card says: in
    characteristic 2 the equation y^2 = f(x) with f squarefree has
    k(Y) = k(x)^{1/2}, so the normalization is P^1 and no degree-two morphism
    exists, while the singularity at infinity and the multiplicities do not use
    the hypothesis. Searched outside the twelve retained sets: Algebraic
    Geometry II, National Taiwan University, 2020 Spring, Chapter V homework,
    Exercise 5 of section 3, PDF p. 11 (tmp/sources/ntu-ag2-chapter5.pdf),
    states characteristic different from 2 and obtains the same delta and genus;
    Yang Pi-Yeh, Hartshorne Solutions, exercise 5.3.5, printed p. 108
    (tmp/sources/lfwin-hartshorne-solutions.pdf), takes
    delta = (r-2)(r-3)/2, dropping the residual term. Not checked: whether the
    printed exercise intends the affine model over a field of characteristic 2
    at all; the card keeps the printed statement and states where the
    hypothesis enters.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    delta_P transcribed for issue #121 from the published solution: Algebraic
    Geometry II, National Taiwan University, 2020 Spring, Chapter V homework,
    Exercise 5 of section 3 (Shuang-Yen Lee), PDF p. 11 of
    tmp/sources/ntu-ag2-chapter5.pdf, read in the extraction
    tmp/sources/ntu-ag2-chapter5.md. That entry states char k != 2, takes the
    chart y != 0, finds multiplicity r-2 at P, one blowup giving
    w^{r-2} = prod(1-a_i w) x^2, then the chain w^e = prod(1-a_i w) x^2 with
    e = r mod 2, and writes delta_P = (r-2)(r-3)/2 + (1/2)(2)(1)floor((r-2)/2).
    Steps infinitely-near-A-singularity and delta-invariant-formula now carry
    that count, with the tangent-cone check at the double point and the two
    terminal exponents (e = 0: x^2 = unit, no point; e = 1: w = x^2 unit,
    nonsingular) written out, since the source says only that there are no
    singularities in either case. Checked against Hartshorne V.3.5, printed
    p. 394, and against (3.9.3) for the sum: the number of double points is
    floor((r-2)/2) and the arithmetic gives delta_P = 4, 8, 12 and g = 2, 2, 3
    at r = 5, 6, 7, and g = floor((r-1)/2) in general. The card's independent
    route through the A_{r-3} type of the residual germ agrees. The source's
    parenthetical "(which is impossible (when char(k) = 2))" is garbled: what
    it means is that the system has no solution when char k != 2, and the
    hypothesis char k != 2 is stated at the head of the entry. Also read:
    Yang Pi-Yeh, exercise 5.3.5, printed p. 108, whose delta is
    (r-2)(r-3)/2 and omits the residual term (3 against 4 at r = 5); Andrew
    Egbert, Exercise V.3.5, PDF p. 278, who computes the multiplicity and the
    genus by Riemann-Hurwitz but never computes delta_P.
---

::: {.problem}
Let $a_1, \ldots, a_r$, $r \geqslant 5$, be distinct elements of $k$, and let $Y$ be the curve in $\PP^2$ given by the (affine) equation $y^2=\prod_{i=1}^r\left(x-a_i\right)$.
Show that the point $P$ at infinity on the $y$-axis is a singular point.
Compute $\delta_P$ and $g(\tilde{Y})$, where $\tilde{Y}$ is the normalization of $Y$.
Show in this way that one obtains hyperelliptic curves of every genus $g \geqslant 2$.
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

The exercise is printed with no hypothesis on $\operatorname{char}k$, and its last two requests need $\operatorname{char}k\ne2$, which enters twice below: step [](#affine-part-nonsingular){.pf-ref} divides by $2$ to get $y=0$, and step [](#infinitely-near-A-singularity){.pf-ref} takes a square root in $k[[v]]$ of the unit $\prod_i(1-a_iv)$. In characteristic $2$ the equation $y^2=f(x)$ with $f$ squarefree defines a purely inseparable double cover, so $k(Y)=k(x)(\sqrt f)=k(x)^{1/2}$, the normalization is $\PP^1$ with $g=0$ for every $r$, and there is no degree-two morphism at all; the construction then gives no hyperelliptic curve. Those two steps carry the hypothesis; the singular point at infinity and step [](#point-at-infinity-singular){.pf-ref} do not need it.

::: pf

::: {.pf-step #unique-point-at-infinity}
The only point of $Y$ on the line at infinity $z=0$ is
$$
P=[0:1:0].
$$

::: pf-proof
Setting $z=0$ in the homogeneous equation gives
$$
-x^r=0.
$$
Thus $x=0$, and the unique projective point with $z=x=0$ is
$$
[0:1:0].
$$
:::

:::

::: {.pf-step #point-at-infinity-singular}
The point $P$ is singular on $Y$.

::: pf-proof
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

:::

::: {.pf-step #affine-part-nonsingular}
The affine part of $Y$ is nonsingular.

::: pf-proof
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

:::

::: {.pf-step #multiplicity-at-infinity}
In the affine chart $y=1$ at $P$, the local equation has multiplicity
$$
\boxed{r-2}.
$$

::: pf-proof
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

:::

::: {.pf-step #strict-transform-equation}
Blow up $P$ and use the chart
$$
x=u,
\qquad
z=uv.
$$
The strict transform has local equation
$$
v^{r-2}=u^2\prod_{i=1}^r(1-a_i v).
$$

::: pf-proof
Substitution in the equation of step [](#multiplicity-at-infinity){.pf-ref} gives
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

:::

::: {.pf-step #infinitely-near-A-singularity}
The strict transform of step [](#strict-transform-equation){.pf-ref} has a unique
singular point, a double point at the origin whose tangent direction is the
exceptional curve, and its germ there is analytically
$$
U^2=v^{r-2},
$$
that is, the $A_{r-3}$ singularity.

::: pf-proof
Put $m=r-2$ and $h(v)=\prod_i(1-a_i v)$. By step [](#strict-transform-equation){.pf-ref} the
strict transform is $v^{m}=u^2h(v)$, and $h(0)=1$, so $h$ is a unit in
$k[[v]]$. Since $2$ is invertible in $k$, that unit has a square root, and the
change of coordinate $U=u\sqrt{h(v)}$ turns the completed local equation into
$U^2=v^{m}=v^{r-2}$; this is the plane curve singularity $A_{r-3}$.

The lowest-degree term of $v^{m}-u^2h(v)$ is $-u^2$ when $m>2$ and $v^2-u^2$
times a unit when $m=2$, so the origin is a double point and its tangent cone is
$u^2=0$ when $m>2$, a single direction along the exceptional curve. The
published solution records the same germ as $w^{r-2}=\prod_i(1-a_iw)x^2$ with
multiplicity two, PDF p. 11.
:::

:::

::: {.pf-step #delta-invariant-formula}
The delta invariant of the original point at infinity is
$$
\boxed{
\delta_P
=
\binom{r-2}{2}
+
\left\lfloor\frac{r-2}{2}\right\rfloor.}
$$

::: pf-proof
By (3.9.3), applied to the normalization of the germ at $P$,
$$
\delta_P=\sum_Q\frac{m_Q(m_Q-1)}2,
$$
the sum over the singular points of $C$ infinitely near $P$, including $P$
[[D-CRVPLSING]]. The published solution counts those points, PDF p. 11: $P$ has
multiplicity $m_0=r-2$, and after it the germ has the form
$$
w^{m}=x^2\prod_i(1-a_iw),\qquad m=r-2,
$$
at a double point, whence one further blowup replaces $m$ by $m-2$ and the same
form by step [](#infinitely-near-A-singularity){.pf-ref}; the exponents met are
$m_0-2, m_0-4, \ldots$ down to $e=r\bmod 2$, and each is a double point because
it exceeds $1$. Their number is
$$
\left\lfloor\frac{m_0}{2}\right\rfloor=\left\lfloor\frac{r-2}{2}\right\rfloor,
$$
and at $e=r\bmod2$ the germ is $x^2=\text{unit}$ for $e=0$, which meets no
point, or $w=x^2\cdot\text{unit}$ for $e=1$, which is nonsingular; so the list is
complete. Hence
$$
\delta_P=\frac{(r-2)(r-3)}2+\frac{2\cdot1}{2}\left\lfloor\frac{r-2}{2}\right\rfloor,
$$
which is the source's formula. The identification of the residual germ with
$A_{r-3}$ gives the same number, $\lfloor(r-2)/2\rfloor$, by the standard formula
$\delta(A_n)=\lfloor(n+1)/2\rfloor$ [[D-CRVPLSING]].
:::

:::

::: {.pf-step #delta-invariant-piecewise}
Equivalently,
$$
\delta_P
=
\begin{cases}
\dfrac{(r-2)^2}{2},&r\text{ even},\\[6pt]
\dfrac{(r-1)(r-3)}{2},&r\text{ odd}.
\end{cases}
$$

::: pf-proof
If $r=2m$, then $r-2=2m-2$ is even and step [](#delta-invariant-formula){.pf-ref} gives
$$
\binom{2m-2}{2}+m-1
=
2(m-1)^2
=
\frac{(r-2)^2}{2}.
$$
If $r=2m+1$, then $r-2=2m-1$ is odd and step [](#delta-invariant-formula){.pf-ref} gives
$$
\binom{2m-1}{2}+m-1
=
2m(m-1)
=
\frac{(r-1)(r-3)}2.
$$
:::

:::

::: {.pf-step #normalization-genus}
The normalization $\widetilde Y$ has genus
$$
\boxed{
g(\widetilde Y)
=
\left\lfloor\frac{r-1}{2}\right\rfloor.}
$$

::: pf-proof
The plane curve $Y$ has degree $r$, hence arithmetic genus
$$
p_a(Y)=\frac{(r-1)(r-2)}2.
$$
By step [](#affine-part-nonsingular){.pf-ref}, $P$ is its only singular point. Therefore
$$
g(\widetilde Y)
=
p_a(Y)-\delta_P.
$$
Using step [](#delta-invariant-piecewise){.pf-ref} gives
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

:::

::: {.pf-step #degree-two-map-to-p1}
The rational function $x$ defines a finite morphism
$$
\widetilde Y\longrightarrow\PP^1
$$
of degree $2$.

::: pf-proof
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

:::

::: {.pf-step #hyperelliptic-every-genus}
Hyperelliptic curves occur in every genus $g\ge2$.

::: pf-proof
Given $g\ge2$, choose either
$$
r=2g+1
\qquad\text{or}\qquad
r=2g+2
$$
distinct scalars $a_i\in k$. Step [](#normalization-genus){.pf-ref} gives
$$
g(\widetilde Y)=g,
$$
and step [](#degree-two-map-to-p1){.pf-ref} gives a degree-two morphism
$$
\widetilde Y\to\PP^1.
$$
Thus $\widetilde Y$ is a hyperelliptic curve of genus $g$.
:::

:::

::: pf-qed
Steps [](#unique-point-at-infinity){.pf-ref}, [](#point-at-infinity-singular){.pf-ref}, [](#affine-part-nonsingular){.pf-ref}, [](#multiplicity-at-infinity){.pf-ref}, [](#strict-transform-equation){.pf-ref}, [](#infinitely-near-A-singularity){.pf-ref}, [](#delta-invariant-formula){.pf-ref} and [](#delta-invariant-piecewise){.pf-ref} resolve the unique point at infinity and compute its delta
invariant, step [](#normalization-genus){.pf-ref} computes the genus of the normalization, and steps
[](#degree-two-map-to-p1){.pf-ref} and [](#hyperelliptic-every-genus){.pf-ref} give hyperelliptic curves of every genus at least two.
:::

:::
:::

::: {.remark title="Published solution"}
Algebraic Geometry II, National Taiwan University, 2020 Spring (course of Chin-Lung Wang), *Chapter V Surfaces* homework solutions, Exercise 5 of §3 (solution by Shuang-Yen Lee), PDF p. 11, works in $\operatorname{char}k\ne2$, which it states, and computes at infinity: the projective model is $z^{r-2}y^2=\prod_i(x-a_iz)$, the multiplicity at $P$ is $r-2$, the first blowup gives $w^{r-2}=\prod_i(1-a_iw)x^2$, and the remaining singularities are $\lfloor(r-2)/2\rfloor$ double points; hence
$$\delta_P=\frac12(r-2)(r-3)+\frac12\cdot2\cdot1\cdot\left\lfloor\frac{r-2}{2}\right\rfloor,$$
the same formula as steps [](#delta-invariant-formula){.pf-ref} and [](#delta-invariant-piecewise){.pf-ref}, and then $p_a(\widetilde Y)=\frac12(r-1)(r-2)-\delta_P=\lfloor(r-1)/2\rfloor$, which is step [](#normalization-genus){.pf-ref}.

Yang Pi-Yeh, *Hartshorne Solutions*, text version `tmp/sources/lfwin-hartshorne-solutions.md`, exercise 5.3.5, printed p. 108, computes $\delta_\infty=\frac12r_\infty(r_\infty-1)=\frac12(r-2)(r-3)$ from the multiplicity $r_\infty=r-2$ alone, which omits the $\lfloor(r-2)/2\rfloor$ from the residual singularity after the first blowup: for $r=5$ it gives $3$ where $\delta_P=4$. Its genus is computed separately by Hurwitz and agrees with step [](#normalization-genus){.pf-ref}, but the two do not then satisfy $p_a(Y)=\delta_P+g$ for $p_a(Y)=\frac12(r-1)(r-2)$.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), text version `tmp/sources/hartshorne-solutions-egbert.md`, Exercise V.3.5, PDF p. 278: he computes the projective closure $z^{r-2}y^2=\prod(x-a_iz)$, checks the Jacobian at $\infty=(0:1:0)$ and finds it zero, notes that after setting $y=1$ the lowest order term is $z^{r-2}$ so the point has multiplicity $r-2$, and then argues that projecting to the $x$-coordinate gives a degree-two cover of $\PP^1$ whose Riemann--Hurwitz count has $2g+2$ branch points, so $n=2g+2$ realizes every genus. He never computes $\delta_P$, which the exercise asks for; steps [](#multiplicity-at-infinity){.pf-ref} to [](#delta-invariant-piecewise){.pf-ref} supply it as $\binom{r-2}{2}+\lfloor(r-2)/2\rfloor$, from the strict transform $v^{r-2}=u^2\prod_i(1-a_iv)$ and the $A_{r-3}$ singularity that its unit factor reduces to. His genus count is step [](#normalization-genus){.pf-ref} by a different route, $p_a(Y)-\delta_P$. Recorded in COMPLAINTS for $\delta_P$.
:::
