---
schema: qual/card@1
id: P-HCAX2
kind: problem
title: Picard's theorem from the modular invariant
classification:
  areas:
  - complex-analysis
  topics:
  - Picard
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Prove Picard's theorem using the fact that the modular invariant $j$ uniformizes the hyperbolic triangle of type $(2,3,\infty)$ by the upper half-plane.
:::

::: {.solution}
We prove the little Picard theorem: an entire function omitting two values of
$\CC$ is constant. Let $J=j/1728$, let $\rho=e^{2\pi i/3}$, and let
$\mathbb H$ be the upper half-plane.

<1>1. Let $\mathbb H'=\mathbb H\setminus\operatorname{PSL}_2(\ZZ)\{i,\rho\}$.
Then $J\colon\mathbb H'\to\CC\setminus\{0,1\}$ is a holomorphic covering map.

::: {.proof}
The given uniformization says that $J$ identifies
$\operatorname{PSL}_2(\ZZ)\backslash\mathbb H$ with $\CC$, with $J(\rho)=0$,
$J(i)=1$, and ramification of order $3$ over $0$ and order $2$ over $1$. The
group $\operatorname{PSL}_2(\ZZ)$ acts properly discontinuously on
$\mathbb H$, and the points with nontrivial stabilizer are exactly the orbits
of $i$ and $\rho$. It therefore acts freely and properly discontinuously on
$\mathbb H'$, so the quotient map $\mathbb H'\to\CC\setminus\{0,1\}$ is a
covering map.
:::

<1>2. It suffices to treat an entire $f$ with $f(\CC)\subseteq\CC\setminus\{0,1\}$.

::: {.proof}
If $f$ omits $a\ne b$, then $(f-a)/(b-a)$ is entire, omits $0$ and $1$, and is
constant exactly when $f$ is.
:::

<1>3. There is a holomorphic $\tilde f\colon\CC\to\mathbb H$ with
$J\circ\tilde f=f$.

::: {.proof}
$\CC$ is simply connected and locally path-connected, so $f$ lifts through the
covering map of step <1>1 to a continuous $\tilde f\colon\CC\to\mathbb H'$.
The covering map is a local biholomorphism, so $\tilde f$ is holomorphic.
:::

<1>4. $f$ is constant.

::: {.proof}
With the Cayley transform $C(\zeta)=(\zeta-i)/(\zeta+i)$, which maps
$\mathbb H$ onto $\DD$, the entire function $C\circ\tilde f$ is bounded, hence
constant by Liouville's theorem. Since $C$ is injective, $\tilde f$ is
constant, and so is $f=J\circ\tilde f$.
:::
:::
