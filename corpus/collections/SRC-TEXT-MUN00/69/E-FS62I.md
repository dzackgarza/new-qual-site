---
schema: qual/card@1
id: E-FS62I
kind: problem
title: Direct sums of cyclic groups are not determined by their factors
classification:
  areas:
  - topology
  topics:
  - Free Products
relations: []
review: draft
---

::: {.exercise}

Show that if $G = G_1 \oplus G_2$, where $G_1$ and $G_2$ are cyclic of orders $m$ and $n$, respectively, then $m$ and $n$ are not uniquely determined by $G$ in general.
[Hint: If $m$ and $n$ are relatively prime, show that $G$ is cyclic of order $mn$.]
:::

::: {.solution}
Let
\[
G_1\cong C_m,\qquad G_2\cong C_n,
\]
with \(\gcd(m,n)=1\). Then the element
\[
(\bar 1,\bar 1)\in C_m\oplus C_n
\]
has order \(\operatorname{lcm}(m,n)=mn\). Since \(|C_m\oplus C_n|=mn\), this element generates the whole group. Hence
\[
C_m\oplus C_n\cong C_{mn}.
\]
Equivalently, this is the Chinese remainder isomorphism
\[
\mathbb Z/(mn)\longrightarrow \mathbb Z/m\oplus\mathbb Z/n,
\qquad [a]_{mn}\longmapsto([a]_m,[a]_n).
\]

Therefore the orders of two cyclic direct-summand factors are not determined by the abstract group. For example,
\[
C_2\oplus C_{15}\cong C_{30}\cong C_3\oplus C_{10},
\]
while the unordered pairs of factor orders are \(\{2,15\}\) and \(\{3,10\}\), which are different.

Thus \(m\) and \(n\) are not uniquely determined by \(G\) in general.
:::
