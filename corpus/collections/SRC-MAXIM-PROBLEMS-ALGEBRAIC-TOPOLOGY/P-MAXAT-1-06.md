---
schema: qual/card@1
id: P-MAXAT-1-06
kind: problem
title: A closed odd-dimensional manifold has Euler characteristic zero
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 1, problem 6 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
The Euler characteristic of a closed manifold of odd dimension is zero.
:::

::: {.solution}

Let $M$ be a closed $n$-manifold with $n$ odd. Work with coefficients in $\FF_2$, so orientability is irrelevant.

::: pf

::: {.pf-step #s1-1}

Poincaré duality gives
$$
H_i(M;\FF_2)
\cong H^{n-i}(M;\FF_2)
$$
for every $i$.


::: pf-proof

Every manifold is orientable over $\FF_2$. Since $M$ is closed, mod-$2$ Poincaré duality identifies homology in degree $i$ with cohomology in complementary degree $n-i$.

:::

:::

::: {.pf-step #s1-2}

Therefore the Betti numbers satisfy
$$
b_i=b_{n-i}.
$$


::: pf-proof

Over the field $\FF_2$, the universal coefficient theorem gives
$$
\dim H^{n-i}(M;\FF_2)
=\dim H_{n-i}(M;\FF_2).
$$
Take dimensions in the duality isomorphism from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

The Euler characteristic is
$$
\chi(M)=\sum_{i=0}^{n}(-1)^ib_i.
$$


::: pf-proof

For a finite CW model of the compact manifold $M$, Euler characteristic equals the alternating sum of homology dimensions over any field.

:::

:::

::: {.pf-step #s1-4}

Pairing the $i$th and $(n-i)$th terms gives zero.


::: pf-proof

Because $n$ is odd, $i\ne n-i$ for every integer $i$, and
$$
(-1)^{n-i}=-(-1)^i.
$$
By step [](#s1-2){.pf-ref}, $b_{n-i}=b_i$. Hence
$$
(-1)^ib_i+(-1)^{n-i}b_{n-i}=0.
$$

:::

:::

::: {.pf-step #s1-5}

Consequently
$$
\boxed{\chi(M)=0}.
$$


::: pf-proof

The finite sum in step [](#s1-3){.pf-ref} decomposes into the cancelling pairs from step [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves the claim for every closed odd-dimensional manifold, orientable or not.

:::

:::

:::
