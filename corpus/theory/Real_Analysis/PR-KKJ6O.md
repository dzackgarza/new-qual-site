---
schema: qual/card@1
id: PR-KKJ6O
kind: proposition
title: Continuity of measure from below and from above
classification:
  areas:
  - real-analysis
  topics:
  - Continuity of Measure
  - Measure Theory
relations: []
review: draft
---

::: {.proposition}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure space]] and let $E_n\in\mcm$ for $n\geq1$ [@Fol13, Theorem 1.8].

(a) If $E_1\subseteq E_2\subseteq\cdots$ and $E\coloneqq\bigcup_{n\geq1}E_n$, then $\mu(E_n)\to\mu(E)$.

(b) If $E_1\supseteq E_2\supseteq\cdots$, $\mu(E_1)<\infty$, and $E\coloneqq\bigcap_{n\geq1}E_n$, then $\mu(E_n)\to\mu(E)$.
:::

::: {.example}
The hypothesis $\mu(E_1)<\infty$ in (b) is needed: for Lebesgue measure $m$ on $\RR$ and $E_n\coloneqq[n,\infty)$, $m(E_n)=\infty$ for all $n$ but $\bigcap_n E_n=\emptyset$.
:::
