---
schema: qual/card@1
id: P-J9BHP
kind: problem
title: The characteristic of an integral domain is zero or prime
classification:
  areas:
  - algebra
  topics:
  - Integral Domains
  - Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Show that the characteristic of an integral domain must be either zero or a prime.
:::

::: {.solution}
Let $R$ be an integral domain with identity $1_R\ne0$.

<1>1. If $\operatorname{char}(R)>0$, then $\operatorname{char}(R)$ is prime.
::: {.proof}
Write
$$
n=\operatorname{char}(R)>0.
$$
By definition, $n$ is the least positive integer such that
$$
n\cdot1_R=0.
$$
Since $1_R\ne0$, one has $n\ge2$.

Suppose, for contradiction, that $n$ is composite. Then
$$
n=ab
$$
for integers $a,b$ with
$$
1<a<n,
\qquad
1<b<n.
$$
In $R$,
$$
(a\cdot1_R)(b\cdot1_R)
=(ab)\cdot1_R
=n\cdot1_R
=0.
$$
Because $R$ is an integral domain, it has no zero divisors. Hence
$$
a\cdot1_R=0
\qquad\text{or}\qquad
b\cdot1_R=0.
$$
Either alternative contradicts the minimality of $n$. Thus $n$ is prime.
:::

<1>2. Therefore
$$
\boxed{\operatorname{char}(R)=0\text{ or }\operatorname{char}(R)\text{ is prime}}.
$$
::: {.proof}
If the characteristic is zero, this is one of the two stated alternatives. If it is positive, step <1>1 shows that it is prime.
:::

<1>3. Q.E.D.
::: {.proof}
Step <1>2 is the required conclusion.
:::
:::
