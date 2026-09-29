---
schema: qual/card@1
id: P-KWIEG
kind: problem
title: Number of roots of $4z^4-6z+3$ in $|z|<1$ and $1<|z|<2$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Find the number of roots of $p(z) = 4z^4 - 6z + 3$ in $\abs{z} < 1$ and $1 < \abs{z} < 2$ respectively.
:::

::: {.solution}
Let $x_0 = \qty{\tfrac38}^{1/3}$.

::: pf

::: {.pf-step #four-roots-in-disk-2}
$p$ has exactly $4$ roots in $\abs{z} < 2$, counted with multiplicity.

::: pf-proof
On $\abs{z} = 2$, $\abs{4z^4} = 64$ and $\abs{-6z + 3} \le 12 + 3 = 15 < 64$. By Rouché's theorem, $p = 4z^4 + (-6z + 3)$ has as many zeros in $\abs{z} < 2$ as $4z^4$, namely $4$.
:::

:::

::: {.pf-step #monotonicity-on-reals}
On $\RR$, $p$ is decreasing on $(-\infty, x_0]$ and increasing on $[x_0, \infty)$.

::: pf-proof
$p'(x) = 16x^3 - 6$ vanishes only at $x_0$, is negative for $x < x_0$, and is positive for $x > x_0$.
:::

:::

::: {.pf-step #two-real-roots}
$p$ has exactly two real roots $r_1<r_2$, with $r_1 \in (\tfrac12, x_0)$ and $r_2 \in (\tfrac34, 1)$.

::: pf-proof
Since $\tfrac18 < \tfrac38 < \tfrac{27}{64}$ and $\tfrac{8}{27}<\tfrac38$, one has $\tfrac23 < x_0 < \tfrac34$. The values
$$p\qty(\tfrac12) = \tfrac14 > 0,
\qquad
p(x_0) = \tfrac32x_0 - 6x_0 + 3 = 3 - \tfrac92x_0 < 0,
\qquad
p\qty(\tfrac34) = \tfrac{81}{64} - \tfrac92 + 3 = -\tfrac{15}{64} < 0,
\qquad
p(1) = 1 > 0$$
use $4x_0^4 = 4x_0\cdot\tfrac38$. By step [](#monotonicity-on-reals){.pf-ref} and the intermediate value theorem, $p$ has exactly one root in $(\tfrac12, x_0)$, exactly one in $(\tfrac34, 1)$, and no other real root: $p > p(\tfrac12) > 0$ on $(-\infty, \tfrac12]$ and $p \ge p(1) > 0$ on $[1,\infty)$, while $p<0$ on $[x_0,\tfrac34]$.
:::

:::

::: {.pf-step #nonreal-roots-pair}
The two nonreal roots are a conjugate pair $z,\bar z$ with $1 < \abs{z} < \sqrt2$.

::: pf-proof
By step [](#four-roots-in-disk-2){.pf-ref} and step [](#two-real-roots){.pf-ref}, $p$ has two further roots, which are nonreal; since $p$ has real coefficients they are conjugate. The product of all four roots is $\tfrac34$, so $\abs{z}^2 r_1r_2 = \tfrac34$. Step [](#two-real-roots){.pf-ref} gives $\tfrac38 < r_1r_2 < x_0 < \tfrac34$, hence $\abs{z}^2 = \tfrac{3/4}{r_1r_2} \in (1, 2)$.
:::

:::

::: {.pf-step #root-counts}
$p$ has $\boxed{2}$ roots in $\abs{z} < 1$ and $\boxed{2}$ roots in $1 < \abs{z} < 2$.

::: pf-proof
The real roots $r_1, r_2$ lie in $(0,1)$ by step [](#two-real-roots){.pf-ref}, and the nonreal roots satisfy $1<\abs{z}<\sqrt2<2$ by step [](#nonreal-roots-pair){.pf-ref}. These are all four roots.
:::

:::

::: pf-qed
Step [](#root-counts){.pf-ref} gives both counts.
:::

:::
:::
