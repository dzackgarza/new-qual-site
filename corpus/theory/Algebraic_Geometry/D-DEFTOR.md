---
schema: qual/card@1
id: D-DEFTOR
kind: definition
title: The $\Tor$ functors, and flatness as $\Tor$-vanishing
classification:
  areas:
  - algebraic-geometry
  topics:
  - Homological Algebra
  - Derived Functors
  - Tor
  - Flatness
relations:
- kind: uses
  target: D-DEFDERIV
- kind: uses
  target: D-DEFFLAT
review: draft
prompts:
- How is $\Tor^A_i(M,N)$ defined, and what is $\Tor_0$?
- State the $\Tor$ criterion for flatness.
- Compute $\Tor^\ZZ_1(\ZZ/m, \ZZ/n)$.
---

::: {.definition title="Tor"}
For an $A$-module $M$, the functors $\Tor^A_i(M,\wait)$, $i \geq 0$, are the left derived functors of the right exact functor $M \tensor_A \wait$.
A short exact sequence $0 \to N' \to N \to N'' \to 0$ induces a long exact sequence
$$
\cdots \to \Tor^A_{i+1}(M, N'') \to \Tor^A_i(M,N') \to \Tor^A_i(M,N) \to \Tor^A_i(M,N'') \to \Tor^A_{i-1}(M,N') \to \cdots
$$
terminating in
$$
\Tor^A_1(M,N'') \to M\tensor_A N' \to M \tensor_A N \to M \tensor_A N'' \to 0 ,
$$
so that $\Tor^A_0(M,N) \cong M \tensor_A N$.
:::

::: {.remark}
$\Tor_1^A(M,N)$ vanishing for all $N$ is equivalent to $\Tor_i^A(M,N)$ vanishing for all $i>0$ and all $N$, and both are equivalent to $M$ being flat.
Moreover, $M$ is flat if and only if $\Tor_1^A(M,A/I)=0$ for every finitely generated ideal $I\subseteq A$.

$\Tor$ is computed from a projective resolution of either argument, and $\Tor_i^A(M,N)\cong\Tor_i^A(N,M)$.
Over $\ZZ$, resolving $\ZZ/m$ by $0\to\ZZ\mapsvia{m}\ZZ\to\ZZ/m\to 0$ and tensoring with an abelian group $B$ gives $\Tor^\ZZ_1(\ZZ/m,B)\cong\ts{b\in B\st mb=0}$, the $m$-torsion of $B$; in particular $\Tor^\ZZ_1(\ZZ/m,\ZZ/n) \cong \ZZ/{\gcd(m,n)}$.
:::
