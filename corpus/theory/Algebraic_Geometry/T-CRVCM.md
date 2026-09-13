---
schema: qual/card@1
id: T-CRVCM
kind: theorem
title: Complex multiplication, and $\operatorname{End}(E,p_0)$ as an order in an imaginary quadratic field
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Complex Multiplication
  - Number Theory
relations:
- kind: uses
  target: T-CRVUNIF
- kind: related-to
  target: PR-CRVGRP
- kind: related-to
  target: T-CRVMODJ
review: draft
prompts:
- Realise $\operatorname{End}(E,p_0)$ inside $\CC$.
- For which $\tau$ does $\CC/\Lambda_\tau$ have complex multiplication?
- What kind of ring can the endomorphism ring of an elliptic curve over $\CC$ be?
- Compute the endomorphism ring for $\tau = i$, for $\tau$ a primitive cube root of unity, and for $\tau = 2i$.
- Why are there only countably many $j$-invariants with complex multiplication?
---

::: {.theorem title="The endomorphism ring inside $\CC$"}
Let $E = \CC/\Lambda$ with $\Lambda = \Lambda_\tau = \gens{1,\tau}_\ZZ$.
Then
\[
\operatorname{End}(E, p_0) \iso R_\Lambda \da \ts{ \alpha \in \CC \st \alpha \Lambda \subseteq \Lambda } ,
\]
the isomorphism carrying an endomorphism to the scalar it is, and carrying $[n]$ to the integer $n$.
Say $E$ has **complex multiplication** when $R_\Lambda \supsetneq \ZZ$.
This happens exactly when $\tau$ is imaginary quadratic, that is $\tau \in K \da \QQ(\sqrt{-d})$ for some squarefree $d > 0$, and in that case
\[
\ZZ \subsetneq R_\Lambda \subseteq \OO_K
\]
is an order: a subring of finite index in the ring of integers.
Concretely, if $A\tau^2 + B\tau + C = 0$ with $A, B, C \in \ZZ$, $A > 0$ and $\gcd(A,B,C) = 1$, then
\[
R_{\Lambda_\tau} = \ZZ[A\tau],
\qquad \disc = B^2 - 4AC = f^2 d_K ,
\]
where $f = [\OO_K : R_{\Lambda_\tau}]$ is the **conductor** of the order.
:::

::: {.example title="The three standard computations"}
**$\tau = i$.** Here $\tau^2 + 1 = 0$, so $A = 1$ and $R = \ZZ[i] = \OO_K$ for $K = \QQ(i)$, the maximal order, conductor $1$.
Its unit group is $\ts{\pm 1, \pm i} \cong C_4$, so $\abs{\Aut(E,p_0)} = 4$, which is the $j = 1728$ row of the automorphism count; the curve is $y^2 = x^3 - ax$ for some $a$.

**$\tau = \rho \da e^{2\pi i/3}$.** Here $\tau^2 + \tau + 1 = 0$, so $A = 1$ and $R = \ZZ[\rho] = \OO_K$ for $K = \QQ(\sqrt{-3})$, conductor $1$.
Its unit group is the sixth roots of unity, $\cong C_6$, so $\abs{\Aut(E,p_0)} = 6$, which is the $j = 0$ row; the curve is $y^2 = x^3 - b$ for some $b$.

**$\tau = 2i$.** Here $\tau^2 + 4 = 0$, so $A = 1$ and $R = \ZZ[2i] = \ZZ + 2\ZZ[i]$, of index $2$ in $\ZZ[i]$: an order of conductor $2$ in $K = \QQ(i)$, with discriminant $-16 = 2^2 \cdot (-4)$.
Its unit group is only $\ts{\pm 1}$, so this curve has just the two automorphisms every elliptic curve has, and $j(2i) \neq 0, 1728$.
This is the example to reach for when asked whether the endomorphism ring must be the full ring of integers: it need not be.
:::

::: {.remark}
The realisation inside $\CC$ is what makes the whole subject computable, so it is worth knowing both directions.
Given $\alpha$ with $\alpha\Lambda \subseteq \Lambda$, multiplication by $\alpha$ descends to a holomorphic endomorphism of $\CC/\Lambda$ fixing $0$, which is algebraic by GAGA. Conversely a holomorphic map $\CC/\Lambda \to \CC/\Lambda$ fixing $0$ lifts to an entire map of $\CC$ fixing $0$ and commuting with $\Lambda$-translation, whose derivative is $\Lambda$-periodic and therefore constant; so the lift is $z \mapsto \alpha z$.
Addition of endomorphisms becomes addition of scalars and composition becomes multiplication, so the identification is a ring isomorphism, not just a bijection.

Why the dichotomy is sharp: $R_\Lambda \subseteq \Lambda$ because $\alpha = \alpha \cdot 1 \in \Lambda$, so $R_\Lambda$ is a rank-one or rank-two subgroup of $\Lambda \cong \ZZ^2$ closed under multiplication.
Rank one is $\ZZ$.
Rank two means some $\alpha \notin \RR$ satisfies a monic-after-clearing integral quadratic, and since $\alpha^2 \in R_\Lambda$ is an integer combination of $1$ and $\alpha$, that quadratic has no real root; writing $\alpha = a + b\tau$ with $b \neq 0$ then puts $\tau$ in the same imaginary quadratic field.
There is no intermediate case, and in particular the endomorphism ring of an elliptic curve over $\CC$ is never an order in a quaternion algebra --- that happens only for supersingular curves in characteristic $p$.

The countability remark is the cheap and correct answer to "can you tell from the equation whether $E$ has CM?". Complex multiplication is decided by $\tau$, and only countably many $\tau$ are imaginary quadratic, so only countably many $j \in \CC$ are CM $j$-invariants; the generic curve has $\operatorname{End} = \ZZ$.
That still leaves it hard to decide for a given equation, because passing from an equation to $\tau$ requires transcendental data.
The route that does work is class field theory.
:::
