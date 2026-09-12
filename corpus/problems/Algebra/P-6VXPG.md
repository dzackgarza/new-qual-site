---
schema: qual/card@1
id: P-6VXPG
kind: problem
title: Roots of an integer polynomial with Galois group $S_n$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Permutations
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Let $f(x) \in \mathbb{Z}[x]$ be an irreducible polynomial of degree $n \ge 2$, and let $K/\mathbb{Q}$ be its splitting field with $\operatorname{Gal}(K/\mathbb{Q}) \cong S_n$.
What algebraic, geometric, and field-theoretic properties must the roots $\alpha_1, \alpha_2, \dots, \alpha_n \in \mathbb{C}$ of $f(x)$ satisfy?
:::

::: solution
Let \(K\) be the splitting field and identify \(G=\operatorname{Gal}(K/\mathbb Q)\) with the full permutation group \(S_n\) on the roots.

Since the characteristic is \(0\), the roots \(\alpha_1,\dots,\alpha_n\) are distinct. Irreducibility gives transitivity, hence each root has degree
\[
[\mathbb Q(\alpha_i):\mathbb Q]=n.
\]
More generally, after ordering the roots, the pointwise stabilizer of \(\alpha_1,\dots,\alpha_k\) is naturally \(S_{n-k}\). By Galois correspondence,
\[
[\mathbb Q(\alpha_1,\dots,\alpha_k):\mathbb Q]
=[S_n:S_{n-k}]=\frac{n!}{(n-k)!}
\]
for \(0\le k\le n-1\); adjoining the last root does not enlarge the field. In particular \([K:\mathbb Q]=n!\).

Every polynomial relation over \(\mathbb Q\) among the ordered roots is transported to another valid relation by every permutation in \(S_n\): if
\(P(\alpha_1,\dots,\alpha_n)=0\), then
\[
P(\alpha_{\sigma(1)},\dots,\alpha_{\sigma(n)})=0
\quad(\sigma\in S_n).
\]
This symmetry does **not** mean that all relations are symmetric polynomials; it says only that the set of rational relations is \(S_n\)-stable.

The discriminant \(\Delta(f)\) is not a square in \(\mathbb Q\), because otherwise the Galois group would lie in \(A_n\). For \(n\ge3\), the unique index-two subgroup of \(S_n\) is \(A_n\), so the unique quadratic intermediate field is
\[
\mathbb Q(\sqrt{\Delta(f)}).
\]
(For \(n=2\), this statement is the same quadratic extension itself.)

Finally, complex conjugation is an element of \(G\); as a permutation of the roots it fixes the real roots and swaps each nonreal conjugate pair. Thus its cycle type records exactly the number of real and nonreal roots.
:::
