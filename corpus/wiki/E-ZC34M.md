---
schema: qual/card@1
id: E-ZC34M
kind: exercise
title: A holomorphic function attaining a minimum of $|f|$ vanishes there or is constant
classification:
  areas:
  - complex-analysis
  topics:
  - maximum-modulus-principle
  - zeros
relations: []
review: draft
solved: true
---

::: {.exercise title="?"}
Let $f: \Omega\to \CC$ be holomorphic and suppose there is a $z_0 \in \Omega$ with $\abs{f(z_0)}\leq \abs{f(z)}$ for all $z\in \Omega$.
Show that either $f(a) = 0$ or $f$ is constant.
:::

::: {.solution}
Suppose $f(z_0)\neq 0$, then the inequality forces there to be no zeros in $\Omega$.
So $g(z) \da 1/f(z)$ is nonzero and holomorphic on $\Omega$ and $\abs{g(z)}\leq \abs{1\over f(z_0)} \da \abs{g(z_0)}$.
Since $z_0\in \Omega$, the MMP forces $g$ to be constant, and thus so is $f$.
:::
