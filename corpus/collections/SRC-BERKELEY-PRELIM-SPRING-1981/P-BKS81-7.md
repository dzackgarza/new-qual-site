---
schema: qual/card@1
id: P-BKS81-7
kind: problem
title: The integral $\int_{-\infty}^{\infty}x\sin x/(1+x^2)^2\,dx$
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
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the integration-by-parts reduction, the upper-half-plane residue at i, and the vanishing semicircle contribution.
---

::: {.problem}
Evaluate
\[
\int_{-\infty}^{\infty}\frac{x\sin x}{(1+x^2)^2}\,dx.
\]
:::

::: {.solution}
<1>1. The target integral satisfies
$$
\int_{-\infty}^{\infty}
\frac{x\sin x}{(1+x^2)^2}\,dx
=
\frac12
\int_{-\infty}^{\infty}
\frac{\cos x}{1+x^2}\,dx.
$$

::: {.proof}
Since
$$
\frac{x}{(1+x^2)^2}
=
-\frac12\frac{d}{dx}\frac1{1+x^2},
$$
integration by parts on $[-R,R]$ gives
$$
\begin{aligned}
\int_{-R}^R\frac{x\sin x}{(1+x^2)^2}\,dx
&=
\left[
-\frac{\sin x}{2(1+x^2)}
\right]_{-R}^R
+
\frac12\int_{-R}^R\frac{\cos x}{1+x^2}\,dx.
\end{aligned}
$$
The boundary term tends to zero as $R\to\infty$. Both improper integrals
converge absolutely, so the displayed identity follows.
:::

<1>2. One has
$$
\int_{-\infty}^{\infty}
\frac{\cos x}{1+x^2}\,dx
=
\frac{\pi}{e}.
$$

::: {.proof}
Integrate
$$
F(z)\coloneqq\frac{e^{iz}}{1+z^2}
$$
around the upper semicircle of radius $R>1$. The only enclosed pole is the
simple pole at $z=i$, with residue
$$
\operatorname{Res}_{z=i}F(z)
=
\frac{e^{ii}}{2i}
=
\frac{e^{-1}}{2i}.
$$
Hence the residue theorem gives a contour integral equal to
$$
2\pi i\frac{e^{-1}}{2i}
=
\frac{\pi}{e}.
$$

On the upper semicircle, $\abs{e^{iz}}\le1$, while
$$
\abs{1+z^2}\ge R^2-1.
$$
Thus the absolute value of the arc integral is at most
$$
\frac{\pi R}{R^2-1},
$$
which tends to zero. Letting $R\to\infty$ therefore yields
$$
\int_{-\infty}^{\infty}
\frac{e^{ix}}{1+x^2}\,dx
=
\frac{\pi}{e}.
$$
Taking real parts gives the asserted cosine integral.
:::

<1>3. Therefore
$$
\boxed{
\int_{-\infty}^{\infty}
\frac{x\sin x}{(1+x^2)^2}\,dx
=
\frac{\pi}{2e}
}.
$$

::: {.proof}
Substitute the value from step <1>2 into the identity from step <1>1.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the requested value.
:::
:::
