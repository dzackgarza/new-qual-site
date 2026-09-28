---
schema: qual/card@1
id: P-BKS04-8A
kind: problem
title: A multilinear map vanishing on equal adjacent arguments is zero when $\dim V<n$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Let $V$ and $W$ be finite-dimensional vector spaces over a field $k$. Let $f\colon V^n\to W$ be a function such that

(a) For each fixed $i\in\{1,\ldots,n\}$ and fixed $v_1,\ldots,v_{i-1},v_{i+1},\ldots,v_n\in V$, the map

$$
\begin{aligned}
&V\to W\\
&x\mapsto f(v_1,\ldots,v_{i-1},x,v_{i+1},\ldots,v_n)
\end{aligned}
$$

is a $k$-linear transformation; and

(b) $f(v_1,\ldots,v_n)=0$ whenever $v_i=v_{i+1}$ for some $i\in\{1,\ldots,n-1\}$.

Prove that either $\dim V\geq n$ or $f$ is identically zero.
:::

::: {.solution}
Fix $i$, and $v_1,\ldots,v_{i-1},v_{i+2},\ldots,v_n\in V$, and define $g(x,y)=f(v_1,\ldots,v_{i-1},x,y,v_{i+2},\ldots,v_n)$. Then

$$
\begin{aligned}
0&=g(x+y,x+y)\\
&=g(x+y,x)+g(x+y,y)\\
&=g(x,x)+g(y,x)+g(x,y)+g(y,y)\\
&=g(y,x)+g(x,y)
\end{aligned}
$$

so interchanging adjacent arguments changes the sign of the value of $f$.

Suppose $v_1,\ldots,v_n\in V$ are such that $v_i=v_j$ for some $i<j$. Then we can interchange arguments repeatedly to move $v_j$ to the $i+1$ position, possibly changing the sign of the value of $f(v_1,\ldots,v_n)$ as we go along.
Since at the end the result is zero, we must have had $f(v_1,\ldots,v_n)=0$ originally.
Thus $f(v_1,\ldots,v_n)=0$ whenever $v_i=v_j$ for some $i\neq j$.

We now solve the problem.
If the conclusion fails, we have $\dim V<n$ and there exist $v_1,\ldots,v_n\in V$ with $f(v_1,\ldots,v_n)\neq0$. Since $\dim V<n$, the vectors $v_1,\ldots,v_n$ must be linearly dependent.
Thus for some $i$, we can write $v_i=\sum_{j\neq i}c_jv_j$ for some constants $c_j\in k$ for $j\neq i$. By linearity of $f$ in the $i$-th argument,

$$
\begin{aligned}
f(v_1,\ldots,v_n)&=\sum_{j\neq i}c_jf(v_1,\ldots,v_{i-1},v_j,v_{i+1},\ldots,v_n)\\
&=\sum_{j\neq i}c_j\cdot0
\end{aligned}
$$

by the previous paragraph, since in each term some $v_j$ appears twice as an argument.
Thus $f(v_1,\ldots,v_n)=0$, a contradiction.
:::
