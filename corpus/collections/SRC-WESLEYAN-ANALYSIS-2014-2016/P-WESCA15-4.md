---
schema: qual/card@1
id: P-WESCA15-4
kind: problem
title: 'Three contour integrals'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, problem 4 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Calculate the following counterclockwise contour integrals:

1. $\displaystyle\int_{|z-i|=10}\left(z+\frac1z\right)^4\,dz$;

2. $\displaystyle\int_{|z|=4}\left(\frac{\sin z}{z}\right)^4\,dz$;

3. $\displaystyle\int_{|z|=1/2}\frac{e^{\sin z}}{z^3\cos z}\,dz$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The first integral is
$$
\boxed{0}.
$$


::: pf-proof

The circle $|z-i|=10$ contains the only singularity $z=0$ of the integrand. Expanding,
$$
\left(z+\frac1z\right)^4
=z^4+4z^2+6+4z^{-2}+z^{-4}.
$$
There is no $z^{-1}$ term, so the residue at $0$ is zero. By the residue theorem,
$$
\int_{|z-i|=10}\left(z+\frac1z\right)^4\,dz
=2\pi i\operatorname{Res}_{z=0}\left(z+\frac1z\right)^4
=0.
$$

:::

:::

::: {.pf-step #s1-2}

The second integral is
$$
\boxed{0}.
$$


::: pf-proof

The quotient
$$
\frac{\sin z}{z}
$$
has a removable singularity at $z=0$, with limiting value $1$. After filling in that value it is entire. Hence
$$
\left(\frac{\sin z}{z}\right)^4
$$
is entire, so Cauchy's theorem gives
$$
\int_{|z|=4}\left(\frac{\sin z}{z}\right)^4\,dz=0.
$$

:::

:::

::: {.pf-step #s1-3}

Inside $|z|=1/2$, the third integrand has only the singularity $z=0$.


::: pf-proof

The zeros of $\cos z$ are
$$
z=\frac\pi2+k\pi,
\qquad k\in\ZZ,
$$
all of which have modulus at least $\pi/2>1/2$. The factor $e^{\sin z}$ is entire and never zero. Thus within the disk $|z|<1/2$, the only singularity of
$$
\frac{e^{\sin z}}{z^3\cos z}
$$
is the pole contributed by $z^3$ at the origin.

:::

:::

::: {.pf-step #s1-4}

The residue of the third integrand at $z=0$ is
$$
\operatorname{Res}_{z=0}\frac{e^{\sin z}}{z^3\cos z}=1.
$$


::: pf-proof

It suffices to compute the coefficient of $z^2$ in
$$
\frac{e^{\sin z}}{\cos z}.
$$
Near $0$,
$$
\sin z=z+O(z^3),
$$
so
$$
e^{\sin z}
=1+z+\frac{z^2}{2}+O(z^3).
$$
Also
$$
\frac1{\cos z}
=1+\frac{z^2}{2}+O(z^4).
$$
Multiplying,
$$
\frac{e^{\sin z}}{\cos z}
=1+z+z^2+O(z^3).
$$
After division by $z^3$, the coefficient of $z^{-1}$ is therefore $1$.

:::

:::

::: {.pf-step #s1-5}

The third integral is
$$
\boxed{2\pi i}.
$$


::: pf-proof

By steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} and the residue theorem,
$$
\int_{|z|=1/2}\frac{e^{\sin z}}{z^3\cos z}\,dz
=2\pi i\operatorname{Res}_{z=0}\frac{e^{\sin z}}{z^3\cos z}
=2\pi i.
$$

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}, and [](#s1-5){.pf-ref} give the three requested values, respectively:
$$
\boxed{0,\quad0,\quad2\pi i}.
$$

:::

:::

:::
