---
schema: qual/card@1
id: P-CASP25C
kind: problem
title: "Square root of an injective holomorphic function with f(0)=0"
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Injective Functions
  - Square Roots
relations: []
review: draft
audit:
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into Lamport steps, and the audit list this card lacked is created here. The source is a course examination, so there is no retained solution set behind the card and the problem statement is the source. Each step re-read: injectivity with f(0) = 0 forces the zero to be simple, since a zero of order k >= 2 makes f k-to-1 near 0; hence f(w) = w h(w) with h holomorphic and zero-free; h(z^2) is therefore a zero-free holomorphic function on the simply connected disc, so it has a holomorphic logarithm and hence a square root; and g = z q does the job. The existence of the logarithm, which the prose asserted in one clause, is now a step with its reason. Not claimed: uniqueness of g, which holds up to sign.
---

::: {.problem}
Let $f : \DD \to \CC$ be a holomorphic function in the unit disc.
Assume $f$ is injective and $f(0) = 0$.
Prove that there exists a holomorphic function $g$ in $\DD$ such that $(g(z))^2 = f(z^2)$ for all $z \in \DD$.
:::

::: {.solution}
The argument is the card's own; the collection is a course examination, so there is no printed solution set behind the card and the problem statement is the source.

::: pf

::: {.pf-step #simple}
The zero of $f$ at $0$ is simple.

::: pf-proof
$f(0)=0$, so $f(z)=z^{k}u(z)$ near $0$ with $k\ge1$ and $u(0)\ne0$. If $k\ge2$ then $f$ takes the value $\varepsilon$ at $k$ distinct points near $0$ for each small $\varepsilon\ne0$ (the $k$-th roots of $\varepsilon/u(0)$ scaled appropriately), contradicting injectivity. Hence $k=1$.
:::

:::

::: {.pf-step #factor}
$f(w)=w\,h(w)$ with $h$ holomorphic and nowhere zero on $\DD$.

::: pf-proof
$h(w)=f(w)/w$ for $w\ne0$ extends holomorphically to $0$ because the zero there is simple; and $h$ has no other zero since $f$ is injective and $f(0)=0$ already accounts for the value $0$.
:::

:::

::: {.pf-step #compose}
$f(z^{2})=z^{2}\,h(z^{2})$, and $z\mapsto h(z^{2})$ is holomorphic and nowhere zero on $\DD$.

::: pf-proof
Substitute $w=z^{2}$ into step [](#factor){.pf-ref}; $z^{2}$ is holomorphic, and $h$ composed with it is holomorphic with values in the nonzero complex numbers, since $h$ never vanishes.
:::

:::

::: {.pf-step #log}
There is $q$ holomorphic on $\DD$ with $q(z)^{2}=h(z^{2})$.

:::: pf-proof

::: {.pf-step #logexists}
A nowhere-zero holomorphic function on the simply connected disc has a holomorphic logarithm.

::: pf-proof
On the simply connected domain $\DD$ a nowhere-zero holomorphic function has a holomorphic logarithm: the integral of $H'/H$ along a path depends only on the endpoints because $H'/H$ is holomorphic on a simply connected domain, and $\exp$ of that primitive is $H$ up to a constant, adjusted by adding a suitable constant.
:::

:::

::: {.pf-step #halves}
$q=\exp\bigl(\tfrac12\log h(z^{2})\bigr)$ satisfies $q^{2}=h(z^{2})$.

::: pf-proof
Let $L$ be a holomorphic logarithm of $z\mapsto h(z^{2})$, which exists by step [](#logexists){.pf-ref} applied to that composite, and put $q=e^{L/2}$; then $q^{2}=e^{L}=h(z^{2})$, and $q$ is holomorphic.
:::

:::

:::

:::

::: {.pf-step}
$g(z)=z\,q(z)$ satisfies $g(z)^{2}=f(z^{2})$.

::: pf-proof
$g$ is holomorphic on $\DD$ as a product of holomorphic functions, and by steps [](#compose){.pf-ref} and [](#log){.pf-ref},
$$
g(z)^{2}=z^{2}q(z)^{2}=z^{2}h(z^{2})=f(z^{2}),
$$
so
$$
\boxed{\exists g\in H(\DD)\text{ with }g(z)^{2}=f(z^{2})\text{ for all }z\in\DD.}
$$
Simplicity of the zero at $0$ is exactly what makes $h$ holomorphic at $0$; injectivity of $f$ is what supplies it.
:::

:::

:::
:::
