---
schema: qual/card@1
id: P-OX3MY
kind: problem
title: "Suppose $T: V \\to V$ is not invertible, then $\\dim \\im T < n$ and $\\dim \\ker T > 0$ by the Rank-Nullity\u2026"
classification:
  areas:
  - algebra
  topics:
  - rank-and-nullity
  - linear-algebra
  - matrices
relations: []
review: draft
---

Suppose $T: V \to V$ is not invertible, then $\dim \im T < n$ and $\dim \ker T > 0$ by the Rank-Nullity theorem.
This means that there is a nontrivial $\vector v \in \ker T$, and a nontrivial vector $\vector w \in \im(T)$, so let $S$ be the matrix formed by the outer product $\vector v \vector w^t$.
Since $\vector w \in \im(T)$, fix an $\vector x_0$ with $T\vector x_0 = \vector w$; this is the vector the second computation will use.

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

For the other order, evaluate at the specific vector $\vector x_0$:
\begin{align*}
ST\vector x_0 
&= S \vector w \\
&= \vector v \vector w^t \vector w \\
&= \inner{\vector w}{\vector w} \vector v \\
&= \norm{\vector w}^2 \vector v \\
&\neq \vector 0,
\end{align*}

since $\vector w \neq \vector 0$ and $\vector v \neq \vector 0$.

> The choice $\vector x_0$ with $T\vector x_0 = \vector w$ is what makes this work.
> Membership in $\im(T)$ alone gives nothing: two vectors of $\im(T)$ can perfectly well be orthogonal, so a general $\vector y \in \im(T)$ may have $\inner{\vector w}{\vector y} = 0$.

$\qed$
