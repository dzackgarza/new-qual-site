---
schema: qual/card@1
id: P-AGH247REALFORMS
kind: problem
title: Real forms of complex schemes and semilinear involutions
classification:
  areas:
  - algebraic-geometry
  topics:
  - Descent
  - Base Change
  - Conics
relations: []
review: draft
---

::: {.problem}
For any scheme $X_0$ over $\RR$, let $X = \fiberprod{X_0}{\RR}{\CC}$.
Let $\alpha: \CC \to \CC$ be complex conjugation, and let $\sigma: X \to X$ be the automorphism obtained by keeping $X_0$ fixed and applying $\alpha$ to $\CC$.
Then $X$ is a scheme over $\CC$, and $\sigma$ is a **semilinear** automorphism: the square formed by $\sigma$ on $X$, by $\alpha$ on $\Spec \CC$, and by the two structure morphisms $X \to \Spec \CC$ commutes.
Since $\sigma^2 = \id$, we call $\sigma$ an **involution**.

a. Let $X$ be a separated scheme of finite type over $\CC$, let $\sigma$ be a semilinear involution on $X$, and assume that for any two points $x_1, x_2 \in X$ there is an open affine subset containing both of them.
This last condition holds for example if $X$ is quasi-projective.
Show that there is a unique separated scheme $X_0$ of finite type over $\RR$ with $\fiberprod{X_0}{\RR}{\CC} \cong X$, such that this isomorphism identifies the given involution of $X$ with the one described above.

For the following statements, $X_0$ denotes a separated scheme of finite type over $\RR$, and $X, \sigma$ the corresponding scheme with involution over $\CC$.

b. Show that $X_0$ is affine if and only if $X$ is.

c. If $X_0, Y_0$ are two such schemes over $\RR$, then to give a morphism $f_0: X_0 \to Y_0$ is equivalent to giving a morphism $f: X \to Y$ which commutes with the involutions, i.e. $f \circ \sigma_X = \sigma_Y \circ f$.

d. If $X \cong \AA^1_\CC$, then $X_0 \cong \AA^1_\RR$.

e. If $X \cong \PP^1_\CC$, then either $X_0 \cong \PP^1_\RR$, or $X_0$ is isomorphic to the conic in $\PP^2_\RR$ given by the homogeneous equation $x_0^2 + x_1^2 + x_2^2 = 0$.
:::
