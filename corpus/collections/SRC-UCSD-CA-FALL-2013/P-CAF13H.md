---
schema: qual/card@1
id: P-CAF13H
kind: problem
title: "Normal family of holomorphic functions with positive real part and bounded evaluation"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $U \subseteq \mathbb{C}$ be a domain, and let $z_0 \in U$.
For $M > 0$, define $\mathcal{F}_M$ to be the family of functions in $\operatorname{Hol}(U)$ with the properties that $$|f(z_0)| \leq M, \qquad \operatorname{Re} f(z) > 0 \;\forall z \in U.$$ Show that $\mathcal{F}_M$ is a normal family: i.e.\ it is relatively compact in the topology of uniform convergence on compact subsets of $U$.
:::

::: solution
For $f\in\mathcal F_M$, define
\[
h_f(z)=\frac1{f(z)+1}.
\]
Since $\operatorname{Re}f(z)>0$, we have
\[
|f(z)+1|\ge \operatorname{Re}(f(z)+1)>1,
\]
so
\[
|h_f(z)|<1
\]
throughout $U$. Thus the family $\{h_f:f\in\mathcal F_M\}$ is locally uniformly
bounded, and Montel's theorem makes it a normal family.

Take any sequence $f_n\in\mathcal F_M$. Passing to a subsequence, we may assume
\[
h_{f_n}\longrightarrow h
\]
uniformly on compact subsets of $U$, where $h$ is holomorphic. At the base point,
\[
|h_{f_n}(z_0)|
=\frac1{|f_n(z_0)+1|}
\ge\frac1{M+1}.
\]
Hence $h(z_0)\ne0$, so $h$ is not identically zero. Every $h_{f_n}$ is
zero-free; by Hurwitz's theorem, $h$ is therefore zero-free on all of $U$.

Consequently, on every compact subset of $U$,
\[
f_n=\frac1{h_{f_n}}-1
\longrightarrow
\frac1h-1
\]
uniformly. The limit is holomorphic. Thus every sequence in $\mathcal F_M$ has a
subsequence converging uniformly on compact subsets to a holomorphic function,
which is exactly relative compactness in the compact-open topology.
:::
