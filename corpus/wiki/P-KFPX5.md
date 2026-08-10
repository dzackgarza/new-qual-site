---
schema: qual/card@1
id: P-KFPX5
kind: problem
title: "Give the definition of a **covering space** $\\hat{X}$"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---
a.  
Give the definition of a **covering space** $\hat{X}$
(and **covering map** $p : \hat{X} \to X$) for a topological space $X$.

b.  
State the homotopy lifting property of covering spaces. 
Use it to show that a covering map $p : \hat{X} \to X$ induces an injection 
$$
p^\ast : \pi_1 (\hat{X}, \hat{x}) \to \pi_1 (X, p(\hat{x}))
$$ 
on fundamental groups.

c.
Let $p : \hat{X} \to X$ be a covering map with $Y$ and $X$ path-connected. 
Suppose that the induced map $p^\ast$ on $\pi_1$ is an isomorphism. 

Prove that $p$ is a homeomorphism.

:::{.remark}
Not done?
:::
:::{.solution}
\hfill
:::{.concept}
\hfill

:::

a. 
.

b.

Homotopy lifting property:

\begin{center}
\begin{tikzcd}
                                                                   &  & \tilde X \arrow[dd, "\pi"] \\
                                                                   &  &                            \\
Y\cross I \arrow[rr, "H"] \arrow[rruu, "\exists \tilde H", dashed] &  & X                         
\end{tikzcd}
\end{center}

$\pi$ clearly induces a map $p_*$ on $\pi_1$ by functoriality, so we'll show that $\ker p_*$ is trivial.
Let $\gamma: S^1 \to \tilde X \in \pi_1(\tilde X)$ and suppose $\alpha \definedas p_*(\gamma) = [e] \in \pi_1(X)$. 
We'll show $\gamma \homotopic [e]$ in $\pi_1(\tilde X)$.

Since $\alpha = [e]$, $\alpha \homotopic \const$ and thus there is a homotopy $H: I\cross S^1 \to X$ such that $H_0 = \const(x_0)$ and $H_1 = \gamma$.
By the HLP, this lifts to $\tilde H: I\cross S^1 \to \tilde X$.
Noting that $\pi\inv(\const(x_0))$ is still a constant loop, this says that $\gamma$ is homotopic to a constant loop and thus nullhomotopic. 

c.

Since both spaces are path-connected, the degree o the covering map $\pi$ is precisely the index of the included fundamental group.
This forces $\pi$ to be a degree 1 covering and hence a homeomorphism.
:::
