---
schema: qual/card@1
id: P-ICQ5R
kind: problem
title: Splitting field and Galois correspondence for $x^4-4x^2+2$
classification:
  areas:
  - algebra
  topics:
  - galois-theory
  - splitting-fields
  - field-extensions
relations: []
review: draft
solved: true
---

::: problem
Let $f(x) = x^4 - 4x^2 + 2 \in \QQ[x]$.

(a) Find the splitting field $K$ of $f$, and compute $[K: \QQ]$.

(b) Find the Galois group $G$ of $f$, both as an explicit group of automorphisms, and as a familiar abstract group to which it is isomorphic.

(c) Exhibit explicitly the correspondence between subgroups of $G$ and intermediate fields between $\QQ$ and $k$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**(a) Splitting field and extension degree:** The polynomial $f(x) = x^4 - 4x^2 + 2$ is irreducible over $\QQ$ by Eisenstein's criterion with $p = 2$.
By the quadratic formula in $x^2$:
$$
x^2 = \frac{4 \pm \sqrt{16 - 8}}{2} = 2 \pm \sqrt 2.
$$
The four roots of $f(x)$ are:
$$
\alpha_1 = \sqrt{2+\sqrt 2}, \quad \alpha_2 = -\sqrt{2+\sqrt 2}, \quad \alpha_3 = \sqrt{2-\sqrt 2}, \quad \alpha_4 = -\sqrt{2-\sqrt 2}.
$$
Notice that:
$$
\alpha_1 \alpha_3 = \sqrt{(2+\sqrt 2)(2-\sqrt 2)} = \sqrt{4 - 2} = \sqrt 2 = \alpha_1^2 - 2 \in \QQ(\alpha_1).
$$
Thus $\alpha_3 = \frac{\alpha_1^2 - 2}{\alpha_1} \in \QQ(\alpha_1)$, so all four roots lie in $\QQ(\alpha_1)$.
Therefore, the splitting field is:
$$
K = \QQ\left(\sqrt{2+\sqrt 2}\right),
$$
and $[K : \QQ] = \deg(f) = 4$.

**(b) Galois group $G = \Gal(K/\QQ)$:** Since $K/\QQ$ is the splitting field of an irreducible separable polynomial of degree 4, $|G| = 4$.
An automorphism $\sigma \in G$ is determined by its action on $\alpha_1$.
Since $f$ is irreducible, there exists $\sigma \in G$ such that $\sigma(\alpha_1) = \alpha_3 = \sqrt{2-\sqrt 2}$.
Then:
$$
\sigma(\sqrt 2) = \sigma(\alpha_1^2 - 2) = \alpha_3^2 - 2 = (2 - \sqrt 2) - 2 = -\sqrt 2.
$$
Hence:
$$
\sigma(\alpha_3) = \sigma\left(\frac{\sqrt 2}{\alpha_1}\right) = \frac{-\sqrt 2}{\alpha_3} = -\alpha_1 = \alpha_2.
$$
$$
\sigma^2(\alpha_1) = \sigma(\alpha_3) = -\alpha_1, \quad \sigma^3(\alpha_1) = \sigma(-\alpha_1) = -\alpha_3 = \alpha_4, \quad \sigma^4(\alpha_1) = \alpha_1.
$$
Thus $\sigma$ generates a cyclic group of order 4:
$$
G = \langle \sigma \rangle \cong \ZZ_4.
$$

**(c) Galois correspondence:** Since $G \cong \ZZ_4$, the subgroups of $G$ are:

1. $G = \langle \sigma \rangle$ of order 4 (index 1)

2. $H = \langle \sigma^2 \rangle = \{\id, \sigma^2\}$ of order 2 (index 2)

3. $\{e\} = \{\id\}$ of order 1 (index 4)

The corresponding intermediate subfields $\QQ \subseteq K^H \subseteq K$ are:

1. $K^G = \QQ$ (degree 1 over $\QQ$)

2. $K^H = \QQ(\sqrt 2)$ (degree 2 over $\QQ$), because $\sigma^2(\sqrt 2) = \sigma(-\sqrt 2) = \sqrt 2$, so $\sqrt 2$ is fixed by $\sigma^2$, whereas $\sigma^2(\alpha_1) = -\alpha_1 \neq \alpha_1$.

3. $K^{\{e\}} = K = \QQ\left(\sqrt{2+\sqrt 2}\right)$ (degree 4 over $\QQ$).
:::
