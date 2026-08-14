---
schema: qual/card@1
id: C-FVT4V
kind: corollary
title: "Injective implies holomorphic inverse"
classification:
  areas:
  - complex-analysis
  topics:
  - biholomorphisms
  - conformal-maps
relations: []
review: draft
---

::: {.corollary title="Injective implies holomorphic inverse"}
If $f: U\to V$ is holomorphic and injective, then $f'(z) \neq 0$ for every $z\in U$.
The inverse defined on the range of $f$ is therefore holomorphic, so the inverse of a conformal map is conformal.
:::

::: {.remark}
Stein and Shakarchi, *Complex Analysis*, ch. 8 Proposition 1.1.
The nonvanishing of $f'$ is the content; injectivity alone gives a set-theoretic inverse and nothing more.
The converse fails: $f(z) = e^z$ has $f' = e^z$ nowhere zero on $\CC$ and is not injective.
:::
