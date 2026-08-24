---
schema: qual/card@1
id: P-PUYFS
kind: problem
title: A compact set and a disjoint closed set in a metric space are positively separated
classification:
  areas:
  - real-analysis
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
---

Let $(X,d)$ be a metric space, $K\subset X$ be compact, and $F\subset X$ be closed.
If $K\cap F=\emptyset$, prove that there exists an $\epsilon>0$ so that $d(k,f)\geq \epsilon$ for all $k\in K$ and $f\in F$.

::: {.proof}
*Proof.* We prove this by contrapositive.
Suppose for all $\epsilon >0$, there exists $k \in K$, $f \in F$ such that $d(k,f)< \epsilon$.
Then for all $n \in \mathbb{N}$, we can choose $k_n \in K$, $f_n \in F$ such that $d(k_n, f_n) < \frac{1}{n}$.

Since $k_n$ is a sequence in $K$, which is compact (and therefore sequentially compact), there exists a subsequence $k_{n_j} \subseteq k_n$ with the property that $k_{n_j}$ converges to some $k_0 \in K$.
Find $N \in \mathbb{N}$ such that for $n \geq N$, $d(k_{n_j}, k_0) < \frac{\epsilon}{2}$ and $\frac{1}{n} < \frac{\epsilon}{2}$.
Then $$d(f_{n_j}, k_0) \leq d(f_{n_j}, k_{n_j}) + d(k_{n_j}, k_0) < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$$

Thus, $f_{n_j}$ also converges to $k_0$, and since $F$ is closed, $k_0 \in F$.
So $K \cap F \neq \emptyset$.
◻
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. The function $\delta(x) \da d(x,F) = \inf_{f\in F} d(x,f)$ is $1$-Lipschitz, hence continuous.
Proof: for $x, x' \in X$ and any $f \in F$, $d(x,f) \le d(x,x') + d(x',f)$, so $\delta(x) \le d(x,x') + \delta(x')$; symmetrically $\delta(x') \le d(x,x') + \delta(x)$, hence $|\delta(x) - \delta(x')| \le d(x,x')$.
<1>2. $\delta$ attains its minimum on the compact set $K$.
Proof: $\delta$ is continuous (<1>1), and a continuous function on a compact set attains its minimum: choose $k_n \in K$ with $\delta(k_n) \to \inf_K \delta$; a subsequence $k_{n_j} \to k \in K$ (sequential compactness in the metric space), and continuity gives $\delta(k) = \inf_K\delta$.
<1>3. $\inf_{k\in K} d(k,F) > 0$.
Proof: by <1>2 the infimum is $\delta(k)$ for some $k \in K$.
If $\delta(k) = 0$, then there is a sequence $f_n \in F$ with $d(k, f_n) \to 0$, so $f_n \to k$; since $F$ is closed, $k \in F$, contradicting $K \cap F = \emptyset$.
Hence $\delta(k) > 0$.
<1>4. There is $\eps > 0$ with $d(k,f) \ge \eps$ for all $k \in K$, $f \in F$.
Proof: take $\eps \da \inf_{k\in K} d(k,F) > 0$ from <1>3; then $d(k,f) \ge d(k,F) \ge \eps$ for all $k \in K$, $f \in F$.
<1>5. Q.E.D.

(The card already contains a proof by contrapositive using sequential compactness; the argument above is the direct version via continuity of the distance function.)
:::
