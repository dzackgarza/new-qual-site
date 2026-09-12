---
schema: qual/card@1
id: P-EMAG4
kind: problem
title: Nonsimplicity at order $351$ and cyclicity at order $33$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Simple Groups
  - Cyclic Groups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked both orders and conclusions against Groups 4 on PDF page 1."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the exhaustive Sylow counts, disjointness and exact cardinality of the prime-order element sets, and the commuting cyclic factors for order 33."
---

::: problem
(a) Prove that a group of order $351 = 3^3 \cdot 13$ cannot be simple.

(b) Prove that a group of order 33 must be cyclic.
:::

::: solution
<1>1. A group of order $351$ has a nontrivial proper normal subgroup.

::: proof
Sylow's theorems give $n_{13}\mid27$ and
$n_{13}\equiv1\pmod{13}$, hence $n_{13}=1$ or
$27$ [@DF04]. If it is one, the unique Sylow
$13$-subgroup is the required normal subgroup.

Otherwise the $27$ subgroups of order thirteen
have $27\cdot12=324$ distinct nonidentity elements:
sharing a nonidentity element would force two
prime-order subgroups to coincide. Thus exactly
$351-324=27$ elements of $G$ are not in that set.
Every Sylow $3$-subgroup has order $27$ and lies
in this complement, since its elements have
orders powers of three, not thirteen. It must
therefore equal the entire complement. This
forces all Sylow $3$-subgroups to coincide, so
the unique one is normal. Its order $27$ is
strictly between one and $351$. In either case
$G$ is not simple.
:::

<1>2. Every group of order $33$ is cyclic.

::: proof
The Sylow counts satisfy
$n_{11}\mid3$, $n_{11}\equiv1\pmod{11}$ and
$n_3\mid11$, $n_3\equiv1\pmod3$ [@DF04].
Since $11\not\equiv1\pmod3$, these give
$n_{11}=n_3=1$. Let $P,Q$ be the normal subgroups
of orders $3,11$. Their intersection has order
dividing both primes, so it is trivial.
The commutator of an element of $P$ with an
element of $Q$ lies in both normal subgroups,
and hence is one. Thus multiplication defines
an injective homomorphism $P\times Q\to G$;
its kernel is trivial because $xy=1$ implies
$x=y^{-1}\in P\cap Q$. Equal orders make it
an isomorphism. Each prime-order factor is
cyclic, and a pair of generators has order
$\operatorname{lcm}(3,11)=33$, proving the claim.
:::
:::
