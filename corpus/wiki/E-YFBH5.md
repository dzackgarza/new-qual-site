---
schema: qual/card@1
id: E-YFBH5
kind: exercise
title: Analytic self-maps of the disc with a zero of order $k$ at $0$ and $|f|\to
  1$ at the boundary
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
solved: true
---

:::{.problem title="?"}
Suppose $f:\DD\to\DD$ is analytic, has a single zero of order $k$ at $z=0$, and satisfies $\lim_{\abs z \to 1} \abs{f(z)} = 1$.
Give with proof a formula for $f(z)$.
:::

:::{.solution}
Note $\abs{f(z)}\leq 1$, and $g\da f(z)/z^k$ has a removable singularity at zero since $g$ is bounded on $\DD$: fixing $\abs{z} = r < 1$,
\[
\abs{g(z)} = \abs{f(z)\over z^k} = \abs{f(z)}r^{-k}\leq r^{-k}\convergesto{r\to 1} 1
.\]
So $g:\DD\to \DD$ since $\abs{g(z)}\leq 1$ on $\DD$ by the MMP.
Since $g$ has no zeros on $\DD$, by the MMP $\abs{g} \geq 1$ on $\DD$, so $\abs{g} = 1$ is constant, making $g(z) = \lambda z$ a rotation.
Then $f(z) = \lambda z^n$.

> Alternative to MMP: if $g$ has no zeros in $\DD$, $g$ admits a conjugate reflection through $\DD$ by $z\mapsto 1/\bar{f(1/\bar z)}$. This is bounded and entire, thus constant, making $g$ constant.

:::
