---
schema: qual/card@1
id: P-ALGS04J
kind: problem
title: "Representing numbers as sums of two squares using Gaussian integer norms"
classification:
  areas:
  - algebra
  topics:
  - Number Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
In the Gaussian integers the norm is used to analyze sums of squares. Use this technique to determine how many ways $N=3^4$ and $M=5^4$ can each be expressed as the sum of two integer squares.
:::

::: {.solution}
<1>1. Integer pairs $(a,b)$ with $a^2+b^2=n$ are in bijection with Gaussian integers $z=a+bi$ of norm $N(z)=n$.
::: {.proof}
By definition,
\[
N(a+bi)=(a+bi)(a-bi)=a^2+b^2.
\]
Thus counting ordered integer pairs is exactly the same as counting Gaussian integers of the prescribed norm.
:::

<1>2. There are exactly four Gaussian integers of norm $3^4$.
::: {.proof}
The rational prime $3$ satisfies $3\equiv3\pmod4$, so it remains prime in $\mathbb Z[i]$. If $N(z)=3^4$, then in the unique factorization domain $\mathbb Z[i]$ the prime factorization of $z\bar z$ is $3^4$. Since conjugation fixes the Gaussian prime $3$, every Gaussian prime divisor of $z$ is associate to $3$. Hence
\[
z=u3^k
\]
for a unit $u\in\{\pm1,\pm i\}$. Taking norms gives
\[
3^4=N(z)=N(3)^k=3^{2k},
\]
so $k=2$. Therefore
\[
z\in\{9,-9,9i,-9i\},
\]
corresponding to
\[
(9,0),\ (-9,0),\ (0,9),\ (0,-9).
\]
Thus $3^4$ has exactly $4$ ordered representations as a sum of two integer squares.
:::

<1>3. There are exactly twenty Gaussian integers of norm $5^4$.
::: {.proof}
The prime $5$ splits in $\mathbb Z[i]$ as
\[
5=(2+i)(2-i)=\pi\bar\pi,
\]
where $\pi$ and $\bar\pi$ are nonassociate Gaussian primes. Hence
\[
5^4=\pi^4\bar\pi^4.
\]
If $N(z)=5^4$, unique factorization gives
\[
z=u\pi^r\bar\pi^{\,4-r}
\qquad(0\le r\le4),
\]
with $u\in\{\pm1,\pm i\}$. Conversely every such element has norm $5^4$. The five possible exponents $r$ give pairwise nonassociate elements because $\pi$ and $\bar\pi$ are nonassociate, and multiplying by the four units gives four distinct associates in each case. Hence there are
\[
5\cdot4=20
\]
Gaussian integers of norm $5^4$, so $5^4$ has exactly $20$ ordered representations as a sum of two integer squares.
:::

<1>4. Therefore the requested numbers of representations are
\[
\boxed{4\text{ for }3^4},\qquad \boxed{20\text{ for }5^4}.
\]
::: {.proof}
Combine <1>2 and <1>3.
:::
:::
