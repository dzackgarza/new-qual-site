---
schema: qual/card@1
id: P-LARQ12
kind: problem
title: 'Maximal ideals and zero divisors in $\ZZ\times\ZZ$'
classification:
  areas: [algebra]
  topics: [Ring Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both product-ring questions with Lerman practice problem 12."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Verified maximality using the quotient by 2Z x Z and exhibited explicit nonzero orthogonal idempotents as zero divisors."
---

::: problem
1. Does $\mathbb Z\times\mathbb Z$ have a maximal ideal?
   If so, give one.

2. Does $\mathbb Z\times\mathbb Z$ have zero divisors?
   If so, give two nonzero zero divisors whose product is zero.
:::

::: solution
<1>1. The ring $\mathbb Z\times\mathbb Z$ has maximal ideals.
::: proof
For example, let
$$
M=2\mathbb Z\times\mathbb Z.
$$
The map
$$
\Phi:\mathbb Z\times\mathbb Z\to\mathbb Z/2\mathbb Z,
\qquad
\Phi(a,b)=a\bmod2
$$
is a surjective ring homomorphism with kernel $M$. Hence
$$
(\mathbb Z\times\mathbb Z)/M\cong\mathbb Z/2\mathbb Z,
$$
which is a field. Therefore $M$ is maximal.
:::

<1>2. The ring has nonzero zero divisors.
::: proof
The two elements
$$
(1,0),\qquad(0,1)
$$
are both nonzero, but
$$
(1,0)(0,1)=(0,0).
$$
Thus each is a nonzero zero divisor, and their product is zero as required.
:::
:::
