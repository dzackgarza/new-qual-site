---
schema: qual/card@1
id: E-IVHVW
kind: exercise
title: Bounded above by Blaschke product
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

:::{.exercise}
Let $f: \DD\to \DD$ with $\ts{a_k}_{k\leq n}$ the zeros of $f$ in $\DD$.
Show that
\[
\abs{f(z)}\leq \prod_{k\leq n} \abs{ \psi_{a_k}(z) }
.\]

:::

:::{.solution}
Define $\Psi(z) \da \prod_{k\leq n} \psi_{a_k}(z)$ and $g(z) \da f(z)/\Psi(z)$.
The claim is that $\abs{g(z)} \leq 1$, which implies the result directly.
Note that $\abs{\Psi(z)} = 1$ for $\abs{z} = 1$, so $\lim_{r\to 1^-} \abs{\Psi(re^{it})} = 1$ along any ray.
Now for $z_r \da re^{it}$ for $r< 1$,
\[
\abs{g(z_r)} = { \abs{f(z_r)} \over \abs{\Psi(z_r)} } \leq {1\over \abs{\Psi(z_r)} } \leq {1\over \displaystyle\sup_{t\in [0, 2\pi]} \abs{\Psi(z_r) } } \convergesto{r\to 1^-} 1
.\]
:::
