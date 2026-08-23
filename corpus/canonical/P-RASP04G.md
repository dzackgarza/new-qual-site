---
schema: qual/card@1
id: P-RASP04G
kind: problem
title: "Unitary equivalence of multiplication operators and functional calculus"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
solved: false
---

::: problem
Let $f, g : X \to [-1,1]$ be measurable functions and $U : L^2(X, \mu) \to L^2(X, \mu)$ be a unitary map such that $UM_fU^{-1} = M_g$. Let $\mathcal{H}$ denote the collection of bounded Borel measurable functions $\varphi : [-1,1] \to \mathbb{R}$ such that $UM_{\varphi \circ f}U^{-1} = M_{\varphi \circ g}$. Show:

(a) $\varphi \in \mathcal{H}$ if $\varphi(x) = \sum_{n=0}^{N} \alpha_n x^n$ is a polynomial with $\alpha_n \in \mathbb{R}$.

(b) $C([-1,1], \mathbb{R}) \subset \mathcal{H}$.

(c) $\mathcal{H}$ contains all bounded real measurable functions.

Hints: 1. The results of the previous exercise are useful. 2. For (a) show $\varphi(M_f) = M_{\varphi \circ f}$. 3. For (c), notice that $UM_{\varphi \circ f}U^{-1} = M_{\varphi \circ g}$ iff
$$
UM_{\varphi \circ f}U^{-1}h = M_{\varphi \circ g}h \quad \text{for all } h \in L^2(\mu).
$$
4. You do not have to prove (b) if you can prove (c).
:::
