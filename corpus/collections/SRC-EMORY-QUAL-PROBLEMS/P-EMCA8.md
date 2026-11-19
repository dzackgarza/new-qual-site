---
schema: qual/card@1
id: P-EMCA8
kind: problem
title: Weierstrass's theorem on locally uniform limits of holomorphic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
  - Holomorphic Functions
  - Morera
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Complex Analysis (8) of Arango-Piñeros, Some quals problems; merged the duplicate E-YMM6X, whose solution repeats this Morera and Cauchy-estimate argument."
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps. The collection is a qualifying examination, so the problem
    statement is the source and the argument is the card's own. Each step re-read: a locally uniform
    limit of continuous functions is continuous; the integrals over the boundary of a closed
    triangle pass to the limit because the boundary is compact, and each vanishes by Cauchy's
    theorem; Morera gives holomorphy; and the derivative estimate comes from Cauchy's formula for
    the derivative on a circle of radius r about each point of K, with r chosen so that the closed
    neighbourhood of K stays in D, which makes the bound independent of the point. The existence of
    such an r is now a step with its reason, distance to the complement being positive and attained
    on a compact set. Not claimed: any statement about derivatives of higher order, which follow by
    iteration but are not asked for.
---

::: {.problem}
Let $(f_n)$ be a sequence of holomorphic functions in a domain $D$.
Suppose that $f_n \to f$ uniformly on each compact subset of $D$.
Show that

(a) $f$ is holomorphic on $D$.

(b) $f_n' \to f'$ uniformly on each compact subset of $D$.
:::

::: {.solution}
The argument is the card's own; the collection is a qualifying examination, so the problem statement is the source.

::: pf

::: {.pf-step #continuity}
$f$ is continuous on $D$.

::: pf-proof
Each $f_{n}$ is holomorphic, hence continuous, and $f_{n}\to f$ uniformly on compact subsets; a locally uniform limit of continuous functions is continuous.
:::

:::

::: {.pf-step #morera}
$\int_{\partial T}f(z)\,dz=0$ for every closed triangle $T\subset D$.

::: pf-proof
$\partial T$ is compact, so $f_{n}\to f$ uniformly on it by hypothesis, and then the integrals converge:
$$
\int_{\partial T}f=\lim_{n}\int_{\partial T}f_{n}.
$$
Each $\int_{\partial T}f_{n}=0$ by Cauchy's theorem, since $f_{n}$ is holomorphic on a domain containing the closed triangle; hence the limit is $0$.
:::

:::

::: {.pf-step #holomorphic}
$f$ is holomorphic on $D$.

::: pf-proof
$f$ is continuous on $D$ by step [](#continuity){.pf-ref} and its integral over the boundary of every closed triangle in $D$ vanishes by step [](#morera){.pf-ref}; Morera's theorem then gives that $f$ is holomorphic.
:::

:::

::: {.pf-step #neighbourhood}
For compact $K\subset D$ there is $r>0$ with $K_{r}=\{z:\operatorname{dist}(z,K)\le r\}$ compact and contained in $D$.

::: pf-proof
Distances from $K$ to the boundary of $D$ are positive and attained, because $K$ is compact and $D$ is open, so $r=\tfrac12\operatorname{dist}(K,\partial D)>0$ works; $K_{r}$ is closed and bounded, hence compact, and lies in $D$.
:::

:::

::: {.pf-step #cauchy}
$\abs{f_{n}'(z)-f'(z)}\le\dfrac1r\sup_{K_{r}}\abs{f_{n}-f}$ for every $z\in K$.

::: pf-proof
For $z\in K$ the circle $\abs{\zeta-z}=r$ lies in $K_{r}\subset D$, and Cauchy's formula for the derivative of the holomorphic function $f_{n}-f$ on that circle gives
$$
f_{n}'(z)-f'(z)=\frac{1}{2\pi i}\int_{\abs{\zeta-z}=r}\frac{f_{n}(\zeta)-f(\zeta)}{(\zeta-z)^{2}}\,d\zeta .
$$
Estimating the integral gives $\frac{1}{2\pi}\cdot2\pi r\cdot\frac{\sup_{K_{r}}\abs{f_{n}-f}}{r^{2}}=\frac1r\sup_{K_{r}}\abs{f_{n}-f}$.
:::

:::

::: {.pf-step #uniform}
$f_{n}'\to f'$ uniformly on $K$, for every compact $K$.

::: pf-proof
The bound in step [](#cauchy){.pf-ref} is independent of $z\in K$, and its right-hand side tends to $0$ as $n\to\infty$ because $f_{n}\to f$ uniformly on the compact set $K_{r}$. So the left-hand side tends to $0$ uniformly on $K$:
$$
\boxed{f\text{ holomorphic},\qquad f_{n}'\to f'\text{ uniformly on compact subsets of }D.}
$$
Parts (a) and (b) are steps [](#holomorphic){.pf-ref} and this one; the shrinking by $r$ into $K_{r}$ is what makes the derivative estimate uniform on $K$.
:::

:::

:::
:::
