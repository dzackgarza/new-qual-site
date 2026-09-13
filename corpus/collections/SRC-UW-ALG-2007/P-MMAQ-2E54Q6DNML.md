---
schema: qual/card@1
id: P-MMAQ-2E54Q6DNML
kind: problem
title: Exactly two groups of order 21
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
Show there are exactly two groups of order 21 up to isomorphism.
:::

::: solution
<1>1. Let $G$ be a group of order
\[
21=3\cdot7.
\]
Then $G$ has a unique Sylow $7$-subgroup $N$.
::: {.proof}
If $n_7$ denotes the number of Sylow $7$-subgroups, the Sylow theorems give
\[
n_7\equiv1\pmod7,
\qquad
n_7\mid3.
\]
The only possibility is $n_7=1$. Hence $N\trianglelefteq G$, and since $|N|=7$, we have
\[
N\cong C_7.
\]
:::

<1>2. Let $H$ be a Sylow $3$-subgroup. Then
\[
H\cong C_3,
\qquad
N\cap H=1,
\qquad
G=NH.
\]
::: {.proof}
Since $|H|=3$, the group $H$ is cyclic. The intersection $N\cap H$ has order dividing both $7$ and $3$, hence is trivial. Therefore
\[
|NH|=\frac{|N||H|}{|N\cap H|}=21=|G|,
\]
so $NH=G$.
:::

<1>3. Thus every group of order $21$ is a semidirect product
\[
G\cong C_7\rtimes_\varphi C_3
\]
for some homomorphism
\[
\varphi:C_3\longrightarrow\operatorname{Aut}(C_7).
\]
::: {.proof}
By <1>1, $N$ is normal, and by <1>2, $G=NH$ with $N\cap H=1$. Conjugation by $H$ on $N$ gives the homomorphism $\varphi$, and these data identify $G$ with the corresponding internal semidirect product.
:::

<1>4. If $\varphi$ is trivial, then
\[
G\cong C_7\times C_3\cong C_{21}.
\]
::: {.proof}
A trivial conjugation action means every element of $H$ commutes with every element of $N$, so the semidirect product is direct. Since $3$ and $7$ are coprime, the direct product of cyclic groups $C_7\times C_3$ is cyclic of order $21$.
:::

<1>5. Up to isomorphism, there is exactly one nontrivial semidirect product $C_7\rtimes C_3$.
::: {.proof}
We have
\[
\operatorname{Aut}(C_7)\cong(\mathbb Z/7\mathbb Z)^\times\cong C_6.
\]
A nontrivial homomorphism $C_3\to C_6$ must be injective, and its image must be a subgroup of order $3$. A cyclic group has a unique subgroup of each order dividing its order, so $C_6$ has exactly one subgroup of order $3$.

There are two injections $C_3\to C_6$ with that image, according to which of the two generators of the image is assigned to a chosen generator of $C_3$. They differ by the automorphism of $C_3$ sending a generator to its inverse, and precomposing a semidirect-product action by an automorphism of the acting group yields an isomorphic semidirect product. Hence there is exactly one isomorphism class arising from a nontrivial action.

Explicitly, if
\[
C_7=\langle a\rangle,
\qquad
C_3=\langle b\rangle,
\]
then multiplication by $2$ modulo $7$ has order $3$, because
\[
2^3\equiv1\pmod7,
\qquad
2\not\equiv1\pmod7.
\]
Thus the unique nonabelian group may be presented as
\[
\langle a,b\mid a^7=b^3=1,\;bab^{-1}=a^2\rangle.
\]
:::

<1>6. The two groups in <1>4 and <1>5 are not isomorphic.
::: {.proof}
The group in <1>4 is abelian. In the group from <1>5,
\[
bab^{-1}=a^2\ne a,
\]
so $a$ and $b$ do not commute; hence it is nonabelian.
:::

<1>7. Therefore there are exactly two groups of order $21$ up to isomorphism:
\[
\boxed{C_{21}}
\qquad\text{and}\qquad
\boxed{C_7\rtimes C_3\text{ with nontrivial action}}.
\]
:::
