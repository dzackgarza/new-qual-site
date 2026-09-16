---
schema: qual/card@1
id: PR-IV2INSEP
kind: proposition
title: Purely inseparable morphisms of curves are composites of Frobenius
classification:
  areas:
  - algebraic-geometry
  topics:
  - Purely Inseparable Extensions
  - Frobenius
  - Curves
relations:
- kind: uses
  target: D-IV2FROBTWIST
- kind: related-to
  target: T-LKT0U
review: draft
prompts:
- What does a purely inseparable morphism of curves look like?
- Does the genus change under a purely inseparable extension?
- Why can Riemann--Hurwitz not be applied to such a morphism?
---

::: {.proposition}
Let $f : X \to Y$ be a finite morphism of curves over $k = \kbar$ with $\characteristic k = p$, and suppose $k(X)/k(Y)$ is purely inseparable of degree $p^n$.
Then $X$ and $Y$ are isomorphic as schemes, $g(X) = g(Y)$, and $f$ is the $n$-fold composite of $k$-linear Frobenius morphisms.
[@Har10a]
:::

::: {.remark title="Why the statement is this strong"}
Purely inseparable means every element of $k(X)$ has a $p$-power lying in $k(Y)$, so $k(Y) \supseteq k(X)^{p^n}$ and the extension is squeezed between $k(X)$ and $k(X)^{p^n}$.
A purely inseparable extension of degree $p^n$ of a function field of transcendence degree $1$ over a perfect field is therefore $k(X) \subseteq k(X)^{1/p^n}$ up to isomorphism, and that inclusion is exactly the one realised by the $n$-fold Frobenius of [[D-IV2FROBTWIST]]. The source of the $k$-linear Frobenius $X_p \to X$ is $X$ itself with its structure morphism composed with the Frobenius of $\Spec k$, so $X \cong Y$ as schemes, and the genus, computed from $\dim_k H^1(\OO)$ on that one scheme, cannot move.
The Frobenius morphism itself is a homeomorphism but not an isomorphism of schemes: on $\Spec k[t]$ it is given by $t \mapsto t^p$, and $k[t] \to k[t]$, $f \mapsto f^p$, is not surjective.

The isomorphism is of schemes, not of $k$-schemes, and that distinction is the whole content.
What changes under the twist is the $k$-structure, not the space and not the sheaf of rings up to isomorphism, so every invariant computed after forgetting $k$ is preserved and the morphism is still not an isomorphism over $k$ and still has degree $p^n$.
:::

::: {.remark title="The trap"}
Riemann--Hurwitz does not apply and cannot be repaired here.
An inseparable $f$ kills differentials, $f^* \Omega_Y \to \Omega_X$ is the zero map, so the cotangent sequence is not left exact and the degree count that proves the formula has nothing to count.
Concretely $\Omega_{X/Y} \cong \Omega_X$, a line bundle of degree $2g-2$ rather than a torsion sheaf, so the "ramification divisor" is not even the right kind of object.

The use of this proposition is as the missing half of the genus inequality.
Every finite morphism of curves factors as a separable morphism after a purely inseparable one; Riemann--Hurwitz gives $g \geq$ across the separable part and this proposition gives equality across the inseparable part.
That is how $g(X) \geq g(Y)$ holds for *every* finite morphism in characteristic $p$, which is the step [[T-IV2LUROTH]] needs.
:::
