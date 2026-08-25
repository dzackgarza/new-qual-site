---
schema: qual/card@1
id: P-APA24I
kind: problem
title: Monomials outside leading terms of a Gröbner basis span the quotient
classification:
  areas:
  - applied-algebra
  topics:
  - Gröbner Bases
relations: []
review: draft
---

::: problem
Let $k$ be a field and let $I \subseteq k[x_1, \ldots, x_n]$ be an ideal.
Fix a monomial order $<$ and let $G = \{g_1, \ldots, g_r\}$ be a Gröbner basis of $I$ with respect to $<$.
Consider the set of monomials
\[
\mathcal{M} := \{ \text{monomials } m = x_1^{a_1} \cdots x_n^{a_n} : \operatorname{LT}(g_i) \nmid m \text{ for } 1 \leq i \leq r \}.
\]
Here $\operatorname{LT}(g_i)$ is the leading term of $g_i$ with respect to the monomial order $<$.

(a) Prove that $\mathcal{M}$ descends to a spanning set of the $k$-vector space $k[x_1, \ldots, x_n]/I$.

(b) If $G$ is a basis of $I$ which is not necessarily Gröbner, does the set $\mathcal{M}$ necessarily span $k[x_1, \ldots, x_n]/I$?
Prove or give a counterexample.
:::
