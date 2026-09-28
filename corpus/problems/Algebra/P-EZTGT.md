---
schema: qual/card@1
id: P-EZTGT
kind: problem
title: $p$-adic numbers and valuations
classification:
  areas:
  - algebra
  topics:
  - Valuation Rings
  - Number Theory
  - Local Rings
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

::: {.problem}
(1) What is a valuation on a field $K$ (specifically a discrete valuation)?
(2) Define the $p$-adic valuation $v_p$ and the $p$-adic absolute value $|\cdot|_p$ on $\mathbb{Q}$.
(3) Define the ring of $p$-adic integers $\mathbb{Z}_p$ and the field of $p$-adic numbers $\mathbb{Q}_p$ (both algebraically via inverse limits and analytically via completion).
:::

::: {.solution}
A discrete valuation on a field $K$ is a map
\[
v:K\to\mathbb Z\cup\{\infty\}
\]
such that
\[
v(x)=\infty\iff x=0,\qquad
v(xy)=v(x)+v(y),\qquad
v(x+y)\ge\min\{v(x),v(y)\},
\]
and whose image on $K^\times$ is all of $\mathbb Z$. Its valuation ring is
\[
\mathcal O_v=\{x:v(x)\ge0\},
\]
with maximal ideal
\[
\mathfrak m_v=\{x:v(x)>0\}.
\]

For a prime $p$, every nonzero $x\in\mathbb Q$ has a unique form
\[
x=p^k\frac ab,
\qquad p\nmid a,b,
\]
and one defines
\[
v_p(x)=k,\qquad v_p(0)=\infty.
\]
The associated absolute value is
\[
|x|_p=p^{-v_p(x)},\qquad |0|_p=0,
\]
and satisfies
\[
|x+y|_p\le\max\{|x|_p,|y|_p\}.
\]

The field of $p$-adic numbers is the metric completion
\[
\mathbb Q_p=\widehat{\mathbb Q}^{\,|\cdot|_p}.
\]
Its valuation ring is
\[
\mathbb Z_p=\{x\in\mathbb Q_p:v_p(x)\ge0\}
=\{x:|x|_p\le1\}.
\]
Algebraically,
\[
\mathbb Z_p\cong\varprojlim_n\mathbb Z/p^n\mathbb Z,
\]
and every $x\in\mathbb Z_p$ has a unique expansion
\[
x=\sum_{n\ge0}a_np^n,\qquad a_n\in\{0,1,\dots,p-1\}.
\]
Finally,
\[
\mathbb Q_p=\operatorname{Frac}(\mathbb Z_p)=\mathbb Z_p[1/p],
\]
so every nonzero $p$-adic number has a Laurent expansion with only finitely many negative powers of $p$.
:::
