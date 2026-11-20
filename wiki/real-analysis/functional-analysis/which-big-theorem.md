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

The uniform boundedness principle applies the Baire category theorem to the complete space $X$.
The open mapping theorem applies the Baire category theorem to $Y$ and uses the completeness of $X$ to sum an absolutely convergent series.
The closed graph theorem follows from the bounded inverse theorem applied to the projection from the graph of $T$, a Banach space, onto $X$.
The Hahn--Banach theorem is proved using Zorn's lemma and holds for every normed space $X$.

## Consequences

::: {.corollary}
If $X$ is a Banach space and $T_n\colon X\to Y$ are bounded linear maps such that $Tx\coloneqq\lim_n T_nx$ exists for every $x\in X$, then $T$ is a bounded linear map.

:::

The sequential test for a closed graph, and its use to prove boundedness without an explicit estimate, is on [[real-analysis/appendices/functional-analysis|Appendix: Functional analysis]].

::: {.corollary}
If $X$ is a normed space and $x\neq y$ in $X$, there is $f\in X^*$ with $f(x)\neq f(y)$.
In particular, the weak topology on $X$ is Hausdorff.

:::

## Hilbert spaces

The Hilbert-space forms of these theorems are on [[real-analysis/functional-analysis/banach-and-hilbert|Banach and Hilbert spaces]].
