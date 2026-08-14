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
---

Let $V$ be a finite dimensional vector space over a field (the field is not necessarily algebraically closed).

Let $\phi : V \to V$ be a linear transformation.
Prove that there exists a decomposition of $V$ as $V = U \oplus W$ , where $U$ and $W$ are $\phi\dash$invariant subspaces of $V$ , $\restrictionof{\phi}{U}$ is nilpotent, and $\restrictionof{\phi}{W}$ is nonsingular.

::: {.solution}
Let $m(x)$ be the minimal polynomial of $\phi$.
If the polynomial $f(x) = x$ doesn't divide $m$, then $f$ does not have zero as an eigenvalue, so $\phi$ is nonsingular and since $0$ is nilpotent, $\phi + 0$ works.

Otherwise, write $\phi(x) = x^m \rho(x)$ where $\gcd(x, \rho(x)) = 1$.

Then
\[
V \cong \frac{k[x]}{m(x)} \cong \frac{k[x]}{(x^m)} \oplus \frac{k[x]}{(\rho)}
\definedas U \oplus W
\]
by the Chinese Remainder theorem.

We can now note that $\restrictionof{\phi}{U}$ is nilpotent because it has characteristic polynomial $x^m$, and $\restrictionof{\phi}{W}$ is nonsingular since $\lambda = 0$ is not an eigenvalue by construction.
:::
