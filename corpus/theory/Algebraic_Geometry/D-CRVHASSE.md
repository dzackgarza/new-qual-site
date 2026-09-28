---
schema: qual/card@1
id: D-CRVHASSE
kind: definition
title: The Hasse invariant, and ordinary versus supersingular
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Characteristic p
  - Group Schemes
relations:
- kind: uses
  target: PR-CRVGRP
- kind: related-to
  target: FE-MORFROB
- kind: related-to
  target: T-CRVCM
review: draft
prompts:
- Define the Hasse invariant.
- Why does it take only two values?
- What is $E[p]$ as a group scheme in each case?
- How many $\bar k$-points does $E[p]$ have in each case, and what is its order as a group scheme?
- What is the endomorphism ring of a supersingular curve?
---

::: {.definition}
Let $k$ be perfect with $\operatorname{ch} k = p > 0$ and let $E/k$ be elliptic, with Frobenius $F \colon E \to E$.
Then $F$ acts on cohomology by
$$
F^* \colon H^1(E; \OO_E) \selfmap ,
$$
which is not $k$-linear but $p$-linear: $F^*(\lambda a) = \lambda^p F^*(a)$ for $\lambda \in k$.
Since $E$ is elliptic, $h^1(\OO_E) = 1$.
Say $E$ has \dfn{Hasse invariant $0$}, and call $E$ \dfn{supersingular}, when $F^* = 0$; otherwise $F^*$ is bijective, $E$ has \dfn{Hasse invariant $1$}, and $E$ is \dfn{ordinary}.
:::

::: {.remark title="Independence of the basis"}
Fix a basis vector $e$ of the line $H^1(E;\OO_E)$ and write $F^*(e) = c\, e$.
Then $F^*(\lambda e) = \lambda^p c \, e = (\lambda^{p-1} c)(\lambda e)$, so changing the basis replaces $c$ by $\lambda^{p-1}c$, and whether $c = 0$ is independent of the basis.
If $c \neq 0$ then $F^*$ is injective, and it is surjective because every element of the perfect field $k$ has a $p$-th root: $\mu e = F^*\big( (\mu/c)^{1/p} e \big)$.
Over an imperfect field with $c\ne0$, the image of $F^*$ is $k^pc\,e$, a proper subset of $k\,e$.
:::

::: {.remark title="The $p$-torsion group scheme"}
The Hasse invariant separates the two possible $p$-torsion group schemes. In both cases $E[p]$ has order $p^2$, while the group of geometric points is $\ZZ/p$ in the ordinary case and trivial in the supersingular case.

- **Ordinary.** $E[p] \cong \mu_p \times \ZZ/p$ over $\bar k$.
  The connected-étale sequence has étale quotient $\ZZ/p$ and connected part $\mu_p$, which is forced by Cartier self-duality of $E[p]$.
  So $E[p](\bar k) \cong \ZZ/p$: $p$ points, not $p^2$.

- **Supersingular.** $E[p]$ is connected with connected Cartier dual --- local-local --- of order $p^2$, the unique self-dual non-split extension of $\alpha_p$ by $\alpha_p$.
  It has no nontrivial $\bar k$-points at all, so $E[p](\bar k) = 0$.

For a prime $\ell \neq p$, $E[\ell] \cong (\ZZ/\ell)^2$ over $\bar k$.
Multiplication by $p$ has degree $p^2$ in both cases; its separable degree is $p$ when $E$ is ordinary and $1$ when $E$ is supersingular.
:::

::: {.remark title="Endomorphisms"}
Let $E_{\bar k}$ be the base change of $E$ to $\bar k$.
For $E$ ordinary, $\operatorname{End}(E_{\bar k},p_0)$ is $\ZZ$ or an order in an imaginary quadratic field, and it is an order in an imaginary quadratic field when $k$ is finite.
For $E$ supersingular, $\operatorname{End}(E_{\bar k},p_0)$ is a maximal order in the quaternion algebra over $\QQ$ ramified exactly at $p$ and $\infty$; it has rank four and is noncommutative.
Over $\CC$, the endomorphism ring of an elliptic curve has rank $1$ or $2$, and the $j$-invariants of the curves with rank $2$ are the singular moduli; the name supersingular refers to the larger endomorphism ring, and a supersingular curve is smooth.
:::
