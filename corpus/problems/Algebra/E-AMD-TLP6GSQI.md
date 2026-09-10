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
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.exercise}
Show that a finitely generated module over a Noetherian local ring is flat iff it is free using Nakayama and Tor.
:::

::: {.solution}
Let \((R,\mathfrak m)\) be a Noetherian local ring and let \(M\) be a finitely generated \(R\)-module.

<1>1. If \(M\) is free, then \(M\) is flat.
::: {.proof}
Every free module is flat: tensoring with a direct sum of copies of \(R\) is a direct sum of copies of the identity functor, hence preserves injections.
:::

<1>2. Assume conversely that \(M\) is flat.
Let \(k=R/\mathfrak m\), put
\[
r=\dim_k(M/\mathfrak mM),
\]
and choose elements \(m_1,\dots,m_r\in M\) whose residue classes form a \(k\)-basis of \(M/\mathfrak mM\).
::: {.proof}
Because \(M\) is finitely generated, \(M/\mathfrak mM\) is a finite-dimensional \(k\)-vector space, so such a basis and such lifts exist.
:::

<1>3. The map
\[
\pi:R^r\longrightarrow M,\qquad e_i\longmapsto m_i,
\]
is surjective.
::: {.proof}
Modulo \(\mathfrak m\), the induced map
\[
\overline\pi:k^r\longrightarrow M/\mathfrak mM
\]
is an isomorphism by the choice of the \(m_i\). Hence
\[
M=\operatorname{im}(\pi)+\mathfrak mM.
\]
Applying Nakayama's lemma to the finitely generated module \(M/\operatorname{im}(\pi)\) gives \(M/\operatorname{im}(\pi)=0\). Thus \(\pi\) is surjective.
:::

<1>4. Let \(K=\ker\pi\). Then \(K\) is finitely generated.
::: {.proof}
The module \(R^r\) is finitely generated over the Noetherian ring \(R\), so every submodule of \(R^r\), in particular \(K\), is finitely generated.
:::

<1>5. Tensoring
\[
0\longrightarrow K\longrightarrow R^r\xrightarrow{\pi}M\longrightarrow0
\]
with \(k\) yields an exact sequence
\[
0\longrightarrow K\otimes_R k\longrightarrow k^r\xrightarrow{\overline\pi}M\otimes_R k\longrightarrow0.
\]
::: {.proof}
The long exact Tor sequence begins
\[
\operatorname{Tor}_1^R(k,M)\longrightarrow K\otimes_Rk\longrightarrow R^r\otimes_Rk.
\]
Since \(M\) is flat, \(\operatorname{Tor}_1^R(k,M)=0\). Also \(R^r\otimes_Rk\cong k^r\) and \(M\otimes_Rk\cong M/\mathfrak mM\). Hence the displayed sequence is exact.
:::

<1>6. We have \(K/\mathfrak mK=0\).
::: {.proof}
Under the standard identifications, the middle map in <1>5 is exactly the map \(\overline\pi:k^r\to M/\mathfrak mM\), which is an isomorphism by <1>2. Exactness therefore gives
\[
K\otimes_Rk=0.
\]
But \(K\otimes_Rk\cong K/\mathfrak mK\).
:::

<1>7. Hence \(K=0\), so \(M\cong R^r\) is free.
::: {.proof}
By <1>4, \(K\) is finitely generated.
By <1>6, \(K=\mathfrak mK\). Nakayama's lemma therefore gives \(K=0\). Thus the surjection \(\pi:R^r\to M\) from <1>3 is an isomorphism.
:::

<1>8. Therefore a finitely generated module over a Noetherian local ring is flat if and only if it is free.
::: {.proof}
Combine <1>1 and <1>7.
:::
:::
