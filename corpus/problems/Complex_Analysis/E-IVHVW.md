---
schema: qual/card@1
id: E-IVHVW
kind: problem
title: A self-map of $\DD$ is bounded by the Blaschke product of its zeros
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Schwarz Lemma
  - Zeros
  - Maximum Modulus Principle
relations: []
review: draft
---

::: {.exercise}
Let $f: \DD\to \DD$ with $\ts{a_k}_{k\leq n}$ the zeros of $f$ in $\DD$.
Show that
\[
\abs{f(z)}\leq \prod_{k\leq n} \abs{ \psi_{a_k}(z) }
.\]

:::

::: {.solution}
Here $\psi_a(z)\da{a-z\over1-\bar az}$, and the zeros $a_k$ are listed with multiplicity.
Define $\Psi(z) \da \prod_{k\leq n} \psi_{a_k}(z)$ and $g(z) \da f(z)/\Psi(z)$.
Each zero of $\Psi$ in $\DD$ is a zero of $f$ of at least the same order, so $g$ has removable singularities and is holomorphic on $\DD$.
The claim is that $\abs{g(z)} \leq 1$, which implies the result directly.
Since $\Psi$ is continuous on $\overline\DD$ with $\abs{\Psi} = 1$ on $\abs{z} = 1$, $m(r)\da\min_{\abs z=r}\abs{\Psi(z)}\to1$ as $r\to1^-$.
Fix $z\in\DD$. For $\abs z<r<1$ close enough to $1$ that $m(r)>0$, the maximum modulus principle on $\abs\zeta\le r$ gives
\[
\abs{g(z)}\le\max_{\abs\zeta=r}\abs{g(\zeta)} = \max_{\abs\zeta=r}{ \abs{f(\zeta)} \over \abs{\Psi(\zeta)} } \leq {1\over m(r)} \convergesto{r\to 1^-} 1
.\]
:::
