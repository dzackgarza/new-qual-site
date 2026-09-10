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
Let $K=\mathbb Q(2^{1/n},\zeta_n)$, the splitting field of $x^n-2$ over $\mathbb Q$.
Show that
\[
\operatorname{Gal}(K/\mathbb Q)\hookrightarrow (\mathbb Z/n\mathbb Z)\rtimes(\mathbb Z/n\mathbb Z)^\times
\]
via $\sigma\mapsto(a,b)$, where
\[
\sigma(2^{1/n})=\zeta_n^a2^{1/n},\qquad \sigma(\zeta_n)=\zeta_n^b.
\]
For $n=3,4,6$, show that this embedding is an isomorphism onto the dihedral group of order $2n$.

> The commonly attempted further deduction $[K:\mathbb Q]=n\varphi(n)$ for all $n$ is false in general; the intersection $\mathbb Q(2^{1/n})\cap\mathbb Q(\zeta_n)$ can be nontrivial.
:::

::: {.solution}
Write $\alpha=2^{1/n}$ and $G=\operatorname{Gal}(K/\mathbb Q)$.

<1>1. Each $\sigma\in G$ determines a unique pair
\[
(a,b)\in \mathbb Z/n\mathbb Z\times(\mathbb Z/n\mathbb Z)^\times
\]
by
\[
\sigma(\alpha)=\zeta_n^a\alpha,\qquad \sigma(\zeta_n)=\zeta_n^b.
\]
::: {.proof}
The conjugates of $\alpha$ are the roots $\zeta_n^a\alpha$ of $x^n-2$, and an automorphism sends the primitive $n$th root $\zeta_n$ to another primitive $n$th root. Since $K=\mathbb Q(\alpha,\zeta_n)$, the pair determines $\sigma$ uniquely.
:::

<1>2. This gives an injective homomorphism into the affine group.
::: {.proof}
If $\sigma_i$ corresponds to $(a_i,b_i)$, then
\[
(\sigma_1\sigma_2)(\alpha)=\zeta_n^{a_1+b_1a_2}\alpha,
\qquad
(\sigma_1\sigma_2)(\zeta_n)=\zeta_n^{b_1b_2}.
\]
Hence composition corresponds to
\[
(a_1,b_1)(a_2,b_2)=(a_1+b_1a_2,b_1b_2),
\]
the semidirect-product law. Injectivity follows from <1>1.
:::

<1>3. For $n=3,4,6$, the embedding is onto and $G\cong D_n$.
::: {.proof}
For these three values, $\varphi(n)=2$ and
\[
(\mathbb Z/n\mathbb Z)^\times=\{\pm1\}.
\]
Also $\mathbb Q(\alpha)\subset\mathbb R$, while $\mathbb Q(\zeta_n)$ is the imaginary quadratic field $\mathbb Q(\sqrt{-3})$ for $n=3,6$ and $\mathbb Q(i)$ for $n=4$. Hence
\[
\mathbb Q(\alpha)\cap\mathbb Q(\zeta_n)=\mathbb Q.
\]
Eisenstein at $2$ gives $[\mathbb Q(\alpha):\mathbb Q]=n$, so
\[
[K:\mathbb Q]=2n.
\]
The target affine group also has order $2n$, hence the injection is an isomorphism. Since the nontrivial unit $-1$ acts on $\mathbb Z/n\mathbb Z$ by inversion,
\[
G\cong (\mathbb Z/n\mathbb Z)\rtimes\{\pm1\}=D_n.
\]
:::

<1>4. The degree formula $[K:\mathbb Q]=n\varphi(n)$ cannot be used for arbitrary $n$.
::: {.proof}
For example, when $n=8$,
\[
\sqrt2=\alpha^4\in\mathbb Q(\alpha),
\qquad
\sqrt2=\zeta_8+\zeta_8^{-1}\in\mathbb Q(\zeta_8).
\]
Thus the two subfields have nontrivial intersection, so their degrees do not multiply. This invalidates the original unrestricted degree argument.
:::
:::
