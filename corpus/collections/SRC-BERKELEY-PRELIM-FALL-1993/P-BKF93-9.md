---
schema: qual/card@1
id: P-BKF93-9
kind: problem
title: Evaluate $\int_{-\infty}^{\infty} e^{-ix}/(x^2-2x+4)\,dx$
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
    Closed the contour in the lower half-plane, where e^{-iz} decays, and
    evaluated the clockwise residue contribution from the pole
    1-i sqrt(3).
---

::: {.problem}
Evaluate
\[
\int_{-\infty}^{\infty}\frac{e^{-ix}}{x^2-2x+4}\,dx.
\]
:::

::: {.solution}
Let
$$
f(z)\coloneqq\frac{e^{-iz}}{z^2-2z+4}.
$$

<1>1. The poles of $f$ are
$$
z=1\pm i\sqrt{3},
$$
and the only pole in the lower half-plane is
$$
z_0\coloneqq1-i\sqrt{3}.
$$

::: {.proof}
One has
$$
z^2-2z+4
=
(z-1)^2+3
=
(z-1-i\sqrt{3})(z-1+i\sqrt{3}).
$$
Both poles are simple, and only $1-i\sqrt{3}$ has negative imaginary part.
:::

<1>2. If the real interval $[-R,R]$ is closed by the lower semicircle, then
the integral over that semicircle tends to $0$ as $R\to\infty$.

::: {.proof}
For $z=x+iy$ in the lower half-plane,
$$
\abs{e^{-iz}}=e^y\leq1.
$$
On the semicircle $\abs z=R$,
$$
\abs{z^2-2z+4}
\geq
R^2-2R-4.
$$
Its length is $\pi R$, so the $ML$ estimate gives
$$
\abs{\int_{\text{lower arc}}f(z)\,dz}
\leq
\frac{\pi R}{R^2-2R-4}
\longrightarrow0.
$$
:::

<1>3. The residue at $z_0=1-i\sqrt{3}$ is
$$
\Res_{z=z_0}f(z)
=
\frac{e^{-\sqrt{3}-i}}{-2i\sqrt{3}}.
$$

::: {.proof}
Since the pole is simple,
$$
\Res_{z=z_0}f(z)
=
\frac{e^{-iz_0}}{2z_0-2}.
$$
Now
$$
2z_0-2=-2i\sqrt{3},
$$
and
$$
e^{-iz_0}
=
e^{-i(1-i\sqrt{3})}
=
e^{-\sqrt{3}-i}.
$$
Substitution gives the displayed residue.
:::

<1>4. One has
$$
\int_{-\infty}^{\infty}\frac{e^{-ix}}{x^2-2x+4}\,dx
=
\boxed{\frac{\pi}{\sqrt{3}}e^{-\sqrt{3}-i}}.
$$

::: {.proof}
The lower semicircular contour is clockwise. By the residue theorem,
$$
\int_{-R}^{R}f(x)\,dx
+
\int_{\text{lower arc}}f(z)\,dz
=
-2\pi i\Res_{z=z_0}f(z).
$$
Letting $R\to\infty$ and using step <1>2 gives
$$
\int_{-\infty}^{\infty}f(x)\,dx
=
-2\pi i
\frac{e^{-\sqrt{3}-i}}{-2i\sqrt{3}}
=
\frac{\pi}{\sqrt{3}}e^{-\sqrt{3}-i}.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested value.
:::
:::
