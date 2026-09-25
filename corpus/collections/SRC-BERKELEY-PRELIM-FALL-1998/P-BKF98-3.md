---
schema: qual/card@1
id: P-BKF98-3
kind: problem
title: Evaluate $\int_0^\infty (1+x^\alpha)^{-1}\,dx$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Substituted t=x^alpha and evaluated the resulting beta-type integral
    with a keyhole contour for z^(beta-1)/(1+z).
---

::: {.problem}
Prove that for every real $\alpha>1$,
\[
\int_0^\infty\frac{dx}{1+x^\alpha}
=
\frac{\pi/\alpha}{\sin(\pi/\alpha)}.
\]
:::

::: {.solution}
Set
$$
\beta\coloneqq\frac1\alpha.
$$
Since $\alpha>1$,
$$
0<\beta<1.
$$

<1>1. The substitution
$$
t=x^\alpha
$$
gives
$$
\int_0^\infty\frac{dx}{1+x^\alpha}
=
\frac1\alpha
\int_0^\infty
\frac{t^{\beta-1}}{1+t}\,dt.
$$

::: {.proof}
From $t=x^\alpha$,
$$
x=t^{1/\alpha}=t^\beta
$$
and
$$
dx
=
\frac1\alpha t^{1/\alpha-1}\,dt
=
\frac1\alpha t^{\beta-1}\,dt.
$$
Substitute into the integral.
:::

<1>2. Define
$$
J(\beta)
\coloneqq
\int_0^\infty
\frac{t^{\beta-1}}{1+t}\,dt.
$$
Then
$$
J(\beta)
=
\frac{\pi}{\sin(\pi\beta)}.
$$

::: {.proof}
Use the branch
$$
z^{\beta-1}
=
\exp\bigl((\beta-1)\Log z\bigr),
\qquad
0<\arg z<2\pi,
$$
and integrate
$$
\frac{z^{\beta-1}}{1+z}
$$
around a keyhole contour about the positive real axis.

Because $0<\beta<1$, the integrals over the outer and inner circular arcs
tend to zero as their radii tend to $\infty$ and $0$. The upper bank
contributes $J(\beta)$. On the lower bank the power acquires the factor
$$
e^{2\pi i(\beta-1)}
=
e^{2\pi i\beta},
$$
and the reversed orientation makes its contribution
$$
-e^{2\pi i\beta}J(\beta).
$$

The only enclosed pole is $z=-1$, where the chosen argument is $\pi$. Its
residue is
$$
e^{i\pi(\beta-1)}.
$$
Thus the residue theorem gives
$$
\bigl(1-e^{2\pi i\beta}\bigr)J(\beta)
=
2\pi i e^{i\pi(\beta-1)}.
$$
Since
$$
1-e^{2\pi i\beta}
=
-2ie^{i\pi\beta}\sin(\pi\beta),
$$
solving for $J(\beta)$ gives
$$
J(\beta)
=
\frac{\pi}{\sin(\pi\beta)}.
$$
:::

<1>3. Therefore
$$
\boxed{
\int_0^\infty\frac{dx}{1+x^\alpha}
=
\frac{\pi/\alpha}{\sin(\pi/\alpha)}
}.
$$

::: {.proof}
Combine steps <1>1 and <1>2 and substitute
$$
\beta=\frac1\alpha.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required identity.
:::
:::
