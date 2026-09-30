---
schema: qual/card@1
id: P-IRNN2
kind: problem
title: $\int_C \frac{dz}{f(z)-f(z_0)}=\frac{2\pi i}{f'(z_0)}$ for a small circle about
  a noncritical point
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Argument Principle
  - Zeros
  - Biholomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $f$ be analytic on a region $R$ and suppose $f'(z_0) \neq 0$ for some $z_0 \in R$.
Show that if $C$ is a circle of sufficiently small radius centered at $z_0$, then 
\[
\frac{2 \pi i}{f^{\prime}\left(z_{0}\right)}=\int_{C} \frac{d z}{f(z)-f\left(z_{0}\right)}
.\]

> Hint: use the inverse function theorem.
:::

::: {.solution}
::: pf

::: pf-step
Local biholomorphism via the Inverse Function Theorem:

::: pf-proof

::: pf-step
Since $f$ is holomorphic on $R$ and $f'(z_0) \neq 0$, the Complex Inverse Function Theorem implies there exist open neighborhoods $U$ of $z_0$ and $V$ of $w_0 = f(z_0)$ such that $f: U \to V$ is a biholomorphism with holomorphic inverse $g = f^{-1}: V \to U$.

::: pf-proof
Complex Inverse Function Theorem.
:::

:::

::: {.pf-step #inverse-derivative}
The derivative of the inverse function at $w_0$ is given by:
\[
g'(w_0) = \frac{1}{f'(g(w_0))} = \frac{1}{f'(z_0)}.
\]

::: pf-proof
chain rule applied to $f(g(w)) = w$.
:::

:::

:::

:::

::: {.pf-step #change-of-variables}
Change of variables in the contour integral:

::: pf-proof

::: pf-step
Choose $r > 0$ sufficiently small such that the closed disk $\overline{D}(z_0, r) \subset U$, and let $C = \partial D(z_0, r)$ be the circle oriented counterclockwise.

::: pf-proof
openness of $U$.
:::

:::

::: pf-step
The image $\Gamma = f(C)$ is a simple closed curve in $V$ winding once counterclockwise around $w_0 = f(z_0)$, so the winding number is $\operatorname{Ind}_\Gamma(w_0) = 1$.

::: pf-proof
conformal mapping of a small disk.
:::

:::

::: pf-step
Substitute $z = g(w)$, which gives $dz = g'(w)\,dw$ and $f(z) - f(z_0) = w - w_0$:
\[
\int_C \frac{dz}{f(z) - f(z_0)} = \int_\Gamma \frac{g'(w)}{w - w_0} \, dw.
\]

::: pf-proof
holomorphic change of variables for line integrals.
:::

:::

:::

:::

::: {.pf-step #cif-evaluation}
Evaluation via Cauchy’s Integral Formula:

::: pf-proof

::: pf-step
Since $g'(w)$ is holomorphic on $V$ and $\Gamma$ is a simple closed curve in $V$ enclosing $w_0$, Cauchy’s Integral Formula yields:
\[
\int_\Gamma \frac{g'(w)}{w - w_0} \, dw = 2\pi i \, g'(w_0).
\]

::: pf-proof
Cauchy's Integral Formula.
:::

:::

::: pf-step
Substituting $g'(w_0) = \frac{1}{f'(z_0)}$ from step [](#inverse-derivative){.pf-ref}:
\[
\int_C \frac{dz}{f(z) - f(z_0)} = 2\pi i \cdot \frac{1}{f'(z_0)} = \frac{2\pi i}{f'(z_0)}.
\]

::: pf-proof
Step [](#inverse-derivative){.pf-ref}.
:::

:::

:::

:::

::: pf-step
Conclusion:
$\int_C \frac{dz}{f(z) - f(z_0)} = \frac{2\pi i}{f'(z_0)}$. Q.E.D.

::: pf-proof
Steps [](#change-of-variables){.pf-ref} and [](#cif-evaluation){.pf-ref}.
:::

:::

:::

:::
