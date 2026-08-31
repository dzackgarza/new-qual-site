---
schema: qual/card@1
id: P-I73ZD
kind: problem
title: The sum metric $d_M+d_N$ on $M\times N$, and compactness of a product of compact
  sets
classification:
  areas:
  - real-analysis
  topics:
  - Metric Spaces
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

Let $(M, d_M)$, $(N, d_N)$ be metric spaces. Define
$d_{M \times N} \colon (M \times N) \times (M \times N) \to \mathbb{R}$
by
$$d_{M \times N}((x_1, y_1), (x_2, y_2)) := d_M(x_1, x_2) + d_N(y_1, y_2).$$

Prove that $(M \times N, d_{M \times N})$ is a metric space.

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
::: {.solution}
**Part 1: $d_{M \times N}$ is a metric.**

<1>1. $d_{M\times N} \ge 0$, and $d_{M\times N}((x_1,y_1),(x_2,y_2)) = 0$ iff $(x_1,y_1) = (x_2,y_2)$.
    ::: {.proof}
    $d_{M\times N} = d_M(x_1,x_2) + d_N(y_1,y_2) \ge 0$ with equality iff both $d_M = 0$ and $d_N = 0$, i.e. $x_1 = x_2$ and $y_1 = y_2$ (metrics separate points).
    :::

<1>2. Symmetry: $d_{M\times N}(p, q) = d_{M\times N}(q, p)$ for all $p, q \in M \times N$.
    ::: {.proof}
    $d_M, d_N$ are symmetric, so the sum is.
    :::

<1>3. Triangle inequality: for $p_i = (x_i, y_i)$, $d_{M\times N}(p_1, p_3) \le d_{M\times N}(p_1, p_2) + d_{M\times N}(p_2, p_3)$.
    ::: {.proof}
    $d_{M\times N}(p_1,p_3) = d_M(x_1,x_3) + d_N(y_1,y_3) \le (d_M(x_1,x_2) + d_M(x_2,x_3)) + (d_N(y_1,y_2) + d_N(y_2,y_3))$ by the triangle inequalities in $M$ and $N$; regroup.
    :::

<1>4. Q.E.D.
    ::: {.proof}
    <1>1–<1>3 are the metric axioms.
    :::

**Part 2: $S \times T$ is compact.**

<1>5. Every sequence $((s_k, t_k)) \subseteq S \times T$ has a convergent subsequence.
    <2>1. $(s_k)$ has a convergent subsequence $s_{k_j} \to s \in S$.
        ::: {.proof}
        $S$ is compact (metric, hence sequentially compact).
        :::
    <2>2. $(t_{k_j})$ has a further convergent subsequence $t_{k_{j_l}} \to t \in T$.
        ::: {.proof}
        $T$ is compact.
        :::
    <2>3. $(s_{k_{j_l}}, t_{k_{j_l}}) \to (s, t) \in S \times T$ in $d_{M\times N}$.
        ::: {.proof}
        $d_{M\times N}((s_{k_{j_l}},t_{k_{j_l}}),(s,t)) = d_M(s_{k_{j_l}}, s) + d_N(t_{k_{j_l}}, t) \to 0$.
        :::

<1>6. Q.E.D.: $S \times T$ is compact.
    ::: {.proof}
    <1>5 is sequential compactness, equivalent to compactness in metric spaces. (Alternatively: $S \times T$ is closed and bounded in the product of complete spaces, or use the open-cover/finite-subcover argument.)
    :::
:::
