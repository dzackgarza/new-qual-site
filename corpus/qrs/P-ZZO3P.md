---
schema: qual/card@1
id: P-ZZO3P
kind: problem
title: "Prove the Fundamental Theorem of Algebra (using complex\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - liouville-s-theorem
  - polynomials
  - zeros
  - entire-functions
relations: []
review: draft
---
Prove the Fundamental Theorem of Algebra (using complex analysis).

:::{.solution}
\hfill
:::{.concept}
\hfill

:::
- Strategy: By contradiction with Liouville's Theorem
- Suppose $p$ is non-constant and has no roots.
- Claim: $1/p(z)$ is a bounded holomorphic function on $\CC$.
  - Holomorphic: clear? Since $p$ has no roots.
  - Bounded: for $z\neq 0$, write
    \begin{align*}
    \frac{P(z)}{z^{n}}=a_{n}+\left(\frac{a_{n-1}}{z}+\cdots+\frac{a_{0}}{z^{n}}\right)
    .\end{align*}

  - The term in parentheses goes to 0 as $\abs{z}\to \infty$
  - Thus there exists an $R>0$ such that
    \begin{align*}
    \abs{z} > R \implies \abs{P(z) \over z^n} \geq c \definedas {\abs{a_n} \over 2}
    .\end{align*}

  - So $p$ is bounded below when $\abs{z} > R$
  - Since $p$ is continuous and has no roots in $\abs{z} \leq R$, it is bounded below when $\abs{z} \leq R$.
  - Thus $p$ is bounded below on $\CC$ and thus $1/p$ is bounded above on $\CC$.
- By Liouville's theorem, $1/p$ is constant and thus $p$ is constant, a contradiction.
:::
