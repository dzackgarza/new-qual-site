---
schema: qual/card@1
id: P-MMAQ-G2X5HB5VJS
kind: problem
title: Equivalence of $\mathrm{Ann}(M)\not\subset\mathfrak{p}$, $M_{\mathfrak{p}}=0$,
  and $M\otimes_A k(\mathfrak{p})=0$ for finitely generated modules
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Modules
  - Ideals
  - Localization
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
Let $A$ be a commutative ring and $M$ a finitely generated $A$-module.
Define
`\begin{align*}
  \Ann(M) = \{a \in A: am = 0 \text{ for all } m \in M\}
.\end{align*}`{=tex}
Show that for a prime ideal $\mathfrak p \subset A$, the following are equivalent:

-   $\Ann(M) \not\subset \mathfrak p$

-   The localization of $M$ at the prime ideal $\mathfrak p$ is $0$.

-   $M \otimes_A k(\mathfrak p) = 0$, where $k(\mathfrak p) = A_{\mathfrak p}/\mathfrak p A_{\mathfrak p}$ is the residue field of $A$ at $\mathfrak p$.
:::


::: solution
Let \(S=A\setminus\mathfrak p\), so \(A_{\mathfrak p}=S^{-1}A\) and \(M_{\mathfrak p}=S^{-1}M\).

<1>1. If
\[
\operatorname{Ann}(M)\not\subset\mathfrak p,
\]
then
\[
M_{\mathfrak p}=0.
\]
::: {.proof}
Choose
\[
s\in\operatorname{Ann}(M)\setminus\mathfrak p.
\]
Then \(s/1\) is a unit in \(A_{\mathfrak p}\), while it annihilates every element of \(M_{\mathfrak p}\). If \(m/1\in M_{\mathfrak p}\), then
\[
\frac{s}{1}\frac{m}{1}=0.
\]
Multiplying by the inverse of \(s/1\) gives \(m/1=0\). Hence \(M_{\mathfrak p}=0\).
:::

<1>2. Conversely, if
\[
M_{\mathfrak p}=0,
\]
then
\[
\operatorname{Ann}(M)\not\subset\mathfrak p.
\]
::: {.proof}
Let \(m_1,\dots,m_r\) generate \(M\). Since \(m_i/1=0\) in \(M_{\mathfrak p}\), for each \(i\) there exists \(s_i\in S\) such that
\[
s_i m_i=0.
\]
Put
\[
s=s_1\cdots s_r.
\]
Because \(\mathfrak p\) is prime and no \(s_i\) belongs to \(\mathfrak p\), we have \(s\notin\mathfrak p\). Moreover \(s\) annihilates every generator \(m_i\), hence all of \(M\). Thus
\[
s\in\operatorname{Ann}(M)\setminus\mathfrak p.
\]
:::

<1>3. There is a natural isomorphism
\[
M\otimes_A k(\mathfrak p)
\cong
M_{\mathfrak p}\otimes_{A_{\mathfrak p}} k(\mathfrak p)
\cong
M_{\mathfrak p}/\mathfrak pA_{\mathfrak p}M_{\mathfrak p}.
\]
::: {.proof}
Since every element of \(S\) maps to a unit in the residue field \(k(\mathfrak p)\), tensoring with \(k(\mathfrak p)\) factors through localization, giving the first isomorphism. The second is the standard tensor-quotient identity
\[
N\otimes_R R/I\cong N/IN
\]
with \(R=A_{\mathfrak p}\), \(I=\mathfrak pA_{\mathfrak p}\), and \(N=M_{\mathfrak p}\).
:::

<1>4. If \(M_{\mathfrak p}=0\), then
\[
M\otimes_A k(\mathfrak p)=0.
\]
::: {.proof}
This is immediate from <1>3.
:::

<1>5. If
\[
M\otimes_A k(\mathfrak p)=0,
\]
then
\[
M_{\mathfrak p}=0.
\]
::: {.proof}
By <1>3,
\[
M_{\mathfrak p}/\mathfrak pA_{\mathfrak p}M_{\mathfrak p}=0.
\]
The \(A_{\mathfrak p}\)-module \(M_{\mathfrak p}\) is finitely generated because \(M\) is finitely generated over \(A\). The ring \(A_{\mathfrak p}\) is local with maximal ideal \(\mathfrak pA_{\mathfrak p}\). Nakayama's lemma therefore yields
\[
M_{\mathfrak p}=0.
\]
:::

<1>6. Hence the three conditions are equivalent:
\[
\boxed{
\operatorname{Ann}(M)\not\subset\mathfrak p
\iff
M_{\mathfrak p}=0
\iff
M\otimes_A k(\mathfrak p)=0.
}
\]
:::
:::
