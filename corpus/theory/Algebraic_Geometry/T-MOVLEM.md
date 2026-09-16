---
schema: qual/card@1
id: T-MOVLEM
kind: theorem
title: The moving lemma
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cycles
  - Rational Equivalence
  - Divisors
relations:
- kind: uses
  target: D-5PQ5W
review: draft
prompts:
- What is the moving lemma?
---

::: {.theorem title="Moving lemma for divisors"}
Let $X$ be a quasiprojective variety over an algebraically closed field, $D$ a Cartier divisor on $X$, and $S \subseteq X$ a finite set of points.
Then $D$ is linearly equivalent to a Cartier divisor $D'$ whose support contains no point of $S$.
:::

::: {.theorem title="Chow's moving lemma"}
Let $X$ be a smooth quasiprojective variety, and let $\alpha$ and $\beta$ be algebraic cycles on $X$.
Then $\alpha$ is rationally equivalent to a cycle $\alpha'$ that meets $\beta$ properly: every irreducible component of $\supp \alpha' \cap \supp \beta$ has codimension $\codim \alpha + \codim \beta$.
:::

::: {.remark}
The moving lemma is what makes the intersection product on the Chow ring $A^*(X)$ of a smooth quasiprojective variety well defined: move one cycle to meet the other properly, intersect with multiplicities, and the rational equivalence class of the result does not depend on the choice of $\alpha'$.
For divisors on a smooth projective surface, it lets the intersection number $C \cdot D$ be computed as a sum of local intersection multiplicities after replacing $D$ by a linearly equivalent divisor with no common component with $C$.
:::
