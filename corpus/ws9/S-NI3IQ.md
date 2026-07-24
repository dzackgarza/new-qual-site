---
schema: qual/card@1
id: S-NI3IQ
kind: solution
title: Solution to P-ULNGG
classification:
  areas:
  - real-analysis
  topics: []
relations:
- kind: solves
  target: P-ULNGG
review: draft
---

:::{.solution}
Without loss of generality we may assume that $E \subseteq [0,1]$. Letting $E_q = \bigcup_{0\le p\le q}\{x : |x-p/q|\le 1/q^3\}$ we see that $m(E_q)\le 2/q^2\ \forall q$ and hence that $\sum_{q=1}^{\infty} m(E_q) < \infty$.

This result now follows from Borel–Cantelli, or arguing directly (as in the proof of B–C) since $E \subseteq \bigcup_{q\ge Q} E_q\ \forall Q$ and $m\left(\bigcup_{q\ge Q} E_q\right) \le \sum_{q\ge Q} \frac{2}{q^2} \to 0$ as $Q\to\infty$.
:::
