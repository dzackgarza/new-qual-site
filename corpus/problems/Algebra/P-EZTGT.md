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
- event: solution-written
  by: Claude Opus 5.5
  date: 2026-10-29
  note: Converted the prose solution to a STYLE-08 structured proof.
---

::: {.problem}
(a) What is a valuation on a field $K$ (specifically a discrete valuation)?

(b) Define the $p$-adic valuation $v_p$ and the $p$-adic absolute value $\abs{\cdot}_p$ on $\QQ$.

(c) Define the ring of $p$-adic integers $\ZZ_p$ and the field of $p$-adic numbers $\QQ_p$ (both algebraically via inverse limits and analytically via completion).
:::

::: {.solution}

::: pf

::: pf-step
(a) A discrete valuation on a field $K$ is a map $v:K\to\ZZ\cup\{\infty\}$, with image $\ZZ$ on $K^\times$, such that
$$
v(x)=\infty\iff x=0,\qquad
v(xy)=v(x)+v(y),\qquad
v(x+y)\ge\min\{v(x),v(y)\}.
$$
Its valuation ring is $\mathcal O_v=\{x:v(x)\ge0\}$, with maximal ideal $\mathfrak m_v=\{x:v(x)>0\}$.

::: pf-proof
This is the definition.
$\mathcal O_v$ is a ring by the last two conditions, and $\mathfrak m_v$ is its unique maximal ideal, because $x\in\mathcal O_v$ is a unit exactly when $v(x)=0$.
:::

:::

::: {.pf-step #vp}
(b) For a prime $p$, write each nonzero $x\in\QQ$ as $x=p^k\frac ab$ with $p\nmid a,b$; then $v_p(x)=k$, $v_p(0)=\infty$, $\abs{x}_p=p^{-v_p(x)}$ and $\abs{0}_p=0$, and $\abs{x+y}_p\le\max\{\abs{x}_p,\abs{y}_p\}$.

::: pf-proof
The exponent $k$ is unique by unique factorization in $\ZZ$, so $v_p$ is well defined.
If $v_p(x),v_p(y)\ge k$, then $x+y=p^k\frac{c}{d}$ with $p\nmid d$, so $v_p(x+y)\ge k$; this gives the ultrametric inequality.
:::

:::

::: pf-step
(c) Analytically, $\QQ_p$ is the metric completion of $\QQ$ with respect to $\abs{\cdot}_p$, and $\ZZ_p=\{x\in\QQ_p:\abs{x}_p\le1\}$ is its valuation ring.
Algebraically, $\ZZ_p\cong\varprojlim_n\ZZ/p^n\ZZ$, each $x\in\ZZ_p$ has a unique expansion $x=\sum_{n\ge0}a_np^n$ with $a_n\in\{0,1,\ldots,p-1\}$, and $\QQ_p=\Frac(\ZZ_p)=\ZZ_p[1/p]$.

::: pf-proof
The valuation $v_p$ of step [](#vp){.pf-ref} extends continuously to the completion, so $\ZZ_p$ is its valuation ring.
The map $\ZZ_p\to\ZZ/p^n\ZZ$ induced by $\ZZ\to\ZZ/p^n\ZZ$ has kernel $p^n\ZZ_p$, and these maps assemble to an isomorphism onto the inverse limit, under which the base-$p$ digits of the compatible residues give the expansion.
Every nonzero $x\in\QQ_p$ is $p^{v_p(x)}u$ with $u\in\ZZ_p^\times$, so $\QQ_p=\ZZ_p[1/p]$, and every nonzero $p$-adic number has a Laurent expansion with only finitely many negative powers of $p$.
:::

:::

:::

:::
