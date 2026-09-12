---
schema: qual/card@1
id: P-ALGS15D
kind: problem
title: PID characterization via submodules of free modules
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Let $R$ be an integral domain.
Prove that $R$ is a PID if and only if every submodule of a finitely generated free $R$-module is again free.
:::

::: {.solution}
We prove both implications.

<1>1. Suppose every submodule of every finitely generated free $R$-module is free.
Then every ideal of $R$ is principal.
::: {.proof}
Let $I\subseteq R$ be an ideal.
Since $R$ is free of rank $1$, the hypothesis implies that $I$ is a free $R$-module.
Because $I\subseteq R$ and $R$ is an integral domain, $\operatorname{rank}_R I\le 1$: indeed, after tensoring with the fraction field $K=\operatorname{Frac}(R)$, the inclusion $I\hookrightarrow R$ gives an inclusion $K\otimes_R I\hookrightarrow K$, so $\dim_K(K\otimes_R I)\le1$.
If $I=0$, then $I=(0)$.
Otherwise $I$ has rank $1$, hence $I=Ra$ for some basis element $a\in I$.
Thus every ideal is principal, so $R$ is a PID.
:::

<1>2. Conversely, suppose $R$ is a PID. We prove by induction on $n$ that every submodule of $R^n$ is free.
::: {.proof}
For $n=0$ the statement is trivial.
Assume it for $R^{n-1}$ and let $M\subseteq R^n$ be a submodule.
:::

<2>1. Let $\pi:R^n\to R$ be projection to the last coordinate.
Then $\ker(\pi|_M)$ is free.
::: {.proof}
We have
\[
\ker(\pi|_M)=M\cap(R^{n-1}\times\{0\}),
\]
which identifies with a submodule of $R^{n-1}$.
It is free by the induction hypothesis.
:::

<2>2. The image $\pi(M)$ is free of rank at most $1$.
::: {.proof}
The image is an ideal of the PID $R$, hence is principal.
Therefore $\pi(M)$ is either $0$ or isomorphic to $R$ as an $R$-module, so it is free.
:::

<2>3. The short exact sequence
\[
0\longrightarrow \ker(\pi|_M)\longrightarrow M\xrightarrow{\pi}\pi(M)\longrightarrow0
\]
splits.
::: {.proof}
The module $\pi(M)$ is free by <2>2, hence projective.
Therefore the surjection $M\to\pi(M)$ admits an $R$-linear section.
:::

<2>4. Hence $M$ is free.
::: {.proof}
By <2>3,
\[
M\cong \ker(\pi|_M)\oplus \pi(M).
\]
Both summands are free by <2>1 and <2>2, and their direct sum is free.
This completes the induction.
:::

<1>3. Therefore $R$ is a PID if and only if every submodule of a finitely generated free $R$-module is free.
::: {.proof}
The forward implication is <1>2 and the reverse implication is <1>1.
:::
:::
