---
schema: qual/card@1
id: P-T3YQ4
kind: problem
title: Nilradical and infinitely many primes in $F[x]$
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Prime Ideals
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
(a) Define the nilradical $\operatorname{Nil}(R)$ of a commutative ring $R$, and state the characterization theorem relating it to the intersection of all prime ideals of $R$.

(b) Prove that the polynomial ring $F[x]$ over a field $F$ contains infinitely many prime ideals.
:::

::: {.solution}

::: pf

::: pf-step

(a) $\operatorname{Nil}(R)=\sqrt{(0)}=\{a\in R: a^m=0\text{ for some }m\ge1\}$, and $\boxed{\operatorname{Nil}(R)=\bigcap_{\mathfrak p\in\Spec R}\mathfrak p}$.

::: pf-proof

The first equality is the definition. The second is the standard characterization of the nilradical as the intersection of all prime ideals.

:::

:::

::: pf-qed

(b) Every nonzero prime ideal of the PID $F[x]$ is $(p)$ with $p$ irreducible. Suppose the nonzero prime ideals were only $(p_1),\ldots,(p_m)$, and set $h=p_1\cdots p_m+1$. Then $h$ is nonconstant, so it has an irreducible factor $q$, and $(q)$ is a nonzero prime ideal; hence $q$ is associate to some $p_j$. Then $p_j$ divides both $h$ and $p_1\cdots p_m$, hence divides $1$, a contradiction. So $F[x]$ has infinitely many nonzero prime ideals.

:::

:::

:::
