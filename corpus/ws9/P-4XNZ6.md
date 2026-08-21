---
schema: qual/card@1
id: P-4XNZ6
kind: problem
title: Weak-type $(1,1)$ bound for the Hardy–Littlewood maximal function
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
Prove that the Hardy-Littlewood maximal function $f^*$ for an integrable function $f$ satisfies $$m(\{x \in \mathbb{R}^d : f^*(x) > \alpha\}) \le \frac{3^d}{\alpha}\|f\|_{L^1(\mathbb{R}^d)}$$ where $\alpha > 0$.
Recall that $$f^*(x) = \sup_{x\in B} \frac{1}{m(B)}\int_B |f(y)|dy, \quad x \in \mathbb{R}^d$$ where the supremum is taken over all balls containing the point $x$.
You may assume the Vitali 3-times Covering Lemma.
State it clearly if you use it.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. Reduce to a finite collection of balls via the Vitali covering lemma.
Proof: fix $\alpha > 0$ and let $E_\alpha = \{x : f^*(x) > \alpha\}$.
For each $x \in E_\alpha$ there is a ball $B_x$ containing $x$ with $\frac{1}{m(B_x)}\int_{B_x}|f| > \alpha$, i.e. $\int_{B_x}|f| > \alpha\,m(B_x)$.
By the Vitali $3$-times covering lemma (stated below), from the family $\{B_x\}_{x\in E_\alpha}$ we may select a countable disjoint subcollection $\{B_j\}$ such that $E_\alpha \subseteq \cup_j 3B_j$ (where $3B$ is the ball with the same center and $3$ times the radius).
<1>2. Vitali $3$-times covering lemma (as used).
Proof: given a family of balls in $\RR^d$ of bounded radius, there is a countable disjoint subfamily $\{B_j\}$ with $\cup B_j \supseteq$ (a.e.) the union of the original family, and in particular $E_\alpha \subseteq \cup_j 3B_j$.
<1>3. Bound the measure of $E_\alpha$.
Proof: by <1>1 and the disjointness of the $B_j$, \[ m(E_\alpha) \le \sum_j m(3B_j) = 3^d \sum_j m(B_j) \le \frac{3^d}{\alpha}\sum_j \int_{B_j}|f| = \frac{3^d}{\alpha}\int_{\cup_j B_j}|f| \le \frac{3^d}{\alpha}\int_{\RR^d}|f|, \] where the inequality $\sum_j m(B_j) \le \frac{1}{\alpha}\sum_j\int_{B_j}|f|$ uses $\int_{B_j}|f| > \alpha\, m(B_j)$ from <1>1. <1>4. Conclude.
Proof: <1>3 gives exactly $m(\{x : f^*(x) > \alpha\}) \le \frac{3^d}{\alpha}\|f\|_{L^1}$.
<1>5. Q.E.D.
:::
