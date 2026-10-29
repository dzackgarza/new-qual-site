---
schema: qual/card@1
id: P-DB72D
kind: problem
title: Abelian groups of order 200
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Abelian Groups
  - Structure Theorem
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
Determine the number of abelian groups of order $200$ up to isomorphism, and list all isomorphism classes in invariant factor and elementary divisor forms.
:::

::: {.solution}
Since
$$
200=2^3 5^2,
$$
a finite abelian group of order $200$ is the product of an abelian group of order $2^3$ and one of order $5^2$. The partitions of $3$ are $3$, $2+1$, and $1+1+1$; the partitions of $2$ are $2$ and $1+1$. Hence there are
$$
p(3)p(2)=3\cdot2=6
$$
isomorphism classes.

Their elementary-divisor forms are
$$
\begin{aligned}
&\ZZ_8\times\ZZ_{25},\\
&\ZZ_8\times\ZZ_5\times\ZZ_5,\\
&\ZZ_4\times\ZZ_2\times\ZZ_{25},\\
&\ZZ_4\times\ZZ_2\times\ZZ_5\times\ZZ_5,\\
&\ZZ_2^3\times\ZZ_{25},\\
&\ZZ_2^3\times\ZZ_5^2.
\end{aligned}
$$

Combining relatively prime primary factors gives the corresponding invariant-factor forms
$$
\begin{aligned}
&\ZZ_{200},\\
&\ZZ_5\times\ZZ_{40},\\
&\ZZ_2\times\ZZ_{100},\\
&\ZZ_{10}\times\ZZ_{20},\\
&\ZZ_2\times\ZZ_2\times\ZZ_{50},\\
&\ZZ_2\times\ZZ_{10}\times\ZZ_{10}.
\end{aligned}
$$
In each invariant-factor decomposition, each factor divides the next.
:::
