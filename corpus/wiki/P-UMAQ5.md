---
schema: qual/card@1
id: P-UMAQ5
kind: problem
title: A continuous $f\in L^1(\RR)$ need not tend to $0$ at infinity, but a uniformly continuous one must
classification:
  areas:
  - real-analysis
  topics:
  - uniform-continuity
  - l1
  - counterexamples
  - limits
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
1. Give an example of a continuous $f\in L^1(\RR)$ such that $f(x) \not\to 0$ as$\abs x \to \infty$.

2. Show that if $f$ is *uniformly* continuous, then
\[
\lim_{\abs x \to \infty} f(x) = 0.
\]

:::

:::{.solution}
Part 1:
Take a train of triangles with base points at $k$ and $k+1$, each of area $2^{-k}$.
Then $\int \abs{f} \approx \sum_{k\geq 0} 2^{-k} <\infty$, but $f(x)\not\to 0$ since $f(x) > 0$ infinitely often.

Part 2:

- Idea: use contradiction to produce a sequence with arbitrarily large terms, and bound below an integral in a ball about each point.
- Suppose $\lim_{\abs{x}\to \infty}f(x) = L > 0$.
  - Then for any $\eps$ there exists an $M$ such that $x\geq M \implies \abs{f(x) - L} < \eps$, so $L-\eps \leq f(x) \leq L+\eps$
  - Choosing $\eps=L/2$ yields $L/2 \leq f(x) \leq 3L/2$, and so
  \[
  \int_\RR \abs f
  \geq \int_{\abs x \geq M} \abs{f} \geq \int_{\abs x\geq M} L/2 \to \infty
  ,\]
  contradicting $f\in L^1(\RR)$. $\contradiction$.

- So it must be that this limit does not exist.
  Fix $\eps>0$, then there are infinitely many $x$ such that $f(x) > \eps$, so choose a sequence $x_n\to \infty$ with $f(x_n) > \eps$ for each $n$.

- Now use uniform continuity: pick a uniform $\delta = \delta(\eps)$ such that $x\in B_\delta(x_n) \implies \abs{f(x) - f(x_n)} < \eps/4$.

- Now use that $f(x_n) - \eps/4 \leq f(x) \leq f(x_n)+\eps/4$ implies that $f(x) \geq 3\eps/4$ whenever $x\in B_\delta(x_n)$ for any $n$ to estimate
\[
\int_{B_\delta(x_n)} \abs{f(x)}\dx 
\geq  2\delta \cdot 3\eps/4 \da C = C_{\delta, \eps} > 0
,\]
where $C$ is a constant.
- But now we've contradicted $f\in L^1$:
\[
\int_\RR \abs{f} \geq \sum_{n\geq 1} \int_{B_\delta(x_n)} \abs{f} \geq \sum_{n\geq 1} C \to \infty
,\]
provided we pass to a further subsequence of $x_n$ such that the balls $B_\delta(x_n)$ are disjoint.
$\contradiction$



  
:::


