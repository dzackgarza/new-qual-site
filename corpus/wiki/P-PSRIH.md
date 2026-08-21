---
schema: qual/card@1
id: P-PSRIH
kind: problem
title: Presentation of the nonabelian group of order $63$ with an element of order
  $9$
classification:
  areas:
  - algebra
  topics:
  - Group Presentations
  - Semidirect Products
  - Classification
relations: []
review: draft
solved: true
---

Give generators and relations for the non-commutative group $G$ of order 63 containing an element of order $9 .$

:::{.solution}
\envlist

- Idea: take a semidirect product involving $C_9$ and $C_7$.
  We'll need some facts: $\Hom(C_m, C_n) \cong C_d$ where $d = \gcd(m, n)$, and $\Aut(C_m)\cong C_m\units$ which has order $\phi(m)$ (since one needs to send generators to generators), which can be explicitly calculated based on the prime factorization of $m$.

- Some calculations we'll need:
  - $\Aut(C_9) \cong C_9\units \cong C_{\phi(9)} \cong C_6$, using that $\phi(p^k) = p^{k-1}(p-1)$.
  - $\Aut(C_7) \cong C_7\units \cong C_{\phi(7)}\cong C_6$ using that $\phi(p) = p-1$.
- To get a nonabelian group, we need a nontrivial semidirect product, so look at $\Hom(G, \Aut(H))$ in the two possible combinations.
  - $\Hom(C_7, \Aut(C_9)) \cong \Hom(C_7, C_6) \cong C_1 \da \ts{e}$ using that $\Hom(C_m, C_n) \cong C_{d}$ for $d = \gcd(m, n)$.
    So there are no nontrivial homs here, so only the direct product is possible.
  - $\Hom(C_9, \Aut(C_7)) \cong \Hom(C_9, C_6) \cong C_3$, so use this!
  - Note that we don't have to consider possibilities for $C_3\cross C_3$, since including this as a factor would yield no elements of order 9.

- So take $G\da C_7 \semidirect_\psi C_9$ for some $\psi: C_9 \to \Aut(C_7)$, and we can take the presentation
\[
G = \gens{x, y\st x^7, y^9, yxy\inv = \psi(x)}
.\]

- It now suffices to find a nontrivial $\psi: C_7\to C_7$.
  Writing it multiplicatively as $C_7 = \gens{x\st x^7}$, any map that sends $x$ to a generator will do.
  It suffices to choose any $k$ coprime to $7$, and then take $\psi(x) \da x^k$, which will be another generator.

- So take 

\[
G = \gens{x, y\st x^7, y^9, yxy\inv = x^2}
.\]
:::
