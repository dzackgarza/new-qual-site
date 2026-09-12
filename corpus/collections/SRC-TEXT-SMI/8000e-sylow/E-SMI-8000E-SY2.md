---
schema: qual/card@1
id: E-SMI-8000E-SY2
kind: problem
title: Every group of order $45$ is abelian
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Sylow Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the card with Smith 8000e Sylow problem 2, including the requested classification up to isomorphism."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Used the Sylow congruence/divisibility conditions to prove both Sylow subgroups normal, then the coprime-order internal direct product and the classification of groups of order 9."
---

::: {.exercise}
Prove every group $G$ of order $45$ is abelian.
[Prove both Sylow subgroups $H,K$ of $G$ are normal. Then prove that $G$ is a direct product $H \times K$. Deduce that every group of order $45$ is abelian, and write down all of them, up to isomorphism.]
:::

::: solution
Write
$$
|G|=45=3^2\cdot5.
$$

<1>1. The Sylow $5$-subgroup is unique and normal.
::: proof
Let $n_5$ be the number of Sylow $5$-subgroups. Sylow's theorem gives
$$
n_5\mid9,
\qquad
n_5\equiv1\pmod5.
$$
The divisors of $9$ are $1,3,9$, and only $1$ is congruent to $1$ modulo
$5$. Hence
$$
n_5=1.
$$
Thus the Sylow $5$-subgroup $K$ is unique, hence normal. Since $|K|=5$,
$$
K\cong C_5.
$$
:::

<1>2. The Sylow $3$-subgroup is unique and normal.
::: proof
Let $n_3$ be the number of Sylow $3$-subgroups. Again Sylow's theorem gives
$$
n_3\mid5,
\qquad
n_3\equiv1\pmod3.
$$
The only divisors of $5$ are $1$ and $5$, and
$5\equiv2\pmod3$. Therefore
$$
n_3=1.
$$
Thus the Sylow $3$-subgroup $H$ is unique and normal, with
$$
|H|=9.
$$
:::

<1>3. The group is the internal direct product of its two Sylow subgroups.
::: proof
Because $|H|=9$ and $|K|=5$ are coprime,
$$
H\cap K=1.
$$
Both $H$ and $K$ are normal, so $HK$ is a subgroup. Its order is
$$
|HK|=\frac{|H||K|}{|H\cap K|}=9\cdot5=45=|G|.
$$
Hence
$$
G=HK.
$$

For $h\in H$ and $k\in K$, normality of both subgroups implies
$$
hkh^{-1}k^{-1}\in H\cap K=1.
$$
Thus every element of $H$ commutes with every element of $K$. Therefore the
multiplication map
$$
H\times K\longrightarrow G,
\qquad
(h,k)\longmapsto hk
$$
is an isomorphism, so
$$
\boxed{G\cong H\times K.}
$$
:::

<1>4. Classify all possibilities.
::: proof
Every group of order $p^2$ is abelian. Hence a group of order $9$ is
isomorphic to exactly one of
$$
C_9,
\qquad
C_3\times C_3.
$$
Since $K\cong C_5$, step <1>3 gives the two possibilities
$$
G\cong C_9\times C_5\cong C_{45}
$$
or
$$
G\cong C_3\times C_3\times C_5.
$$
Both are abelian. Consequently every group of order $45$ is abelian, and,
up to isomorphism, the complete list is
$$
\boxed{C_{45},\qquad C_3\times C_3\times C_5.}
$$
:::
:::
