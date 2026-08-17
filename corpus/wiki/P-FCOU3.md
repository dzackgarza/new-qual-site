---
schema: qual/card@1
id: P-FCOU3
kind: problem
title: "\\label{hilbert_space_exam_question}"
classification:
  areas:
  - real-analysis
  topics:
  - hilbert-spaces
  - l2
relations: []
review: draft
solved: true
---
\label{hilbert_space_exam_question}

Let $\theset{u_n}_{n=1}^\infty$ be an orthonormal sequence in a Hilbert space $H$.

a. Let $x\in H$ and verify that 
\[
\left\|x-\sum_{n=1}^{N}\left\langle x, u_{n}\right\rangle u_{n}\right\|_H^{2} =
\|x\|_H^{2}-\sum_{n=1}^{N}\left|\left\langle x, u_{n}\right\rangle\right|^{2}
.\]
for any $N\in \NN$ and deduce that
\[
\sum_{n=1}^{\infty}\left|\left\langle x, u_{n}\right\rangle\right|^{2} \leq\|x\|_H^{2}
.\]

b. Let $\theset{a_n}_{n\in \NN} \in \ell^2(\NN)$ and prove that there exists an $x\in H$ such that $a_n = \inner{x}{u_n}$ for all $n\in \NN$, and moreover $x$ may be chosen such that 
\[
\norm{x}_H = \qty{ \sum_{n\in \NN} \abs{a_n}^2}^{1\over 2}
.\]

c. Prove that if $\theset{u_n}$ is *complete*, Bessel's inequality becomes an equality.

:::{.solution title="part b"}
\envlist

- Take $\theset{a_n} \in \ell^2$, then note that $\sum \abs{a_n}^2 < \infty \implies$ the tails vanish.

- Define $x \definedas \displaystyle\lim_{N\to\infty} S_N$ where $S_N = \sum_{k=1}^N a_k u_k$

- $\theset{S_N}$ is Cauchy and $H$ is complete, so $x\in H$.

- By construction, 
\[
\inner{x}{u_n} = \inner{\sum_k a_k u_k}{u_n} = \sum_k a_k \inner{u_k}{u_n} = a_n 
\]
since the $u_k$ are all orthogonal.

- By Pythagoras since the $u_k$ are normal,
\[
\norm{x}^2 = \norm{\sum_k a_k u_k}^2 = \sum_k \norm{a_k u_k}^2 = \sum_k \abs{a_k}^2
.\]

:::

:::{.solution title="part c"}
Let $x$ and $u_n$ be arbitrary. 

\[
\inner{x - \sum_{k=1}^\infty \inner{x}{u_k}u_k }{u_n}
&=
\inner{x}{u_n}
-
\inner{\sum_{k=1}^\infty \inner{x}{u_k}u_k }{u_n} \\
&=
\inner{x}{u_n}
-
\sum_{k=1}^\infty  \inner{\inner{x}{u_k}u_k }{u_n} \\
&=
\inner{x}{u_n}
-
\sum_{k=1}^\infty  \inner{x}{u_k} \inner{u_k }{u_n} \\
&= \inner{x}{u_n} - \inner{x}{u_n} = 0 \\
\implies 
x - \sum_{k=1}^\infty \inner{x}{u_k}u_k &= 0 \quad\text{by completeness}
.\]

So 
\[
x = \sum_{k=1}^\infty \inner{x}{u_k} u_k
\implies
\norm{x}^2 = \sum_{k=1}^\infty \abs{\inner{x}{u_k}}^2. \qed
.\]


:::
