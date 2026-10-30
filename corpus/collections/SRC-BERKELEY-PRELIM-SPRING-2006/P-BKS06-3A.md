---
schema: qual/card@1
id: P-BKS06-3A
kind: problem
title: Matrix of the orthogonal projection onto the hyperplane $x_1+\cdots+x_n=0$
classification:
  areas: [prelim]
  topics:
  - Linear Algebra
relations: []
review: draft
---

::: {.problem}
Let $S = \{ (x_{1}, \ldots, x_{n}) \in \RR^{n} \st x_{1} + \cdots + x_{n} = 0 \}$. Find (with justification) the $n \times n$ matrix $P$ of the orthogonal projection from $\RR^{n}$ onto $S$. That is, $P$ has image $S$, and $P^{2} = P = P^{T}$.
:::

::: {.solution}

The answer is $P=I-\frac1nJ$, where $J$ is the $n\times n$ matrix of ones: the diagonal entries of $P$ are $\frac{n-1}{n}$ and the other entries are $-\frac1n$.

::: pf

::: {.pf-step #s1}

Let $w=\frac1{\sqrt n}(1,\ldots,1)^T$. Then $S=w^{\perp}$ and $\norm{w}=1$.

::: pf-proof

$\langle v,w\rangle=\frac1{\sqrt n}(v_1+\cdots+v_n)$, which vanishes exactly when $v\in S$. Also $\langle w,w\rangle=n\cdot\frac1n=1$.

:::

:::

::: {.pf-step #s2}

The matrix $P=I-ww^T=I-\frac1nJ$ satisfies $P^2=P=P^T$ and has image $S$.

::: pf-proof

$P^T=P$ because $(ww^T)^T=ww^T$. Since $w^Tw=1$,
$$
P^2=I-2ww^T+w(w^Tw)w^T=I-ww^T=P.
$$
For every $v$, $\langle Pv,w\rangle=\langle v,w\rangle-\langle v,w\rangle\langle w,w\rangle=0$, so the image lies in $S$. For $v\in S$, $Pv=v-w\langle w,v\rangle=v$, so every vector of $S$ is in the image.

:::

:::

::: pf-qed

By step [](#s2){.pf-ref}, $P=I-\frac1nJ$ is the orthogonal projection onto $S$. It is unique, because a symmetric idempotent matrix is determined by its image.

:::

:::

:::
