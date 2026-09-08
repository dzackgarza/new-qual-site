---
schema: qual/card@1
id: P-ALGS26A
kind: problem
title: "Structure of groups of order 5·7·11"
classification:
  areas:
  - algebra
  topics:
  - Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Suppose $G$ is a group of order $5 \cdot 7 \cdot 11$.

(a) Prove that $G \cong (\mathbb{Z}/11\mathbb{Z}) \rtimes (\mathbb{Z}/35\mathbb{Z})$.

(b) Prove that there are exactly two such groups up to isomorphism.
:::


::: {.solution}
**(a).**

<1>1. The Sylow \(11\)-subgroup \(N\) of \(G\) is unique and normal.
::: {.proof}
Its number \(n_{11}\) divides \(35\) and satisfies \(n_{11}\equiv1\pmod{11}\). Among the divisors \(1,5,7,35\), only \(1\) is congruent to \(1\pmod{11}\). Hence \(n_{11}=1\). Since \(|N|=11\), one has \(N\cong C_{11}\).
:::

<1>2. The Sylow \(7\)-subgroup \(R\) of \(G\) is unique and normal.
::: {.proof}
Its number \(n_7\) divides \(55\) and satisfies \(n_7\equiv1\pmod7\). The divisors \(1,5,11,55\) are congruent modulo \(7\) to \(1,5,4,6\), respectively. Thus \(n_7=1\), and \(R\cong C_7\).
:::

<1>3. Let \(P\) be any Sylow \(5\)-subgroup. Then \(H=PR\) is a subgroup of order \(35\).
::: {.proof}
Because \(R\trianglelefteq G\), the product \(PR\) is a subgroup. The groups \(P\) and \(R\) have coprime orders \(5\) and \(7\), so \(P\cap R=1\), and therefore \(|PR|=35\).
:::

<1>4. The group \(H\) is cyclic of order \(35\).
::: {.proof}
Inside a group of order \(35=5\cdot7\), the number of Sylow \(7\)-subgroups divides \(5\) and is \(1\pmod7\), hence is \(1\). The number of Sylow \(5\)-subgroups divides \(7\) and is \(1\pmod5\); since \(7\not\equiv1\pmod5\), it too is \(1\). Thus both Sylow subgroups are normal, so
\[
H\cong C_5\times C_7\cong C_{35}.
\]
:::

<1>5. One has \(G=NH\) and \(N\cap H=1\).
::: {.proof}
The intersection has order dividing both \(11\) and \(35\), so it is trivial. Hence
\[
|NH|=|N||H|=11\cdot35=|G|.
\]
Thus \(NH=G\).
:::

<1>6. Therefore
\[
G\cong C_{11}\rtimes C_{35}.
\]
::: {.proof}
By <1>1, \(N\cong C_{11}\) is normal; by <1>4, \(H\cong C_{35}\); and <1>5 gives \(G=NH\) with trivial intersection. This is exactly an internal semidirect product.
:::

**(b).**

<1>7. The semidirect product is determined by a homomorphism
\[
\varphi:C_{35}\longrightarrow\operatorname{Aut}(C_{11})\cong C_{10}.
\]
Its image has order either \(1\) or \(5\).
::: {.proof}
The image order divides both \(35\) and \(10\), hence divides \(\gcd(35,10)=5\). Thus it is \(1\) or \(5\).
:::

<1>8. If \(\varphi\) is trivial, the resulting group is
\[
C_{11}\times C_{35}\cong C_{385}.
\]
::: {.proof}
A semidirect product with trivial action is the direct product. Since \(11\) and \(35\) are coprime, the direct product of the two cyclic groups is cyclic.
:::

<1>9. All nontrivial actions \(C_{35}\to C_{10}\) give isomorphic semidirect products.
::: {.proof}
The cyclic group \(C_{10}\) has a unique subgroup of order \(5\), so every nontrivial action has that subgroup as its image. Its kernel has order \(7\), hence is the unique subgroup \(C_7\le C_{35}\). Thus a nontrivial action is equivalent to an isomorphism
\[
C_{35}/C_7\cong C_5\longrightarrow C_5\le C_{10}.
\]
Any two such isomorphisms differ by an automorphism of \(C_5\). The reduction map
\[
\operatorname{Aut}(C_{35})\cong(\mathbb Z/35\mathbb Z)^\times
\longrightarrow
(\mathbb Z/5\mathbb Z)^\times\cong\operatorname{Aut}(C_5)
\]
is surjective: for any unit class modulo \(5\), choose by the Chinese remainder theorem a representative congruent to that class modulo \(5\) and to \(1\) modulo \(7\). Precomposing the action by the corresponding automorphism of \(C_{35}\) therefore carries any nontrivial action to any other, and the associated semidirect products are isomorphic.
:::

<1>10. A nontrivial action exists.
::: {.proof}
The group \((\mathbb Z/11\mathbb Z)^\times\cong C_{10}\) contains an element of order \(5\); for example, multiplication by \(3\) has order \(5\) modulo \(11\). Map a generator of \(C_{35}\) to this automorphism.
:::

<1>11. Hence there are exactly two groups of order \(5\cdot7\cdot11\) up to isomorphism: the cyclic group \(C_{385}\) and one nontrivial semidirect product \(C_{11}\rtimes C_{35}\).
::: {.proof}
By <1>6 every such group has this semidirect form. By <1>7 the action is either trivial or nontrivial; <1>8 gives the trivial isomorphism class, while <1>9--<1>10 show that the nontrivial actions constitute exactly one further isomorphism class.
:::
:::
