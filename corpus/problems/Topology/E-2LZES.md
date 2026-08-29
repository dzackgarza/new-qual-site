---
schema: qual/card@1
id: E-2LZES
kind: exercise
title: Compactness, limit point compactness, and sequential compactness are equivalent for metrizable spaces
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that for $X$ metrizable, the following are equivalent:

- $X$ is compact;

- $X$ is limit point compact;

- $X$ is sequentially compact.
:::

::: {.remark}
The original exercise read "Show that if $X$ is metrizable, then $X$ is compact", which is false ($\RR$ is metrizable and not compact).
The equivalence above repairs it; the neighbouring exercises suggest the intended statement.
:::

::: solution
**Goal:** Prove the equivalence of compactness, limit point compactness, and sequential compactness for any metrizable space $(X, d)$.

<1>1. Compact $\implies$ Limit point compact: *Proof:* <2>1. Let $X$ be compact, and let $A \subseteq X$ be an infinite subset.
<2>2. Suppose for contradiction that $A$ has no limit point in $X$.
<2>3. Then for every $x \in X$, there exists an open neighborhood $U_x$ such that $U_x \cap A \subseteq \{x\}$.
<2>4. The family $\{U_x\}_{x \in X}$ is an open cover of $X$.
Since $X$ is compact, there exists a finite subcover $\{U_{x_1}, \dots, U_{x_k}\}$.
<2>5. Then $A = A \cap \bigcup_{i=1}^k U_{x_i} = \bigcup_{i=1}^k (A \cap U_{x_i}) \subseteq \{x_1, \dots, x_k\}$.
<2>6. This implies $|A| \le k$, contradicting the assumption that $A$ is infinite.
Hence $A$ has a limit point.

<1>2. Limit point compact $\implies$ Sequentially compact: *Proof:* <2>1. Let $(x_n)_{n=1}^\infty$ be a sequence in $X$.
<2>2. Case 1 (finite range): If $R = \{x_n : n \in \mathbb{Z}_+\}$ is finite, by the Pigeonhole Principle there exists a point $x \in R$ and a subsequence $(x_{n_k})$ with $x_{n_k} = x$ for all $k$, which converges to $x$.
<2>3. Case 2 (infinite range): If $R$ is infinite, limit point compactness implies $R$ has a limit point $x \in X$.
<2>4. In a metric space, every open ball $B(x, \varepsilon)$ contains infinitely many points of $R$.
<2>5. We inductively construct a subsequence: choose $n_1$ such that $x_{n_1} \in B(x, 1) \setminus \{x\}$.
Having chosen $n_1 < \dots < n_{k-1}$, choose $n_k > n_{k-1}$ such that $x_{n_k} \in B(x, 1/k)$.
<2>6. Then $d(x_{n_k}, x) < 1/k \to 0$, so $(x_{n_k}) \to x$, proving sequential compactness.

<1>3. Sequentially compact $\implies$ Compact: *Proof:* <2>1. **Lebesgue Number Lemma:** Every open cover $\mathcal{U}$ of a sequentially compact metric space has a Lebesgue number $\delta > 0$.
- If not, for each $n \in \mathbb{Z}_+$ there exists a set $C_n \subset X$ with $\operatorname{diam}(C_n) < 1/n$ not contained in any $U \in \mathcal{U}$.
- Pick $y_n \in C_n$.
By sequential compactness, a subsequence $(y_{n_k})$ converges to some $y_0 \in X$.
- Since $\mathcal{U}$ covers $X$, $y_0 \in U_0$ for some $U_0 \in \mathcal{U}$.
Choose $\varepsilon > 0$ such that $B(y_0, \varepsilon) \subseteq U_0$.
- For large $k$, $d(y_{n_k}, y_0) < \varepsilon/2$ and $\operatorname{diam}(C_{n_k}) < \varepsilon/2$, which implies $C_{n_k} \subseteq B(y_0, \varepsilon) \subseteq U_0$, contradiction.
<2>2. **Total Boundedness:** $X$ is totally bounded.
- If for some $\varepsilon > 0$, $X$ cannot be covered by finitely many $\varepsilon$-balls, inductively pick $z_1 \in X$ and $z_{n+1} \notin \bigcup_{i=1}^n B(z_i, \varepsilon)$.
- Then $d(z_i, z_j) \ge \varepsilon$ for all $i \neq j$, so $(z_n)$ can have no convergent subsequence, contradicting sequential compactness.
<2>3. **Finite subcover extraction:** Let $\mathcal{U}$ be an open cover of $X$.
- Let $\delta > 0$ be a Lebesgue number for $\mathcal{U}$.
- By total boundedness, cover $X$ by finitely many balls $B(p_1, \delta/2), \dots, B(p_m, \delta/2)$.
- Since $\operatorname{diam}(B(p_j, \delta/2)) \le \delta$, each ball is contained in some $U_j \in \mathcal{U}$.
- Then $\{U_1, \dots, U_m\}$ is a finite subcover of $\mathcal{U}$, proving $X$ is compact.

<1>4. Conclusion: The three compactness notions are fully equivalent for metrizable spaces.
Q.E.D.
:::
