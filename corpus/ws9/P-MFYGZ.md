---
schema: qual/card@1
id: P-MFYGZ
kind: problem
title: Let $f \in L^1(\mathbb{R}^d)$ and $M_f$ denote the Hardy-Littlewood ma…
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

:::{.problem title="?"}
Let $f \in L^1(\mathbb{R}^d)$ and $M_f$ denote the Hardy-Littlewood maximal function of $f$; in other words,
$$M_f(x) = \sup_B \frac{1}{m(B)}\int_B |f(y)|dy, \quad x \in \mathbb{R}^d$$
where the supremum is taken over all balls containing the point $x$. Prove that
$$m(\{x : M_f(x) > \alpha\}) \le \frac{A}{\alpha}\|f\|_{L^1(\mathbb{R}^d)}, \quad \forall \alpha > 0$$
where $A$ is a constant depending only on $d$ and $\|f\|_{L^1(\mathbb{R}^d)} = \int_{\mathbb{R}^d}|f(x)|dx$.
:::
