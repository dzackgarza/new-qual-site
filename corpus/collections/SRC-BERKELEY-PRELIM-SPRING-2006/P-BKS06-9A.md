---
schema: qual/card@1
id: P-BKS06-9A
kind: problem
title: UC Berkeley Spring 2006 prelim 9A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $p$ be a prime.
Let G be a finite non-cyclic group of order $p ^ { m }$ for some m. Prove that G has at least $p + 3$ subgroups.
:::

::: {.solution}
We will use the following two facts:

(i) A nontrivial p-group has a nontrivial center Z (nontrivial conjugacy classes have size divisible by $p ,$ as does the whole group, so {1} cannot be the only trivial one).

(ii) If G is a group with center $Z _ { i }$ , and $G / Z$ is cyclic, then G is abelian (since if $a \in G$ generates $G / Z$ , every element of $G$ is of the form $a ^ { n } z$ for some $n \in \mathbb { Z }$ and $z \in Z )$ We use induction on m.

Suppose $m \le 2$ Since G has order 1, $p ,$ or $p ^ { 2 }$ , it is abelian (for order $p ^ { 2 }$ , combine (i) and (ii) above).
Since it is not cyclic, we have $G \simeq \mathbb { Z } / p \mathbb { Z } \times \mathbb { Z } / p \mathbb { Z }$ . So G has one trivial subgroup, $( p ^ { 2 } - 1 ) / ( p - 1 ) = p + \bar { 1 }$ subgroups of order $p ,$ and G itself.
Thus G has exactly $p + 3$ subgroups.

Now suppose $m > 2$ By (i), the center $Z$ of G is nontrivial.
Since G is a nontrivial $p { \mathrm { - g r o u p } }$ , it has a nontrivial center Z. If $G / Z$ is non-cyclic, then by the inductive hypothesis it has $\geq p + 3$ subgroups, and their inverse images in G are distinct subgroups of G. If $G / Z$ is cyclic, then G is abelian by (ii); but G is not cyclic, so by the structure theory of finite abelian groups, it must contain $\mathbb { Z } / p \mathbb { Z } \times \mathbb { Z } / p \mathbb { Z }$ , which already contains $p + 3$ subgroups.
:::
