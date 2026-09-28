---
schema: qual/card@1
id: P-BKF14-5A
kind: problem
title: 'Gauss--Lucas theorem: critical points lie in the convex hull of the roots'
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
    Independently checked the retained Fall 2014 solution packet: the
    logarithmic derivative has positive real part in a separated half-plane,
    and a separating line gives the Gauss--Lucas conclusion.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the logarithmic-derivative identity and the affine rotation and
    translation used to separate a hypothetical critical point from the
    convex hull of the roots.
---

::: {.problem}
(a) Suppose that $P(z)=c(z-a_1)\cdots(z-a_n)$ is a complex polynomial.
If $z$ has positive real part and all the roots $a_i$ have negative real part, show that $P'(z)/P(z)$ has positive real part.

(b) Show that all the roots of the derivative $P'$ of a complex polynomial lie in the convex hull of the roots of $P$.
:::

::: {.solution}
<1>1. If $w\in\CC$ has $\Re w>0$, then
$$
\Re\!\left(\frac1w\right)>0.
$$

::: {.proof}
Since
$$
\frac1w=\frac{\overline w}{|w|^2},
$$
one has
$$
\Re\!\left(\frac1w\right)
=
\frac{\Re w}{|w|^2}>0.
$$
:::

<1>2. Under the hypotheses of part (a),
$$
\Re\!\left(\frac{P'(z)}{P(z)}\right)>0.
$$

::: {.proof}
The assumptions imply $z\ne a_i$ for every $i$, so $P(z)\ne0$. Taking
the logarithmic derivative of
$$
P(z)=c\prod_{i=1}^n(z-a_i)
$$
gives
$$
\frac{P'(z)}{P(z)}
=
\sum_{i=1}^n\frac1{z-a_i}.
$$
For every $i$,
$$
\Re(z-a_i)=\Re z-\Re a_i>0.
$$
Each summand therefore has positive real part by step <1>1, and so does
their sum.
:::

<1>3. Let $K$ be the convex hull of the roots of $P$. If
$\zeta\notin K$, there is an affine change of complex coordinate
$$
w=e^{-i\theta}(z-c)
$$
such that the image $w_0=e^{-i\theta}(\zeta-c)$ has positive real part
and every transformed root
$$
\alpha_i=e^{-i\theta}(a_i-c)
$$
has negative real part.

::: {.proof}
The set $K$ is compact and convex. Since $\zeta\notin K$, the strict
separation theorem in $\RR^2$ gives a line separating $\zeta$ from
$K$. A translation moves that line through the origin, and a rotation
makes it the imaginary axis. Choosing the orientation so that $\zeta$
lies on the right gives exactly the stated inequalities for real
parts.
:::

<1>4. No zero of $P'$ lies outside $K$.

::: {.proof}
Suppose for contradiction that $P'(\zeta)=0$ for some
$\zeta\notin K$. Use step <1>3 and define
$$
Q(w)\coloneqq P(e^{i\theta}w+c).
$$
The roots of $Q$ are the numbers $\alpha_i$, all of which have negative
real part, while $w_0=e^{-i\theta}(\zeta-c)$ has positive real part.
Moreover,
$$
Q'(w_0)=e^{i\theta}P'(\zeta)=0.
$$
Since $w_0$ is not a root of $Q$, this gives
$$
\frac{Q'(w_0)}{Q(w_0)}=0.
$$
But step <1>2, applied to $Q$ at $w_0$, says that this quotient has
strictly positive real part. This contradiction proves the claim.
:::

<1>5. Therefore every root of $P'$ lies in the convex hull of the roots
of $P$.

::: {.proof}
This is exactly the conclusion of step <1>4, with $K$ equal to that
convex hull.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>2 proves part (a), and step <1>5 proves part (b).
:::
:::
