---
schema: qual/card@1
id: P-QQTBQ
kind: problem
title: Every finitely generated torsion-free abelian group is free abelian
classification:
  areas:
  - algebra
  topics:
  - Free Modules
  - Torsion
  - Abelian Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Prove that every finitely generated torsion-free abelian group is free abelian.
:::

::: solution
By the structure theorem for finitely generated abelian groups,
\[
G\cong \mathbb Z^r\oplus \mathbb Z/d_1\mathbb Z\oplus\cdots\oplus\mathbb Z/d_s\mathbb Z
\]
with $d_i\ge2$. The finite direct summand is exactly the torsion subgroup of $G$. If $G$ is torsion-free, then $s=0$, so
\[
G\cong\mathbb Z^r.
\]
Hence every finitely generated torsion-free abelian group is free abelian.
:::
