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
(a) What is a valuation on a field $K$ (specifically a discrete valuation)?

(b) Define the $p$-adic valuation $v_p$ and the $p$-adic absolute value $\abs{\cdot}_p$ on $\QQ$.

(c) Define the ring of $p$-adic integers $\ZZ_p$ and the field of $p$-adic numbers $\QQ_p$ (both algebraically via inverse limits and analytically via completion).
:::

::: {.solution}
(a) A discrete valuation on a field $K$ is a map
$$
v:K\to\ZZ\cup\{\infty\}
$$
such that
$$
v(x)=\infty\iff x=0,\qquad
v(xy)=v(x)+v(y),\qquad
v(x+y)\ge\min\{v(x),v(y)\},
$$
and whose image on $K^\times$ is all of $\ZZ$. Its valuation ring is
$$
\mathcal O_v=\{x:v(x)\ge0\},
$$
with maximal ideal
$$
\mathfrak m_v=\{x:v(x)>0\}.
$$

(b) For a prime $p$, every nonzero $x\in\QQ$ has a unique form
$$
x=p^k\frac ab,
\qquad p\nmid a,b,
$$
and one defines
$$
v_p(x)=k,\qquad v_p(0)=\infty.
$$
The associated absolute value is
$$
\abs{x}_p=p^{-v_p(x)},\qquad \abs{0}_p=0,
$$
and satisfies
$$
\abs{x+y}_p\le\max\{\abs{x}_p,\abs{y}_p\}.
$$

(c) The field of $p$-adic numbers is the metric completion
$$
\QQ_p=\widehat{\QQ}^{\,\abs{\cdot}_p}.
$$
Its valuation ring is
$$
\ZZ_p=\{x\in\QQ_p:v_p(x)\ge0\}
=\{x:\abs{x}_p\le1\}.
$$
Algebraically,
$$
\ZZ_p\cong\varprojlim_n\ZZ/p^n\ZZ,
$$
and every $x\in\ZZ_p$ has a unique expansion
$$
x=\sum_{n\ge0}a_np^n,\qquad a_n\in\{0,1,\ldots,p-1\}.
$$
Finally,
$$
\QQ_p=\Frac(\ZZ_p)=\ZZ_p[1/p],
$$
so every nonzero $p$-adic number has a Laurent expansion with only finitely many negative powers of $p$.
:::
