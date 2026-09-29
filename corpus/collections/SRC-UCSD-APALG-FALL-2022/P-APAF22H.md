---
schema: qual/card@1
id: P-APAF22H
kind: problem
title: Class-sum scalars $\omega_\alpha^\lambda$ and the transposition class in $\mathbb{C}S(d)$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
relations: []
review: draft
---

::: {.problem}
Given a Young diagram $\alpha \vdash d$, identify the corresponding conjugacy class $C_\alpha \subset S(d)$ with the formal sum of its elements, so that it becomes an element of the group algebra $\mathbb{C}S(d)$.
Given another Young diagram $\lambda \vdash d$, show that $C_\alpha$ acts in the corresponding irreducible representation $V_\lambda$ of $\mathbb{C}S(d)$ as multiplication by a scalar $\omega_\alpha^\lambda$, and compute this number in terms of the character of $V_\lambda$.
Now, compute $\omega_\alpha^\lambda$ explicitly in the case $\alpha = (2,1^{d-2})$, corresponding to the conjugacy class of transpositions.
:::

::: {.solution}

Let
\[
K_\alpha:=\sum_{g\in C_\alpha}g\in\mathbb C S_d.
\]

::: pf

::: {.pf-step #class-sum-is-central}
The element $K_\alpha$ is central in $\mathbb C S_d$.

::: pf-proof
For $h\in S_d$,
\[
hK_\alpha h^{-1}
=\sum_{g\in C_\alpha}hgh^{-1}.
\]
Conjugation by $h$ permutes the elements of the conjugacy class $C_\alpha$, so the sum is again $K_\alpha$.
:::

:::

::: {.pf-step #class-sum-acts-by-scalar}
On the irreducible $S_d$-module $V^\lambda$, the class sum $K_\alpha$ acts by a scalar $\omega_\alpha^\lambda$.

::: pf-proof
By step [](#class-sum-is-central){.pf-ref}, the operator afforded by $K_\alpha$ commutes with every operator in the irreducible representation $V^\lambda$. Schur's lemma therefore implies that it is scalar.
:::

:::

::: {.pf-step #scalar-formula-general}
If $f^\lambda=\dim V^\lambda$ and $\chi^\lambda$ is its character, then
\[
\boxed{\omega_\alpha^\lambda
=\frac{|C_\alpha|\,\chi^\lambda(\alpha)}{f^\lambda}}
=\frac{d!}{z_\alpha}\frac{\chi^\lambda(\alpha)}{f^\lambda},
\]
where $z_\alpha=\prod_i i^{m_i}m_i!$ for $\alpha=(1^{m_1}2^{m_2}\cdots)$.

::: pf-proof
Taking traces in step [](#class-sum-acts-by-scalar){.pf-ref} gives
\[
\omega_\alpha^\lambda f^\lambda
=\operatorname{tr}_{V^\lambda}(K_\alpha)
=\sum_{g\in C_\alpha}\chi^\lambda(g)
=|C_\alpha|\chi^\lambda(\alpha).
\]
The class-size formula is $|C_\alpha|=d!/z_\alpha$.
:::

:::

::: {.pf-step #jm-element-decomposition}
For the transposition class $\alpha=(2,1^{d-2})$, let
\[
X_k:=\sum_{i<k}(i\ k)\in\mathbb C S_d
\qquad(1\le k\le d).
\]
Then
\[
K_{(2,1^{d-2})}=\sum_{k=1}^d X_k.
\]
Moreover, in the Young seminormal basis $(v_T)$ of $V^\lambda$ indexed by standard tableaux $T$ of shape $\lambda$,
\[
X_kv_T=c_T(k)v_T,
\]
where $c_T(k)=j-i$ if the box containing $k$ lies in row $i$ and column $j$.

::: pf-proof
The first identity is immediate because every transposition $(i\ k)$ with $i<k$ occurs exactly once in the double sum.
The second statement is the Young--Jucys--Murphy eigenvalue theorem for Specht modules; see A. Okounkov and A. Vershik, *A New Approach to the Representation Theory of the Symmetric Groups. 2*, arXiv:math/0503040, Section 5.
:::

:::

::: {.pf-step #transposition-scalar-as-content-sum}
Therefore the transposition class sum acts on $V^\lambda$ by
\[
\omega_{(2,1^{d-2})}^\lambda
=\sum_{(i,j)\in\lambda}(j-i).
\]

::: pf-proof
For any standard tableau $T$ of shape $\lambda$, step [](#jm-element-decomposition){.pf-ref} gives
\[
K_{(2,1^{d-2})}v_T
=\sum_{k=1}^d c_T(k)v_T.
\]
As $k$ runs from $1$ to $d$, the boxes containing $k$ run through all boxes of the Young diagram exactly once. Hence
\[
\sum_{k=1}^d c_T(k)=\sum_{(i,j)\in\lambda}(j-i),
\]
which depends only on the shape $\lambda$, not on $T$. Thus this is the scalar from step [](#class-sum-acts-by-scalar){.pf-ref}.
:::

:::

::: {.pf-step #transposition-scalar-explicit}
Equivalently,
\[
\boxed{
\omega_{(2,1^{d-2})}^\lambda
=\sum_i\binom{\lambda_i}{2}-\sum_j\binom{\lambda'_j}{2}
=\frac12\sum_i\lambda_i(\lambda_i-2i+1).}
\]

::: pf-proof
Summing column indices minus row indices over the Young diagram gives
\[
\sum_{(i,j)\in\lambda}(j-i)
=\sum_i\sum_{j=1}^{\lambda_i}(j-1)
-\sum_j\sum_{i=1}^{\lambda'_j}(i-1),
\]
which is
\[
\sum_i\binom{\lambda_i}{2}-\sum_j\binom{\lambda'_j}{2}.
\]
Alternatively, summing row by row,
\[
\sum_{j=1}^{\lambda_i}(j-i)
=\frac{\lambda_i(\lambda_i+1)}2-i\lambda_i
=\frac12\lambda_i(\lambda_i-2i+1),
\]
and summing over $i$ gives the last expression.
:::

:::

::: pf-step
Combining steps [](#scalar-formula-general){.pf-ref} and [](#transposition-scalar-explicit){.pf-ref} yields the equivalent character-ratio formula
\[
\frac{\chi^\lambda(2,1^{d-2})}{f^\lambda}
=\frac{1}{\binom d2}
\left(
\sum_i\binom{\lambda_i}{2}-\sum_j\binom{\lambda'_j}{2}
\right).
\]

::: pf-proof
The transposition class has size $\binom d2$. Substitute this and the scalar from step [](#transposition-scalar-explicit){.pf-ref} into the general formula of step [](#scalar-formula-general){.pf-ref}.
:::

:::

::: pf-qed
Step [](#scalar-formula-general){.pf-ref} identifies $C_\alpha$ and gives $\omega_\alpha^\lambda$ in general; step [](#transposition-scalar-explicit){.pf-ref} gives $\omega_{(2,1^{d-2})}^\lambda$ explicitly.
:::

:::

:::
