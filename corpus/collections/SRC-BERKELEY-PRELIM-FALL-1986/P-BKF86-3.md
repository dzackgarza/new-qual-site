---
schema: qual/card@1
id: P-BKF86-3
kind: problem
title: Integral of $x^3-3xy^2$ over the region between two circles
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
---

::: {.problem}
Evaluate
\[
\iint_{\mathcal R}(x^3-3xy^2)\,dx\,dy,
\]
where
\[
\mathcal R=\{(x,y)\in\mathbb R^2 : (x+1)^2+y^2\le 9,\ (x-1)^2+y^2\ge 1\}.
\]
:::

::: {.solution}
Let
$$
D_-=\{(x,y):(x+1)^2+y^2\leq9\},
\qquad
D_+=\{(x,y):(x-1)^2+y^2\leq1\}.
$$

::: pf

::: {.pf-step #s1}

One has
$$
D_+\subseteq D_-,
$$
and therefore
$$
\mathcal R=D_-\setminus D_+.
$$

::: pf-proof

The centers of $D_-$ and $D_+$ are $(-1,0)$ and $(1,0)$, whose distance is $2$. Since
$$
2+1=3,
$$
the disk of radius $1$ centered at $(1,0)$ lies inside the disk of radius $3$ centered at $(-1,0)$; the two boundary circles are internally tangent at $(2,0)$. The description of $\mathcal R$ is then immediate from its two defining inequalities.

:::

:::

::: {.pf-step #s2}

If
$$
D(c,R)=\{(x,y):(x-c)^2+y^2\leq R^2\},
$$
then
$$
\iint_{D(c,R)}(x^3-3xy^2)\,dx\,dy
=
\pi R^2c^3.
$$

::: pf-proof

Make the translation
$$
x=c+u.
$$
Then the disk becomes $u^2+y^2\leq R^2$, and
$$
\begin{aligned}
(c+u)^3-3(c+u)y^2
&=
c^3+3c^2u+3cu^2+u^3\\
&\quad-3cy^2-3uy^2.
\end{aligned}
$$
On the disk centered at the origin, the terms containing an odd power of $u$ integrate to zero by the symmetry $u\mapsto-u$. Also rotational symmetry gives
$$
\iint_{u^2+y^2\leq R^2}u^2\,du\,dy
=
\iint_{u^2+y^2\leq R^2}y^2\,du\,dy.
$$
Hence the contributions $3cu^2$ and $-3cy^2$ cancel after integration. Only the constant term remains, so
$$
\iint_{D(c,R)}(x^3-3xy^2)\,dx\,dy
=
c^3\operatorname{area}(D(c,R))
=
\pi R^2c^3.
$$

:::

:::

::: pf-step

The integral over $D_-$ is
$$
-9\pi,
$$
and the integral over $D_+$ is
$$
\pi.
$$

::: pf-proof

Apply step [](#s2){.pf-ref} with $(c,R)=(-1,3)$ and $(c,R)=(1,1)$:
$$
\iint_{D_-}(x^3-3xy^2)\,dx\,dy
=
\pi\cdot 3^2\cdot(-1)^3
=
-9\pi,
$$
while
$$
\iint_{D_+}(x^3-3xy^2)\,dx\,dy
=
\pi\cdot1^2\cdot1^3
=
\pi.
$$

:::

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{
\iint_{\mathcal R}(x^3-3xy^2)\,dx\,dy=-10\pi
}.
$$

::: pf-proof

By step [](#s1){.pf-ref} and additivity of the integral,
$$
\begin{aligned}
\iint_{\mathcal R}(x^3-3xy^2)\,dx\,dy
&=
\iint_{D_-}(x^3-3xy^2)\,dx\,dy
-\iint_{D_+}(x^3-3xy^2)\,dx\,dy\\
&=
-9\pi-\pi\\
&=
-10\pi.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required evaluation.

:::

:::

:::
