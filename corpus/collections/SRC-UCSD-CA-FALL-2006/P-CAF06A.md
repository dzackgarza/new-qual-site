---
schema: qual/card@1
id: P-CAF06A
kind: problem
title: "An analytic function on the disk with unit modulus on the boundary is rational"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
If $f(z)$ is analytic in $\abs{z} < 1$, continuous on $\abs{z} \leq 1$ and satisfies $\abs{f} = 1$ on $\abs{z} = 1$, show that $f(z)$ is rational.

Hint: First consider the case that $f(z)$ has no zero.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own Blaschke-product argument follows, with the finiteness of the zeros, the factorisation, the two maximum-modulus applications and the conclusion as separate steps.

Let $f$ be analytic in $\DD$, continuous on $\overline{\DD}$, with $\abs{f}=1$ on $\abs{z}=1$.

::: pf

::: {.pf-step #zeros}
$f$ has only finitely many zeros in $\DD$.

::: pf-proof
By continuity and $\abs{f}=1$ on the circle there is a neighbourhood of $\abs{z}=1$ on which $\abs{f}\ge\tfrac12$, so $f$ has no zeros there; hence the zero set of $f$ in $\overline{\DD}$ is a closed subset of a compact disc $\abs{z}\le r$ with $r<1$. Zeros of a non-identically-zero analytic function are isolated, and an isolated-point set that is compact is finite, so there are finitely many zeros $a_{1},\dots,a_{m}$, listed with multiplicity. (If $f\equiv0$ the condition $\abs{f}=1$ on the circle fails, so this case does not arise.)
:::

:::

::: {.pf-step #blaschke}
With $B(z)=\prod_{j\le m}\dfrac{z-a_{j}}{1-\overline{a_{j}}z}$: $B$ is rational, holomorphic on $\overline{\DD}$ with no poles there, has zero set exactly $\theset{a_{j}}$ with multiplicities, and $\abs{B}=1$ on $\abs{z}=1$.

::: pf-proof
For $\abs{a}<1$ the denominator $1-\bar a z$ does not vanish for $\abs{z}\le1$ because $\abs{\bar a z}\le\abs{a}<1$, so $B$ is holomorphic on $\overline{\DD}$; its zeros are the $a_{j}$ with the listed multiplicities. On $\abs{z}=1$, $\abs{z-a}=\abs{\bar z z-\bar z a}=\abs{1-\bar a z}$, so each factor has modulus $1$.
:::

:::

::: {.pf-step #quotient}
$h=f/B$ extends to a holomorphic zero-free function on a neighbourhood of $\overline{\DD}$, with $\abs{h}=1$ on $\abs{z}=1$.

::: pf-proof
Near each $a_{j}$ both $f$ and $B$ vanish to the same order, so the quotient extends holomorphically and without zeros across $a_{j}$; elsewhere in $\overline{\DD}$ we have $B\ne0$, so $h$ is holomorphic, and $h\ne0$ because $f$'s zeros are exactly those of $B$. On the circle $\abs{h}=\abs{f}/\abs{B}=1/1=1$.
:::

:::

::: {.pf-step #constant}
$h$ is constant.

::: pf-proof
$\abs{h}\le1$ on $\DD$ by the maximum modulus principle applied to $h$ on the disc. Since $h$ is zero-free, $1/h$ is holomorphic, and the same argument applied to $1/h$ (whose boundary modulus is also $1$) gives $\abs{h}\ge1$. So $\abs{h}=1$ on the disc, and $h$ maps the disc into the circle, which has empty interior; by the open mapping theorem $h$ is constant, $h\equiv c$ with $\abs{c}=1$.
:::

:::

::: {.pf-qed}
$f=cB$ by step [](#constant){.pf-ref}, so $f(z)=c\prod_{j\le m}\dfrac{z-a_{j}}{1-\overline{a_{j}}z}$ is a rational function.
:::

:::

:::
