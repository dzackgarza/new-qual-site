---
schema: qual/card@1
id: P-BERK85S-12
kind: problem
title: Evaluate the Euler beta integral $\int_0^\infty x^{\alpha-1}/(1+x)\,dx$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Established convergence exactly for 0<Re(alpha)<1 and evaluated
    the integral by a keyhole contour for z^{alpha-1}/(1+z), using
    the branch 0<arg z<2pi. The two sides of the cut differ by
    e^{2pi i alpha}, and the sole residue at -1 yields
    pi/sin(pi alpha).
---

::: {.problem}
Prove that
\[
\int_0^\infty\frac{x^{\alpha-1}}{1+x}\,dx
=\frac{\pi}{\sin(\pi\alpha)}.
\]
What restrictions must be placed on $\alpha$?
:::

::: {.solution}
For $x>0$, define
$$
x^{\alpha-1}
=
\exp((\alpha-1)\log x),
$$
where $\log x$ is the real logarithm.

<1>1. The improper integral
$$
I(\alpha)
\coloneqq
\int_0^\infty\frac{x^{\alpha-1}}{1+x}\,dx
$$
converges exactly when
$$
\boxed{0<\Re\alpha<1}.
$$

::: {.proof}
Near $0$,
$$
\frac{x^{\alpha-1}}{1+x}
\sim
x^{\alpha-1},
$$
and
$$
\int_0^1x^{\alpha-1}\,dx
$$
converges exactly when $\Re\alpha>0$.

Near infinity,
$$
\frac{x^{\alpha-1}}{1+x}
\sim
x^{\alpha-2},
$$
and
$$
\int_1^\infty x^{\alpha-2}\,dx
$$
converges exactly when $\Re\alpha<1$. Thus both endpoints converge
exactly in the displayed strip. In that strip the integral is in fact
absolutely convergent.
:::

<1>2. Assume henceforth that $0<\Re\alpha<1$. On
$$
\CC\setminus[0,\infty)
$$
use the branch
$$
\Log z=\log\abs z+i\arg z,
\qquad
0<\arg z<2\pi,
$$
and set
$$
F(z)
\coloneqq
\frac{e^{(\alpha-1)\Log z}}{1+z}.
$$
Then $F$ has a single pole in this slit plane, at $z=-1$, with
$$
\operatorname{Res}_{z=-1}F
=
-e^{i\pi\alpha}.
$$

::: {.proof}
The only zero of the denominator is $-1$, whose argument in the chosen
branch is $\pi$. Hence
$$
\operatorname{Res}_{z=-1}F
=
e^{(\alpha-1)i\pi}
=
-e^{i\pi\alpha}.
$$
:::

<1>3. Integrate $F$ around the positively oriented keyhole contour
with radii $0<\epsilon<1<R$ about the positive real axis. The outer
and inner circular contributions tend to $0$ as
$$
R\to\infty,
\qquad
\epsilon\to0.
$$

::: {.proof}
On either circular arc, the factor
$$
e^{-\Im(\alpha)\arg z}
$$
is bounded by a constant depending only on $\alpha$.

On $\abs z=R$,
$$
\abs{F(z)}
\leq
C_\alpha
\frac{R^{\Re\alpha-1}}{R-1}.
$$
Multiplying by the arc length $2\pi R$ gives
$$
O(R^{\Re\alpha-1})\longrightarrow0
$$
because $\Re\alpha<1$.

On $\abs z=\epsilon$,
$$
\abs{F(z)}
\leq
C_\alpha
\frac{\epsilon^{\Re\alpha-1}}{1-\epsilon}.
$$
Multiplying by the arc length $2\pi\epsilon$ gives
$$
O(\epsilon^{\Re\alpha})\longrightarrow0
$$
because $\Re\alpha>0$.
:::

<1>4. In the same limit, the sum of the two straight portions of the
keyhole contour is
$$
\left(1-e^{2\pi i\alpha}\right)I(\alpha).
$$

::: {.proof}
On the upper side of the positive axis, $\arg z\to0$, so the
integrand tends to
$$
\frac{x^{\alpha-1}}{1+x},
$$
and that segment runs from $\epsilon$ to $R$.

On the lower side, $\arg z\to2\pi$, so
$$
e^{(\alpha-1)\Log z}
=
e^{2\pi i(\alpha-1)}x^{\alpha-1}
=
e^{2\pi i\alpha}x^{\alpha-1}.
$$
That segment is traversed from $R$ back to $\epsilon$. Its limiting
contribution is therefore
$$
-e^{2\pi i\alpha}I(\alpha).
$$
Adding the two contributions gives the claim.
:::

<1>5. The residue theorem gives
$$
\left(1-e^{2\pi i\alpha}\right)I(\alpha)
=
-2\pi i e^{i\pi\alpha}.
$$

::: {.proof}
By step <1>3, the circular integrals disappear in the limit. By step
<1>4, the remaining contour integral tends to the left-hand side.
Step <1>2 and the residue theorem give
$$
2\pi i\operatorname{Res}_{z=-1}F
=
-2\pi i e^{i\pi\alpha}.
$$
:::

<1>6. For $0<\Re\alpha<1$,
$$
\boxed{
I(\alpha)
=
\frac{\pi}{\sin(\pi\alpha)}.
}
$$

::: {.proof}
Use
$$
1-e^{2\pi i\alpha}
=
-2i e^{i\pi\alpha}\sin(\pi\alpha)
$$
in step <1>5 and cancel the nonzero common factor
$-2i e^{i\pi\alpha}$.
:::

<1>7. If $\alpha$ is required to be real, the restriction is exactly
$$
\boxed{0<\alpha<1}.
$$

::: {.proof}
This is step <1>1 specialized to real $\alpha$.
:::

<1>8. Q.E.D.

::: {.proof}
Steps <1>1, <1>6, and <1>7 give the convergence restriction and the
required value of the integral.
:::
:::
