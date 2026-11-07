---
schema: qual/card@1
id: E-HAT-2.3-3
kind: problem
title: Reduced homology theory vanishes on point; suspension isomorphism follows
classification:
  areas:
  - topology
  topics:
  - Homology
  - Axiomatic Homology
  - Suspension
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.3, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 2.3, Exercise 3; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both halves: applying exactness to the pair $(*,*)$ makes both maps the identity, so
    $\tilde h_n(*)$ is its own kernel and vanishes; and the exact sequence of $(CX,X)$ with $CX$
    contractible gives a boundary isomorphism $\tilde h_{n+1}(CX/X)\cong\tilde h_n(X)$, with
    $CX/X=SX$.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 3 of §2.3 as printed on p. 165. The vanishing at a point is right:
    in the exact sequence of the pair (*,*) both maps are the identity, so the middle group is
    both zero and the whole group. For the suspension, the cone is contractible, so its h-groups
    vanish by homotopy invariance once h(point) = 0, and the pair sequence of (CX,X) sandwiches
    h~_{n+1}(SX) between two vanishing groups. Axioms (1) and (2) are now cited to p. 160.
    What is not covered: no certificate.
---

::: {.problem}
Show that if $\tilde{h}$ is a reduced homology theory, then $\tilde{h}_n(\text{point}) = 0$ for all $n$.
Deduce that there are suspension isomorphisms $\tilde{h}_n(X) \approx \tilde{h}_{n+1}(SX)$ for all $n$.
:::

::: {.solution}
Apply the exactness axiom, axiom (2) of p. 160, to the CW pair $(*,*)$. The inclusion $*\to *$ and the quotient map $*\to */*=*$ are both the identity. Thus the exact sequence contains
$$
\widetilde h_n(*)\xrightarrow{\mathrm{id}}\widetilde h_n(*)
\xrightarrow{\mathrm{id}}\widetilde h_n(*).
$$
The image of the first map is the whole group, while the kernel of the second is zero. Exactness forces $\widetilde h_n(*)=0$ for every $n$.

Let $CX$ be the cone on $X$. It is contractible, so homotopy invariance, axiom (1) of p. 160, gives $\widetilde h_k(CX)=\widetilde h_k(\mathrm{pt})=0$ for every $k$. The exact sequence of the CW pair $(CX,X)$ therefore contains
$$
0=\widetilde h_{n+1}(CX)
\longrightarrow\widetilde h_{n+1}(CX/X)
\xrightarrow{\partial}\widetilde h_n(X)
\longrightarrow\widetilde h_n(CX)=0.
$$
Since $CX/X\cong SX$, the boundary map gives the required suspension isomorphism.
:::
