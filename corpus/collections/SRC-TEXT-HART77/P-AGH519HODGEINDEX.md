---
schema: qual/card@1
id: P-AGH519HODGEINDEX
kind: problem
title: Hodge index inequality and divisors of type $(a,b)$ on a product of curves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne V.1.9, the retained Egbert companion calculation, and the
    local Hodge-index and Nakai--Moishezon statements. Part (a) is the standard
    projection to the orthogonal complement of an ample class. For part (b),
    the proof below replaces the source hint's scaled auxiliary divisor by the
    simpler class F=D-bl-am, whose square is exactly D^2-2ab and whose
    intersections with both rulings vanish.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
a. If $H$ is an ample divisor on the surface $X$, and if $D$ is any divisor, show that
\[
\left(D^2\right)\left(H^2\right) \leqslant(D . H)^2 .
\]

b. Now let $X$ be a product of two curves $X=C \times C^{\prime}$.
Let $l=C \times \mathrm{pt}$, and $m=\mathrm{pt} \times C^{\prime}$.
For any divisor $D$ on $X$, let $a=D . l$, $b=D . m$.
Then we say $D$ has type $(a, b)$.
If $D$ has type $(a, b)$, with $a, b \in \ZZ$, show that
\[
D^2 \leqslant 2 a b ,
\]
and equality holds if and only if $D \equiv b l+a m$.

Hint: Show that $H=l+m$ is ample, let $E=l-m$, let $D^{\prime}=\left(H^2\right)\left(E^2\right) D-\left(E^2\right)(D \cdot H) H-\left(H^2\right)(D \cdot E) E$, and apply (1.9). This inequality is due to Castelnuovo and Severi.
See Grothendieck [2].
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $H$ is ample, then $H^2>0$.

::: pf-proof

This is one of the two numerical conditions in the Nakai--Moishezon criterion
[[T-SRFNAKAI]].

:::

:::

::: {.pf-step #s2}

For any divisor $D$ on $X$, define
$$
F=(H^2)D-(D\cdot H)H.
$$
Then $F\cdot H=0$ and $F^2\leq0$.

::: pf-proof

Bilinearity gives
$$
F\cdot H
=(H^2)(D\cdot H)-(D\cdot H)H^2
=0.
$$
If $F\not\equiv0$, the Hodge index theorem [[T-SRFHODGE]] gives $F^2<0$.
If $F\equiv0$, then $F^2=0$. Thus in all cases $F^2\leq0$.

:::

:::

::: {.pf-step #s3}

For every divisor $D$ and ample divisor $H$,
$$
\boxed{(D^2)(H^2)\leq(D\cdot H)^2}.
$$

::: pf-proof

Expanding the square in step [](#s2){.pf-ref} gives
$$
\begin{aligned}
F^2
&=(H^2)^2D^2
-2(H^2)(D\cdot H)^2
+(D\cdot H)^2H^2\\
&=H^2\qty((H^2)D^2-(D\cdot H)^2).
\end{aligned}
$$
By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, the left side is nonpositive and $H^2$ is positive.
Dividing by $H^2$ yields the stated inequality. This proves part (a).

:::

:::

::: {.pf-step #s4}

On $C\times C'$, the ruling classes satisfy
$$
l^2=m^2=0,
\qquad
l\cdot m=1,
$$
and
$$
H=l+m
$$
is ample.

::: pf-proof

Distinct fibres of either projection are disjoint and numerically equivalent,
so each fibre has self-intersection zero. A fibre of the first projection and
a fibre of the second meet transversally in one point, hence $l\cdot m=1$.
Thus
$$
H^2=(l+m)^2=2>0.
$$

Let $\Gamma\subseteq C\times C'$ be an irreducible curve. The two projections
cannot both be constant on $\Gamma$. Their degrees on the normalization of
$\Gamma$ are nonnegative, and at least one is positive. These degrees are
respectively the intersection numbers $m\cdot\Gamma$ and
$l\cdot\Gamma$. Therefore
$$
H\cdot\Gamma=l\cdot\Gamma+m\cdot\Gamma>0.
$$
The Nakai--Moishezon criterion [[T-SRFNAKAI]] now shows that $H$ is ample.

:::

:::

::: {.pf-step #s5}

If $D$ has type $(a,b)$, put
$$
F=D-bl-am.
$$
Then
$$
F\cdot l=F\cdot m=F\cdot H=0
$$
and
$$
F^2=D^2-2ab.
$$

::: pf-proof

By definition,
$$
D\cdot l=a,
\qquad
D\cdot m=b.
$$
Using step [](#s4){.pf-ref},
$$
\begin{aligned}
F\cdot l
&=a-b(l^2)-a(m\cdot l)=0,\\
F\cdot m
&=b-b(l\cdot m)-a(m^2)=0.
\end{aligned}
$$
Hence $F\cdot H=0$. Also
$$
\begin{aligned}
F^2
&=D^2-2D\cdot(bl+am)+(bl+am)^2\\
&=D^2-2(ba+ab)+2ab\\
&=D^2-2ab.
\end{aligned}
$$

:::

:::

::: {.pf-step #s6}

Every divisor $D$ of type $(a,b)$ satisfies
$$
\boxed{D^2\leq2ab}.
$$

::: pf-proof

By steps [](#s4){.pf-ref} and [](#s5){.pf-ref}, $H$ is ample and $F\cdot H=0$. The Hodge index theorem
therefore gives $F^2\leq0$. Step [](#s5){.pf-ref} identifies this inequality with
$$
D^2-2ab\leq0.
$$

:::

:::

::: {.pf-step #s7}

Equality holds precisely when
$$
\boxed{D\equiv bl+am}.
$$

::: pf-proof

If $D^2=2ab$, then step [](#s5){.pf-ref} gives $F^2=0$. Since $F\cdot H=0$ and $H$ is
ample, the strict form of the Hodge index theorem [[T-SRFHODGE]] forces
$F\equiv0$. Thus
$$
D\equiv bl+am.
$$

Conversely, if $D\equiv bl+am$, then numerical equivalence preserves
self-intersection and step [](#s4){.pf-ref} gives
$$
D^2=(bl+am)^2=2ab.
$$

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove part (a), and steps [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} prove part (b), including
the equality criterion.

:::

:::

:::
