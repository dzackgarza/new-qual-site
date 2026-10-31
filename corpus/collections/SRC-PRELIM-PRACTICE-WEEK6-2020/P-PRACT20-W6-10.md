---
schema: qual/card@1
id: P-PRACT20-W6-10
kind: problem
title: Functions not tending to $0$ at infinity despite integrability or vanishing along integer translates
classification:
  areas:
  - prelim
  topics:
  - Improper Integrals
  - Uniform Continuity
relations: []
review: draft
---

::: {.problem}
Find continuous functions $f, g : [0, \infty) \to \RR$ such that

(A) $\int_{0}^{\infty} f(x)\, dx$ converges but $f(x) \not\to 0$ as $x \to \infty$,

(B) $\{g(t + n)\}_{n \in \NN}$ converges to zero as $n \to \infty$ for any fixed $t \geq 0$ but $g(x) \not\to 0$ as $x \to \infty$.

Bonus: show that neither of these is possible if we stipulate that $f, g$ are uniformly continuous.
:::

::: {.solution}
One function serves for both (A) and (B).

For $n\in\NN$, define $f_n\colon[0,\infty)\to\RR$ by

$$
f_n(x)=\begin{cases}2n^2(x-n),&n\leq x<n+\frac{1}{2n^2},\\[2pt]2n^2\left(n+\frac{1}{n^2}-x\right),&n+\frac{1}{2n^2}\leq x<n+\frac{1}{n^2},\\[2pt]0,&\text{otherwise}.\end{cases}
$$

The graph of $f_n$ is a continuous triangular spike of height $1$ on $[n,n+1/n^2)$, and these intervals are disjoint. Let $f=\sum_{n=1}^\infty f_n$ on $[0,\infty)$; on each bounded interval only finitely many terms are nonzero, so $f$ is continuous.

(A) Each spike has integral $\int_0^\infty f_n(x)\,dx=\frac12\cdot\frac{1}{n^2}\cdot1=\frac{1}{2n^2}$, so

$$
\int_0^\infty f(x)\,dx=\sum_{n=1}^\infty\frac{1}{2n^2}<\infty.
$$

(B) Take $g=f$ and fix $t\geq0$. Write $t=m+s$ with $m\in\ZZ_{\geq0}$ and $s\in[0,1)$, so $g(t+n)=f(s+(m+n))$. If $s=0$, then $s+k$ is an integer and $f(s+k)=0$ for every $k$. If $s\in(0,1)$, choose $N$ with $1/N^2<s$; then $s+k\notin[k,k+1/k^2)$ for $k\geq N$, so $f(s+k)=0$. In both cases $g(t+n)\to0$.

In both cases $f(x)\not\to0$ as $x\to\infty$: the sequence $x_n=n+\frac{1}{2n^2}\to\infty$ has $f(x_n)=1$ for all $n$.
:::
