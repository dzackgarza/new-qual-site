---
schema: qual/card@1
id: E-AMD-J3YZ5TXF
kind: problem
title: The Galois group of $x^n - 2$ over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Roots of Unity
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Corrected the false unrestricted degree product and restricted the dihedral conclusion to the cases actually proved.
---

::: {.exercise}
Let $K=\QQ(2^{1/n},\zeta_n)$, the splitting field of $x^n-2$ over $\QQ$.
Show that
$$
\Gal(K/\QQ)\hookrightarrow (\ZZ/n\ZZ)\rtimes(\ZZ/n\ZZ)^\times
$$
via $\sigma\mapsto(a,b)$, where
$$
\sigma(2^{1/n})=\zeta_n^a2^{1/n},\qquad \sigma(\zeta_n)=\zeta_n^b.
$$
For $n=3,4,6$, show that this embedding is an isomorphism onto the dihedral group of order $2n$.
:::

::: {.solution}
Write $\alpha=2^{1/n}$ and $G=\Gal(K/\QQ)$.

::: pf

::: {.pf-step #sigma-determined-by-pair}
Each $\sigma\in G$ determines a unique pair
$$
(a,b)\in \ZZ/n\ZZ\times(\ZZ/n\ZZ)^\times
$$
by
$$
\sigma(\alpha)=\zeta_n^a\alpha,\qquad \sigma(\zeta_n)=\zeta_n^b.
$$

::: pf-proof
The conjugates of $\alpha$ are the roots $\zeta_n^a\alpha$ of $x^n-2$, and an automorphism sends the primitive $n$th root $\zeta_n$ to another primitive $n$th root. Since $K=\QQ(\alpha,\zeta_n)$, the pair determines $\sigma$ uniquely.
:::

:::

::: pf-step
This gives an injective homomorphism into the affine group.

::: pf-proof
If $\sigma_i$ corresponds to $(a_i,b_i)$, then
$$
(\sigma_1\sigma_2)(\alpha)=\zeta_n^{a_1+b_1a_2}\alpha,
\qquad
(\sigma_1\sigma_2)(\zeta_n)=\zeta_n^{b_1b_2}.
$$
Hence composition corresponds to
$$
(a_1,b_1)(a_2,b_2)=(a_1+b_1a_2,b_1b_2),
$$
the semidirect-product law. Injectivity follows from step [](#sigma-determined-by-pair){.pf-ref}.
:::

:::

::: pf-step
For $n=3,4,6$, the embedding is onto and $G\cong D_n$.

::: pf-proof
For these three values, $\varphi(n)=2$ and
$$
(\ZZ/n\ZZ)^\times=\{\pm1\}.
$$
Also $\QQ(\alpha)\subset\RR$, while $\QQ(\zeta_n)$ is the imaginary quadratic field $\QQ(\sqrt{-3})$ for $n=3,6$ and $\QQ(i)$ for $n=4$. Hence
$$
\QQ(\alpha)\cap\QQ(\zeta_n)=\QQ.
$$
Eisenstein at $2$ gives $[\QQ(\alpha):\QQ]=n$, so
$$
[K:\QQ]=2n.
$$
The target affine group also has order $2n$, hence the injection is an isomorphism. Since the nontrivial unit $-1$ acts on $\ZZ/n\ZZ$ by inversion,
$$
G\cong (\ZZ/n\ZZ)\rtimes\{\pm1\}=D_n.
$$
:::

:::

:::

:::

::: {.remark}
The degree formula $[K:\QQ]=n\varphi(n)$ fails for general $n$, because $\QQ(2^{1/n})\cap\QQ(\zeta_n)$ can be larger than $\QQ$. For $n=8$, with $\alpha=2^{1/8}$,
$$
\sqrt2=\alpha^4\in\QQ(\alpha),
\qquad
\sqrt2=\zeta_8+\zeta_8^{-1}\in\QQ(\zeta_8).
$$
:::
