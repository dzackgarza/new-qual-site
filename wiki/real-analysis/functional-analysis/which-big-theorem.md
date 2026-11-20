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

## Which theorem applies?

| Question | Theorem |
| --- | --- |
| Is a family of operators pointwise bounded on a Banach space? | [[FT-JRRRW|Uniform boundedness]] |
| Is a bounded operator between Banach spaces surjective? | [[T-KQTPR|Open mapping]] |
| Is a linear map between Banach spaces known to have closed graph? | [[T-TTLXS|Closed graph]] |
| Is a bounded functional given on a subspace? | [[T-OW2QG|Hahn--Banach]] |

The bounded inverse theorem is the open mapping theorem for a bijection: [[T-FO27T]].

## Consequences

::: {.corollary}
If $X$ is a Banach space and $T_n\colon X\to Y$ are bounded linear maps such that $Tx\coloneqq\lim_n T_nx$ exists for every $x\in X$, then $T$ is a bounded linear map ([[FT-JRRRW|uniform boundedness]] applied to $\theset{T_n}$, [@Fol99, Theorem 5.13]).

:::

The sequential test for a closed graph, and its use to prove boundedness without an explicit estimate, is on [[real-analysis/appendices/functional-analysis|Appendix: Functional analysis]].

::: {.corollary}
If $X$ is a normed space and $x\neq y$ in $X$, there is $f\in X^*$ with $f(x)\neq f(y)$ ([[T-OW2QG|Hahn--Banach]], part 2 of its corollary, [@Fol99, Theorem 5.8(c)]).
In particular, the weak topology on $X$ is Hausdorff.

:::

## Hilbert spaces

The Hilbert-space forms of these theorems are on [[real-analysis/functional-analysis/banach-and-hilbert|Banach and Hilbert spaces]].
