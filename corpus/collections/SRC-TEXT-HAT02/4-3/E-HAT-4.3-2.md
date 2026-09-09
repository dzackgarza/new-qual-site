---
schema: qual/card@1
id: E-HAT-4.3-2
kind: problem
title: "Group structure on $\\langle X, S^1 \\rangle$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that the group structure on $S^1$ coming from multiplication in $\mathbb{C}$ induces a group structure on $\langle X, S^1 \rangle$ such that the bijection $\langle X, S^1 \rangle \to H^1(X; \mathbb{Z})$ of Theorem 4.57 is an isomorphism.

::: {.solution}
For maps \(f,g:X\to S^1\), define
\[
(fg)(x)=f(x)g(x)
\]
using multiplication in \(S^1\subset\mathbb C\). Pointwise multiplication and inversion descend to homotopy classes, giving a group structure on \(\langle X,S^1\rangle\).

Let
\[
u\in H^1(S^1;\mathbb Z)
\]
be the canonical generator. For the multiplication
\[
\mu:S^1\times S^1\to S^1,
\]
restriction to each factor has degree \(1\), so by Künneth
\[
\mu^*u=\operatorname{pr}_1^*u+\operatorname{pr}_2^*u.
\]
Therefore
\[
(fg)^*u=(f,g)^*\mu^*u=f^*u+g^*u.
\]
Theorem 4.57 identifies \([f]\) with \(f^*u\), hence this bijection preserves addition. Thus
\[
\boxed{\langle X,S^1\rangle\cong H^1(X;\mathbb Z)}
\]
as groups.
:::
