---
schema: qual/card@1
id: P-PUYFS
kind: problem
title: "Let $(X,d)$ be a metric space, $K\\subset X$ be"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
Let $(X,d)$ be a metric space, $K\subset X$ be
compact, and $F\subset X$ be closed. If $K\cap F=\emptyset$, prove
that there exists an $\epsilon>0$ so that $d(k,f)\geq \epsilon$ for
all $k\in K$ and $f\in F$.

:::{.proof}
*Proof.* We prove this by contrapositive. Suppose for all
$\epsilon >0$, there exists $k \in K$, $f \in F$ such that
$d(k,f)< \epsilon$. Then for all $n \in \mathbb{N}$, we can choose
$k_n \in K$, $f_n \in F$ such that $d(k_n, f_n) < \frac{1}{n}$.

Since $k_n$ is a sequence in $K$, which is compact (and therefore
sequentially compact), there exists a subsequence
$k_{n_j} \subseteq k_n$ with the property that $k_{n_j}$ converges
to some $k_0 \in K$. Find $N \in \mathbb{N}$ such that for
$n \geq N$, $d(k_{n_j}, k_0) < \frac{\epsilon}{2}$ and
$\frac{1}{n} < \frac{\epsilon}{2}$. Then
$$d(f_{n_j}, k_0) \leq d(f_{n_j}, k_{n_j}) + d(k_{n_j}, k_0) < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$$

Thus, $f_{n_j}$ also converges to $k_0$, and since $F$ is closed,
$k_0 \in F$. So $K \cap F \neq \emptyset$. ◻
:::
