---
schema: qual/card@1
id: P-TATE85-X7-01
kind: problem
title: Galois groups of degree 7 polynomials with square discriminant and three real roots
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed part (I) from the page headed X^7 - 7X + 3 in Tate_Galois_Theory_Problems.pdf; the OCR had glued math delimiters to words and dropped TeX into prose.
---

::: {.problem}
Suppose $f(X) \in \mathbb{Z}[X]$ is monic irreducible of degree $7$, has a square discriminant, and has exactly three real roots.
Prove that $G_f$ is isomorphic either to $A_7$ or to the group $G_{168} = \mathrm{GL}(3, \mathbb{F}_2) \cong \mathrm{PSL}(2, \mathbb{F}_7)$.
Note that $G_{168}$ is isomorphic to a subgroup of $S_7$, in fact of $A_7$, via the action of $G_{168} = \mathrm{GL}_3(\mathbb{F}_2)$ on the $7$ nonzero vectors in $\mathbb{F}_2^3$.

(By considering Sylow subgroups, especially the ones for $7$, this can be done from scratch without too much trouble.
But it is even easier if you know that the only non-abelian simple groups of order $< 1000$ are $A_5$ of order $60 = 2^2 \cdot 3 \cdot 5$, $G_{168}$ of order $168 = 2^3 \cdot 3 \cdot 7$, $A_6$ of order $360 = 2^3 \cdot 3^2 \cdot 5$, $\mathrm{PSL}(2, \mathbb{F}_8)$ of order $504 = 2^3 \cdot 3^2 \cdot 7$, and $\mathrm{PSL}(2, \mathbb{F}_{11})$ of order $660 = 2^2 \cdot 3 \cdot 5 \cdot 11$.)
:::
