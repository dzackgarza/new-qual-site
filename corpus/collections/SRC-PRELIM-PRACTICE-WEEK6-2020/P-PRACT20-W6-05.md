---
schema: qual/card@1
id: P-PRACT20-W6-05
kind: problem
title: Uniformly continuous functions on $(0,1)$ have limits at $0$
classification:
  areas:
  - prelim
  topics:
  - Uniform Continuity
  - Cauchy Sequences
relations: []
review: draft
---

::: {.problem}
Suppose that $f : (0, 1) \to \RR$ is uniformly continuous.
Let $\{x_{n}\}$ be a sequence in $(0, 1)$ such that $x_{n} \to 0$. Show that the sequence $\{f(x_{n})\}$ converges.
[Note: generalizing this fact, one can show that if $U \subset \RR^{n}$ is open and bounded, then $f : U \to \RR$ is uniformly continuous iff $f$ can be continuously extended to the closure $\overline{U}$.]
:::

::: {.solution}
Set $y_n=f(x_n)$ and let $\varepsilon>0$. Since $f$ is uniformly continuous, there is $\delta>0$, independent of $x,y$, such that $\abs{x-y}<\delta\implies\abs{f(x)-f(y)}<\varepsilon$ for all $x,y\in(0,1)$. Since $x_n\to0$, the sequence $(x_n)$ is Cauchy, so there is $N\in\NN$ with $\abs{x_n-x_m}<\delta$ whenever $n,m\geq N$. Then

$$
\abs{y_n-y_m}=\abs{f(x_n)-f(x_m)}<\varepsilon
$$

for $n,m\geq N$. So $(y_n)$ is Cauchy and converges to some $f_0\in\RR$.

The limit does not depend on the sequence: if also $x_n'\to0$, the interleaved sequence $x_1,x_1',x_2,x_2',\dots$ tends to $0$, so its image converges, and the two subsequences have the same limit. The same argument at $1$ gives a limit $f_1$ of $f(w_n)$ for every sequence $w_n\to1$ in $(0,1)$. Defining $F(0)=f_0$, $F(1)=f_1$ and $F(x)=f(x)$ for $x\in(0,1)$ gives a continuous extension of $f$ to $[0,1]$, which indicates how to prove the note.
:::
