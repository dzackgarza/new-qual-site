---
schema: qual/card@1
id: FD-H764S
kind: definition
title: Elementary divisors of a finite abelian group
prompts:
- What are the elementary divisors of a finite abelian group?
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Abelian Groups
relations: []
review: draft
---

::: {.definition}
Let $G$ be a finite abelian group.
By the [[D-JQNJQ|elementary divisor decomposition]], there are primes $p_1,\ldots,p_m$, not necessarily distinct, and integers $\alpha_1,\ldots,\alpha_m\geq 1$ with
$$
G \cong \bigoplus_{i=1}^m \ZZ/p_i^{\alpha_i} \ZZ,
$$
and the list $p_1^{\alpha_1},\ldots,p_m^{\alpha_m}$ is unique up to order.
These prime powers are the \dfn{elementary divisors} of $G$.
:::
