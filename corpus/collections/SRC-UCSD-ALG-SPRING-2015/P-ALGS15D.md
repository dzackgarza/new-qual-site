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

::: {.problem}
Let $R$ be an integral domain.
Prove that $R$ is a PID if and only if every submodule of a finitely generated free $R$-module is again free.
:::

::: {.solution}
We prove both implications.

::: pf

::: {.pf-step #s1}

Suppose every submodule of every finitely generated free $R$-module is free.
Then every ideal of $R$ is principal.

::: pf-proof

Let $I\subseteq R$ be an ideal.
Since $R$ is free of rank $1$, the hypothesis implies that $I$ is a free $R$-module.
Because $I\subseteq R$ and $R$ is an integral domain, $\operatorname{rank}_R I\le 1$: indeed, after tensoring with the fraction field $K=\operatorname{Frac}(R)$, the inclusion $I\hookrightarrow R$ gives an inclusion $K\otimes_R I\hookrightarrow K$, so $\dim_K(K\otimes_R I)\le1$.
If $I=0$, then $I=(0)$.
Otherwise $I$ has rank $1$, hence $I=Ra$ for some basis element $a\in I$.
Thus every ideal is principal, so $R$ is a PID.

:::

:::

::: {.pf-step #s2}

Conversely, suppose $R$ is a PID. We prove by induction on $n$ that every submodule of $R^n$ is free.

::: pf-proof

For $n=0$ the statement is trivial.
Assume it for $R^{n-1}$ and let $M\subseteq R^n$ be a submodule.

::: {.pf-step #s2-1}

Let $\pi:R^n\to R$ be projection to the last coordinate.
Then $\ker(\pi|_M)$ is free.

::: pf-proof

We have
\[
\ker(\pi|_M)=M\cap(R^{n-1}\times\{0\}),
\]
which identifies with a submodule of $R^{n-1}$.
It is free by the induction hypothesis.

:::

:::

::: {.pf-step #s2-2}

The image $\pi(M)$ is free of rank at most $1$.

::: pf-proof

The image is an ideal of the PID $R$, hence is principal.
Therefore $\pi(M)$ is either $0$ or isomorphic to $R$ as an $R$-module, so it is free.

:::

:::

::: {.pf-step #s2-3}

The short exact sequence
\[
0\longrightarrow \ker(\pi|_M)\longrightarrow M\xrightarrow{\pi}\pi(M)\longrightarrow0
\]
splits.

::: pf-proof

The module $\pi(M)$ is free by step [](#s2-2){.pf-ref}, hence projective.
Therefore the surjection $M\to\pi(M)$ admits an $R$-linear section.

:::

:::

::: pf-step

Hence $M$ is free.

::: pf-proof

By step [](#s2-3){.pf-ref},
\[
M\cong \ker(\pi|_M)\oplus \pi(M).
\]
Both summands are free by steps [](#s2-1){.pf-ref} and [](#s2-2){.pf-ref}, and their direct sum is free.
This completes the induction.

:::

:::

:::

:::

::: pf-step

Therefore $R$ is a PID if and only if every submodule of a finitely generated free $R$-module is free.

::: pf-proof

The forward implication is step [](#s2){.pf-ref} and the reverse implication is step [](#s1){.pf-ref}.

:::

:::

:::

:::
