---
schema: qual/card@1
id: T-OTR5M
kind: theorem
title: "Borel-Cantelli"
classification:
  areas:
  - real-analysis
  topics:
  - borel-cantelli
  - measure-theory
relations: []
review: draft
---
:::{.theorem title="Borel-Cantelli"}
Let $\{E_{k}\}$ be a countable collection of measurable sets.
Then
\[
\sum_{k} m(E_{k}) < \infty \implies \text{ almost every } x\in \RR \text{ is in at most finitely many } E_{k}
\iff
m(\limsup_k E_k) = 0
.\]

In words, interpreting $E_k$ as events and $m(E_k) = \PP(E_k)$ as a probability: if the sum of probabilities of events is finite, the probability of infinitely many events occurring is zero.
:::
