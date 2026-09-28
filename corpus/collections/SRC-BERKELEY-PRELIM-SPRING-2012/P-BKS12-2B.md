---
schema: qual/card@1
id: P-BKS12-2B
kind: problem
title: Structure of $(\mathbb Z/2012\mathbb Z)^\times$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 4 of the retained Spring 2012 solution PDF and independently reviewed the CRT decomposition.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the unit-group factors modulo 4 and 503 and the coprime splitting of the cyclic group of order 502.
---

::: {.problem}
Let G be the group $( \ZZ / 2012 \ZZ ) ^ { * }$ (this is the group whose elements are classes a (mod 2012) with $\gcd ( a , 2012 ) = 1$ , and whose group operation is multiplication modulo 2012).

Determine the structure of G as an abstract abelian group.
When doing so, break it down into as many (nontrivial) pieces as possible.

Note that 2012 has prime factorization $2 ^ { 2 } \cdot 503$, and that 502 has prime factorization $2 \cdot 251$
:::

::: {.solution}
<1>1. The Chinese remainder theorem gives
$$
(\ZZ/2012\ZZ)^\times
\cong
(\ZZ/4\ZZ)^\times
\times
(\ZZ/503\ZZ)^\times.
$$

::: {.proof}
Since
$$
2012=4\cdot503
$$
and
$$
\gcd(4,503)=1,
$$
the Chinese remainder theorem gives a ring isomorphism
$$
\ZZ/2012\ZZ
\cong
\ZZ/4\ZZ
\times
\ZZ/503\ZZ.
$$
An element in a product ring is a unit exactly when each coordinate is a
unit, so restricting the isomorphism to unit groups gives the claim.
:::

<1>2. One has
$$
(\ZZ/4\ZZ)^\times\cong C_2.
$$

::: {.proof}
The two units modulo $4$ are
$$
1
\qquad\text{and}\qquad
3.
$$
The nonidentity element satisfies
$$
3^2\equiv1\pmod4,
$$
so the group is cyclic of order $2$.
:::

<1>3. One has
$$
(\ZZ/503\ZZ)^\times\cong C_{502}.
$$

::: {.proof}
The number $503$ is prime, so
$$
\ZZ/503\ZZ=\FF_{503}
$$
is a finite field. Its multiplicative group of nonzero elements is cyclic
and has
$$
503-1=502
$$
elements.
:::

<1>4. The cyclic group $C_{502}$ decomposes as
$$
C_{502}\cong C_2\times C_{251}.
$$

::: {.proof}
Since
$$
502=2\cdot251
$$
with
$$
\gcd(2,251)=1,
$$
the Chinese remainder theorem for cyclic groups gives
$$
\ZZ/502\ZZ
\cong
\ZZ/2\ZZ
\times
\ZZ/251\ZZ.
$$
:::

<1>5. Therefore
$$
\boxed{
(\ZZ/2012\ZZ)^\times
\cong
C_2\times C_2\times C_{251}
}.
$$

::: {.proof}
Combine steps <1>1--<1>4:
$$
\begin{aligned}
(\ZZ/2012\ZZ)^\times
&\cong
C_2\times C_{502}\\
&\cong
C_2\times C_2\times C_{251}.
\end{aligned}
$$
The displayed factors all have prime order, so this is split into as many
nontrivial cyclic factors as possible.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required abstract-group structure.
:::
:::
