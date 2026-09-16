---
schema: qual/card@1
id: T-TORDIV
kind: theorem
title: Divisors, class group and Picard group from the rays
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Class Groups
  - Picard Group
relations:
- kind: uses
  target: PR-O8V3I
review: draft
prompts:
- Describe the torus-invariant divisors on a toric variety and compute the class group.
- What is the canonical divisor of a toric variety?
- What is the rank of the Picard group of a simplicial toric variety?
---

::: {.theorem title="The two sequences"}
Let $\Sigma$ have rays $\Sigma(1)$ with primitive generators $u_\rho$, and suppose $\abs{\Sigma}$ spans $N_\RR$.
Each ray $\rho$ is the closure of a codimension-one orbit, giving a prime divisor $D_\rho$, and
\[
\Div_T(X_\Sigma) = \bigoplus_{\rho \in \Sigma(1)} \ZZ D_\rho \cong \ZZ^{\Sigma(1)} .
\]
There are exact sequences
\[
0 \to M \to \bigoplus_{\rho} \ZZ D_\rho \to \Cl(X_\Sigma) \to 0 ,
\qquad
0 \to M \to \CDiv_T(X_\Sigma) \to \Pic(X_\Sigma) \to 0 ,
\]
compatible with the inclusions $\CDiv_T \subseteq \Div_T$ and $\Pic \subseteq \Cl$.
The left map is
\[
m \mapsto \operatorname{div}(\chi^m) = \sum_{\rho \in \Sigma(1)} \inp{m}{u_\rho} D_\rho .
\]
:::

::: {.theorem title="Canonical divisor"}
$\omega_{X_\Sigma} \cong \OO\big( -\sum_\rho D_\rho \big)$, so $K_X \sim -\sum_{\rho \in \Sigma(1)} D_\rho$.
:::

::: {.remark}
So the class group is the cokernel of an explicit integer matrix whose rows are the ray generators.
Two consequences are immediate.
It has rank $\size \Sigma(1) - \dim N_\RR$, and it has torsion exactly when the rays fail to generate $N$ as a lattice.
When $\Sigma$ is simplicial, $\Pic$ has finite index in $\Cl$ and $\rank \Pic(X_\Sigma) = \size \Sigma(1) - \dim N_\RR$ as well — for $\FF_a$ this is $4 - 2 = 2$, a fibre and a section.

Cartier divisors are cut out locally: $D = \sum a_\rho D_\rho$ is Cartier iff for every maximal cone $\sigma$ there is $m_\sigma \in M$ with $\inp{m_\sigma}{u_\rho} = -a_\rho$ for all $\rho \leq \sigma$, and then $D|_{U_\sigma} = \operatorname{div}(\chi^{-m_\sigma})$.
Equivalently $\CDiv_T(U_\sigma) \cong M/M(\sigma)$ where $M(\sigma) = \sigma^\perp \intersect M$.

For $\PP^n$ the $n+1$ rays give $D_0, \ldots, D_n$, all linearly equivalent, so $K_{\PP^n} \sim -(n+1)H$ and $\omega_{\PP^n} = \OO(-n-1)$ falls out of counting rays.
:::
