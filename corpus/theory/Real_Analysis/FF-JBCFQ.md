---
schema: qual/card@1
id: FF-JBCFQ
kind: fact
title: $\limsup$ and $\liminf$ of a sequence of sets
prompts:
- Define $\limsup, \liminf$ for sequences of sets. What are their containments?
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Borel-Cantelli
relations: []
review: draft
---

::: {.fact}
Let $(A_n)_{n\geq 1}$ be a sequence of subsets of a set $X$.
Its [[D-PAEDW|limit inferior and limit superior]] are
$$
\liminf _{n \to \infty} A_n=\bigcup_{n \geq 1} \bigcap_{j \geq n} A_j, \qquad \limsup _{n \to \infty} A_n=\bigcap_{n \geq 1} \bigcup_{j \geq n} A_j.
$$
A point $x\in X$ lies in $\liminf_n A_n$ if and only if $x\in A_j$ for all but finitely many $j$, and in $\limsup_n A_n$ if and only if $x\in A_j$ for infinitely many $j$.
In particular, $\liminf _{n \to \infty} A_n \subseteq \limsup _{n \to \infty} A_n$.
:::

::: {.proof}
A point lies in $\bigcap_{j\geq n}A_j$ for some $n$ exactly when it lies in every $A_j$ with $j\geq n$ for some $n$, that is, in all but finitely many $A_j$.
A point lies in $\bigcup_{j\geq n}A_j$ for every $n$ exactly when for every $n$ it lies in some $A_j$ with $j\geq n$, that is, in infinitely many $A_j$.
A point in all but finitely many $A_j$ lies in infinitely many of them.
:::
