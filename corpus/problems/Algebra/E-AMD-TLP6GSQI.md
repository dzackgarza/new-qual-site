---
schema: qual/card@1
id: E-AMD-TLP6GSQI
kind: problem
title: Finitely generated modules over a Noetherian local ring are flat iff free
classification:
  areas:
  - algebra
  topics:
  - Nakayama's Lemma
  - Free Modules
  - Homological Algebra
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

::: {.exercise}
Show that a finitely generated module over a Noetherian local ring is flat iff it is free using Nakayama and Tor.
:::


::: {.solution}
Let $(R,\mfm)$ be the Noetherian local ring and $M$ the finitely generated $R$-module.

::: pf

::: pf-step
If $M$ is free, then $M$ is flat.

::: pf-proof
Every free module is a direct sum of copies of $R$, and tensoring with a free module preserves injections because it is a direct sum of copies of the original map.
:::

:::

::: pf-step
If $M$ is flat, then $M$ is free.

::: pf-proof

::: {.pf-step #choose-basis-lifts}
Let
$$
n=\dim_{R/\mfm}(M/\mfm M).
$$
Choose elements $m_1,\ldots,m_n\in M$ whose residue classes form a basis of $M/\mfm M$.

::: pf-proof
Since $M$ is finitely generated, $M/\mfm M$ is a finite-dimensional vector space over the residue field $R/\mfm$.
:::

:::

::: pf-step
The map
$$
\pi:R^n\longrightarrow M,
\qquad e_i\longmapsto m_i,
$$
is surjective.

::: pf-proof
The classes of the $m_i$ generate $M/\mfm M$. Hence
$$
M=Rm_1+\cdots+Rm_n+\mfm M.
$$
Nakayama's lemma gives $M=Rm_1+\cdots+Rm_n$, so $\pi$ is surjective.
:::

:::

::: {.pf-step #kernel-finitely-generated}
Let $K=\ker\pi$. Then $K$ is finitely generated.

::: pf-proof
The module $R^n$ is finitely generated over the Noetherian ring $R$, so every submodule of $R^n$, in particular $K$, is finitely generated.
:::

:::

::: {.pf-step #tensored-sequence-exact}
Tensoring
$$
0\longrightarrow K\longrightarrow R^n\longrightarrow M\longrightarrow0
$$
with $k\coloneqq R/\mfm$ gives an exact sequence
$$
0\longrightarrow K/\mfm K
\longrightarrow k^n
\longrightarrow M/\mfm M
\longrightarrow0.
$$

::: pf-proof
The long exact Tor sequence begins
$$
\Tor_1^R(M,k)\longrightarrow K\otimes_Rk
\longrightarrow R^n\otimes_Rk
\longrightarrow M\otimes_Rk\longrightarrow0.
$$
Because $M$ is flat, $\Tor_1^R(M,k)=0$. Also
$K\otimes_Rk\cong K/\mfm K$, $R^n\otimes_Rk\cong k^n$, and
$M\otimes_Rk\cong M/\mfm M$.
:::

:::

::: {.pf-step #kn-to-mmodmm-iso}
The map $k^n\to M/\mfm M$ in step [](#tensored-sequence-exact){.pf-ref} is an isomorphism, so
$$
K/\mfm K=0.
$$

::: pf-proof
By construction in step [](#choose-basis-lifts){.pf-ref}, the images of $e_1,\ldots,e_n$ are exactly the chosen basis of $M/\mfm M$. Hence the induced map $k^n\to M/\mfm M$ is an isomorphism. Exactness in step [](#tensored-sequence-exact){.pf-ref} then forces its kernel $K/\mfm K$ to vanish.
:::

:::

::: {.pf-step #k-zero-pi-iso}
Nakayama's lemma gives $K=0$. Hence $\pi:R^n\to M$ is an isomorphism, so $M$ is free.

::: pf-proof
By step [](#kernel-finitely-generated){.pf-ref}, $K$ is finitely generated, and by step [](#kn-to-mmodmm-iso){.pf-ref}, $K=\mfm K$. Nakayama's lemma therefore gives $K=0$. Since $\pi$ is already surjective, it is an isomorphism.
:::

:::

:::

:::

:::

:::
