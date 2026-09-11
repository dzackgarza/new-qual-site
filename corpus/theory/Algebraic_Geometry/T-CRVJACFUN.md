---
schema: qual/card@1
id: T-CRVJACFUN
kind: theorem
title: The Jacobian represents $\Pic^0(X/-)$, and is a smooth proper group scheme of dimension $g$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Jacobians
  - Moduli
  - Group Schemes
relations:
- kind: uses
  target: T-MWDVL
- kind: uses
  target: D-MODPIC
- kind: related-to
  target: T-U5QSY
- kind: related-to
  target: PR-CRVGRP
review: draft
prompts:
- What functor does the Jacobian represent, and why is the quotient by $p^* \Pic(T)$ there?
- Why is $\Jac(X)$ smooth of dimension $g$?
- Why is $\Jac(X)$ proper?
- What are the fibres of the map from the $n$-fold symmetric product to $\Jac(X)$?
- Construct the Jacobian without using $\CC$.
---

::: {.definition title="Families of degree-zero line bundles"}
Let $X/k$ be a smooth projective curve of genus $g$ with a point $p_0$, and let $T \in \Sch^{\mathrm{ft}}_{/k}$ with second projection $p \colon X \times T \to T$.
Put
\[
\Pic^0(X \times T) \da \ts{ \mcf \in \Pic(X \times T) \st \deg \ro{\mcf}{X_t} = 0 \ \forall t \in T },
\qquad
\Pic^0(X/T) \da \Pic^0(X \times T) \, / \, p^* \Pic(T) ,
\]
the families of degree-zero line bundles on $X$ parameterised by $T$.
:::

::: {.theorem title="Representability"}
There is a $k$-scheme $\Jac(X)$ of finite type together with a universal $\mcl \in \Pic^0\big(X / \Jac(X)\big)$ such that for every $T$ and every $\mcm \in \Pic^0(X/T)$ there is a unique $f \colon T \to \Jac(X)$ with $f^* \mcl = \mcm$.
That is, $\Jac(X)$ represents $\Pic^0(X/{-})$.
Moreover:

- On $k$-points, $\Jac(X)(k) = \Pic^0(X)$.

- $\Jac(X)$ is a group scheme over $k$: the identity is the class of $\OO_X$, inversion is $\mcl \mapsto \mcl^{-1}$, and addition is $p_1^*\mcl \tensor p_2^*\mcl$.

- $\T_0 \Jac(X) \iso H^1(X; \OO_X)$, so $\Jac(X)$ is smooth of dimension $g$.

- $\Jac(X)$ is proper over $k$, hence an abelian variety.

For $X = E$ elliptic, $E \iso \Jac(E)$.
:::

::: {.theorem title="The symmetric product"}
For each $n$ the assignment
\[
\phi^n \colon X^{\times n} \to \Jac(X),
\qquad
(p_1, \ldots, p_n) \mapsto \mcl\big( \textstyle\sum p_i - n p_0 \big)
\]
is a morphism, symmetric in its arguments, so it factors through $\Sym^n X$.
It is surjective for $n \geq g$, and the fibre of $\Sym^n X \to \Jac(X)$ over the class of $D$ is the complete linear system $\abs{D} \iso \PP^{\ell(D)-1}$.
:::

::: {.remark title="Reading the definition"}
Two features of the functor are where the questions land.

The quotient by $p^*\Pic(T)$ is not a technicality: without it the functor is not representable, because a line bundle on $X \times T$ can be twisted by one pulled back from the base without changing any fibre, so the assignment $T \mapsto \Pic^0(X\times T)$ has automorphisms and cannot have a universal object.
Quotienting kills exactly that ambiguity.
The same issue reappears as the reason a universal family needs a rigidification, and it is why $\Jac$ is a fine moduli space while $\AA^1$ for elliptic curves is only coarse.

That $k$-points give $\Pic^0(X)$ is then formal: a $k$-point is a map $\spec k \to \Jac(X)$, which by the universal property is an element of $\Pic^0(X/k) = \Pic^0(X)$.
So the scheme structure is extra information laid over a set one already knew.
:::

::: {.remark title="Smooth, of dimension $g$, and proper"}
The dimension computation is the cleanest use of dual numbers in the subject.
A tangent vector at $0$ is a map $T = \spec k[\eps]/\eps^2 \to \Jac(X)$ sending the closed point to $0$, hence a class in $\Pic^0(X/T)$ restricting to $0$ over $\spec k$.
The exponential sequence for dual numbers gives
\[
0 \to H^1(X; \OO_X) \to \Pic\big(X[\eps]\big) \to \Pic(X) \to 0 ,
\]
so those classes are exactly $H^1(X;\OO_X)$, of dimension $g$.
That is smoothness at the origin only; a group scheme is homogeneous under its own translations, so smoothness propagates to every point.
This "check it at the identity, translate everywhere else" step is what makes group schemes easy and is worth naming.

Properness is the valuative criterion applied to a DVR $R$ with fraction field $K$: one must extend a line bundle on $X \times \spec K$ over $X \times \spec R$.
But $X \times \spec R$ is regular, so a Weil divisor extends and is automatically Cartier, and the extension is unique.
Irreducibility comes from the other direction, via $\phi^n$: for $n \geq g$ Riemann--Roch makes every degree-$n$ class effective, so $\phi^n$ is surjective from an irreducible variety, and the generic fibre is finite because a general divisor of degree $g$ is nonspecial with $\ell(D) = 1$.
Hence $\dim \Jac(X) = g$ by a second, independent route.
:::

::: {.remark title="Against the analytic construction"}
Over $\CC$ one can write $\Jac(X) = H^0(\Omega^1)\dual / H_1(X,\ZZ)$ and prove Abel and Jacobi inversion by integration; that construction produces a complex torus and needs GAGA to become algebraic.
The functorial construction above needs no ground field hypothesis, which is the reason to carry it: in characteristic $p$, and for families, the analytic route is unavailable and the representability statement is the definition.
The two agree over $\CC$, and the agreement is Abel's theorem.

The genus $1$ case is the one to state last, because it is where the two theories collapse into each other: $\phi^1 \colon X \to \Jac(X)$ is already an isomorphism, so an elliptic curve carries a group law with no auxiliary object, and every statement about $\Pic^0$ can be read as a statement about points of the curve.
:::
