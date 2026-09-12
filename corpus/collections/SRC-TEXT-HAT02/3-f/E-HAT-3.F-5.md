---
schema: qual/card@1
id: E-HAT-3.F-5
kind: problem
title: "$\\operatorname{Ext}(A, \\mathbb{Z})$ as a cokernel"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.F, Exercise 5; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that $\operatorname{Ext}(A, \mathbb{Z})$ is isomorphic to the cokernel of $\operatorname{Hom}(A, \mathbb{Q}) \to \operatorname{Hom}(A, \mathbb{Q}/\mathbb{Z})$, the map induced by the quotient map $\mathbb{Q} \to \mathbb{Q}/\mathbb{Z}$.
Use this to get another proof that $\operatorname{Ext}(\mathbb{Z}_{p^\infty}, \mathbb{Z}) \approx \widehat{\mathbb{Z}}_p$ for $p$ prime.

::: {.solution}
Apply $\operatorname{Hom}(A,-)$ and its derived functor $\operatorname{Ext}(A,-)$ to
\[
0\longrightarrow\mathbb Z\longrightarrow\mathbb Q
\longrightarrow\mathbb Q/\mathbb Z\longrightarrow0.
\]
Since $\mathbb Q$ is divisible, Exercise 4 gives
\[
\operatorname{Ext}(A,\mathbb Q)=0.
\]
The resulting exact sequence therefore contains
\[
\operatorname{Hom}(A,\mathbb Q)
\longrightarrow
\operatorname{Hom}(A,\mathbb Q/\mathbb Z)
\longrightarrow
\operatorname{Ext}(A,\mathbb Z)
\longrightarrow0.
\]
Hence
\[
\boxed{\operatorname{Ext}(A,\mathbb Z)
\cong\operatorname{coker}\bigl(\operatorname{Hom}(A,\mathbb Q)	o
\operatorname{Hom}(A,\mathbb Q/\mathbb Z)\bigr).}
\]

Now take $A=\mathbb Z_{p^\infty}$. Since $A$ is torsion and $\mathbb Q$ is torsionfree,
\[
\operatorname{Hom}(A,\mathbb Q)=0.
\]
Thus
\[
\operatorname{Ext}(\mathbb Z_{p^\infty},\mathbb Z)
\cong\operatorname{Hom}(\mathbb Z_{p^\infty},\mathbb Q/\mathbb Z).
\]
The $p$-primary subgroup of $\mathbb Q/\mathbb Z$ is itself isomorphic to $\mathbb Z_{p^\infty}$, so every homomorphism lands there and
\[
\operatorname{Hom}(\mathbb Z_{p^\infty},\mathbb Q/\mathbb Z)
\cong\operatorname{End}(\mathbb Z_{p^\infty}).
\]
An endomorphism is determined by compatible multipliers modulo $p^n$ on the unique cyclic subgroup of order $p^n$. Hence
\[
\operatorname{End}(\mathbb Z_{p^\infty})
\cong\varprojlim_n\mathbb Z/p^n\mathbb Z
=\widehat{\mathbb Z}_p.
\]
Therefore
\[
\boxed{\operatorname{Ext}(\mathbb Z_{p^\infty},\mathbb Z)
\cong\widehat{\mathbb Z}_p.}
\]
:::
