---
schema: qual/card@1
id: P-JWEN2
kind: problem
title: 'Dini''s theorem: monotone continuous functions decreasing to $0$ on $[0,1]$
  converge uniformly'
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
  - Continuity
relations: []
review: draft
---

::: {.problem}
Suppose $\theset{f_n}_{n\in \NN}$ is a sequence of continuous functions $f_n: [0, 1]\to \RR$ such that 
\[  
f_n(x) \geq f_{n+1}(x) \geq 0 \quad \forall n\in \NN,\, \forall x\in [0, 1]
.\]
Prove that if $\theset{f_n}$ converges pointwise to $0$ on $[0, 1]$ then it converges to $0$ uniformly on $[0, 1]$.
:::

::: {.solution}
Fix $\varepsilon>0$ and define
\[
U_n=\{x\in[0,1]: f_n(x)<\varepsilon\}.
\]
Each $U_n$ is open in $[0,1]$ because $f_n$ is continuous. Since
$f_{n+1}\le f_n$, the sets are increasing:
\[
U_1\subseteq U_2\subseteq\cdots.
\]
Pointwise convergence to $0$ implies that every $x\in[0,1]$ belongs to some
$U_n$, hence
\[
[0,1]=\bigcup_{n=1}^\infty U_n.
\]
Compactness of $[0,1]$ gives a finite subcover. Because the $U_n$ are nested,
there is therefore a single index $N$ such that $U_N=[0,1]$. For all $n\ge N$
and all $x\in[0,1]$,
\[
0\le f_n(x)\le f_N(x)<\varepsilon.
\]
Thus
\[
\sup_{x\in[0,1]}|f_n(x)|<\varepsilon
\qquad(n\ge N),
\]
which is uniform convergence to $0$.
:::
