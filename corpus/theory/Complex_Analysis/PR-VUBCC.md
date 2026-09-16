---
schema: qual/card@1
id: PR-VUBCC
kind: proposition
title: Zeros of holomorphic functions are isolated
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Holomorphic Functions
relations: []
review: draft
---

::: {.proposition}
Let $f\colon D_r(a)\to\CC$ be [[D-E7A5W|holomorphic]] and not identically zero.
Then there exists $0<\rho<r$ such that $f(z)\neq0$ for all $z\in D_\rho(a)\sm\ts{a}$.
:::

::: {.proof}
If $f(a)\neq0$, continuity of $f$ gives a disc about $a$ on which $f$ does not vanish.
Otherwise $f(a)=0$. Since $f$ is represented by its Taylor series on $D_r(a)$ and is not identically zero, some Taylor coefficient is nonzero, so $a$ is a [[D-65VIK|zero]] of some finite order $N\ge1$: $f(z)=(z-a)^Ng(z)$ with $g$ holomorphic on $D_r(a)$ and $g(a)\neq0$.
By continuity, $g$ does not vanish on some disc $D_\rho(a)$, and then $f$ does not vanish on $D_\rho(a)\sm\ts{a}$.
:::
