---
schema: qual/card@1
id: P-ALGS21E
kind: problem
title: "Higher Ext groups over Z for Z/2Z with coefficients in Z and Q"
classification:
  areas:
  - algebra
  topics:
  - Homological Algebra
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
For $i \geq 0$, calculate $\operatorname{Ext}^i_\mathbb{Z}(\mathbb{Z}/2\mathbb{Z}, \mathbb{Z})$ and $\operatorname{Ext}^i_\mathbb{Z}(\mathbb{Z}/2\mathbb{Z}, \mathbb{Q})$.
:::


::: {.solution}
<1>1. Use the free resolution
\[
0\longrightarrow\mathbb Z\xrightarrow{\cdot2}\mathbb Z\longrightarrow\mathbb Z/2\mathbb Z\longrightarrow0.
\]
::: {.proof}
Multiplication by \(2\) is injective on \(\mathbb Z\), and its cokernel is \(\mathbb Z/2\mathbb Z\). Thus this is a projective resolution of length \(1\).
:::

<1>2. For any abelian group \(M\), applying \(\operatorname{Hom}_{\mathbb Z}(-,M)\) gives the cochain complex
\[
0\longrightarrow M\xrightarrow{\cdot2}M\longrightarrow0.
\]
Hence
\[
\operatorname{Ext}^0_{\mathbb Z}(\mathbb Z/2,M)=\ker(2:M\to M),
\]
\[
\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/2,M)=M/2M,
\]
and \(\operatorname{Ext}^i=0\) for \(i\ge2\).
::: {.proof}
One has \(\operatorname{Hom}_{\mathbb Z}(\mathbb Z,M)\cong M\), and precomposition with multiplication by \(2\) becomes multiplication by \(2\) on \(M\). The cohomology in degrees \(0\) and \(1\) is therefore the displayed kernel and cokernel, and there are no higher terms.
:::

<1>3. Taking \(M=\mathbb Z\),
\[
\operatorname{Ext}^i_{\mathbb Z}(\mathbb Z/2,\mathbb Z)
\cong
\begin{cases}
0,&i=0,\\
\mathbb Z/2\mathbb Z,&i=1,\\
0,&i\ge2.
\end{cases}
\]
::: {.proof}
Multiplication by \(2\) on \(\mathbb Z\) is injective, so the degree-zero kernel is zero, and its cokernel is \(\mathbb Z/2\mathbb Z\). Apply <1>2.
:::

<1>4. Taking \(M=\mathbb Q\),
\[
\operatorname{Ext}^i_{\mathbb Z}(\mathbb Z/2,\mathbb Q)=0
\qquad\text{for every }i\ge0.
\]
::: {.proof}
Multiplication by \(2\) is an automorphism of \(\mathbb Q\), so both its kernel and cokernel are zero. Higher Ext groups vanish by <1>2.
:::
:::
