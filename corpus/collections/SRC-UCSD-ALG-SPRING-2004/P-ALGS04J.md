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
<1>1. A representation $a^2+b^2=m$ is equivalent to a Gaussian integer $a+bi\in\mathbb Z[i]$ of norm $m$.
::: {.proof}
The Gaussian norm is $N(a+bi)=(a+bi)(a-bi)=a^2+b^2$.
:::

<1>2. There are exactly four ordered pairs $(a,b)\in\mathbb Z^2$ with $a^2+b^2=3^4$.
::: {.proof}
Since $3\equiv3\pmod4$, the rational prime $3$ remains prime in $\mathbb Z[i]$. If $N(\alpha)=3^4$, unique factorization gives $\alpha=u3^k$ for a unit $u\in\{\pm1,\pm i\}$, because no other Gaussian prime can occur. Taking norms gives $3^{2k}=3^4$, hence $k=2$. Thus
\[
\alpha\in\{9,-9,9i,-9i\},
\]
corresponding to $(9,0),(-9,0),(0,9),(0,-9)$.
:::

<1>3. There are exactly twenty ordered pairs $(a,b)\in\mathbb Z^2$ with $a^2+b^2=5^4$.
::: {.proof}
Since $5=(2+i)(2-i)$ in $\mathbb Z[i]$, put $\pi=2+i$. Then
\[
5^4=\pi^4\bar\pi^4.
\]
If $N(\alpha)=5^4$, unique factorization gives
\[
\alpha=u\pi^k\bar\pi^{\,4-k}
\qquad(0\le k\le4),
\]
with $u\in\{\pm1,\pm i\}$. Conversely every such element has norm $5^4$. The five values of $k$ give pairwise nonassociate elements because $\pi$ and $\bar\pi$ are nonassociate, and multiplying by the four units gives four distinct associates for each $k$. Hence there are $5\cdot4=20$ Gaussian integers of norm $5^4$, equivalently twenty ordered integer pairs $(a,b)$.
:::

<1>4. Therefore the required numbers of representations are
\[
r_2(3^4)=4,
\qquad
r_2(5^4)=20.
\]
::: {.proof}
Combine <1>2 and <1>3.
:::
:::
