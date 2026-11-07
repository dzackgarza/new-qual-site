---
schema: qual/card@1
id: E-HAT-3.3-5
kind: problem
title: Orientability of products
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 5; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 5; it matches the printed text. The card says 'nonempty manifolds', which the print leaves implicit.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both directions: product charts with the product orientation in one direction, and in the
    other the restriction of the orientation system of $M\times N$ to $M\times\{y_0\}$, which is
    the tensor of the system of $M$ with a fixed copy of $\ZZ$.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Statement restored to the printed sentence (Hatcher p.257 §3.3 Ex.5), which has no nonemptiness
    hypothesis; the earlier card silently added one. The printed "iff" is false as it stands, and the
    solution now says why: $M=\emptyset$ is vacuously orientable and $M\times N=\emptyset$ with it, so
    the converse needs both factors nonempty. The equivalence itself is unchanged. Not checked here:
    whether the local-orientation system of a product is the tensor of the two (the Künneth-type
    identification is cited, not rederived).
---

::: {.problem}
Show that $M \times N$ is orientable iff $M$ and $N$ are both orientable.
:::

::: {.solution}
The printed statement needs both factors nonempty, and that is the case proved below: if $M=\emptyset$ then $M\times N=\emptyset$, which is vacuously orientable — the empty function is an orientation — whatever $N$ is. So fix nonempty $M$ and $N$.

Suppose first that $M^m$ and $N^n$ are oriented. Around $(x,y)\in M\times N$, choose oriented coordinate balls $U\ni x$ and $V\ni y$. Give $U\times V$ the product orientation. If one changes either oriented chart by an orientation-preserving transition map, the product transition map has positive determinant. Hence these product orientations are compatible and $M\times N$ is orientable.

Conversely suppose $M\times N$ is orientable. The local orientation system of a product is the tensor product of the two local orientation systems:
$$
H_{m+n}(M\times N,(M\times N)-\{(x,y)\};\ZZ)
\cong
H_m(M,M-\{x\};\ZZ)\otimes
H_n(N,N-\{y\};\ZZ).
$$
Fix $y_0\in N$. Restricting the orientation system of $M\times N$ to $M\times\{y_0\}$ gives the orientation system of $M$ tensored with the fixed rank-one group
$$
H_n(N,N-\{y_0\};\ZZ).
$$
Since the restricted product orientation system is trivial, the orientation system of $M$ is trivial. Thus $M$ is orientable. The same argument with a fixed $x_0\in M$ shows that $N$ is orientable.

Therefore
$$
\boxed{M\times N\text{ is orientable iff both }M\text{ and }N\text{ are orientable}.}
$$
:::
