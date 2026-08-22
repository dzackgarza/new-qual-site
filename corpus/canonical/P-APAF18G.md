---
schema: qual/card@1
id: P-APAF18G
kind: problem
title: Linear independence of standard monomials for a Gröbner basis
classification:
  areas:
  - applied-algebra
  topics:
  - Gröbner Bases
relations: []
review: draft
solved: false
---

::: problem
Let $k$ be a field and let $I\subseteq k[x_1,\ldots,x_n]$ be an ideal.
Fix a monomial order $<$ and let $G=\{g_1,\ldots,g_s\}$ be a Gröbner basis for $I$ with respect to $<$.

(a) Explain why the collection of cosets
\[
\bigl\{m+I:\ m\text{ a monomial in }x_1,\ldots,x_n\text{ and }\operatorname{LM}(g_i)\nmid m\text{ for }1\le i\le s\bigr\}
\]
is linearly independent in the quotient $k[x_1,\ldots,x_n]/I$.

(b) Is the conclusion of (a) still true if $G$ is a basis for $I$ which is not necessarily Gröbner?
Prove or give a counterexample.
:::
