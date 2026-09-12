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
<1>1. If \(M\) is free, then \(M\) is flat.
::: {.proof}
Every free module is a direct sum of copies of \(R\), and tensoring with a free module preserves injections because it is a direct sum of copies of the original map.
:::

<1>2. Conversely, suppose \((R,\mathfrak m)\) is Noetherian local and \(M\) is finitely generated and flat. Let
\[
n=\dim_{R/\mathfrak m}(M/\mathfrak m M).
\]
Choose elements \(m_1,\dots,m_n\in M\) whose residue classes form a basis of \(M/\mathfrak m M\).
::: {.proof}
Since \(M\) is finitely generated, \(M/\mathfrak m M\) is a finite-dimensional vector space over the residue field \(R/\mathfrak m\).
:::

<1>3. The map
\[
\pi:R^n\longrightarrow M,
\qquad e_i\longmapsto m_i,
\]
is surjective.
::: {.proof}
The classes of the \(m_i\) generate \(M/\mathfrak mM\). Hence
\[
M=Rm_1+\cdots+Rm_n+\mathfrak mM.
\]
Nakayama's lemma gives \(M=Rm_1+\cdots+Rm_n\), so \(\pi\) is surjective.
:::

<1>4. Let \(K=\ker\pi\). Then \(K\) is finitely generated.
::: {.proof}
The module \(R^n\) is finitely generated over the Noetherian ring \(R\), so every submodule of \(R^n\), in particular \(K\), is finitely generated.
:::

<1>5. Tensoring
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
::: {.proof}
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

<1>6. The map \(k^n\to M/\mathfrak mM\) in <1>5 is an isomorphism, so
\[
K/\mathfrak mK=0.
\]
::: {.proof}
By construction in <1>2, the images of \(e_1,\dots,e_n\) are exactly the chosen basis of \(M/\mathfrak mM\). Hence the induced map \(k^n\to M/\mathfrak mM\) is an isomorphism. Exactness in <1>5 then forces its kernel \(K/\mathfrak mK\) to vanish.
:::

<1>7. Nakayama's lemma gives \(K=0\). Hence \(\pi:R^n\to M\) is an isomorphism, so \(M\) is free.
::: {.proof}
By <1>4, \(K\) is finitely generated, and by <1>6, \(K=\mathfrak mK\). Nakayama's lemma therefore gives \(K=0\). Since \(\pi\) is already surjective, it is an isomorphism.
:::

<1>8. Therefore a finitely generated module over a Noetherian local ring is flat if and only if it is free.
::: {.proof}
Combine <1>1 and <1>7.
:::
:::
