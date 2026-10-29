---
schema: qual/card@1
id: P-XR6IK
kind: problem
title: An irreducible polynomial of degree $p$ over $\FF_p$ for each prime $p$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Irreducibility Criteria
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

::: {.problem}
For each prime $p$, give an explicit polynomial of degree $p$ that is irreducible over the finite field $\FF_p$, constructed in a uniform way across all primes $p$.
Prove that your polynomial is irreducible over $\FF_p$.
:::

::: {.solution}
For a prime $p$, let $f(x)=x^p-x-1\in\FF_p[x]$, and let $\alpha$ be a root of $f$ in an algebraic closure of $\FF_p$.

::: pf

::: {.pf-step #orbit}
$\alpha^{p^m}=\alpha+m$ for every integer $m\ge0$, with $m$ read in $\FF_p$.

::: pf-proof
For $m=0$ this is trivial.
If it holds for $m$, then $\alpha^{p^{m+1}}=(\alpha+m)^p=\alpha^p+m=\alpha+1+m$, because Frobenius is additive, fixes $\FF_p$, and $\alpha^p=\alpha+1$.
:::

:::

::: {.pf-step #degree}
$[\FF_p(\alpha):\FF_p]=p$.

::: pf-proof
The degree of $\FF_p(\alpha)$ over $\FF_p$ is the least $m>0$ with $\alpha^{p^m}=\alpha$.
By step [](#orbit){.pf-ref}, this is the least $m>0$ with $m=0$ in $\FF_p$, namely $m=p$.
:::

:::

::: pf-step
$\boxed{x^p-x-1}$ is irreducible over $\FF_p$.

::: pf-proof
The minimal polynomial of $\alpha$ divides $f$ and has degree $p=\deg f$ by step [](#degree){.pf-ref}, so it equals $f$ up to a unit, and $f$ is irreducible.
:::

:::

:::

:::
