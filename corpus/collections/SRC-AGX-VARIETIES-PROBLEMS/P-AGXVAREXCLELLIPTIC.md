---
schema: qual/card@1
id: P-AGXVAREXCLELLIPTIC
kind: problem
title: The class group of $V(y^2-x(x^2-1))$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Class Groups
  - Weil Divisors
  - Elliptic Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Exercise 10.2 in the recorded source. Under the notes'
    standing algebraically-closed characteristic-zero convention, it asks for
    the affine elliptic cubic y^2=x(x^2-1) and states that every divisor is
    linearly equivalent to zero or to a point of the curve.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Made the source's standing base field and affine ambient space explicit
    on the standalone card.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked smoothness and the unique point at infinity of the projective
    closure, the divisor restriction quotient by that point, the degree
    splitting of Pic, and the genus-one identification with Pic^0. Cross-
    checked the latter against PR-CRVGRP and FE-DIVP1E.
---

::: {.problem}
Let $k$ be an algebraically closed field of characteristic zero, and let
$$
X=V\bigl(y^2-x(x^2-1)\bigr)\subseteq\AA^2_k.
$$
Compute the divisor class group $\Cl(X)$.
:::

::: {.solution}
Let $\overline X\subseteq\PP^2_k$ be the projective closure of $X$.

<1>1. The curve $\overline X$ is a smooth plane cubic of genus $1$, and
$$
\overline X\setminus X=\{O\},
\qquad
O=[0:1:0].
$$

::: {.proof}
In homogeneous coordinates $[X:Y:Z]$,
$$
\overline X
=
V(F),
\qquad
F=Y^2Z-X^3+XZ^2.
$$
On the line at infinity $Z=0$, the equation is $X^3=0$, so the only point at
infinity is
$$
O=[0:1:0].
$$
Moreover,
$$
F_Z=Y^2+2XZ,
$$
so
$$
F_Z(O)=1,
$$
and $O$ is smooth.

On the affine chart $Z=1$, a singular point would satisfy
$$
y^2-x^3+x=0,
\qquad
2y=0,
\qquad
1-3x^2=0.
$$
The second equation gives $y=0$, and the first then gives
$$
x\in\{0,1,-1\}.
$$
At these three values,
$$
1-3x^2\in\{1,-2\},
$$
so the third equation cannot hold. Thus $\overline X$ is smooth everywhere.

A smooth plane cubic has genus
$$
\frac{(3-1)(3-2)}2=1.
$$
Together with the chosen point $O$, this makes $\overline X$ an elliptic
curve.
:::

<1>2. Since $X$ is smooth,
$$
\Cl(X)=\Pic(X).
$$

::: {.proof}
Every local ring of a smooth curve is a discrete valuation ring. Hence every
Weil divisor on $X$ is locally principal, so every Weil divisor is Cartier.
Therefore the Weil divisor class group and the Picard group coincide.
:::

<1>3. Restriction of divisors induces an isomorphism
$$
\Pic(\overline X)\big/\ZZ[O]
\xrightarrow{\sim}
\Pic(X).
$$

::: {.proof}
Every divisor on $X$ is also a divisor on $\overline X$ whose support avoids
$O$, so restriction gives a surjection
$$
\Pic(\overline X)\longrightarrow\Pic(X).
$$

Suppose a divisor class $[D]\in\Pic(\overline X)$ restricts to zero in
$\Pic(X)$. Then for some
$$
g\in k(X)^\times=k(\overline X)^\times
$$
one has
$$
D|_X=\div_X(g).
$$
Consequently,
$$
D-\div_{\overline X}(g)
$$
is supported on the single missing point $O$, so it equals $mO$ for some
$m\in\ZZ$. Thus
$$
[D]\in\ZZ[O].
$$
Conversely, the divisor $O$ restricts to the zero divisor on $X$. Hence the
kernel is exactly $\ZZ[O]$, proving the quotient description.
:::

<1>4. There is a canonical isomorphism
$$
\Pic(\overline X)\big/\ZZ[O]
\xrightarrow{\sim}
\Pic^0(\overline X).
$$

::: {.proof}
The degree homomorphism
$$
\deg:\Pic(\overline X)\longrightarrow\ZZ
$$
has kernel $\Pic^0(\overline X)$, and the map
$$
n\longmapsto[nO]
$$
is a section because $\deg(nO)=n$. Therefore
$$
\Pic(\overline X)
\cong
\Pic^0(\overline X)\oplus\ZZ[O].
$$
Quotienting by the second summand gives the displayed isomorphism.
:::

<1>5. The Abel--Jacobi map
$$
\alpha:\overline X(k)\longrightarrow\Pic^0(\overline X),
\qquad
P\longmapsto[P-O],
$$
is an isomorphism of groups.

::: {.proof}
Let $D$ be a divisor of degree $0$ on $\overline X$. Since $\overline X$ has
genus $1$, Riemann--Roch applied to the degree-one divisor $D+O$ gives
$$
\ell(D+O)=1.
$$
Hence there is a unique effective divisor of degree $1$ in the class of
$D+O$. Such a divisor is a single point $P$, so
$$
D\sim P-O.
$$
This proves surjectivity of $\alpha$.

If
$$
P-O\sim Q-O,
$$
then $P$ and $Q$ are effective divisors in the same degree-one complete
linear system. The uniqueness just proved gives $P=Q$, so $\alpha$ is
injective.

Under the usual elliptic-curve group law with identity $O$, this bijection is
a group isomorphism ([[PR-CRVGRP|the elliptic-curve group law]]).
:::

<1>6. The divisor class group of the affine curve is
$$
\boxed{
\Cl(X)
\cong
\overline X(k),
}
$$
where $\overline X(k)$ carries its elliptic-curve group law with identity
$O=[0:1:0]$.

::: {.proof}
Combining steps <1>2--<1>5 gives
$$
\Cl(X)
\cong
\Pic(X)
\cong
\Pic(\overline X)/\ZZ[O]
\cong
\Pic^0(\overline X)
\cong
\overline X(k).
$$
:::

<1>7. Equivalently, every divisor on $X$ is linearly equivalent either to
$0$ or to a point $P\in X(k)$.

::: {.proof}
Under the isomorphism of step <1>6, the identity element $O\in\overline X(k)$
corresponds to the zero class because the divisor $O$ disappears on
$X=\overline X\setminus\{O\}$.

Every other point of $\overline X(k)$ lies in $X(k)$. For
$$
P\in X(k),
$$
the degree-zero class $[P-O]$ on $\overline X$ restricts to the divisor class
$[P]$ on $X$. Hence every nonzero class of $\Cl(X)$ is represented by a
point of $X$, exactly as stated in the source exercise.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>6 computes the group, and step <1>7 gives the source's equivalent
representative description.
:::
:::
