---
schema: qual/card@1
id: P-T6YA3
kind: problem
title: The $R/(p)$-module structure on $A/pA$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Vector Spaces
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $R$ be a commutative ring with identity, $p \in R$ an element, and $A$ an $R$-module.
Show that the quotient group $A/pA$ is naturally an $R/(p)$-module with scalar multiplication defined by
\[
(r + (p)) \cdot (a + pA) = ra + pA.
\]
In particular, show that if $(p)$ is a maximal ideal, $A/pA$ is a vector space over the field $R/(p)$.
:::

::: {.solution}
<1>1. The scalar multiplication $(r + (p)) \cdot (a + pA) = ra + pA$ is well-defined.
<2>1. Suppose $r + (p) = r' + (p)$ and $a + pA = a' + pA$.
Proof: setup of coset representatives.
<2>2. Then $r - r' = c p$ for some $c \in R$, and $a - a' \in pA$, so $a - a' = p u$ for some $u \in A$.
Proof: definition of ideals and submodules.
<2>3. Compute the difference of the outputs:
\[
ra - r'a' = r(a - a') + (r - r')a' = r(pu) + (cp)a' = p(ru + ca').
\]
Proof: ring and module arithmetic.
<2>4. Since $ru + ca' \in A$, $p(ru + ca') \in pA$.
Proof: definition of $pA = \{px : x \in A\}$.
<2>5. Hence $ra + pA = r'a' + pA$, so the action is independent of the choice of coset representatives.
Proof: <2>3 and <2>4.

<1>2. The action satisfies all module axioms:
<2>1. Distributivity over module addition:
\[
(r + (p)) \cdot \bigl((a + pA) + (b + pA)\bigr) = (r + (p)) \cdot (a + b + pA) = r(a+b) + pA = (ra + pA) + (rb + pA).
\]
Proof: distributivity in the $R$-module $A$: $r(a+b) = ra + rb$.
<2>2. Distributivity over ring addition:
\[
\bigl((r + (p)) + (s + (p))\bigr) \cdot (a + pA) = (r + s + (p)) \cdot (a + pA) = (r+s)a + pA = (ra + pA) + (sa + pA).
\]
Proof: module axiom $(r+s)a = ra + sa$.
<2>3. Compatibility with ring multiplication:
\[
\bigl((r + (p))(s + (p))\bigr) \cdot (a + pA) = (rs + (p)) \cdot (a + pA) = (rs)a + pA = r(sa) + pA = (r + (p)) \cdot (sa + pA).
\]
Proof: module axiom $(rs)a = r(sa)$.
<2>4. Action of the ring identity:
\[
(1_R + (p)) \cdot (a + pA) = 1_R a + pA = a + pA.
\]
Proof: module axiom $1_R a = a$.

<1>3. If $(p)$ is a maximal ideal in $R$, then $R/(p)$ is a field, and any module over a field is a vector space.
Proof: quotient of a commutative ring by a maximal ideal is a field.

<1>4. Conclusion:
$A/pA$ is an $R/(p)$-module, and is a vector space over $R/(p)$ when $(p)$ is maximal. Q.E.D.
Proof: <1>1, <1>2, and <1>3.
:::
