---
schema: qual/card@1
id: P-BKF78-4
kind: problem
title: Evaluate a Poisson-kernel-type trigonometric integral
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 4 of the deterministic MinerU Flash extraction of the Berkeley Fall 1978 preliminary exam.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Checked the contour substitution, the enclosed pole in each range of r,
    both residue computations, and the final combination as
    2 pi / abs(1-r^2).
---

::: {.problem}
Evaluate
\[
\int_0^{2\pi}\frac{d\theta}{1-2r\cos\theta+r^2},
\]
where $r^2\ne1$.
:::

::: {.solution}
For the real parameter $r$ in the problem, $r^2\ne1$ implies either
$\abs{r}<1$ or $\abs{r}>1$.
Write $I(r)$ for the integral in the problem.

::: pf

::: {.pf-step #contour-integral}
With $z=e^{i\theta}$, the integral is
$$
I(r)
=
\oint_{\abs{z}=1}
\frac{dz}{i(z-r)(1-rz)}.
$$

::: pf-proof
On $\abs{z}=1$,
$$
d\theta=\frac{dz}{iz}
\qquad\text{and}\qquad
\cos\theta=\frac{1}{2}\left(z+z^{-1}\right).
$$
Hence
$$
z\left(1-2r\cos\theta+r^2\right)
=(z-r)(1-rz),
$$
so substitution into the original integral gives the displayed contour integral.
:::

:::

::: {.pf-step #case-r-less-1}
If $\abs{r}<1$, then
$$
I(r)=\frac{2\pi}{1-r^2}.
$$

::: pf-proof
In this case the integrand in step [](#contour-integral){.pf-ref} has exactly one pole inside
$\abs{z}=1$, namely $z=r$. Its residue there is
$$
\frac{1}{i(1-r^2)}.
$$
The residue theorem therefore gives
$$
I(r)
=
2\pi i\frac{1}{i(1-r^2)}
=
\frac{2\pi}{1-r^2}.
$$
:::

:::

::: {.pf-step #case-r-greater-1}
If $\abs{r}>1$, then
$$
I(r)=\frac{2\pi}{r^2-1}.
$$

::: pf-proof
Now $z=r$ lies outside the unit circle, while $z=1/r$ lies inside it.
Thus the only enclosed pole is $z=1/r$. Its residue is
$$
\frac{1}{i(r^2-1)},
$$
because
$$
\lim_{z\to1/r}
\frac{z-1/r}{i(z-r)(1-rz)}
=
\frac{1}{i(1/r-r)(-r)}
=
\frac{1}{i(r^2-1)}.
$$
The residue theorem gives the stated value.
:::

:::

::: {.pf-step #combined-formula}
Therefore
$$
\boxed{
\int_0^{2\pi}
\frac{d\theta}{1-2r\cos\theta+r^2}
=
\frac{2\pi}{\abs{1-r^2}}
}.
$$

::: pf-proof
If $\abs{r}<1$, then $1-r^2>0$, so step [](#case-r-less-1){.pf-ref} gives the boxed
formula. If $\abs{r}>1$, then $r^2-1>0$, so step [](#case-r-greater-1){.pf-ref} gives the same
formula.
:::

:::

::: pf-qed
Step [](#combined-formula){.pf-ref} is the requested evaluation.
:::

:::
:::
