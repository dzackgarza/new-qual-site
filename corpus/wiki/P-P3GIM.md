---
schema: qual/card@1
id: P-P3GIM
kind: problem
title: "Let $V$ be a finite dimensional vector space over a field (the field i\u2026"
classification:
  areas:
  - algebra
  topics:
  - nilpotence
  - jordan-canonical-form
  - minimal-and-characteristic-polynomials
relations: []
review: draft
solved: true
---

Let $V$ be a finite dimensional vector space over a field (the field is not necessarily algebraically closed).

Let $\phi : V \to V$ be a linear transformation.
Prove that there exists a decomposition of $V$ as $V = U \oplus W$ , where $U$ and $W$ are $\phi\dash$invariant subspaces of $V$ , $\restrictionof{\phi}{U}$ is nilpotent, and $\restrictionof{\phi}{W}$ is nonsingular.

::: {.solution}
Let $m(x)$ be the minimal polynomial of $\phi$.
If $x$ does not divide $m(x)$, then $0$ is not an eigenvalue of $\phi$, so $\phi$ is nonsingular and $V = 0 \oplus V$ works, the zero space carrying the nilpotent part.

Otherwise, write $m(x) = x^k \rho(x)$ with $k\geq 1$ and $\gcd(x, \rho(x)) = 1$, so $\rho(0)\neq 0$.

View $V$ as a $k[x]\dash$module with $x$ acting by $\phi$, and set
\[
U \definedas \ker \phi^k, \qquad W \definedas \ker \rho(\phi)
.\]

Since $x^k$ and $\rho$ are coprime, there are $u(x), v(x)$ with $u x^k + v\rho = 1$.
Applying this to any $w\in V$ writes $w = v(\phi)\rho(\phi) w + u(\phi)\phi^k w$ with the first summand in $U$ and the second in $W$, because $m(\phi) = 0$.
If $w \in U\intersect W$ then the same identity gives $w = 0$.
Hence
\[
V = U \oplus W
.\]

Both summands are $\phi\dash$invariant, since $\phi$ commutes with $\phi^k$ and with $\rho(\phi)$.

Finally $\restrictionof{\phi}{U}$ is nilpotent, because $\phi^k$ kills $U$ by definition, and $\restrictionof{\phi}{W}$ is nonsingular: if $\phi w = 0$ for $w\in W$ then $\rho(\phi)w = \rho(0)w = 0$, and $\rho(0)\neq 0$ forces $w=0$.

> Note that $V \cong k[x]/(m(x))$ only when $V$ is a cyclic $k[x]\dash$module, which is not given here, so the decomposition is taken on $V$ itself rather than on the quotient ring.
:::
