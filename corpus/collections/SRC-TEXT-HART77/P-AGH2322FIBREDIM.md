---
schema: qual/card@1
id: P-AGH2322FIBREDIM
kind: problem
title: Dimension of the fibres of a dominant morphism
classification:
  areas:
  - algebraic-geometry
  topics:
  - Dimension Theory
  - Fibres
  - Constructible Sets
relations: []
review: draft
---

::: {.problem}
Let $f: X \to Y$ be a dominant morphism of integral schemes of finite type over a field $k$.

a. Let $Y'$ be a closed irreducible subset of $Y$ whose generic point $\eta'$ is contained in $f(X)$.
Let $Z$ be any irreducible component of $f\inv(Y')$ such that $\eta' \in f(Z)$, and show that $\codim(Z, X) \leq \codim(Y', Y)$.

b. Let $e = \krulldim X - \krulldim Y$ be the relative dimension of $X$ over $Y$.
For any point $y \in f(X)$, show that every irreducible component of the fibre $X_y$ has dimension $\geq e$.

c. Show that there is a dense open subset $U \subseteq X$ such that for any $y \in f(U)$ one has $\krulldim U_y = e$.

d. Going back to the original morphism $f: X \to Y$, for any integer $h$ let $E_h$ be the set of points $x \in X$ such that, letting $y = f(x)$, there is an irreducible component $Z$ of the fibre $X_y$ containing $x$ with $\krulldim Z \geq h$.
Show that $E_e = X$, that $E_h$ is not dense in $X$ when $h > e$, and that $E_h$ is closed for all $h$.

e. Prove the following theorem of Chevalley.
For each integer $h$, let $C_h$ be the set of points $y \in Y$ such that $\krulldim X_y = h$.
Then the subsets $C_h$ are constructible, and $C_e$ contains an open dense subset of $Y$.
:::

::: {.remark}
For (b), let $Y' = \cl\qty{\ts{y}}$ and use (a) together with II.3.20(b). For (c), first reduce to the case where $X = \Spec A$ and $Y = \Spec B$ are affine, so that $A$ is a finitely generated $B$-algebra.
Take $t_1, \ldots, t_e \in A$ forming a transcendence base of $K(X)$ over $K(Y)$, and let $X_1 = \Spec B[t_1, \ldots, t_e]$, which is affine $e$-space over $Y$; the morphism $X \to X_1$ is generically finite, so II.3.7 applies.
For (d), use (b), then (c), then induction on $\krulldim X$.
See Cartan and Chevalley, exposé 8.
:::
