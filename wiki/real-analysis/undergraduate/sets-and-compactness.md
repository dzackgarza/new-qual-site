---
order: 20
title: Sets and compactness
topics:
- Compactness
- Metric Spaces
- Completeness
- Euclidean Spaces
- Countability
- Closure
---

# Sets and compactness

## Compactness

[[T-YOZX6]]

[[PR-FKJCO]]

[[T-QPTHZ]]

## Series and suprema

[[PR-6C3GQ]]

[[C-WR7YV]]

[[PR-OGEEA]]

[[L-JBMRH]]

## Nowhere dense sets

[[PR-CZS5F]]

[[T-7FJFK]]

[[FT-6WPJI]]

[[PR-JTFMW]]

## Compactness in function spaces

[[PR-HRAOC]]

[[FF-XZGIY]]

::: {.remark}
If $U\subseteq\RR^n$ is open and $(f_k)$ is a pointwise bounded, equicontinuous sequence in $C(U)$, then some subsequence converges uniformly on every compact subset of $U$ to a continuous function.

:::

## Standard facts

- **Bolzano--Weierstrass.** Every bounded sequence in $\RR^n$ has a convergent subsequence.

- **Nested intervals.** If $I_n = [a_n,b_n]$ are nonempty closed bounded intervals with $I_{n+1} \subseteq I_n$, then $\bigcap_n I_n \neq \emptyset$.

- **Completeness via series.** A normed space is complete if and only if every absolutely convergent series in it converges.

- Closed subsets of compact sets are compact, and compact subsets of Hausdorff spaces are closed.

- **Urysohn's lemma.** If $A$ and $B$ are disjoint closed subsets of a metric space or of a compact Hausdorff space $X$, there is a continuous $f\colon X \to [0,1]$ with $f|_A = 0$ and $f|_B = 1$.

- A continuous function with compact support on $\RR^n$ is bounded and uniformly continuous; see [[real-analysis/undergraduate/continuity#Uniform continuity|Continuity]] for the proof of the Heine--Cantor theorem.
