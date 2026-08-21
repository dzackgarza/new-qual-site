---
schema: qual/card@1
id: P-MFYGZ
kind: problem
title: Weak-$(1,1)$ inequality for the Hardy–Littlewood maximal function
classification:
  areas:
  - real-analysis
  topics:
  - Maximal Functions
  - Measure Theory
  - L¹
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Let $f \in L^1(\mathbb{R}^d)$ and $M_f$ denote the Hardy-Littlewood maximal function of $f$; in other words, $$M_f(x) = \sup_B \frac{1}{m(B)}\int_B |f(y)|dy, \quad x \in \mathbb{R}^d$$ where the supremum is taken over all balls containing the point $x$.
Prove that $$m(\{x : M_f(x) > \alpha\}) \le \frac{A}{\alpha}\|f\|_{L^1(\mathbb{R}^d)}, \quad \forall \alpha > 0$$ where $A$ is a constant depending only on $d$ and $\|f\|_{L^1(\mathbb{R}^d)} = \int_{\mathbb{R}^d}|f(x)|dx$.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Reduce the claim to a covering argument.
Proof: fix $\alpha > 0$ and set $E_\alpha = \{x : M_f(x) > \alpha\}$.
For each $x \in E_\alpha$ there is a ball $B_x \ni x$ with $\frac{1}{m(B_x)}\int_{B_x}|f| > \alpha$, i.e. $m(B_x) < \frac{1}{\alpha}\int_{B_x}|f|$.
The family $\{B_x\}_{x\in E_\alpha}$ covers $E_\alpha$.
<1>2. Apply the Vitali covering lemma.
Proof: by the Vitali covering lemma there is a countable subfamily of pairwise disjoint balls $\{B_j\}$ with $E_\alpha \subseteq \bigcup_j 5B_j$, where $5B_j$ is the ball with the same center and five times the radius.
Therefore \[m(E_\alpha) \le \sum_j m(5B_j) = 5^d\sum_j m(B_j) \le \frac{5^d}{\alpha}\sum_j \int_{B_j}|f| \le \frac{5^d}{\alpha}\int_{\mathbb{R}^d}|f|\,dx,\] the last step by disjointness of the $B_j$.
So the weak $(1,1)$ inequality holds with $A = 5^d$.
<1>3. Q.E.D.
:::
