---
schema: qual/card@1
id: P-ALGF21B
kind: problem
title: Groups of order $2^n \cdot 11$ are solvable
classification:
  areas:
  - algebra
  topics:
  - Group Theory
  - Classification
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 2 of the official UCSD Algebra Qualifying Exam, Fall 2021 source; the order hypothesis and the two-case hint agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the Sylow-11 count for n<10 and the coset-action reduction through a solvable 2-group kernel and an image of order 2^r*11 with r at most 8.
---

::: problem
Let $G$ be a group of order $2^n \cdot 11$ for some $n \geq 0$.
Prove that $G$ is solvable.
(Hint: Consider the cases $n < 10$ and $n \geq 10$ separately.
In the latter case, define a group homomorphism $\varphi \colon G \to S_{11}$ and consider its kernel and image.)
:::

::: {.solution}
<1>1. The multiplicative order of $2$ modulo $11$ is $10$.
::: {.proof}
One computes
\[
2^5=32\equiv-1\pmod{11},
\]
so
\[
2^{10}\equiv1\pmod{11}.
\]
The proper positive divisors of $10$ are $1,2,5$, and
\[
2\not\equiv1,
\qquad
2^2=4\not\equiv1,
\qquad
2^5\equiv-1\not\equiv1
\pmod{11}.
\]
Hence the order is exactly $10$.
:::

<1>2. If $0\le n<10$, then the Sylow $11$-subgroup of $G$ is normal.
::: {.proof}
Let $s$ be the number of Sylow $11$-subgroups.
The Sylow theorems give
\[
s\mid 2^n
\qquad\text{and}\qquad
s\equiv1\pmod{11}.
\]
Thus $s=2^j$ for some $0\le j\le n<10$.
By <1>1, among the powers $2^j$ with $0\le j<10$, only $2^0=1$ is congruent to $1$ modulo $11$.
Therefore
\[
s=1.
\]
Hence the Sylow $11$-subgroup is unique and therefore normal.
:::

<1>3. Every group of order $2^n\cdot11$ with $n<10$ is solvable.
::: {.proof}
Let $Q\trianglelefteq G$ be the unique Sylow $11$-subgroup from <1>2.
Then
\[
|Q|=11,
\]
so $Q$ is cyclic and hence solvable.
Also
\[
|G/Q|=2^n,
\]
so $G/Q$ is a finite $2$-group and therefore solvable.
An extension of a solvable group by a solvable group is solvable; hence $G$ is solvable.
:::

<1>4. Assume $n\ge10$, and let $P$ be a Sylow $2$-subgroup of $G$.
The action of $G$ on the left cosets $G/P$ gives a homomorphism
\[
\varphi:G\longrightarrow S_{11}.
\]
::: {.proof}
Since
\[
[G:P]=11,
\]
left multiplication of $G$ on the set $G/P$ of eleven left cosets gives a permutation representation on eleven points, hence a homomorphism to $S_{11}$.
:::

<1>5. The kernel $K:=\ker\varphi$ is a $2$-group, and hence is solvable.
::: {.proof}
Every element of $K$ fixes every coset, in particular the coset $P$.
Thus if $k\in K$, then
\[
kP=P,
\]
so $k\in P$.
Therefore
\[
K\le P.
\]
Since $P$ is a $2$-group, so is $K$; every finite $p$-group is solvable.
:::

<1>6. The image $\varphi(G)$ has order
\[
2^r\cdot11
\]
for some $0\le r\le8$.
::: {.proof}
By <1>5, $K$ is a $2$-group, so $|K|$ is a power of $2$.
The first isomorphism theorem gives
\[
|\varphi(G)|=[G:K]=\frac{2^n\cdot11}{|K|}.
\]
Thus the factor $11$ remains, and
\[
|\varphi(G)|=2^r\cdot11
\]
for some $r\ge0$.

Since $\varphi(G)\le S_{11}$, Lagrange's theorem implies that $2^r$ divides the $2$-part of $11!$.
Legendre's formula gives
\[
v_2(11!)
=\left\lfloor\frac{11}{2}\right\rfloor
+\left\lfloor\frac{11}{4}\right\rfloor
+\left\lfloor\frac{11}{8}\right\rfloor
=5+2+1=8.
\]
Hence $r\le8$.
:::

<1>7. The image $\varphi(G)$ is solvable.
::: {.proof}
By <1>6,
\[
|\varphi(G)|=2^r\cdot11
\]
with $r\le8<10$.
Therefore <1>3 applies to $\varphi(G)$, proving that it is solvable.
:::

<1>8. If $n\ge10$, then $G$ is solvable.
::: {.proof}
By <1>5, the normal subgroup
\[
K=\ker\varphi
\]
is solvable.
By the first isomorphism theorem and <1>7,
\[
G/K\cong\varphi(G)
\]
is solvable.
Therefore $G$ is an extension of a solvable group by a solvable group, and hence is solvable.
:::

<1>9. Consequently every group of order $2^n\cdot11$ is solvable.
::: {.proof}
The case $n<10$ is <1>3, and the case $n\ge10$ is <1>8.
:::
:::
