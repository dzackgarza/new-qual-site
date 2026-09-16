---
schema: qual/card@1
id: PR-EWOP5
kind: proposition
title: Holomorphic functions have isolated zeros
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Identity Theorem
  - Holomorphic Functions
relations: []
review: draft
---

::: {.proposition}
Let $f\colon\CC\to \CC$ be [[D-E7A5W|holomorphic]] and not identically zero.
Then the [[D-65VIK|zeros]] of $f$ are isolated: every $z_0$ with $f(z_0)=0$ has a punctured neighborhood on which $f$ has no zeros.
:::

::: {.proof}
By [[PR-5A64G]], near a zero $z_0$ we have $f(z)=(z-z_0)^ng(z)$ with $n\ge1$ and $g$ holomorphic and nonvanishing on a neighborhood $U$ of $z_0$.
For $z\in U\setminus\theset{z_0}$ both factors are nonzero, so $f(z)\neq0$.
:::
