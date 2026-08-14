---
schema: qual/card@1
id: P-I73ZD
kind: problem
title: "Let $(M, d_M)$, $(N, d_N)$ be metric spaces. Define"
classification:
  areas:
  - real-analysis
  topics:
  - metric-spaces
  - compactness
relations: []
review: draft
---
Let $(M, d_M)$, $(N, d_N)$ be metric spaces. Define
$d_{M \times N} \colon (M \times N) \times (M \times N) \to \mathbb{R}$
by
$$d_{M \times N}((x_1, y_1), (x_2, y_2)) := d_M(x_1, x_2) + d_N(y_1, y_2).$$

1.  
Prove that $(M \times N, d_{M \times N})$ is a metric space.

2.  
Let $S \subseteq M$ and $T \subseteq N$ be compact sets in
$(M, d_M)$ and $(N, d_N)$, respectively. Prove that $S \times T$
is a compact set in $(M \times N, d_{M \times N})$.

:::{.proof}
*Proof.* To prove that $(M \times N, d_{M \times N})$ is a
metric space we must prove that $d_{M\times N}$ is a metric on
$M \times N$.

-   Positive Definite-

Let $(x_1,y_1), (x_2,y_2) \in M \times N$. Then since $d_M$
is a metric on $M$, then $d_M(x_1,x_2)\geq 0$ for all
$x_i,x_j \in M$ and $d_N$ is a metric on $N$ and likewise
$d_N(y_1,y_2)\geq 0$ for any $y_i,y_j \in N.$

Then by definition
$d_{M\times N}((x_1,y_1),(x_2,y_2))=d_M(x_1,x_2)+d_N(y_1,y_2)\geq 0 + 0 =0.$
Hence since $(x_1,y_1),(x_2,y_2)$ are arbitrary,
$d_{M\times N}((x_1,y_1),(x_2,y_2))\geq 0$ for all
$(x_i,y_i),(x_j,y_j)\in M \times N$.

Suppose that $d_{M \times N}((x_1,y_1),(x_2,y_2))=0.$ By
definition
$d_{M \times N}((x_1,y_1),(x_2,y_2))=d_M(x_1,x_2)+d_N(y_1,y_2)$.
Therefore $d_M(x_1,x_2)+d_N(y_1,y_2)=0$, since $d_M, d_N$
are metrics, then $d_M(x_1,x_2)\geq 0, d_N(y_1,y_2)\geq 0$,
which implies that $d_M(x_1,x_2)=d_N(y_1,y_2)=0$ and also
since they are metrics we have that $x_1=x_2, y_1=y_2.$
Hence, $(x_1,y_1)=(x_2,y_2).$

Now suppose that $(x_1,y_1)=(x_2,y_2).$ Then
$x_1=x_2, y_1=y_2$ and for the metrics $d_M, d_N$ we would
have $d_M(x_1,x_2)=0, d_N(y_1,y_2)=0.$ Thus
$d_{M \times N}((x_1,y_1),(x_2,y_2))=d_M(x_1,x_2)+d_N(y_1,y_2)=0+0=0$.

Therefore $d_{M \times N}((x_1,y_1),(x_2,y_2))=0$ if and
only if $(x_1,y_1)=(x_2,y_2).$

-   Symmetric

Let $(x_1,y_1), (x_2,y_2) \in M \times N$. Then since $d_M$
is a metric on $M$, then $d_M(x_1,x_2)=d_M(x_2,x_1)$ for all
$x_i,x_j \in M$ and $d_N$ is a metric on $N$ and likewise
$d_N(y_1,y_2)=d_N(y_2,y_1)$ for any $y_i,y_j \in N.$
Therefore, $$\begin{aligned}
d_{M \times N}((x_1,y_1),(x_2,y_2))&=d_M(x_1,x_2)+d_N(y_1,y_2)\\
&=d_M(x_2,x_1)+d_N(y_2,y_1)\\
&=d_{M \times N}((x_2,y_2),(x_1,y_1)).
\end{aligned}$$

-   Triangle Inequality

Since $d_M, d_N$ are metrics then for all
$x_1,x_2,x_3 \in M, y_1,y_2,y_3 \in N$ we have that
$d_M(x_1,x_2)\leq d_M(x_1,x_3)+d_M(x_3,x_2)$ and that
$d_N(y_1,y_2)\leq d_N(y_1,y_3)+d_N(y_3,y_2).$ Therefore,
$$\begin{aligned}
d_{M \times N}((x_1,y_1),(x_2,y_2))&=d_M(x_1,x_2)+d_N(y_1,y_2)\\
d_M(x_1,x_2)+d_N(y_1,y_2) &\leq d_M(x_1,x_3)+d_M(x_3,x_2)+d_N(y_1,y_3)+d_N(y_3,y_2)\\
d_M(x_1,x_3)+d_M(x_3,x_2)+d_N(y_1,y_3)+d_N(y_3,y_2) &=d_M(x_1,x_3)+d_N(y_1,y_3)+d_M(x_3,x_2)+d_N(y_3,y_2)\\
d_M(x_1,x_3)+d_N(y_1,y_3)+d_M(x_3,x_2)+d_N(y_3,y_2)&=d_M((x_1,y_1),(x_3,y_3))+d_M((x_3,y_3),(x_2,y_2)). 
\end{aligned}$$

Hence
$d_{M \times N}((x_1,y_1),(x_2,y_2))\leq d_M((x_1,y_1),(x_3,y_3))+d_M((x_3,y_3),(x_2,y_2)).$

Therefore $d_{M \times N}$ is a metric on $M \times N$ and
$(M \times N, d_{M\times N})$ is a metric space. ◻
:::

:::{.proof}
*Proof.* By part a we showed that $(M \times N, d_{M \times N})$
is a metric space. Let $\{s_n,t_n\}$ be a sequence in
$S \times T.$ Since $\{s_n\}$ is a sequence on a compact set $S$
in a metric space $(M,d_M)$ then it has a convergent subsequence
${s_{n_k}}.$ Let $\lim_{k \to \infty}{s_{n_k}}=s_0.$

Since $\{t_{n_k}\}$ is a sequence on a compact set $T$ in a
metric space. Thus $\{t_{n_k}\}$ has a convergent subsequence
$\{t_{n_{k_j}}\}.$ Let $\lim_{j\to \infty} t_{n_{k_j}}=t_0.$
Thus $\{s_{n_{k_j}}\}$ is a subsequence of $\{s_{n_k}\}.$ And
since $\{s_{n_k}\}$ converges to $s_0$, then any subsequence
also converges to $s_0.$

Let $\epsilon >0$ be given. Then for $\epsilon/2$ there exists
$N_1, N_2\in \mathbb{N}$ such that for all
$n_{k_j}\geq N_1, d_M(s_{n_{k_j}},s_0)<\epsilon/2$, and for all
$n_{k_j}\geq N_2, d_N(t_{n_{k_j}},t_0)<\epsilon/2$. Choose
$N=\text{Max}(\{N_1,N_2\}).$

Then
$d_{M \times N}((s_{n_{k_j}},t_{n_{k_j}}),(s_0,t_0))=d_M(s_{n_{k_j}},s_0)+d_N(t_{n_{k_j}},t_0)<\epsilon/2 + \epsilon/2 = \epsilon.$

Therefore
$d_{M \times N}((s_{n_{k_j}},t_{n_{k_j}}),(s_0,t_0))< \epsilon.$

Hence $\{(s_{n_{k_j}},t_{n_{k_j}})$ converges to $(s_0,t_0).$
Therefore $S \times T$ is sequentially compact and $S \times T$
is therefore compact. ◻
:::
