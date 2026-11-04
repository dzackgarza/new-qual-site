---
schema: qual/card@1
id: E-HAT-4.3-3
kind: problem
title: "Circle retract from direct summand on $H_1$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 3; the stored statement matches.
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
Suppose that a CW complex $X$ contains a subcomplex $S^1$ such that the inclusion $S^1 \hookrightarrow X$ induces an injection $H_1(S^1; \ZZ) \to H_1(X; \ZZ)$ with image a direct summand of $H_1(X; \ZZ)$.
Show that $S^1$ is a retract of $X$.
:::

::: {.solution}
Let
$$
i:S^1\hookrightarrow X
$$
be the inclusion. By hypothesis its image in $H_1(X;\ZZ)$ is a direct summand isomorphic to $\ZZ$. Hence there is a homomorphism
$$
\lambda:H_1(X;\ZZ)\to\ZZ
$$
whose composite with
$$
i_*:H_1(S^1)\to H_1(X)
$$
is the identity.

The universal coefficient theorem gives
$$
H^1(X;\ZZ)\cong\operatorname{Hom}(H_1(X),\ZZ).
$$
Let $u\in H^1(X;\ZZ)$ correspond to $\lambda$. By Theorem 4.57 choose
$$
r:X\to S^1
$$
with $r^*(\iota)=u$, where $\iota$ generates $H^1(S^1)$. Then
$$
(ri)^*\iota=i^*u=\iota,
$$
so $ri:S^1\to S^1$ has degree $1$ and is homotopic to the identity.

Since $S^1\subset X$ is a subcomplex, the homotopy extension property extends a homotopy
$$
ri\simeq\operatorname{id}_{S^1}
$$
to a homotopy of $r$. At the endpoint we obtain $r':X\to S^1$ satisfying
$$
r'i=\operatorname{id}_{S^1}.
$$
Hence
$$
\boxed{S^1\text{ is a retract of }X.}
$$
:::
