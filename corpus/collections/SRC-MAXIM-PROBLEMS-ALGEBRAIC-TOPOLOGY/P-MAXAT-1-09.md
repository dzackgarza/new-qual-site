---
schema: qual/card@1
id: P-MAXAT-1-09
kind: problem
title: $\sigma(M)\equiv\chi(M)\pmod 2$ for a closed oriented $4n$-manifold
classification:
  areas: [topology]
  topics:
  - Signature
  - Euler Characteristic
  - Intersection Form
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 1, problem 9 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Let $M$ be a closed, oriented $4n$-dimensional manifold.
Show that the signature $\sigma(M)$ is congruent mod $2$ to the Euler characteristic $\chi(M)$.
:::

::: {.solution}

Let $M$ be a closed oriented manifold of dimension $4n$, and write
$$
b_i=\dim_{\QQ}H^i(M;\QQ).
$$

::: pf

::: {.pf-step #s1-1}

Poincaré duality gives
$$
b_i=b_{4n-i}.
$$


::: pf-proof

The cup-product pairing
$$
H^i(M;\QQ)\times H^{4n-i}(M;\QQ)
\longrightarrow\QQ
$$
obtained by evaluation on the fundamental class is perfect. Hence the paired vector spaces have equal dimensions.

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
\chi(M)\equiv b_{2n}\pmod2.
$$


::: pf-proof

In
$$
\chi(M)=\sum_{i=0}^{4n}(-1)^ib_i,
$$
every degree $i\ne2n$ pairs with $4n-i$. Since $4n$ is even, the two terms in such a pair have the same sign, and by step [](#s1-1){.pf-ref} their sum is
$$
2(-1)^ib_i,
$$
which is even. The only unpaired term is the middle term $b_{2n}$, whose sign is positive.

:::

:::

::: {.pf-step #s1-3}

Let
$$
Q(x,y)=\langle x\smile y,[M]\rangle
$$
be the middle-dimensional intersection form on $H^{2n}(M;\RR)$. If its positive and negative indices are $b_+$ and $b_-$, then
$$
b_{2n}=b_++b_-.
$$


::: pf-proof

Poincaré duality makes $Q$ nondegenerate. Since $2n$ is even, graded commutativity makes it symmetric. By Sylvester's law of inertia, the real vector space decomposes into positive- and negative-definite subspaces of dimensions $b_+$ and $b_-$; nondegeneracy leaves no null subspace. Hence its dimension is $b_++b_-$. Scalar extension from $\QQ$ to $\RR$ does not change dimension, so this is $b_{2n}$.

:::

:::

::: {.pf-step #s1-4}

By definition,
$$
\sigma(M)=b_+-b_-.
$$


::: pf-proof

The signature of a nonsingular real symmetric bilinear form is its number of positive eigenvalues minus its number of negative eigenvalues. The manifold signature is the signature of $Q$.

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\sigma(M)\equiv b_{2n}\pmod2.
$$


::: pf-proof

By steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref},
$$
b_{2n}-\sigma(M)
=(b_++b_-)-(b_+-b_-)
=2b_-,
$$
which is even.

:::

:::

::: {.pf-step #s1-6}

Combining steps [](#s1-2){.pf-ref} and [](#s1-5){.pf-ref} gives
$$
\boxed{\sigma(M)\equiv\chi(M)\pmod2}.
$$


::: pf-proof

Both integers are congruent modulo $2$ to $b_{2n}$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required congruence.

:::

:::

:::
