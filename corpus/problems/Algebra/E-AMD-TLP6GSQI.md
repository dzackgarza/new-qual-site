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

::: pf

::: {.pf-step #free-implies-flat}
If \(M\) is free, then \(M\) is flat.

::: pf-proof
Every free module is a direct sum of copies of \(R\), and tensoring with a free module preserves injections because it is a direct sum of copies of the original map.
:::

:::

::: {.pf-step #choose-basis-lifts}
Conversely, suppose \((R,\mathfrak m)\) is Noetherian local and \(M\) is finitely generated and flat. Let
\[
n=\dim_{R/\mathfrak m}(M/\mathfrak m M).
\]
Choose elements \(m_1,\dots,m_n\in M\) whose residue classes form a basis of \(M/\mathfrak m M\).

::: pf-proof
Since \(M\) is finitely generated, \(M/\mathfrak m M\) is a finite-dimensional vector space over the residue field \(R/\mathfrak m\).
:::

:::

::: pf-step
The map
\[
\pi:R^n\longrightarrow M,
\qquad e_i\longmapsto m_i,
\]
is surjective.

::: pf-proof
The classes of the \(m_i\) generate \(M/\mathfrak mM\). Hence
\[
M=Rm_1+\cdots+Rm_n+\mathfrak mM.
\]
Nakayama's lemma gives \(M=Rm_1+\cdots+Rm_n\), so \(\pi\) is surjective.
:::

:::

::: {.pf-step #kernel-finitely-generated}
Let \(K=\ker\pi\). Then \(K\) is finitely generated.

::: pf-proof
The module \(R^n\) is finitely generated over the Noetherian ring \(R\), so every submodule of \(R^n\), in particular \(K\), is finitely generated.
:::

:::

::: {.pf-step #tensored-sequence-exact}
Tensoring
\[
0\longrightarrow K\longrightarrow R^n\longrightarrow M\longrightarrow0
\]
with \(k:=R/\mathfrak m\) gives an exact sequence
\[
0\longrightarrow K/\mathfrak mK
\longrightarrow k^n
\longrightarrow M/\mathfrak mM
\longrightarrow0.
\]

::: pf-proof
The long exact Tor sequence begins
\[
\operatorname{Tor}_1^R(M,k)\longrightarrow K\otimes_Rk
\longrightarrow R^n\otimes_Rk
\longrightarrow M\otimes_Rk\longrightarrow0.
\]
Because \(M\) is flat, \(\operatorname{Tor}_1^R(M,k)=0\). Also
\(K\otimes_Rk\cong K/\mathfrak mK\), \(R^n\otimes_Rk\cong k^n\), and
\(M\otimes_Rk\cong M/\mathfrak mM\).
:::

:::

::: {.pf-step #kn-to-mmodmm-iso}
The map \(k^n\to M/\mathfrak mM\) in step [](#tensored-sequence-exact){.pf-ref} is an isomorphism, so
\[
K/\mathfrak mK=0.
\]

::: pf-proof
By construction in step [](#choose-basis-lifts){.pf-ref}, the images of \(e_1,\dots,e_n\) are exactly the chosen basis of \(M/\mathfrak mM\). Hence the induced map \(k^n\to M/\mathfrak mM\) is an isomorphism. Exactness in step [](#tensored-sequence-exact){.pf-ref} then forces its kernel \(K/\mathfrak mK\) to vanish.
:::

:::

::: {.pf-step #k-zero-pi-iso}
Nakayama's lemma gives \(K=0\). Hence \(\pi:R^n\to M\) is an isomorphism, so \(M\) is free.

::: pf-proof
By step [](#kernel-finitely-generated){.pf-ref}, \(K\) is finitely generated, and by step [](#kn-to-mmodmm-iso){.pf-ref}, \(K=\mathfrak mK\). Nakayama's lemma therefore gives \(K=0\). Since \(\pi\) is already surjective, it is an isomorphism.
:::

:::

::: pf-step
Therefore a finitely generated module over a Noetherian local ring is flat if and only if it is free.

::: pf-proof
Combine steps [](#free-implies-flat){.pf-ref} and [](#k-zero-pi-iso){.pf-ref}.
:::

:::

:::

:::
