---
schema: qual/card@1
id: P-LARQ4
kind: problem
title: A composite of ring homomorphisms is a ring homomorphism
classification:
  areas: [algebra]
  topics: [Ring Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the two composable ring homomorphisms and requested composite with Lerman practice problem 4; restored the missing source arrow in the first map."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked preservation of addition, multiplication, zero, negatives, and identity under the unital convention."
---

::: problem
Let $\phi:G\to H$ and $\psi:H\to K$ be ring homomorphisms.
Prove that $\psi\circ\phi:G\to K$ is a ring homomorphism.
:::

::: solution
Let $x,y\in G$.

<1>1. The composite preserves addition and multiplication.
::: proof
Using first that $\phi$ and then that $\psi$ is a ring homomorphism,
$$
(\psi\circ\phi)(x+y)
=\psi(\phi(x+y))
=\psi(\phi(x)+\phi(y))
=(\psi\circ\phi)(x)+(\psi\circ\phi)(y),
$$
and similarly
$$
(\psi\circ\phi)(xy)
=\psi(\phi(xy))
=\psi(\phi(x)\phi(y))
=(\psi\circ\phi)(x)(\psi\circ\phi)(y).
$$
Thus the composite preserves the two ring operations.
:::

<1>2. The remaining ring-homomorphism axioms are also preserved.
::: proof
Additive preservation gives
$$
(\psi\circ\phi)(0_G)=\psi(0_H)=0_K
$$
and
$$
(\psi\circ\phi)(-x)=\psi(-\phi(x))=-\psi(\phi(x)).
$$
If ring homomorphisms are required to preserve identities, then
$$
(\psi\circ\phi)(1_G)=\psi(\phi(1_G))=\psi(1_H)=1_K.
$$
Hence under either the unital or nonunital convention, $\psi\circ\phi$ satisfies exactly the corresponding ring-homomorphism axioms.
:::
:::
