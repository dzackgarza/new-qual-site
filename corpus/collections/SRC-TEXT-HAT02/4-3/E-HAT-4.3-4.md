---
schema: qual/card@1
id: E-HAT-4.3-4
kind: problem
title: "Maps between Eilenberg--MacLane spaces"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m6__proofs-4-3-1-12.md (1-12: 10 correct, 5 a dimension slip, 9 a wrong assertion; both repaired) and m2__proofs-4-3-13-24.md (13-24: 10 correct, 20 a display misalignment repaired by identifying the principal fibration, 22 the missing converse of an iff, later restated and proved, and 24, whose whole proof was then written). No card in this slice has an unmet piece.

---

::: {.problem}
Given abelian groups $G$ and $H$ and CW complexes $K(G, n)$ and $K(H, n)$, show that the map $\langle K(G, n), K(H, n) \rangle \to \operatorname{Hom}(G, H)$ sending a homotopy class $[f]$ to the induced homomorphism $f_*: \pi_n(K(G, n)) \to \pi_n(K(H, n))$ is a bijection.
:::

::: {.solution}
Representability gives
$$
\langle K(G,n),K(H,n)\rangle
\cong H^n(K(G,n);H).
$$
Since $G$ is abelian, Hurewicz gives
$$
H_n(K(G,n);\ZZ)\cong\pi_n(K(G,n))\cong G,
$$
with $H_{n-1}=0$ for $n>1$. For $n=1$, $H_0\cong\ZZ$, so its Ext term also vanishes. The universal coefficient theorem therefore gives
$$
H^n(K(G,n);H)
\cong\operatorname{Hom}(H_n(K(G,n)),H)
\cong\operatorname{Hom}(G,H).
$$
Under these identifications, the class represented by
$$
f:K(G,n)\to K(H,n)
$$
is exactly the homomorphism induced on $\pi_n$, by naturality of Hurewicz and of the representing cohomology class. Thus
$$
\boxed{\langle K(G,n),K(H,n)\rangle\xrightarrow{\cong}\operatorname{Hom}(G,H),\quad[f]\mapsto f_*.}
$$
:::
