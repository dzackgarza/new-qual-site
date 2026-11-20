---
title: Universal covers and the classification of covers
order: 221
topics:
- Covering Spaces
- Covering Transformations
- Universal Cover
- Group Actions
---

# Universal covers and the classification of covers

The basic properties of a covering map, the lifting criteria, deck transformations, and the classification of connected covering spaces by subgroups of the fundamental group.

## Universal covers

[[D-MWD2L]]

[[PR-UBJ6P]]

::: {.remark}
A Galois cover $\tilde X\to X$ with $\Deck(\tilde X) = G$ is equivalently a principal $G\dash$bundle for a discrete $G$:

\begin{tikzcd}
G 
  \ar[r] 
& 
\tilde X
  \ar[d] 
\\
& 
X 
\end{tikzcd}

:::

[[T-SKJB2]]

[[T-EF5IX]]

::: {.remark title="Lifts from simply connected spaces"}
If $Y$ is simply connected, path-connected, and locally path-connected, then $f_*(\pi_1(Y))$ is trivial, so every map $f\colon Y\to X$ lifts to $\tilde X$.

:::

[[PR-R5EN3]]

[[T-F4PQY]]

::: {.theorem title="Classification of covering spaces"}
Let $X$ be path-connected, locally path-connected, and [[D-EPQ54|semilocally simply connected]], with basepoint $x_0$.
Sending a connected covering space $p\colon(\tilde X,\tilde x_0)\to(X,x_0)$ to $p_*\pi_1(\tilde X,\tilde x_0)$ gives bijections
$$
\begin{aligned}
\correspond{\text{connected based covering spaces } (\tilde X,\tilde x_0)\to(X,x_0)}/\text{based isomorphism}
&\mapstofrom
\correspond{\text{subgroups } H\leq\pi_1(X,x_0)}, \\
\correspond{\text{connected covering spaces } \tilde X\to X}/\text{isomorphism over } X
&\mapstofrom
\correspond{\text{subgroups } H\leq\pi_1(X,x_0)}/\text{conjugacy},
\end{aligned}
$$
under which normal covering spaces correspond to normal subgroups $H\normal\pi_1(X,x_0)$ [@Hat02, Theorem 1.38].

:::

[[PR-BHJGY]]

