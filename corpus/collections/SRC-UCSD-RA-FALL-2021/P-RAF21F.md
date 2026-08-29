---
schema: qual/card@1
id: P-RAF21F
kind: problem
title: "When is an atomic measure Radon? Summability over convergent subsequences"
classification:
  areas:
  - real-analysis
  topics:
  - Radon Measures
  - Dirac Measures
  - Borel Measures
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: problem
Let $\delta_x$ denote the Dirac delta mass at $x \in \mathbb{R}^n$.
Let $\{x_j\}_{j=1}^\infty$ be a sequence in $\mathbb{R}^n$, $\{c_j\}_{j=1}^\infty$ a sequence of positive numbers, and $\mu$ the Borel measure on $\mathbb{R}^n$ corresponding to the series $\sum_{j=1}^\infty c_j \delta_{x_j}$.
Prove that $\mu$ is Radon if and only if for all convergent subsequences $\{x_{j_k}\}_{k=1}^\infty$ it holds that $\sum_{k=1}^\infty c_{j_k} < \infty$.
:::

::: solution
**Theorem.**  
Let
$$\mu=\sum_{j\ge1} c_j\delta_{x_j},\qquad c_j>0.$$
Then $\mu$ is Radon iff every convergent subsequence $\{x_{j_k}\}$ satisfies
$$
\sum_{k=1}^\infty c_{j_k}<\infty.
$$

*Proof.* We prove both implications.

**Lemma 1.**  
If $\mu$ is Radon, then every convergent subsequence has finite mass.

*Proof.*  
Let $\{x_{j_k}\}$ be convergent and set
$$
K:=\{x\}\cup\{x_{j_k}:k\ge1\}.
$$
Radon means locally finite, hence compact sets have finite measure.
Therefore $\mu(K)<\infty$ and because the atoms at distinct points are disjoint,
$$
\sum_{k=1}^\infty c_{j_k}\le \mu(K)<\infty.
$$
So the subseries is finite. ∎

**Lemma 2.**  
If every convergent subsequence has finite mass, then every compact set $C\subseteq\mathbb R^n$ has $\mu(C)<\infty$.

*Proof.*  
Assume some compact $C$ has $\mu(C)=\infty$ and fix a point $x\in C$.
By compactness, if every $r>0$ satisfies $\mu(C\cap B(x,r))<\infty$, then a finite cover by such balls would force $\mu(C)<\infty$.
Hence for this $x$, there exists a radius sequence $r_m\downarrow0$ such that
$$
\mu\bigl(C\cap B(x,r_m)\bigr)=\infty.
$$
Choose disjoint finite index blocks
$$
I_m\subseteq\{j:x_j\in C\cap B(x,r_m)\},\qquad
\max I_{m-1}<\min I_m,
$$
with
$$
\sum_{j\in I_m}c_j>1.
$$
The concatenation of indices in $I_1,I_2,\dots$ gives a convergent subsequence
$\{x_{j_k}\}$ with limit $x$, and selected mass
$$
\sum_{k=1}^\infty c_{j_k}=\sum_{m=1}^\infty\sum_{j\in I_m}c_j=\infty,
$$
contradiction. Hence every compact set has finite measure. ∎

**Lemma 3.**  
If every compact set has finite $\mu$-mass, then $\mu$ is Radon.

*Proof.*  
For an atomic Borel measure on $\mathbb R^n$, finite mass on compacts is
equivalent to local finiteness.
Local finiteness is exactly the defining condition for being Radon on $\mathbb R^n$. ∎

Lemma 1 gives the forward implication.
Lemmas 2 and 3 give the reverse implication.
Therefore the theorem holds. ∎
:::
