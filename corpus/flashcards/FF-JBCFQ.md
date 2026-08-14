---
schema: qual/card@1
id: FF-JBCFQ
kind: fact
title: "Define $\\limsup, \\liminf$ for sequences of sets. What are their containments?"
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
  - borel-cantelli
relations: []
review: draft
---

::: {.fact title="Define $ \limsup, \liminf $ for sequences of sets. What are their containments?"}
$$\liminf _{n \rightarrow \infty} A_n=\bigcup_{n \geq 1} \bigcap_{j \geq n} A_j, \qquad \limsup _{n \rightarrow \infty} A_n=\bigcap_{n \geq 1} \bigcup_{j \geq n} A_j$$

- Supremum: Union, $ \limsup = \inf\sup $, in infinitely many

- Infimum: Intersection, $ \liminf = \sup\inf $, eventually in

- $ \liminf _{n \rightarrow \infty} A_n \subseteq \limsup _{n \rightarrow \infty} A_n $ since "all but finitely many" implies "infinitely often".
:::
