---
schema: qual/card@1
id: P-HFGO16
kind: problem
title: The kernel of evaluation at an extension-field element
classification:
  areas: [algebra]
  topics: [Field Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Fields and Galois Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $F$ be a field, and let $\theta$ lie in an extension field.
There is an isomorphism $F[\theta]\cong F[x]/A$ for an ideal $A\subseteq F[x]$.
Describe $A$ when $\theta$ is algebraic and when $\theta$ is transcendental.
:::

::: solution
Let
\[
\operatorname{ev}_\theta:F[x]\longrightarrow F[\theta],
\qquad
f(x)\longmapsto f(\theta).
\]
Then
\[
A=\ker(\operatorname{ev}_\theta).
\]

<1>1. If $\theta$ is transcendental over $F$, then $A=(0)$.
::: proof
By definition of transcendence, no nonzero polynomial in $F[x]$ vanishes at
$\theta$. Hence
\[
\ker(\operatorname{ev}_\theta)=0.
\]
Therefore
\[
F[\theta]\cong F[x].
\]
:::

<1>2. If $\theta$ is algebraic over $F$, then
\[
A=(m_\theta(x)),
\]
where $m_\theta$ is the minimal polynomial of $\theta$ over $F$.
::: proof
Certainly $m_\theta(\theta)=0$, so
\[
(m_\theta)\subseteq A.
\]
Conversely, let $f\in A$. Divide by the monic polynomial $m_\theta$:
\[
f=qm_\theta+r,
\qquad
\deg r<\deg m_\theta.
\]
Evaluating at $\theta$ gives
\[
0=f(\theta)=r(\theta).
\]
By minimality of the degree of $m_\theta$, this forces $r=0$. Thus
$m_\theta$ divides $f$, and $A=(m_\theta)$.
:::

Hence
\[
F[\theta]\cong
\begin{cases}
F[x], & \theta\text{ transcendental},\\
F[x]/(m_\theta), & \theta\text{ algebraic}.
\end{cases}
\]
:::
