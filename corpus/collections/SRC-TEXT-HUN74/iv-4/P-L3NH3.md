---
schema: qual/card@1
id: P-L3NH3
kind: problem
title: Hungerford 4.4.5
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Rings
  - Homomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $R$ be a unital ring, show that there is a ring homomorphism $\mathrm{Hom}_R(R, R) \to R^{op}$ where $\mathrm{Hom}_R$ denotes left $R-$module homomorphisms.
Conclude that if $R$ is commutative, then there is a ring isomorphism $\mathrm{Hom}_R(R, R) \cong R$.
:::

::: {.solution}
**Goal.** Show $\operatorname{Hom}_R(R,R) \cong R^{\mathrm{op}}$, and $\operatorname{Hom}_R(R,R) \cong R$ when $R$ is commutative.

<1>1. Define $\Phi: \operatorname{Hom}_R(R,R) \to R^{\mathrm{op}}$ by $\Phi(f) = f(1)$.
Proof: evaluate a left $R$-module homomorphism at $1$.

<1>2. $\Phi$ is a bijection.
<2>1. A left $R$-module homomorphism $f: R \to R$ is determined by $f(1)$.
Proof: $f(r) = f(r \cdot 1) = r f(1)$ (since $f$ is $R$-linear).
<2>2. Conversely, for any $a \in R$, the map $f_a(r) = ra$ is a left $R$-module homomorphism.
Proof: $f_a(r_1 + r_2) = (r_1 + r_2)a = r_1 a + r_2 a$ and $f_a(sr) = (sr)a = s(ra) = s f_a(r)$.
<2>3. Hence $\Phi$ is a bijection with inverse $a \mapsto f_a$.
Proof: <1>2.1 and <1>2.2.

<1>3. $\Phi$ is a ring homomorphism to $R^{\mathrm{op}}$.
<2>1. $\Phi(f \circ g) = (f \circ g)(1) = f(g(1)) = f(1) \cdot g(1)$.
Proof: $g(1) = g(1) \cdot 1$, and $f(g(1)) = f(g(1)\cdot 1) = g(1) f(1)$.
<2>2. In $R^{\mathrm{op}}$, the product is $f(1) \cdot_{\mathrm{op}} g(1) = g(1) f(1)$.
Proof: the multiplication in $R^{\mathrm{op}}$ is reversed.
<2>3. Hence $\Phi(f \circ g) = \Phi(f) \cdot_{\mathrm{op}} \Phi(g)$, so $\Phi$ is a ring homomorphism to $R^{\mathrm{op}}$.
Proof: <1>3.1 and <1>3.2.

<1>4. If $R$ is commutative, then $R^{\mathrm{op}} = R$, so $\operatorname{Hom}_R(R,R) \cong R$.
Proof: in a commutative ring, the opposite ring is the same ring.

<1>5. Q.E.D.
Proof: <1>3 gives the homomorphism to $R^{\mathrm{op}}$; <1>4 gives the isomorphism to $R$ in the commutative case.
:::
