---
schema: qual/card@1
id: D-QTJ7T
kind: definition
title: Normal Family
classification:
  areas:
  - complex-analysis
  topics:
  - Normal Families
relations:
- kind: related-to
  target: D-VZNMF
review: draft
---

::: {.definition title="Normal Family"}
Let $\Omega \subseteq \CC$ be open.
A family $\mcf$ of holomorphic functions on $\Omega$ is **normal** iff every sequence in $\mcf$ has a subsequence converging uniformly on every compact subset of $\Omega$.
The limit need not lie in $\mcf$: normality is precompactness of $\mcf$ in the topology of locally uniform convergence, not compactness.

This is what makes the Riemann mapping theorem's extremal argument work: one maximizes $\abs{f'(z_0)}$ over the injective maps $\Omega \to \DD$ fixing $z_0$, and normality is what supplies a limit of a maximizing sequence.
:::

::: {.remark}
Two conventions are in use and they are not equivalent.
Stein and Shakarchi require a locally uniformly convergent subsequence, as above.
Ahlfors instead calls a family normal iff every sequence has a subsequence that either converges uniformly on compact sets **or** tends uniformly to $\infty$ on compact sets, which is convergence in the spherical metric on the Riemann sphere and lets the definition cover meromorphic families unchanged.
The family $\ts{f_n(z) = n(z^2 - n)}$ on $\CC$ is normal in Ahlfors' sense and not in Stein and Shakarchi's.
:::

::: {.concept}
See Stein and Shakarchi, *Complex Analysis*, ch. 8, §3.2, p. 225, and Theorem 3.3 there for Montel's theorem.
Ahlfors' convention is *Complex Analysis*, ch. 5, §4.5 (The Classical Definition), Definition 3; the family $n(z^2-n)$ is his own example there.
:::
