---
schema: qual/card@1
id: P-RAF20A
kind: problem
title: "True or false: weakly closed sets, nested compacts, vague convergence, Schwartz convolution"
classification:
  areas:
  - real-analysis
  topics:
  - Weak Topology
  - Compactness
  - Vague Convergence
  - Radon Measures
  - Schwartz Space
relations: []
review: draft
---

::: problem
Determine if each of the following statements is true or false.
If true, give a brief proof.
If false, give a counterexample or prove your assertion.

(1) Let $X$ be a Banach space and $A$ a closed subset of $X$.
Then $A$ is sequentially weakly closed, i.e., if $u_n \in A$ ($n = 1, 2, \ldots$) and $u_n \to u$ weakly for some $u \in X$, then $u \in A$.

(2) Let $X$ be a compact Hausdorff topological space.
Let $\{K_j\}$ ($j = 1, 2, \ldots$) be a sequence of decreasing, nonempty compact subsets of $X$.
Then $\bigcap_{j=1}^\infty K_j \neq \emptyset$.

(3) Let $X$ be a locally compact Hausdorff space and $M(X)$ the Banach space of all complex Radon measures on $X$.
Let $\mu \in M(X)$ and $\mu_n \in M(X)$ ($n = 1, 2, \ldots$) and assume that $\mu_n \to \mu$ vaguely in $M(X)$.
Then $\mu_n(E) \to \mu(E)$ for any Borel set $E \subseteq X$.

(4) Let $\mathcal{S}$ denote the Schwartz space on $\mathbb{R}^n$.
Let $f, g \in \mathcal{S}$.
If $f * g = 0$ in $\mathbb{R}^n$ then either $f = 0$ identically in $\mathbb{R}^n$ or $g = 0$ identically in $\mathbb{R}^n$.
:::
