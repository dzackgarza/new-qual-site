---
schema: qual/card@1
id: P-BKF18-4B
kind: problem
title: The integral $\int_{-\infty}^{\infty}(x-\sin x)/x^3\,dx$
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: "The source-supplied Fall 2018 solution has an incorrect factor: two integrations by parts give one-half times the Dirichlet integral, not one-sixth. The erroneous companion answer is therefore not imported."
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Rechecked the retained Fall 2018 solution against the problem. Its factor
    1/6 is incorrect: the half-line integral is one-half of the Dirichlet
    integral, so the integral over the real line is pi/2.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked convergence at zero and infinity, both integration-by-parts
    boundary terms, the evenness reduction, and the final use of the standard
    Dirichlet integral.
---

::: {.problem}
Evaluate
\[
\int_{-\infty}^{\infty}\frac{x-\sin x}{x^3}\,dx.
\]
:::

::: {.solution}
<1>1. The integrand has a removable singularity at $0$, is integrable
on $\RR$, and is even.

::: {.proof}
The Taylor expansion
$$
\sin x
=
x-\frac{x^3}{6}+O(x^5)
$$
gives
$$
\frac{x-\sin x}{x^3}
=
\frac16+O(x^2)
$$
as $x\to0$. Thus the singularity at $0$ is removable.

For $|x|\ge1$,
$$
\left|
\frac{x-\sin x}{x^3}
\right|
\le
\frac1{x^2}+\frac1{|x|^3},
$$
so the integral converges absolutely at infinity.

Finally, both $x-\sin x$ and $x^3$ are odd, so their quotient is even.
:::

<1>2. Put
$$
J
\coloneqq
\int_0^\infty\frac{x-\sin x}{x^3}\,dx.
$$
Then
$$
J
=
\frac12
\int_0^\infty\frac{1-\cos x}{x^2}\,dx.
$$

::: {.proof}
Perform integration by parts on $[\varepsilon,R]$ with
$$
u=x-\sin x,
\qquad
dv=\frac{dx}{x^3}.
$$
Then
$$
du=(1-\cos x)\,dx,
\qquad
v=-\frac1{2x^2},
$$
so
$$
\int_\varepsilon^R\frac{x-\sin x}{x^3}\,dx
=
\left[
-\frac{x-\sin x}{2x^2}
\right]_\varepsilon^R
+
\frac12
\int_\varepsilon^R\frac{1-\cos x}{x^2}\,dx.
$$

As $R\to\infty$,
$$
\frac{R-\sin R}{R^2}\to0.
$$
As $\varepsilon\to0^+$,
$$
\frac{\varepsilon-\sin\varepsilon}{\varepsilon^2}
=
O(\varepsilon)
\to0.
$$
Taking the limits gives the claim.
:::

<1>3. One has
$$
\int_0^\infty\frac{1-\cos x}{x^2}\,dx
=
\int_0^\infty\frac{\sin x}{x}\,dx.
$$

::: {.proof}
Again integrate by parts on $[\varepsilon,R]$, now with
$$
u=1-\cos x,
\qquad
dv=\frac{dx}{x^2}.
$$
Then
$$
du=\sin x\,dx,
\qquad
v=-\frac1x,
$$
and hence
$$
\int_\varepsilon^R\frac{1-\cos x}{x^2}\,dx
=
\left[
-\frac{1-\cos x}{x}
\right]_\varepsilon^R
+
\int_\varepsilon^R\frac{\sin x}{x}\,dx.
$$
The boundary term at infinity tends to $0$ because $1-\cos R$ is
bounded, and the boundary term at $0$ tends to $0$ because
$$
1-\cos\varepsilon
=
O(\varepsilon^2).
$$
Taking limits proves the identity.
:::

<1>4. The half-line integral is
$$
J=\frac{\pi}{4}.
$$

::: {.proof}
The standard Dirichlet integral gives
$$
\int_0^\infty\frac{\sin x}{x}\,dx
=
\frac{\pi}{2}.
$$
Combining this with steps <1>2--<1>3 yields
$$
J
=
\frac12\cdot\frac{\pi}{2}
=
\frac{\pi}{4}.
$$
:::

<1>5. Therefore
$$
\boxed{
\int_{-\infty}^{\infty}
\frac{x-\sin x}{x^3}\,dx
=
\frac{\pi}{2}.
}
$$

::: {.proof}
By step <1>1 the integrand is even, so
$$
\int_{-\infty}^{\infty}
\frac{x-\sin x}{x^3}\,dx
=
2J.
$$
Now apply step <1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the requested value.
:::
:::
