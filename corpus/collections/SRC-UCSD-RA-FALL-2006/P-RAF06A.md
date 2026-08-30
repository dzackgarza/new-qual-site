---
schema: qual/card@1
id: P-RAF06A
kind: problem
title: "True or false: five statements in measure theory and functional analysis"
classification:
  areas:
  - real-analysis
  topics:
  - Borel Measures
  - Stone-Weierstrass
  - Radon-Nikodym
  - Uniform Boundedness Principle
  - Banach-Alaoglu Theorem
relations: []
review: draft
---

::: problem
Determine if the statements below are True or False.
If True, give a brief proof.
If False, give a counterexample.

(a) Let $\mu$ be a Borel measure on $\mathbb{R}$ such that $\mu(B) < \infty$ for every bounded Borel set $B$.
Let $E$ be a Borel set and assume that $\mu(K) = 0$ for every compact set $K \subset E$.
Then $\mu(E) = 0$.

(b) Let $f : [-1, 1] \to \mathbb{R}$ be continuous with $f(0) = 0$.
For every $\varepsilon > 0$, there exists an integer $n \geq 1$ and continuous functions $u_j : [-1, 1] \to \mathbb{R}$, $j = 1, \ldots, n$, such that $u_j(x) = 0$ only at $x = 0$ and $\sup_{x \in [-1,1]} \left|f(x) - \sum_{j=1}^n u_j(x)\right| < \varepsilon$.

(c) Let $\nu$ be a complex measure and $\mu$ a (positive) measure on $(X, \mathcal{M})$.
Suppose that $X = A \cup B$ with $A \cap B = \emptyset$ and $\nu(A) = 0$.
Moreover, assume that there is a measurable function $f : B \to \mathbb{C}$ such that $\nu(E) = \int_E f \, d\mu$ for every measurable $E \subset B$.
Then there is a measurable function $g : X \to \mathbb{C}$ such that $\nu = g \, d\mu$.

(d) Let $\{f_n\}$ be a sequence in $L^4(X, \mu)$.
Suppose that $\lim_{n \to \infty} \int_X f_n g \, d\mu$ exists (as a complex number) for every $g \in L^{4/3}(X, \mu)$.
Then there is $M > 0$ such that $\|f_n\|_4 \leq M$ for every $n$.

(e) Let $\{f_n\}$ be a sequence in $L^4(X, \mu)$.
Suppose that there is $M > 0$ such that $\|f_n\|_4 \leq M$ for every $n$.
Then there is a subsequence $\{f_{n_k}\}$ such that $\lim_{k \to \infty} \int_X f_{n_k} g \, d\mu$ exists (as a complex number) for every $g \in L^{4/3}(X, \mu)$.
:::
