---
schema: qual/card@1
id: D-QTJ7T
kind: definition
title: Normal family
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

::: {.definition}
Let $\Omega\subseteq\CC$ be open.
A family $\mathcal F$ of [[D-E7A5W|holomorphic]] functions on $\Omega$ is \dfn{normal} if every sequence in $\mathcal F$ has a subsequence converging uniformly on every compact subset of $\Omega$.
:::

::: {.remark}
The limit of such a subsequence need not lie in $\mathcal F$: normality says that $\mathcal F$ is precompact in the topology of [[D-AIQG3|locally uniform convergence]], and $\mathcal F$ is compact in that topology exactly when, in addition, every such limit lies in $\mathcal F$.
:::

::: {.remark}
In the proof of the Riemann mapping theorem for a simply connected open set $\Omega\subsetneq\CC$ and $z_0\in\Omega$, one maximizes $\abs{f'(z_0)}$ over the injective holomorphic maps $f\colon\Omega\to\DD$ with $f(z_0)=0$.
This family is uniformly bounded, hence normal by Montel's theorem, so a maximizing sequence has a locally uniformly convergent subsequence, whose limit is the candidate Riemann map.
:::

::: {.remark}
Two conventions are in use and they are not equivalent.
Stein and Shakarchi require a locally uniformly convergent subsequence, as in the definition.
Ahlfors instead calls a family normal if every sequence has a subsequence that either converges uniformly on compact sets or tends uniformly to $\infty$ on compact sets; this is convergence in the spherical metric on the Riemann sphere, and it applies unchanged to families of meromorphic functions.
:::

::: {.example}
The family $\{f_n\}_{n\ge1}$ with $f_n(z)=n(z^2-n)$ on $\CC$ is normal in Ahlfors' sense and not in Stein and Shakarchi's.
On $\abs{z}\le R$ and for $n>R^2$, $\abs{f_n(z)}\ge n^2-nR^2\to\infty$ uniformly, so every subsequence tends uniformly to $\infty$ on compact sets and none converges uniformly on compact sets to a finite function.
:::

::: {.concept}
See [@SS03], and Theorem 3.3 there for Montel's theorem.
Ahlfors' convention and the example $n(z^2-n)$ are in [@Ahl79].
:::
