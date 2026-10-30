---
schema: qual/card@1
id: P-BKS06-8A
kind: problem
title: A holomorphic function on the disk injective off the origin is injective
classification:
  areas: [prelim]
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $D = \{ z \in \CC : \abs{ z } < 1 \}$ . Let $f \colon D \to \CC$ be holomorphic, and suppose that the restriction of $f$ to $D - \{ 0 \}$ is injective.
Prove that $f$ is injective.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$f$ is not constant.

::: pf-proof

$D-\{0\}$ has more than one point, and $f$ is injective on it.

:::

:::

::: {.pf-step #s2}

There is no $a\in D-\{0\}$ with $f(a)=f(0)$.

::: pf-proof

Suppose there is such an $a$, and let $\alpha=f(0)=f(a)$. Choose disjoint open disks $D_0$ and $D_a$ in $D$, centered at $0$ and $a$. By step [](#s1){.pf-ref} and the open mapping theorem, $f(D_0)$ and $f(D_a)$ are open sets that contain $\alpha$, so $G=f(D_0)\cap f(D_a)$ is an open neighborhood of $\alpha$. Choose $\xi\in G$ with $\xi\ne\alpha$, and choose $z_0\in D_0$ and $z_a\in D_a$ with $f(z_0)=f(z_a)=\xi$. Since $\xi\ne\alpha=f(0)$, neither point is $0$, and $z_0\ne z_a$ because the disks are disjoint. This contradicts the injectivity of $f$ on $D-\{0\}$.

:::

:::

::: pf-qed

Two distinct points of $D$ are either both in $D-\{0\}$, where $f$ is injective, or one of them is $0$, which step [](#s2){.pf-ref} handles. So $f$ is injective.

:::

:::

:::
