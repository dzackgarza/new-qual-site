---
schema: qual/card@1
id: P-WESCA16-3
kind: problem
title: 'Three complex and real integrals'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Compute:

(a) $\displaystyle\int_\gamma e^{2z^2}\,dz$, where $\gamma$ is the counterclockwise square of side length $2$ centered at $0$;

(b) $\displaystyle\int_{|z|=5}\left(\frac1z-\frac1{z^2}\right)^3\,dz$;

(c) $\displaystyle\int_{-\infty}^{\infty}\frac{x+1}{(x^2+1)^2}\,dx$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The integral in part (a) is
$$
\boxed{\int_\gamma e^{2z^2}\,dz=0}.
$$


::: pf-proof

The function
$$
z\longmapsto e^{2z^2}
$$
is entire. The contour $\gamma$ is closed, so Cauchy's integral theorem gives
$$
\int_\gamma e^{2z^2}\,dz=0.
$$

:::

:::

::: {.pf-step #s1-2}

The Laurent expansion of the integrand in part (b) is
$$
\left(\frac1z-\frac1{z^2}\right)^3
=\frac1{z^3}-\frac3{z^4}+\frac3{z^5}-\frac1{z^6}.
$$


::: pf-proof

Expand the cube:
$$
\left(z^{-1}-z^{-2}\right)^3
=z^{-3}-3z^{-4}+3z^{-5}-z^{-6}.
$$

:::

:::

::: {.pf-step #s1-3}

The integral in part (b) is
$$
\boxed{
\int_{|z|=5}
\left(\frac1z-\frac1{z^2}\right)^3\,dz=0}.
$$


::: pf-proof

The only singularity inside the circle is $z=0$. By step [](#s1-2){.pf-ref}, the coefficient
of $z^{-1}$ in the Laurent expansion is $0$, so the residue at $0$ is $0$.
The residue theorem therefore gives the stated value.

:::

:::

::: {.pf-step #s1-4}

The odd part of the integrand in part (c) integrates to zero:
$$
\int_{-\infty}^{\infty}\frac{x}{(x^2+1)^2}\,dx=0.
$$


::: pf-proof

The function
$$
x\longmapsto\frac{x}{(x^2+1)^2}
$$
is odd and absolutely integrable on $\RR$. Its integral over the
symmetric interval $[-R,R]$ is zero for every $R$, and passing to the limit
gives the claim.

:::

:::

::: {.pf-step #s1-5}

One has
$$
\int_{-\infty}^{\infty}\frac{dx}{(x^2+1)^2}
=\frac{\pi}{2}.
$$


::: pf-proof

Set $x=\tan\theta$. Then
$$
dx=\sec^2\theta\,d\theta,
\qquad
1+x^2=\sec^2\theta,
$$
and $x$ ranges from $-\infty$ to $\infty$ as
$\theta$ ranges from $-\pi/2$ to $\pi/2$. Hence
$$
\int_{-\infty}^{\infty}\frac{dx}{(x^2+1)^2}
=\int_{-\pi/2}^{\pi/2}\cos^2\theta\,d\theta
=\frac{\pi}{2}.
$$

:::

:::

::: {.pf-step #s1-6}

The integral in part (c) is
$$
\boxed{
\int_{-\infty}^{\infty}\frac{x+1}{(x^2+1)^2}\,dx
=\frac{\pi}{2}}.
$$


::: pf-proof

Split the integral into the sum of its $x$ numerator term and its constant
numerator term. Step [](#s1-4){.pf-ref} evaluates the first as $0$, and step [](#s1-5){.pf-ref} evaluates
the second as $\pi/2$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-3){.pf-ref}, and [](#s1-6){.pf-ref} give the three requested values.

:::

:::

:::
