---
schema: qual/card@1
id: P-WESCA08-II2
kind: problem
title: 'Two contour integrals on large circles'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Evaluate
$$
\int_{\abs{z-i}=10}\left(z+\frac1z\right)^4\,dz
$$
and
$$
\int_{\abs{z}=4}\left(\frac{\sin z}{z}\right)^{100}\,dz.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Expand the first integrand:
$$
\boxed{
\left(z+\frac1z\right)^4
=
z^4+4z^2+6+\frac4{z^2}+\frac1{z^4}}.
$$


::: pf-proof

Apply the binomial theorem:
$$
\begin{aligned}
\left(z+\frac1z\right)^4
&=
z^4
+4z^3\frac1z
+6z^2\frac1{z^2}
+4z\frac1{z^3}
+\frac1{z^4}\\
&=
z^4+4z^2+6+\frac4{z^2}+\frac1{z^4}.
\end{aligned}
$$

:::

:::

::: pf-step

The only singularity of the first integrand is
$$
z=0,
$$
and it lies inside the circle
$$
\abs{z-i}=10.
$$


::: pf-proof

The expansion in step [](#s1-1){.pf-ref} shows that the only negative powers occur at
$z=0$. Moreover,
$$
\abs{0-i}=1<10.
$$

:::

:::

::: {.pf-step #s1-3}

The residue at $z=0$ is zero:
$$
\boxed{
\operatorname{Res}_{z=0}
\left(z+\frac1z\right)^4
=0}.
$$


::: pf-proof

The residue is the coefficient of $z^{-1}$ in the Laurent expansion.
Step [](#s1-1){.pf-ref} contains no $z^{-1}$-term.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
\int_{\abs{z-i}=10}
\left(z+\frac1z\right)^4\,dz
=0}.
$$


::: pf-proof

By the residue theorem,
$$
\int_{\abs{z-i}=10}
\left(z+\frac1z\right)^4\,dz
=
2\pi i\,
\operatorname{Res}_{z=0}
\left(z+\frac1z\right)^4.
$$
Apply step [](#s1-3){.pf-ref}.

:::

:::

::: pf-step

Define
$$
g(z)
=
\begin{cases}
\dfrac{\sin z}{z},&z\ne0,\\[6pt]
1,&z=0.
\end{cases}
$$
Then $g$ is entire.


::: pf-proof

The Taylor series
$$
\sin z
=
z-\frac{z^3}{3!}+\frac{z^5}{5!}-\cdots
$$
gives, for $z\ne0$,
$$
\frac{\sin z}{z}
=
1-\frac{z^2}{3!}+\frac{z^4}{5!}-\cdots.
$$
The right-hand side is a power series converging on all of $\CC$,
and its value at $0$ is $1$. Thus the apparent singularity at $0$ is
removable and the specified extension is entire.

:::

:::

::: {.pf-step #s1-6}

Hence
$$
\boxed{
g(z)^{100}}
$$
is entire.


::: pf-proof

A finite product of entire functions is entire.

:::

:::

::: {.pf-step #s1-7}

On the circle $\abs{z}=4$,
$$
g(z)^{100}
=
\left(\frac{\sin z}{z}\right)^{100}.
$$


::: pf-proof

The circle $\abs{z}=4$ does not contain $z=0$, so the defining formula for
$g$ there is exactly
$$
g(z)=\frac{\sin z}{z}.
$$

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{
\int_{\abs{z}=4}
\left(\frac{\sin z}{z}\right)^{100}\,dz
=0}.
$$


::: pf-proof

By steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref}, the integrand on the contour is the restriction of the
entire function $g^{100}$. Cauchy's integral theorem gives zero around the
closed circle.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} and [](#s1-8){.pf-ref} evaluate the two requested contour integrals.

:::

:::

:::
