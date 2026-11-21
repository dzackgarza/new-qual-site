---
schema: qual/card@1
id: P-CASP19E
kind: problem
title: 'Partial sums of $\sum_{n\geq 1} f^{(n)}(z)/n!$ converge in $H(\DD)$ for $f$ holomorphic on $B(0,2)$'
classification:
  areas:
  - complex-analysis
  topics:
  - Taylor Series
  - Uniform Convergence
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Let $f$ be an analytic function in $B(0, 2)$.
Prove the sequence $g_N(z) := \sum_{n=1}^{N} \frac{f^{(n)}(z)}{n!}$, $N \geq 1$, converges in the space $H(\DD)$ of analytic functions on $\DD$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, with the choice of $r$, the Cauchy estimate and the conclusion as separate steps.

Let $f$ be analytic in $B(0,2)$ and $g_{N}(z)=\sum_{n=1}^{N}\frac{f^{(n)}(z)}{n!}$.

::: pf

::: {.pf-step #radius}
For $K\Subset\DD$ there is $r$ with $1<r<2-\sup_{z\in K}\abs{z}$, and then the closed disc $\overline{B(z,r)}$ lies in $B(0,2)$ for every $z\in K$.

::: pf-proof
$K$ is compact, so $\rho=\sup_{z\in K}\abs{z}<1$; take any $r$ with $1<r<2-\rho$, which exists because $2-\rho>1$. For $z\in K$ and $\abs{\zeta-z}\le r$ one has $\abs{\zeta}\le\abs{z}+r\le\rho+r<2$, so $\zeta\in B(0,2)$.
:::

:::

::: {.pf-step #cauchy}
With $M=\sup\theset{\abs{f(\zeta)}\mid\dist(\zeta,K)\le r}<\infty$ one has $\dfrac{\abs{f^{(n)}(z)}}{n!}\le\dfrac{M}{r^{n}}$ for every $z\in K$ and $n\ge1$.

::: pf-proof
$f$ is continuous on the compact set $\theset{\zeta\mid\dist(\zeta,K)\le r}\subseteq B(0,2)$, so $M<\infty$. The Cauchy estimates for the disc $B(z,r)$, which lies in the domain of $f$ by step [](#radius){.pf-ref}, give $\abs{f^{(n)}(z)}\le\dfrac{n!\,M_{z}}{r^{n}}$ with $M_{z}=\sup_{\abs{\zeta-z}=r}\abs{f(\zeta)}\le M$.
:::

:::

::: {.pf-step #uniform}
$\sum_{n\ge1}\dfrac{f^{(n)}(z)}{n!}$ converges uniformly on $K$.

::: pf-proof
By step [](#cauchy){.pf-ref} the $n$-th term is bounded by $Mr^{-n}$ with $r>1$, and $\sum_{n\ge1}Mr^{-n}=M\frac{r^{-1}}{1-r^{-1}}<\infty$; the Weierstrass $M$-test gives uniform convergence on $K$.
:::

:::

::: {.pf-qed}
Every compact $K\Subset\DD$ is contained in the interior of a compact subset of $\DD$ on which the series converges uniformly, so $(g_{N})$ converges locally uniformly on $\DD$; by Weierstrass' theorem the limit is holomorphic, so $g_{N}$ converges in $H(\DD)$.
:::

:::

:::
