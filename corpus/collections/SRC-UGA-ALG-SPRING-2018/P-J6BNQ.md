---
schema: qual/card@1
id: P-J6BNQ
kind: problem
title: Galois groups of the compositum and intersection of two splitting fields over
  $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Subgroups
relations: []
review: draft
audit:
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Replaced the false commutativity claim and invalid fixed-point equivalence by normal-subgroup and fixed-field arguments.
---

::: problem
Let $K$ be a Galois extension of $\QQ$ with Galois group $G$, and let $E_1 , E_2$ be intermediate fields of $K$ which are the splitting fields of irreducible $f_i (x) \in \QQ[x]$. 

Let $E = E_1 E_2 \subset K$. 

Let $H_i = \Gal(K/E_i)$ and $H = \Gal(K/E)$.

a.
Show that $H = H_1 \cap H_2$.

b.
Show that $H_1 H_2$ is a subgroup of $G$.

c.
Show that 
\[
\Gal(K/(E_1 \cap E_2 )) = H_1 H_2
.\]
:::

:::{.concept}
\envlist

- The Galois correspondence:
  - $H_1 \intersect H_2 \mapstofrom E_1 E_2$, 
  - $H_1 H_2 \mapstofrom E_1 \intersect E_2$.
:::

:::{.solution}
<1>1. $H=H_1\cap H_2$.
::: {.proof}
An automorphism $\sigma\in G$ lies in $H$ exactly when it fixes the compositum $E_1E_2$ pointwise.
This certainly implies that it fixes the subfields $E_1$ and $E_2$, so
\[
H\subseteq H_1\cap H_2.
\]

Conversely, if $\sigma\in H_1\cap H_2$, then $\sigma$ fixes both $E_1$ and $E_2$ pointwise.
Every element of $E_1E_2$ is obtained from elements of $E_1\cup E_2$ by finitely many field operations, and a field automorphism respects these operations.
Hence $\sigma$ fixes $E_1E_2$ pointwise, so $\sigma\in H$.
:::

<1>2. Each $H_i$ is normal in $G$.
::: {.proof}
Each $E_i$ is a splitting field over $\QQ$.
Thus $E_i/\QQ$ is normal, and since $\operatorname{char}\QQ=0$, it is separable as well.
Hence $E_i/\QQ$ is Galois.

By the fundamental theorem of Galois theory for $K/\QQ$, this is equivalent to
\[
H_i=\Gal(K/E_i)\triangleleft G.
\]
:::

<1>3. $H_1H_2$ is a subgroup of $G$.
::: {.proof}
Let $h_1,h_1'\in H_1$ and $h_2,h_2'\in H_2$.
Since $H_1\triangleleft G$ by <1>2,
\[
h_2h_1'h_2^{-1}\in H_1.
\]
Therefore
\[
(h_1h_2)(h_1'h_2')
=h_1(h_2h_1'h_2^{-1})(h_2h_2')\in H_1H_2.
\]
Similarly,
\[
(h_1h_2)^{-1}
=h_2^{-1}h_1^{-1}
=(h_2^{-1}h_1^{-1}h_2)h_2^{-1}\in H_1H_2.
\]
Thus $H_1H_2\le G$.
:::

<1>4. The fixed field of $H_1H_2$ is $E_1\cap E_2$.
::: {.proof}
Since $H_i\subseteq H_1H_2$,
\[
K^{H_1H_2}\subseteq K^{H_1}\cap K^{H_2}=E_1\cap E_2.
\]

Conversely, if $x\in E_1\cap E_2$, then every $h_1\in H_1$ and every $h_2\in H_2$ fixes $x$.
Hence every product $h_1h_2$ fixes $x$, so
\[
E_1\cap E_2\subseteq K^{H_1H_2}.
\]
:::

<1>5. $\Gal(K/(E_1\cap E_2))=H_1H_2$.
::: {.proof}
By <1>3, $H_1H_2$ is a subgroup of $G$, and by <1>4 its fixed field is $E_1\cap E_2$.
The Galois correspondence gives the claimed identity.
:::

:::
