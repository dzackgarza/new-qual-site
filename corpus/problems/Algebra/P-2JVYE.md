---
schema: qual/card@1
id: P-2JVYE
kind: problem
title: Schur's lemma
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Semisimplicity
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
State/prove/explain Schur's lemma.
:::

::: {.solution}
Let $R$ be a ring and let $M,N$ be simple left $R$-modules.

::: pf

::: {.pf-step #s1}

Every nonzero $R$-linear map $f:M\to N$ is an isomorphism.

::: pf-proof

The kernel $\ker f$ is an $R$-submodule of the simple module $M$, so
\[
\ker f=0 \quad\text{or}\quad \ker f=M.
\]
Since $f\ne0$, the second alternative is impossible; hence $\ker f=0$ and $f$ is injective.

Likewise, the image $\operatorname{im}f$ is a nonzero submodule of the simple module $N$, so
\[
\operatorname{im}f=N.
\]
Thus $f$ is surjective as well, hence an isomorphism.

:::

:::

::: pf-step

If $M$ and $N$ are nonisomorphic simple modules, then
\[
\operatorname{Hom}_R(M,N)=0.
\]

::: pf-proof

Any nonzero homomorphism would be an isomorphism by step [](#s1){.pf-ref}, contradicting $M\not\cong N$.

:::

:::

::: pf-step

Every nonzero element of $\operatorname{End}_R(M)$ is invertible; hence $\operatorname{End}_R(M)$ is a division ring.

::: pf-proof

Apply step [](#s1){.pf-ref} with $N=M$. Every nonzero endomorphism of $M$ is an automorphism, which is precisely the statement that every nonzero element of $\operatorname{End}_R(M)$ is a unit.

:::

:::

::: pf-step

This is Schur's lemma.

::: pf-proof

The usual representation-theoretic formulation is obtained by taking $R$ to be a group algebra: irreducible representations correspond to simple modules, so a nonzero intertwiner between irreducibles is an isomorphism, and the endomorphism ring of an irreducible representation is a division ring.

:::

:::

:::

:::
