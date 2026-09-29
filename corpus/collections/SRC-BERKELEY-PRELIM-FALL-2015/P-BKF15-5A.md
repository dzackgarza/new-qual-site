---
schema: qual/card@1
id: P-BKF15-5A
kind: problem
title: Gauss--Lucas theorem via $\sum 1/(z-c_i)=0$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2015 solution packet. Its
    half-plane sentence has the reciprocal terms in the wrong oriented
    half-plane, and its logarithmic-derivative argument requires a separate
    case for critical points that are repeated roots of p.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked strict separation from a convex hull, the sign of the reciprocal
    real parts after normalization, and both cases p(zeta)=0 and p(zeta) not
    equal to 0 in the Gauss--Lucas argument.
---

::: {.problem}
(a) Suppose $z , c _ { 1 } , \ldots , c _ { n }$ are distinct complex numbers, and

$$
{ \frac { 1 } { z - c _ { 1 } } } + \cdots + { \frac { 1 } { z - c _ { n } } } = 0 .
$$

Show that $z$ lies in the convex hull of $c_1,\ldots,c_n$.

(b) Let $p ( z )$ be a non-constant polynomial.
Show that every zero of $p'(z)$ lies in the convex hull of the zeroes of $p(z)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Suppose the point $z$ does not lie in the convex hull of
$$
c_1,\ldots,c_n.
$$
Then, after translating all points by $-z$ and multiplying by a
nonzero complex number, one may arrange that
$$
z=0
\qquad\text{and}\qquad
\Re(c_i)>0
$$
for every $i$.

::: pf-proof

The convex hull
$$
K=\operatorname{conv}\{c_1,\ldots,c_n\}
$$
is compact and convex. If $z\notin K$, strict separation in
$\RR^2\cong\CC$ gives a line separating $z$ from $K$. Translating by
$-z$ moves $z$ to $0$, and multiplying by a complex number of modulus
$1$ rotates the separating line to the imaginary axis, with the image
of $K$ in the open right half-plane.

:::

:::

::: {.pf-step #s2}

Under the normalization in step [](#s1){.pf-ref},
$$
\Re\!\left(\frac1{z-c_i}\right)<0
$$
for every $i$.

::: pf-proof

Now $z=0$, so
$$
\frac1{z-c_i}=-\frac1{c_i}.
$$
Since $\Re(c_i)>0$,
$$
\Re\!\left(\frac1{c_i}\right)
=
\frac{\Re(c_i)}{|c_i|^2}
>
0.
$$
Multiplying by $-1$ gives the claimed strict negativity.

:::

:::

::: {.pf-step #s3}

Part (a) holds:
$$
\boxed{
\sum_{i=1}^n\frac1{z-c_i}=0
\quad\Longrightarrow\quad
z\in\operatorname{conv}\{c_1,\ldots,c_n\}.
}
$$

::: pf-proof

Suppose instead that $z$ lay outside the convex hull. Apply the affine
normalization from step [](#s1){.pf-ref}. Translation and multiplication by a
nonzero complex scalar preserve the equation up to multiplication of
its left-hand side by a nonzero scalar, so it remains an equation with
sum $0$.

But by step [](#s2){.pf-ref} every summand has strictly negative real part.
Therefore their sum also has strictly negative real part and cannot be
$0$. This contradiction proves the claim.

:::

:::

::: {.pf-step #s4}

Let the zeros of the nonconstant polynomial $p$ be
$$
c_1,\ldots,c_n,
$$
listed with multiplicity. If $\zeta$ is a zero of $p'$ and
$p(\zeta)=0$, then $\zeta$ lies in the convex hull of the zeros of
$p$.

::: pf-proof

In this case $\zeta$ itself is one of the zeros $c_i$. Every point in
the defining set of a convex hull belongs to that convex hull.

:::

:::

::: {.pf-step #s5}

If $p'(\zeta)=0$ and $p(\zeta)\ne0$, then
$$
\sum_{i=1}^n\frac1{\zeta-c_i}=0.
$$

::: pf-proof

Write
$$
p(w)=a\prod_{i=1}^n(w-c_i),
\qquad
a\ne0.
$$
Since $p(\zeta)\ne0$, one has $\zeta\ne c_i$ for every $i$. The
logarithmic derivative identity is therefore valid at $\zeta$:
$$
\frac{p'(\zeta)}{p(\zeta)}
=
\sum_{i=1}^n\frac1{\zeta-c_i}.
$$
The left-hand side is $0$ because $p'(\zeta)=0$.

:::

:::

::: {.pf-step #s6}

Every zero of $p'$ lies in the convex hull of the zeros of $p$.

::: pf-proof

Let $\zeta$ be a zero of $p'$. If $p(\zeta)=0$, apply step [](#s4){.pf-ref}. If
$p(\zeta)\ne0$, step [](#s5){.pf-ref} gives the hypothesis of part (a), and step
[](#s3){.pf-ref} implies
$$
\zeta\in\operatorname{conv}\{c_1,\ldots,c_n\}.
$$
Thus the conclusion holds in both cases.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves part (a), and step [](#s6){.pf-ref} proves part (b).

:::

:::

:::
