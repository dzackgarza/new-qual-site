---
schema: qual/card@1
id: P-AHI7C
kind: problem
title: Annihilators of torsion modules over an integral domain
classification:
  areas:
  - algebra
  topics:
  - Torsion
  - Modules
  - Integral Domains
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---
::: {.problem}
Let $R$ be an integral domain and let $M$ be a nonzero torsion $R\dash$module.

a. Prove that if $M$ is finitely generated then the annihilator in $R$ of $M$ is nonzero.

b. Give an example of a non-finitely generated torsion $R\dash$module whose annihilator is $(0)$, and justify your answer.
:::

::: {.solution}
For any $R$-module $N$, write $\operatorname{Ann}_R(N)=\{r\in R:rN=0\}$.

::: pf

::: {.pf-step #s1}

If $M$ is finitely generated, then $\operatorname{Ann}_R(M)\neq(0)$.

::: pf-proof

Choose generators $m_1,\ldots,m_t$ for the nonzero module $M$. Since $M$ is torsion, for each $i$ choose $0\neq r_i\in R$ with $r_im_i=0$. Put $r=\prod_{i=1}^t r_i$. The domain property gives $r\neq0$. Since $r$ is a multiple of every $r_i$, it annihilates every generator $m_i$. Thus it annihilates every $R$-linear combination of the generators, hence all of $M$, and $0\neq r\in\operatorname{Ann}_R(M)$.

:::

:::

::: {.pf-step #s2}

The $\ZZ$-module
$$
\boxed{N=\bigoplus_{p\text{ prime}}\ZZ/p\ZZ}
$$
is torsion, is not finitely generated, and has $\operatorname{Ann}_{\ZZ}(N)=(0)$.

::: pf-proof

Every element of $N$ has finite support, say at the primes $p_1,\ldots,p_s$. Multiplication by the nonzero integer $p_1\cdots p_s$ annihilates that element; the zero element is annihilated by $1$. Thus $N$ is torsion.

If $n_1,\ldots,n_t$ generated $N$, the union of their finite supports would be a finite set $S$ of primes. Every linear combination would vanish outside $S$, while $N$ has a nonzero element supported at any prime outside $S$. Since there are infinitely many primes, this is a contradiction; hence $N$ is not finitely generated.

If $a\in\ZZ$ annihilates $N$, then its action on the summand $\ZZ/p\ZZ$ is zero for every prime $p$, so every prime divides $a$. A nonzero integer has only finitely many prime divisors, forcing $a=0$. Conversely, zero annihilates $N$. Therefore $\operatorname{Ann}_{\ZZ}(N)=(0)$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} establishes part (a), and step [](#s2){.pf-ref} supplies and verifies the example requested in part (b).

:::

:::

:::
