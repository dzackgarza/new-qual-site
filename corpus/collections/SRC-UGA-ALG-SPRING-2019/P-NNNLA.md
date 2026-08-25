---
schema: qual/card@1
id: P-NNNLA
kind: problem
title: Degree of $\QQ(\zeta_8)$, its quadratic subfields, and $[\QQ(\zeta_8,\sqrt[4]{2}):\QQ]$
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Field Extensions
  - Galois Theory
relations: []
review: draft
---

Let $\zeta = e^{2\pi i/8}$.

a.
What is the degree of $\QQ(\zeta)/\QQ$?

b.
How many quadratic subfields of $\QQ(\zeta)$ are there?

c.
What is the degree of $\QQ(\zeta, \sqrt[4] 2)$ over $\QQ$?

:::{.concept}
\envlist

- $\zeta_n \definedas e^{2\pi i \over n}$, and $\zeta_n^k$ is a primitive $n$th root of unity $\iff \gcd(n, k) = 1$
  - In general, $\zeta_n^k$ is a primitive ${n \over \gcd(n, k)}$th root of unity.
- $\deg \Phi_n(x) = \phi(n)$
- $\phi(p^k) = p^k - p^{k-1} = p^{k-1}(p-1)$ 
  - Proof: for a nontrivial gcd, the possibilities are 
  \[
  p, 2p, 3p, 4p, \cdots, p^{k-2}p, p^{k-1}p
  .\]

- $\Gal(\QQ(\zeta)/\QQ) \cong \ZZ/(n)\units$

:::

:::{.solution}
\envlist

Let $K = \QQ(\zeta)$.

:::{.proof title="of a"}
\envlist

- $\zeta \definedas e^{2\pi i / 8}$ is a primitive $8$th root of unity
- The minimal polynomial of a **primitive** $n$th root of unity is the $n$th cyclotomic polynomial $\Phi_n$
- The degree of the field extension is the degree of $\Phi_8$, which is
\[
\phi(8) = \phi(2^3) = 2^{3-1} \cdot (2-1) = 4
.\]
- So $[\QQ(\zeta): \QQ] = 4$.

:::

:::{.proof title="of b"}
\envlist

- $\Gal(\QQ(\zeta)/\QQ) \cong \ZZ/(8)\units \cong \ZZ/(2) \cross \ZZ/(2)$, the Klein four-group.
  It is **not** $\ZZ/(4)$: every element of $\ZZ/(8)\units = \ts{1,3,5,7}$ squares to $1$, so there is no element of order $4$.
- The Klein four-group has exactly three subgroups of index 2.
- Thus there are exactly **three** intermediate fields of degree 2, namely $\QQ(i)$, $\QQ(\sqrt 2)$ and $\QQ(\sqrt{-2})$.

:::

:::{.proof title="of c"}
\envlist

- Let $L = \QQ(\zeta, \sqrt[4] 2)$.

- Note $\QQ(\zeta) = \QQ(i, \sqrt 2)$
  - $\QQ(i, \sqrt{2})\subseteq \QQ(\zeta)$
    - $\zeta_8^2 = i$, and $\zeta_8 = \sqrt{2}\inv + i\sqrt{2}\inv$ so $\zeta_8 + \zeta_8 \inv = 2/\sqrt{2} = \sqrt{2}$.
  - $\QQ(\zeta) \subseteq \QQ(i, \sqrt{2})$: 
    - $\zeta = e^{2\pi i / 8} = \cos(\pi/4) + i\sin(\pi/4) = {\sqrt 2 \over 2}\qty{1+i}$.

- Thus $L = \QQ(i, \sqrt{2})(\sqrt[4]{2}) = \QQ(i, \sqrt 2, \sqrt[4] 2) = \QQ(i, \sqrt[4]{2})$.
  - Uses the fact that $\QQ(\sqrt 2) \subseteq \QQ(\sqrt[4] 2)$ since $\sqrt[4]{2}^2 = \sqrt{2}$ 

- Conclude
\[
[L: \QQ] = [L: \QQ(\sqrt[4] 2)] ~[\QQ(\sqrt[4] 2): \QQ] = 2 \cdot 4 = 8
\]
  using the fact that the minimal polynomial of $i$ over any subfield of $\RR$ is always $x^2 + 1$, so $\min_{\QQ(\sqrt[4] 2)}(i) = x^2 + 1$ which is degree 2.


:::


:::


