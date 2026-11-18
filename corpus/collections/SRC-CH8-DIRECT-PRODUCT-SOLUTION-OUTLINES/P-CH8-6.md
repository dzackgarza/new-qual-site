---
schema: qual/card@1
id: P-CH8-6
kind: problem
title: $\ZZ_8\oplus\ZZ_2\not\cong\ZZ_4\oplus\ZZ_4$
classification:
  areas:
    - algebra
  topics:
    - Direct Products
relations: []
review: draft
---

::: {.problem}
Prove, by comparing orders of elements, that $\ZZ_{8} \oplus \ZZ_{2}$ is not isomorphic to $\ZZ_{4} \oplus \ZZ_{4}$.
:::

::: {.solution}

The argument is the card's own: the two groups have different sets of element orders.

::: pf

::: {.pf-step #order8}

$\ZZ_{8}\oplus\ZZ_{2}$ has an element of order $8$.

::: pf-proof

The element $(1,1)$ has order $\operatorname{lcm}(o(1),o(1))=\operatorname{lcm}(8,2)=8$, since in a direct product the order of a pair is the least common multiple of the orders of its entries, and $1$ has order $8$ in $\ZZ_{8}$ and order $2$ in $\ZZ_{2}$.

:::

:::

::: {.pf-step #noorder8}

$\ZZ_{4}\oplus\ZZ_{4}$ has no element of order $8$.

::: pf-proof

An element $(a,b)\in\ZZ_{4}\oplus\ZZ_{4}$ has order $\operatorname{lcm}(o(a),o(b))$, and each of $o(a),o(b)$ divides $4$, so each lies in $\{1,2,4\}$. A least common multiple of two numbers from $\{1,2,4\}$ divides $4$, hence is $1$, $2$ or $4$, never $8$.

:::

:::

::: {.pf-step #conclusion}

$\ZZ_{8}\oplus\ZZ_{2}\not\cong\ZZ_{4}\oplus\ZZ_{4}$.

::: pf-proof

An isomorphism preserves the order of every element, so it carries the set of element orders of one group onto that of the other. Steps [](#order8){.pf-ref} and [](#noorder8){.pf-ref} show the two sets differ:
$$
\boxed{8\in\{\text{element orders of }\ZZ_{8}\oplus\ZZ_{2}\}\quad\text{but}\quad 8\notin\{\text{element orders of }\ZZ_{4}\oplus\ZZ_{4}\}.}
$$

:::

:::

:::

:::

::: {.remark}
Certificate. `proofs/cards/CH8DirectProduct.g` (`P-CH8-6`) computes the
element-order multisets of both groups in GAP: $\ZZ_{8}\oplus\ZZ_{2}$ has one
element of order $8$ and four of order $4$, $\ZZ_{4}\oplus\ZZ_{4}$ has none of
order $8$ and twelve of order $4$, so the multisets differ and the groups are
not isomorphic.
:::
