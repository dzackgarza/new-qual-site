---
schema: qual/card@1
id: P-Y2AZO
kind: problem
title: The Hardy–Littlewood weak-type $(1,1)$ inequality
classification:
  areas:
  - real-analysis
  topics:
  - maximal-functions
  - measure-theory
  - l1
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
For $f:\mathbb{R}\to\mathbb{R}$ in $L^1(\mathbb{R})$, let $Mf$ be the (centered) Hardy-Littlewood maximal function.
Prove there is a constant $A$ such that for any $\lambda>0$, $$m\{x\in\mathbb{R}: Mf(x)>\lambda\} \le \frac{A}{\lambda}||f||_{L^1}$$ where $m$ is Lebesgue measure.
If you use a covering lemma, you should prove it.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** Prove the weak (1,1) bound $m\{x : Mf(x) > \lambda\} \le \frac{A}{\lambda}\|f\|_{L^1}$ for the centered Hardy–Littlewood maximal function, proving the covering lemma used.

<1>1. Setup: $Mf(x) = \sup_{r > 0} \frac{1}{2r}\int_{x-r}^{x+r}|f|$; fix $\lambda > 0$, set $E_\lambda = \{x : Mf(x) > \lambda\}$.
Proof: definitions.

<1>2. For each $x \in E_\lambda$, choose $r_x > 0$ with $\frac{1}{2r_x}\int_{x-r_x}^{x+r_x}|f| > \lambda$, i.e. $\int_{I_x}|f| > 2\lambda r_x$ where $I_x = (x - r_x, x + r_x)$.
Proof: definition of the supremum (choose $r_x$ realizing the inequality up to the sup; since $Mf(x) > \lambda$, some $r$ works with $> \lambda$).

<1>3. Covering lemma (Vitali-type): from the family $\{I_x : x \in E_\lambda\}$, extract a countable disjoint subfamily $\{I_j\}$ with $E_\lambda \subseteq \bigcup_j 5I_j$ (the intervals scaled by $5$). Proof: (proving it) — the standard Vitali covering lemma in one dimension: take a maximal disjoint subfamily.
Greedy: choose $I_1$ with $r_{I_1} > \frac12 \sup r_x$; discard all intervals intersecting $I_1$; repeat.
The discarded intervals have radius $\le 2r_{I_1}$ (actually $\le 2$ times the chosen radius), so they're contained in $5I_1$.
Inductively the chosen intervals are disjoint and every $I_x$ meets some chosen $I_j$ with $r_{I_x} \le 2r_{I_j}$, so $I_x \subseteq 5I_j$; hence $E_\lambda \subseteq \bigcup_j 5I_j$.
(For the centered intervals here, the constant $5$ works; $3$ would suffice with care — we use $5$ to be safe.)

<1>4. $m(E_\lambda) \le \sum_j m(5I_j) = 5\sum_j m(I_j) \le \frac{5}{2\lambda}\sum_j \int_{I_j}|f| = \frac{5}{2\lambda}\int_{\cup I_j}|f| \le \frac{5}{2\lambda}\|f\|_1$.
Proof: <1>3 gives $m(E_\lambda) \le \sum_j m(5I_j) = 5\sum_j 2r_j$; and $2\lambda r_j < \int_{I_j}|f|$ by <1>2, so $\sum_j 2r_j < \frac{1}{\lambda}\sum_j\int_{I_j}|f|$; disjointness of the $I_j$'s lets the sum of integrals equal the integral over the union, which is $\le \|f\|_1$.

<1>5. Q.E.D. Proof: <1>4 is the weak (1,1) bound with $A = 5/2$ (any constant works).
:::
