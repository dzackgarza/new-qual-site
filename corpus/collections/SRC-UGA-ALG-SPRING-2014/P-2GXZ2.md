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
Let $R$ be a commutative ring and $a\in R$.
Prove that $a$ is not nilpotent $\iff$ there exists a commutative ring $S$ and a ring homomorphism $\phi: R\to S$ such that $\phi(a)$ is a unit.

> Note: by definition, $a$ is nilpotent $\iff$ there is a natural number $n$ such that $a^n = 0$.
:::

::: {.solution}
<1>1. As printed, the equivalence fails if the zero ring is permitted as $S$.

::: {.proof}
The unique homomorphism $R\to0$ sends every $a\in R$ to $0=1$, which is a unit of the zero ring. For example, $a=0\in\mathbb Z$ is nilpotent but satisfies the stated existence condition with $S=0$. The equivalence therefore requires $S$ to be a nonzero ring.
:::

<1>2. If $a$ is nilpotent, its image under no ring homomorphism to a nonzero ring is invertible.

::: {.proof}
If $a^m=0$ and $\phi:R\to S$ is a homomorphism, then $\phi(a)^m=0$. If $\phi(a)$ were a unit, multiplying by its inverse power would give $1_S=0_S$, contradicting $S\neq0$.
:::

<1>3. If $a$ is not nilpotent, there exists a homomorphism to a nonzero commutative ring in which its image is a unit:
\[
\boxed{\phi:R\longrightarrow R[a^{-1}]}.
\]

::: {.proof}
Set $T=\{1,a,a^2,\ldots\}$. The hypothesis implies $0\notin T$. Hence the localization $R[T^{-1}]$ is nonzero: if $1/1=0/1$, the localization equality criterion would give some $t\in T$ with $t=0$. The canonical homomorphism $\phi:R\to R[T^{-1}]$ sends $a$ to $a/1$, whose inverse is $1/a$. This provides the required ring $S=R[T^{-1}]$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 identifies the necessary nonzero-ring hypothesis. Under that hypothesis, steps <1>2 and <1>3 prove the two directions of the equivalence.
:::
:::
