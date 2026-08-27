---
schema: qual/card@1
id: D-FAIJX
kind: definition
title: Mayer-Vietoris Sequence
classification:
  areas:
  - topology
  topics:
  - Mayer-Vietoris
  - Homology
relations:
- kind: related-to
  target: T-3VUOH
review: draft
---

::: {.definition}
Let $A, B \subseteq X$ with $X = A^\circ \union B^\circ$.
The **Mayer-Vietoris sequence** of the pair $(A,B)$ is the long exact sequence
\[
\cdots \to H_n(A\intersect B) \mapsvia{\Phi} H_n(A) \oplus H_n(B) \mapsvia{\Psi} H_n(X) \mapsvia{\del} H_{n-1}(A \intersect B) \to \cdots \to H_0(X) \to 0
,\]
where $\Phi(x) = (i_*x,\, j_*x)$ is induced by the two inclusions of $A\intersect B$ and $\Psi(a,b) = k_*a - l_*b$ by the two inclusions into $X$.
It is the long exact homology sequence of the short exact sequence of chain complexes
\[
0 \to C_n(A\intersect B) \mapsvia{x \mapsto (x, -x)} C_n(A)\oplus C_n(B) \mapsvia{(x,y)\mapsto x+y} C_n(A+B) \to 0
,\]
using that $C_*(A+B) \injects C_*(X)$ induces an isomorphism on homology.

The connecting map is explicit: represent $\alpha \in H_n(X)$ by a cycle $z = x+y$ with $x$ a chain in $A$ and $y$ a chain in $B$; then $\del x = -\del y$ is a cycle in $A\intersect B$, and $\del\alpha \da [\del x]$.

There is a formally identical sequence for reduced homology when $A \intersect B \neq \emptyset$, and one for cohomology with the arrows reversed.
:::

::: {.concept}
See Hatcher, §2.2, p. 149.
:::
