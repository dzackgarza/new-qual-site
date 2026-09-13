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
- How many points does $E[p]$ have, and why is counting points the wrong invariant here?
- What is the endomorphism ring of a supersingular curve?
---

::: {.definition}
Let $k$ be perfect with $\operatorname{ch} k = p > 0$ and let $E/k$ be elliptic, with Frobenius $F \colon E \to E$.
Then $F$ acts on cohomology by
\[
F^* \colon H^1(E; \OO_E) \selfmap ,
\]
which is not $k$-linear but $p$-linear: $F^*(\lambda a) = \lambda^p F^*(a)$ for $\lambda \in k$.
Since $E$ is elliptic, $h^1(\OO_E) = 1$.
Say $E$ has **Hasse invariant $0$**, and call $E$ **supersingular**, when $F^* = 0$; otherwise $F^*$ is bijective, the **Hasse invariant is $1$**, and $E$ is **ordinary**.
:::

::: {.remark title="Why only two values"}
Fix a basis vector $e$ of the line $H^1(E;\OO_E)$ and write $F^*(e) = c\, e$.
Then $F^*(\lambda e) = \lambda^p c \, e = (\lambda^{p-1} c)(\lambda e)$, so changing the basis replaces $c$ by $\lambda^{p-1}c$.
Whether $c = 0$ is therefore independent of the basis, and that dichotomy is the invariant.
If $c \neq 0$ then $F^*$ is injective, and it is surjective because $k$ is perfect, so $p$-th roots exist: $\mu e = F^*\big( (\mu/c)^{1/p} e \big)$.
Hence $F^*$ is zero or bijective, with no intermediate case.
Perfectness is used only for surjectivity; over an imperfect field the statement would fail, which is why the definition carries that hypothesis.
This is a discrete invariant of a smooth curve with no analogue over $\CC$.
:::

::: {.remark title="The $p$-torsion group scheme"}
The Hasse invariant is exactly the invariant that separates the two possible $p$-torsion group schemes, and the point of stating it schematically is that $E[p]$ always has order $p^2$ while its point count collapses.

- **Ordinary.** $E[p] \cong \mu_p \times \ZZ/p$ over $\bar k$.
  The connected-étale sequence has étale quotient $\ZZ/p$ and connected part $\mu_p$, which is forced by Cartier self-duality of $E[p]$.
  So $E[p](\bar k) \cong \ZZ/p$: $p$ points, not $p^2$.

- **Supersingular.** $E[p]$ is connected with connected Cartier dual --- local-local --- of order $p^2$, the unique self-dual non-split extension of $\alpha_p$ by $\alpha_p$.
  It has no nontrivial $\bar k$-points at all, so $E[p](\bar k) = 0$.

This is the contrast with $\ell \neq p$, where $E[\ell] \cong (\ZZ/\ell)^2$ always.
Multiplication by $p$ still has degree $p^2$ in both cases; what changes is how much of that degree is inseparable, which is why the scheme and not the point set is the right object.
:::

::: {.remark title="Endomorphisms"}
The dichotomy repeats in the endomorphism ring, and the supersingular case has no characteristic-zero analogue.
For $E$ ordinary, $\operatorname{End}(E,p_0)$ is $\ZZ$ or an order in an imaginary quadratic field, as over $\CC$.
For $E$ supersingular, $\operatorname{End}(E,p_0)$ is a maximal order in the quaternion algebra over $\QQ$ ramified exactly at $p$ and $\infty$ --- rank four, and noncommutative.
"Supersingular" therefore does not mean singular: the curve is smooth, and the word records that the endomorphism ring is *larger* than singular values of $j$ over $\CC$ ever produce.
:::
