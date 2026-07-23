---
schema: qual/card@1
id: P-OX3MY
kind: problem
title: "Suppose $T: V \\to V$ is not invertible, then $\\dim \\im T < n$ and $\\di\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
Suppose $T: V \to V$ is not invertible, then $\dim \im T < n$ and $\dim \ker T > 0$ by the Rank-Nullity theorem.
This means that there is a nontrivial $\vector v \in \ker T$, and a nontrivial vector $\vector w \in \im(T)$, so let $S$ be the matrix formed by the outer product $\vector v \vector w^t$.

We then consider how $ST$ acts on vectors $\vector x$:

\begin{align*}
TS\vector x 
&= T\vector v \vector w^t \vector x  \\
&= (T\vector v )\vector w^t \vector x  \\
&= \vector 0 \vector w^t \vector x \\
&= \mathbf{0_n} \vector x \\
&= \vector 0
,\end{align*}

where $\mathbf{0_n}$ is the $n\times n$ matrix of all zeros.

Similarly,
\begin{align*}
ST\vector x 
&\definedas S \vector y \\
&= \vector v \vector w^t \vector y \\
&= \inner{\vector w}{\vector y} \vector v \\
&= c_i \vector v \\
&\neq \vector 0,
\end{align*}

where $\inner{\vector w}{\vector y} \definedas c_i \neq 0$ because $\vector y \in \im(T) = (\im(T)\perp)\perp$, so $\vector y$ and $\vector w$ can not be orthogonal.

$\qed$

