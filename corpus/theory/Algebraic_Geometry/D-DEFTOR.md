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
\[
\cdots \to \Tor^A_{i+1}(M, N'') \to \Tor^A_i(M,N') \to \Tor^A_i(M,N) \to \Tor^A_i(M,N'') \to \Tor^A_{i-1}(M,N') \to \cdots
\]
terminating in
\[
\Tor^A_1(M,N'') \to M\tensor_A N' \to M \tensor_A N \to M \tensor_A N'' \to 0 ,
\]
so that $\Tor^A_0(M,N) \cong M \tensor_A N$.
:::

::: {.remark}
$\Tor_1^A(M,N)$ vanishing for all $N$ is equivalent to $\Tor_i^A(M,N)$ vanishing for all $i>0$ and all $N$, and both are equivalent to $M$ being flat.
This is the usable criterion: flatness needs checking in one degree only, and over a Noetherian ring only against the cyclic modules $A/I$.

$\Tor$ is computed by free or projective resolutions, never injective ones.
Over $\ZZ$, resolving $\ZZ/m$ by $0\to\ZZ\mapsvia{m}\ZZ\to\ZZ/m\to 0$ and tensoring with $\ZZ/n$ gives $\Tor^\ZZ_1(\ZZ/m,\ZZ/n) = \ZZ/{\gcd(m,n)}$: exactly the torsion the tensor product loses, which is where the name comes from.
$\Tor$ is symmetric in its two arguments, the same balancing phenomenon as for $\Ext$.
:::
