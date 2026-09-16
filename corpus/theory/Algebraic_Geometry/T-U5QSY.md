---
schema: qual/card@1
id: T-U5QSY
kind: theorem
title: The Jacobian, Abel's theorem, and the Abel--Jacobi map
classification:
  areas:
  - algebraic-geometry
  topics:
  - Jacobians
  - Abel-Jacobi Map
  - Elliptic Curves
relations:
- kind: uses
  target: PR-Y5S7V
- kind: uses
  target: T-MWDVL
review: draft
prompts:
- State Abel's theorem.
- What is the significance of the Jacobian?
- What kind of map is the Abel--Jacobi map, and what is it in genus $1$?
---

::: {.definition}
For $X$ a smooth projective curve of genus $g$ over $\CC$,
\[
\Jac(X) = H^0(X,\Omega^1)\dual / H_1(X,\ZZ) ,
\]
a complex torus of dimension $g$, and an abelian variety.
The \dfn{Abel--Jacobi map} sends a degree-zero divisor $\sum (p_i - q_i)$ to $\sum \int_{q_i}^{p_i}$, a linear functional on $H^0(\Omega^1)$ taken modulo periods.
:::

::: {.theorem title="Abel"}
A divisor of degree zero is principal exactly when its image under the Abel--Jacobi map is zero.
Hence $\Pic^0(X) \cong \Jac(X)$.
:::

::: {.theorem title="Jacobi inversion"}
The Abel--Jacobi map is surjective, so $\Jac(X)$ is exactly the group of degree-zero divisor classes.
:::

::: {.remark}
The significance is the sentence the two theorems combine to: the Jacobian is a projective variety whose points are the degree-zero line bundles on $X$, so a discrete-looking classification problem becomes a geometric object of dimension $g$.

Fixing a base point $p_0$ gives $X \to \Jac(X)$, $p \mapsto [p - p_0]$, which is an embedding for $g \geq 1$.
In genus $1$ it is an isomorphism, and that is the answer to the follow-up: an elliptic curve is its own Jacobian, and the group law on $E$ is the statement that $[p] + [q] = [r] + [0]$ exactly when $p + q = r$ under that law.
Everything special about elliptic curves is this coincidence of $X$ with $\Jac X$.
:::
