---
schema: qual/card@1
id: P-ULNGG
kind: problem
title: Almost every point of a finite-measure set lies in only finitely many of the
  sets $E_q=\bigcup_{0\le p\le q}\{x:|x-p/q|\le 1/q^3\}$
classification:
  areas:
  - real-analysis
  topics:
  - Borel-Cantelli
  - Measure Theory
relations: []
review: draft
---

::: {.problem}
[Reconstructed from solution — no problem statement page was present in this solutions-only document.] Let $E$ be a set of finite Lebesgue measure.
For each positive integer $q$ let $E_q = \bigcup_{0\le p \le q}\{x : |x-p/q|\le 1/q^3\}$.
Show that almost every $x\in E$ lies in only finitely many of the sets $E_q$.
:::

::: {.solution}
Without loss of generality we may assume that $E \subseteq [0,1]$.
Letting $E_q = \bigcup_{0\le p\le q}\{x : |x-p/q|\le 1/q^3\}$ we see that $m(E_q)\le 2/q^2\ \forall q$ and hence that $\sum_{q=1}^{\infty} m(E_q) < \infty$.

This result now follows from Borel–Cantelli, or arguing directly (as in the proof of B–C) since $E \subseteq \bigcup_{q\ge Q} E_q\ \forall Q$ and $m\left(\bigcup_{q\ge Q} E_q\right) \le \sum_{q\ge Q} \frac{2}{q^2} \to 0$ as $Q\to\infty$.
:::
