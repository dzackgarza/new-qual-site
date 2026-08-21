---
schema: qual/card@1
id: D-PAEDW
kind: definition
title: Limsup and Liminf of Sets
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Borel-Cantelli
relations: []
review: draft
---

:::{.definition title="Limsup and Liminf of Sets"}
\[
\liminf_{n} E_{n} \da \Union_{N=1}^\infty \Intersect_{n=N}^\infty E_{n} &= \theset{x \suchthat x\in E_{n} \text{ for all but finitely many } n}  \\
\limsup_{n} E_{n} \da \Intersect_{N=1}^\infty \Union_{n=N}^{\infty} E_{n} &= \theset{x \suchthat x\in E_{n} \text{ for infinitely many } n} 
.\]

:::
