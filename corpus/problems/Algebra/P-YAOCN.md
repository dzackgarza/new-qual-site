---
schema: qual/card@1
id: P-YAOCN
kind: problem
title: The minimal polynomial over $L$ divides the minimal polynomial over $F$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Let $L/F$ be a field extension, and let $\alpha$ be algebraic over $F$.
Let $m_F(x) = \operatorname{irr}(\alpha, F) \in F[x]$ and $m_L(x) = \operatorname{irr}(\alpha, L) \in L[x]$ be the minimal polynomials of $\alpha$ over $F$ and over $L$, respectively.
Prove that $m_L(x)$ divides $m_F(x)$ in the polynomial ring $L[x]$.
:::

::: solution
Because $F\subseteq L$, we may regard
\[
m_F(x)\in F[x]
\]
as a polynomial in $L[x]$. Divide it by the minimal polynomial $m_L(x)$:
\[
m_F(x)=q(x)m_L(x)+r(x),
\qquad \deg r<\deg m_L.
\]
Evaluating at $\alpha$ gives
\[
0=m_F(\alpha)=q(\alpha)m_L(\alpha)+r(\alpha)=r(\alpha).
\]
If $r\ne0$, this would be a nonzero polynomial in $L[x]$ of degree smaller than $m_L$ that annihilates $\alpha$, contradicting minimality of $m_L$. Hence $r=0$, so
\[
\boxed{m_L(x)\mid m_F(x)\text{ in }L[x]}.
\]
:::
