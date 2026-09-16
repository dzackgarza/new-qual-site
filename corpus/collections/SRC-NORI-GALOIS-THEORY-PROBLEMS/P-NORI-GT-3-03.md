---
schema: qual/card@1
id: P-NORI-GT-3-03
kind: problem
title: Towers of quadratic extensions of $\mathbb F_p$ by iterated square roots
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 3.3 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
Let p be a prime which is  1 mod $2 ^ { k }$ , but not congruent to 1 modulo a higher power of 2. Assume $k \geq 2$ . Assume that $u _ { 0 } \in \mathbb { F } _ { p }$ is not a square.
Construct a sequence of pairs $\left( E _ { n } , u _ { n } \right)$ where $E _ { n }$ is a field and $u _ { n } \in E _ { n }$ as follows.
Define $( E _ { 0 } , u _ { 0 } ) = ( \mathbb { F } _ { p } , u _ { 0 } )$

Assume that $( E _ { n } , u _ { n } )$ has been defined.
Let $E _ { n + 1 }$ be a field extension of $E _ { n }$ obtaing by adjoining a square-root $u _ { n + 1 }$ of $u _ { n } \in E _ { n }$

Show that $\mathrm { d e g } ( E _ { n } / E _ { n - 1 } ) = 2$ for all $n > 0$
:::
