---
schema: qual/card@1
id: D-VUDRJ
kind: definition
title: Relative homotopy groups
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space, $A\subseteq X$ a subspace, $x_0 \in A$, and $n\geq 1$.
Let $D^n$ be the closed unit ball, $S^{n-1} = \del D^n$, and $s_0\in S^{n-1}$ a basepoint.
A \dfn{map of triples} $f\colon (D^n, S^{n-1}, s_0) \to (X, A, x_0)$ is a continuous map $f\colon D^n\to X$ with $f(S^{n-1})\subseteq A$ and $f(s_0) = x_0$.
The \dfn{relative homotopy group} is
$$
\pi_n(X, A, x_0) \coloneqq \ts{ f\colon (D^n, S^{n-1}, s_0) \to (X, A, x_0) } / \homotopic,
$$
the set of [[D-Z7I7F|homotopy]] classes of maps of triples, where the homotopies are through maps of triples.
:::

::: {.proposition}
Let $X$ be a topological space, $A\subseteq X$ a subspace, and $x_0\in A$.

(a) $\pi_n(X, A, x_0)$ is a group for $n\geq 2$ and an abelian group for $n\geq 3$; $\pi_1(X, A, x_0)$ is a pointed set.

(b) The sequence
$$
\cdots \to \pi_n(A, x_0) \to \pi_n(X, x_0) \to \pi_n(X, A, x_0) \xrightarrow{\del} \pi_{n-1}(A, x_0)\to \cdots \to \pi_0(X, x_0),
$$
whose unlabelled maps are induced by the inclusions $(A, x_0)\injects(X, x_0)$ and $(X, x_0, x_0)\injects (X, A, x_0)$ and where $\del$ restricts a map of triples to $S^{n-1}$, is exact.
:::

::: {.concept}
[@Hat02, §4.1, pp. 343--344, Theorem 4.3].
:::
