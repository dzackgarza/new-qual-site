---
title: Which big theorem?
order: 0
topics:
- Functional Analysis
- Banach Spaces
---

# Which big theorem?

Let $X$ and $Y$ be normed spaces.
The statements are on [[real-analysis/appendices/functional-analysis|Appendix: Functional analysis]].

| Hypothesis | Theorem | Conclusion |
| --- | --- | --- |
| $X$ Banach; $T_\alpha\colon X\to Y$ bounded linear with $\sup_\alpha\norm{T_\alpha x}<\infty$ for each $x$ | uniform boundedness | $\sup_\alpha\norm{T_\alpha}<\infty$ |
| $X, Y$ Banach; $T\colon X\to Y$ bounded linear and surjective | open mapping | $T$ is open; if $T$ is also injective, $T^{-1}$ is bounded |
| $X, Y$ Banach; $T\colon X\to Y$ linear with closed graph | closed graph | $T$ is bounded |
| $M\subseteq X$ a subspace; $f$ a bounded linear functional on $M$ | Hahn--Banach | an extension $F\in X^*$ of $f$ with $\norm F = \norm f$ |

The first three theorems are proved from the Baire category theorem and require completeness.
The Hahn--Banach theorem is proved using Zorn's lemma and holds for every normed space $X$.

## Consequences

::: {.corollary}
If $X$ is a Banach space and $T_n\colon X\to Y$ are bounded linear maps such that $Tx\coloneqq\lim_n T_nx$ exists for every $x\in X$, then $T$ is a bounded linear map.

:::

::: {.proof}
$T$ is linear as a pointwise limit of linear maps.
Each sequence $(T_nx)_n$ converges, hence is bounded, so the uniform boundedness principle gives $C\coloneqq\sup_n\norm{T_n}<\infty$, and $\norm{Tx} = \lim_n\norm{T_nx}\leq C\norm x$.

:::

::: {.remark}
To show that the graph of a linear map $T\colon X\to Y$ is closed, it suffices to show that $x_n\to x$ and $Tx_n\to y$ imply $y = Tx$; the convergence of $(Tx_n)$ is a hypothesis rather than something to prove.

:::

::: {.corollary}
If $X$ is a normed space and $x\neq y$ in $X$, there is $f\in X^*$ with $f(x)\neq f(y)$.
In particular, the weak topology on $X$ is Hausdorff.

:::

::: {.proof}
By the Hahn--Banach theorem there is $f\in X^*$ with $\norm f = 1$ and $f(x-y) = \norm{x-y}\neq0$.

:::

## Hilbert spaces

In a Hilbert space $H$, every closed subspace $M$ has an orthogonal projection $P\colon H\to M$ with $H = M\oplus M^\perp$, the Riesz representation theorem identifies $H^*$ with $H$, and for an orthonormal basis $\theset{e_n}$ Parseval's identity gives $\norm x^2 = \sum_n\abs{\inner x{e_n}}^2$.
In particular, a bounded linear functional on a closed subspace $M$ extends to $H$ with the same norm by composing it with $P$, without the Hahn--Banach theorem.
See [[real-analysis/functional-analysis/banach-and-hilbert|Banach and Hilbert spaces]].
