---
schema: qual/card@1
id: E-AMD-GEZ3H4G7
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
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Let $F\subseteq L\subseteq\Omega$ be fields and let $\alpha\in\Omega$ be algebraic over $F$. Show that the minimal polynomial of $\alpha$ over $L$ divides the minimal polynomial of $\alpha$ over $F$ in $L[x]$.
:::

::: {.solution}
Assume $F\subseteq L\subseteq\Omega$ are fields and $\alpha\in\Omega$ is algebraic over $F$. Then $\alpha$ is also algebraic over $L$, since its minimal polynomial over $F$ lies in $L[x]$ and annihilates $\alpha$.

Let
\[
m_F=m_{\alpha,F},\qquad m_L=m_{\alpha,L}.
\]
Divide $m_F$ by $m_L$ in $L[x]$:
\[
m_F=q\,m_L+r,\qquad \deg r<\deg m_L.
\]
Evaluating at $\alpha$ gives
\[
0=m_F(\alpha)=r(\alpha),
\]
because $m_L(\alpha)=0$. By minimality of $m_L$, the only polynomial in $L[x]$ of degree smaller than $\deg m_L$ that annihilates $\alpha$ is the zero polynomial. Hence $r=0$.

Therefore
\[
\boxed{m_{\alpha,L}\mid m_{\alpha,F}\quad\text{in }L[x].}
\]
:::
