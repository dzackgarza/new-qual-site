---
schema: qual/card@1
id: E-OBU6T
kind: problem
title: An injective analytic map on $\CC\setminus\{z_0\}$, bounded off a neighborhood
  of $z_0$, is a Möbius transformation $\frac{az+b}{cz+d}$ with $c\neq 0$
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Biholomorphisms
  - Removable Singularities
  - Poles
relations: []
review: draft
---

::: {.problem}
Let $f(z)$ be an analytic function on $\CC \setminus \{ z_0 \}$, where $z_0$ is a fixed point.
Assume that $f(z)$ is bijective from $\CC \setminus \{ z_0 \}$ onto its image, and that $f(z)$ is bounded outside $D_r(z_0)$, where $r$ is some fixed positive number.
Show that there exist $a, b, c, d \in \CC$ with $ad-bc \neq 0$, $c \neq 0$ such that $\displaystyle f(z) = \frac{az + b}{cz + d}$.
:::

::: {.solution}

::: pf

::: {.pf-step #infinity}
$f$ has a removable singularity at $\infty$.

::: pf-proof
$f(1/w)$ is holomorphic and bounded on $0<\abs{w}<1/(\abs{z_0}+r)$, so by Riemann's removable singularity theorem it extends holomorphically over $w=0$.
:::

:::

::: {.pf-step #pole}
$f$ has a pole at $z_0$.

::: pf-proof
If $z_0$ were removable, $f$ would extend to an entire function, bounded by step [](#infinity){.pf-ref}, hence constant by Liouville's theorem, contradicting injectivity.
If $z_0$ were essential, then by the great Picard theorem $f$ would take some value infinitely often near $z_0$, contradicting injectivity.
:::

:::

::: {.pf-step #rational}
$f$ is a rational function of degree $1$.

::: pf-proof
By steps [](#infinity){.pf-ref} and [](#pole){.pf-ref}, $f$ extends to a meromorphic function on the Riemann sphere, which is a rational function $p/q$ in lowest terms.
If its degree $m=\max(\deg p,\deg q)$ were at least $2$, then all but finitely many $w\in\CC$ would have $m$ distinct preimages on the sphere, at least two of which lie in $\CC\setminus\{z_0\}$ once $w\neq f(\infty)$, contradicting injectivity.
$f$ is nonconstant, so $m=1$.
:::

:::

::: pf-step
$f(z) = \frac{az+b}{cz+d}$ with $ad-bc\neq0$ and $c\neq0$.

::: pf-proof
A rational function of degree $1$ is $\frac{az+b}{cz+d}$ with $ad-bc\neq0$.
If $c=0$, $f$ would be a polynomial of degree $1$, with no pole at $z_0$, contradicting step [](#pole){.pf-ref}.
:::

:::

:::

:::
