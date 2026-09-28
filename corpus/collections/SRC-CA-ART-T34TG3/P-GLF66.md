---
schema: qual/card@1
id: P-GLF66
kind: problem
title: $\int_0^{2\pi}\frac{d\theta}{a+b\cos\theta}=\frac{2\pi}{\sqrt{a^2-b^2}}$ for
  $a>|b|$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Trigonometry
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Show that if $a,b\in \RR$ with $a > \abs{b}$, then
\[
\int_{0}^{2 \pi} \frac{d \theta}{a+b \cos \theta}=\frac{2 \pi}{\sqrt{a^{2}-b^{2}}}
.\]
:::

::: {.solution}
Write $I$ for the integral.

<1>1. If $b = 0$, then $I = \dfrac{2\pi}{\sqrt{a^2 - b^2}}$.

::: {.proof}
The integrand is the constant $1/a$, so $I = 2\pi/a = 2\pi/\sqrt{a^2}$.
:::

<1>2. If $b\neq0$, then
$$I = \frac{2}{i} \oint_{\abs{z} = 1} g(z)\,dz,
\qquad
g(z)\coloneqq\frac{1}{bz^2 + 2az + b},$$
with the unit circle oriented counterclockwise.

::: {.proof}
With $z = e^{i\theta}$, one has $d\theta = \frac{dz}{iz}$ and $\cos \theta = \frac{z + z^{-1}}{2}$, so
$$a + b \cos \theta = \frac{bz^2 + 2az + b}{2z}
\qquad\text{and}\qquad
\frac{d\theta}{a+b\cos\theta} = \frac{2z}{bz^2 + 2az + b}\cdot\frac{dz}{iz}.$$
:::

<1>3. If $b\neq0$, the only pole of $g$ inside the unit circle is
$$z_1 = \frac{-a + \sqrt{a^2 - b^2}}{b},
\qquad\text{and}\qquad
\operatorname{Res}(g, z_1) = \frac{1}{2\sqrt{a^2 - b^2}}.$$

::: {.proof}
The roots of $bz^2 + 2az + b$ are $z_1$ and $z_2 = \frac{-a - \sqrt{a^2 - b^2}}{b}$, and $z_1 z_2 = 1$. Since $a > \abs{b} > 0$,
$$\abs{z_2} = \frac{a + \sqrt{a^2 - b^2}}{\abs{b}} > \frac{a}{\abs{b}} > 1,$$
so $\abs{z_1} = 1/\abs{z_2} < 1$. The pole at $z_1$ is simple, with residue
$$\frac{1}{b(z_1 - z_2)} = \frac{1}{b \cdot \frac{2\sqrt{a^2 - b^2}}{b}}.$$
:::

<1>4. If $b\neq0$, then $I = \dfrac{2\pi}{\sqrt{a^2 - b^2}}$.

::: {.proof}
By steps <1>2 and <1>3 and the residue theorem,
$$I = \frac{2}{i} \cdot 2\pi i \operatorname{Res}(g, z_1) = \frac{4\pi}{2\sqrt{a^2 - b^2}}.$$
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1 and <1>4 give $I = \boxed{\dfrac{2\pi}{\sqrt{a^2 - b^2}}}$ in both cases.
:::
:::
