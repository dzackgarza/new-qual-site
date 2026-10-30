---
schema: qual/card@1
id: P-2GXZ2
kind: problem
title: $a\in R$ is not nilpotent if and only if $\phi(a)$ is a unit for some ring
  homomorphism $\phi:R\to S$
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Localization
  - Rings
relations: []
review: draft
---

::: {.problem}
All rings have a multiplicative identity different from zero, and ring homomorphisms send $1$ to $1$. Let $R$ be a commutative ring and $a\in R$.
Prove that $a$ is not nilpotent $\iff$ there exists a commutative ring $S$ and a ring homomorphism $\phi: R\to S$ such that $\phi(a)$ is a unit.

> Note: by definition, $a$ is nilpotent $\iff$ there is a natural number $n$ such that $a^n = 0$.
:::

::: {.solution}

::: pf

::: {.pf-step #nil}

If $a$ is nilpotent, then $\phi(a)$ is not a unit for any ring homomorphism $\phi:R\to S$.

::: pf-proof

Let $a^m=0$. Then $\phi(a)^m=\phi(a^m)=0$. If $\phi(a)t=1$ for some $t\in S$, then $1=(\phi(a)t)^m=\phi(a)^mt^m=0$ in the commutative ring $S$, contradicting $1\neq0$ in $S$.

:::

:::

::: {.pf-step #loc}

If $a$ is not nilpotent, then the localization $\phi:R\to S=R[a^{-1}]$ makes $\phi(a)$ a unit.

::: pf-proof

Let $A=\{1,a,a^2,\ldots\}$, a multiplicative set, and let $S=A^{-1}R$ with $\phi(r)=r/1$. Then $(a/1)(1/a)=a/a=1$, so $\phi(a)$ is a unit. The ring $S$ is nonzero: $1/1=0/1$ would mean $a^k\cdot1=0$ for some $k$, which is false because $a$ is not nilpotent.

:::

:::

::: pf-qed

Steps [](#nil){.pf-ref} and [](#loc){.pf-ref} prove the two implications.

:::

:::

:::
