---
schema: qual/card@1
id: E-HAT-3.F-5
kind: problem
title: "$\\operatorname{Ext}(A, \\ZZ)$ as a cokernel"
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

::: {.problem}
Show that $\operatorname{Ext}(A, \ZZ)$ is isomorphic to the cokernel of $\operatorname{Hom}(A, \QQ) \to \operatorname{Hom}(A, \QQ/\ZZ)$, the map induced by the quotient map $\QQ \to \QQ/\ZZ$.
Use this to get another proof that $\operatorname{Ext}(\ZZ_{p^\infty}, \ZZ) \approx \widehat{\ZZ}_p$ for $p$ prime.
:::

::: {.solution}
Apply $\operatorname{Hom}(A,-)$ and its derived functor $\operatorname{Ext}(A,-)$ to
$$
0\longrightarrow\ZZ\longrightarrow\QQ
\longrightarrow\QQ/\ZZ\longrightarrow0.
$$
Since $\QQ$ is divisible, Exercise 4 gives
$$
\operatorname{Ext}(A,\QQ)=0.
$$
The resulting exact sequence therefore contains
$$
\operatorname{Hom}(A,\QQ)
\longrightarrow
\operatorname{Hom}(A,\QQ/\ZZ)
\longrightarrow
\operatorname{Ext}(A,\ZZ)
\longrightarrow0.
$$
Hence
$$
\boxed{\operatorname{Ext}(A,\ZZ)
\cong\operatorname{coker}\bigl(\operatorname{Hom}(A,\QQ)\to
\operatorname{Hom}(A,\QQ/\ZZ)\bigr).}
$$

Now take $A=\ZZ_{p^\infty}$. Since $A$ is torsion and $\QQ$ is torsionfree,
$$
\operatorname{Hom}(A,\QQ)=0.
$$
Thus
$$
\operatorname{Ext}(\ZZ_{p^\infty},\ZZ)
\cong\operatorname{Hom}(\ZZ_{p^\infty},\QQ/\ZZ).
$$
The $p$-primary subgroup of $\QQ/\ZZ$ is itself isomorphic to $\ZZ_{p^\infty}$, so every homomorphism lands there and
$$
\operatorname{Hom}(\ZZ_{p^\infty},\QQ/\ZZ)
\cong\operatorname{End}(\ZZ_{p^\infty}).
$$
An endomorphism is determined by compatible multipliers modulo $p^n$ on the unique cyclic subgroup of order $p^n$. Hence
$$
\operatorname{End}(\ZZ_{p^\infty})
\cong\varprojlim_n\ZZ/p^n\ZZ
=\widehat{\ZZ}_p.
$$
Therefore
$$
\boxed{\operatorname{Ext}(\ZZ_{p^\infty},\ZZ)
\cong\widehat{\ZZ}_p.}
$$
:::
