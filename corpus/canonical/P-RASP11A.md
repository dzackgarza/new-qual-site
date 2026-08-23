---
schema: qual/card@1
id: P-RASP11A
kind: problem
title: "True or false: operator limits, L1 convergence, product compactness, weak L2 subsequences, differentiation of measures"
classification:
  areas:
  - real-analysis
  topics:
  - Bounded Operators
  - L1 Spaces
  - Product Topology
  - Weak Convergence
  - Differentiation of Measures
relations: []
review: draft
solved: false
---

::: problem
Answer True or False. Support your claim with a short explanation or counterexample.

(a) If $T_n \in L(X, Y)$ is a sequence of bounded linear operators with $X, Y$ Banach spaces, then if $Tx := \lim_n T_n x$ exists in the $Y$ norm for all $x \in X$, one has $T \in L(X, Y)$.

(b) Let $(X, \mathcal{M}, \mu)$ be any measure space. If $f_n, f \in L^1(d\mu)$ are measurable functions such that $f_n \to f$ $\mu$-a.e. and $\lim_n \int f_n = \int f$, then $f_n \to f$ in $L^1(d\mu)$.

(c) If $\{X_\alpha\}_{\alpha \in A}$ is any collection of compact Hausdorff topological spaces, then $E \subset \prod_{\alpha \in A} X_\alpha$ with the product topology is compact iff it is closed.

(d) If $f_n \in L^2([0, 1])$ converge weakly to $f \in L^2([0, 1])$, then there is a subsequence such that $f_{n_k} \to f$ pointwise a.e. with respect to Lebesgue measure.

(e) If $\mu$ is a positive finite Borel measure on $\mathbb{R}^n$ which is absolutely continuous with respect to Lebesgue measure, and
$$
\lim_{r \to 0} \frac{\mu(B_r(x))}{|B_r(x)|} = 0 \quad \text{for a.e. } x \in \mathbb{R}^n,
$$
then $\mu \equiv 0$. Here $B_r(x)$ is the ball of radius $r$ at $x$.
:::