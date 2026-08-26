---
schema: qual/card@1
id: P-A4JGH
kind: problem
title: Negation of uniform convergence and a pointwise but nonuniform example
classification:
  areas:
  - prelim
  topics:
  - Logic and Quantifiers
  - Uniform Convergence
relations: []
review: draft
---

::: problem
A sequence $\{f_n:\mathbb R\to\mathbb R\}_{n=1}^{\infty}$ converges uniformly to $f:\mathbb R\to\mathbb R$ if, for every $\varepsilon>0$, there is a positive integer $N$ such that
\[
n>N\quad\Longrightarrow\quad |f_n(x)-f(x)|<\varepsilon
\]
for all $x\in\mathbb R$.

1. What must one check to show that a sequence does not converge uniformly?

2. Give an example such that $f_n(x)$ converges to $f(x)$ for every $x\in\mathbb R$, but the sequence does not converge uniformly.
:::

::: solution
The negation of uniform convergence is
\[
\exists\varepsilon_0>0\ \forall N\in\mathbb N\ \exists n>N\ \exists x\in\mathbb R:
|f_n(x)-f(x)|\geq\varepsilon_0.
\]

For example, let $f_n(x)=x/n$ and $f(x)=0$.
For each fixed $x$, one has $x/n\to0$.
The convergence is not uniform.
Take $\varepsilon_0=1$.
For every $N$, choose $n=N+1$ and $x=n$.
Then
\[
|f_n(x)-f(x)|=1.
\]
:::
