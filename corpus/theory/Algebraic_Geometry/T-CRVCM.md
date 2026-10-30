---
schema: qual/card@1
id: T-CRVCM
kind: theorem
title: Complex multiplication, and $\operatorname{End}(E,p_0)$ as an order in an imaginary quadratic field
slogan: 'Over $\CC$, an elliptic curve has extra endomorphisms exactly when its lattice is imaginary quadratic; then $\Endo(E)$ is an order in that field.'
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
Let $E = \CC/\Lambda$ with $\Lambda = \Lambda_\tau = \generators{1,\tau}_\ZZ$.
Then
$$
\operatorname{End}(E, p_0) \xrightarrow{\sim} R_\Lambda
\coloneqq \theset{ \alpha \in \CC \st \alpha \Lambda \subseteq \Lambda } ,
$$
where the endomorphism induced by multiplication by $\alpha$ corresponds to $\alpha$, and $[n]$ corresponds to $n\in\ZZ$.
By the [[PR-CRVGRP|definition of multiplication by $n$]], $E$ has complex multiplication exactly when $R_\Lambda\supsetneq\ZZ$.
This happens exactly when $\tau$ is imaginary quadratic, that is $\tau \in K\coloneqq \QQ(\sqrt{-d})$ for some squarefree $d > 0$, and in that case
$$
\ZZ \subsetneq R_\Lambda \subseteq \OO_K
$$
is an order: a subring of finite index in the ring of integers.
Concretely, if $A\tau^2 + B\tau + C = 0$ with $A, B, C \in \ZZ$, $A > 0$ and $\gcd(A,B,C) = 1$, then
$$
R_{\Lambda_\tau} = \ZZ[A\tau],
\qquad \disc = B^2 - 4AC = f^2 d_K ,
$$
where $d_K$ is the discriminant of $K$ and $f=[\OO_K:R_{\Lambda_\tau}]$.
:::

::: {.example title="The three standard computations"}
**$\tau = i$.** Here $\tau^2 + 1 = 0$, so $A = 1$ and $R = \ZZ[i] = \OO_K$ for $K = \QQ(i)$, the maximal order.
Its unit group is $\theset{\pm 1, \pm i} \cong C_4$, so $\abs{\Aut(E,p_0)} = 4$, which is the $j = 1728$ row of the automorphism count; the curve is $y^2 = x^3 - ax$ for some $a$.

**$\tau = \rho\coloneqq e^{2\pi i/3}$.** Here $\tau^2 + \tau + 1 = 0$, so $A = 1$ and $R = \ZZ[\rho] = \OO_K$ for $K = \QQ(\sqrt{-3})$.
Its unit group is the sixth roots of unity, $\cong C_6$, so $\abs{\Aut(E,p_0)} = 6$, which is the $j = 0$ row; the curve is $y^2 = x^3 - b$ for some $b$.

**$\tau = 2i$.** Here $\tau^2 + 4 = 0$, so $A = 1$ and $R = \ZZ[2i] = \ZZ + 2\ZZ[i]$, an order of index $2$ in $\ZZ[i]$ with discriminant $-16 = 2^2 \cdot (-4)$.
Its unit group is only $\theset{\pm 1}$, so this curve has just the two automorphisms every elliptic curve has, and $j(2i) \neq 0, 1728$.
Thus the endomorphism ring need not be the full ring of integers of the imaginary quadratic field.
:::

::: {.remark}
The realization inside $\CC$ identifies endomorphisms with lattice-preserving scalars in both directions.
Given $\alpha$ with $\alpha\Lambda \subseteq \Lambda$, multiplication by $\alpha$ descends to a holomorphic endomorphism of $\CC/\Lambda$ fixing $0$, which is algebraic by GAGA. Conversely a holomorphic map $\CC/\Lambda \to \CC/\Lambda$ fixing $0$ lifts to an entire map of $\CC$ fixing $0$ and commuting with $\Lambda$-translation, whose derivative is $\Lambda$-periodic and therefore constant; so the lift is $z \mapsto \alpha z$.
Addition of endomorphisms becomes addition of scalars and composition becomes multiplication, so the identification is a ring isomorphism, not just a bijection.

The dichotomy has no intermediate case. Indeed, $R_\Lambda \subseteq \Lambda$ because $\alpha = \alpha \cdot 1 \in \Lambda$, so $R_\Lambda$ is a rank-one or rank-two subgroup of $\Lambda \cong \ZZ^2$ closed under multiplication.
Rank one is $\ZZ$.
If the rank is two, then $R_\Lambda$ contains some $\alpha \notin \RR$, since $\Lambda \cap \RR = \ZZ$; as $\alpha^2 \in R_\Lambda$ is an integer combination of $1$ and $\alpha$, the element $\alpha$ is a root of a monic integral quadratic with no real root; writing $\alpha = a + b\tau$ with $b \neq 0$ then puts $\tau$ in the same imaginary quadratic field.
In particular the endomorphism ring of an elliptic curve over $\CC$ is never an order in a quaternion algebra --- that happens only for supersingular curves in characteristic $p$.

Complex multiplication is decided by the lattice parameter $\tau$, and only countably many $\tau$ are imaginary quadratic, so only countably many $j \in \CC$ are CM $j$-invariants; the generic curve has $\operatorname{End} = \ZZ$.
Passing from an equation to $\tau$ requires transcendental data; [[T-CRVCMCFT|integrality of $j$ for CM curves]] gives an arithmetic test on $j$ instead.
:::
