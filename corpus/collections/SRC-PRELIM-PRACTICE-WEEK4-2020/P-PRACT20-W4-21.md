---
schema: qual/card@1
id: P-PRACT20-W4-21
kind: problem
title: Eigenvectors for distinct eigenvalues are linearly independent
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Eigenvalues and Eigenvectors
relations: []
review: draft
---

::: {.problem}
Suppose that A has distinct eigenvalues $\lambda _ { 1 } , \ldots , \lambda _ { k }$ with corresponding eigenvectors $v _ { 1 } , \dots v _ { k }$ . Show that $\{ v _ { 1 } \ldots , v _ { k } \}$ is a linearly independent set.
:::

::: {.solution}
<1>1. The claim holds for one eigenvector.
::: {.proof}
An eigenvector is nonzero by definition, so $\{v_1\}$ is linearly independent.
:::

<1>2. If the claim holds for $k$ distinct eigenvalues, then it holds for $k+1$ distinct eigenvalues.
::: {.proof}
Suppose
$$
\alpha_1v_1+\cdots+\alpha_kv_k+\alpha_{k+1}v_{k+1}=0,
$$
where
$$
Av_j=\lambda_jv_j
$$
and the $\lambda_j$ are pairwise distinct. Apply $A-\lambda_{k+1}I$. The last term vanishes and we obtain
$$
\sum_{j=1}^k
\alpha_j(\lambda_j-\lambda_{k+1})v_j=0.
$$
By the induction hypothesis, $v_1,\dots,v_k$ are linearly independent. Hence
$$
\alpha_j(\lambda_j-\lambda_{k+1})=0
\qquad(1\le j\le k).
$$
Since $\lambda_j\ne\lambda_{k+1}$, this gives
$$
\alpha_1=\cdots=\alpha_k=0.
$$
The original relation then reduces to
$$
\alpha_{k+1}v_{k+1}=0.
$$
Because $v_{k+1}\ne0$, we also have $\alpha_{k+1}=0$. Thus $v_1,\dots,v_{k+1}$ are linearly independent.
:::

<1>3. The eigenvectors $v_1,\dots,v_k$ are linearly independent for every $k\ge1$.
::: {.proof}
This follows from steps <1>1--<1>2 by induction on $k$.
:::

<1>4. Q.E.D.
::: {.proof}
Step <1>3 is exactly the required conclusion.
:::
:::
