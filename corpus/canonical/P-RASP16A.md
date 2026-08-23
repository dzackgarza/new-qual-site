---
schema: qual/card@1
id: P-RASP16A
kind: problem
title: "True or false: limsup measures, Lebesgue points, weak+norm convergence, Schwartz convolution, second derivative of |x|"
classification:
  areas:
  - real-analysis
  topics:
  - Borel-Cantelli Lemma
  - Lebesgue Points
  - Weak Convergence
  - Schwartz Space
  - Distributions
relations: []
review: draft
solved: false
---

::: problem
Determine if each of the following statements is true or false.
If true, give a brief proof.
If false, give a counterexample or prove your assertion.

(1) Let $(X, \mathcal{M}, \mu)$ be a measure space and $E_j \in \mathcal{M}$ ($j = 1, 2, \ldots$). Denote by $E = \{x \in X : x \in E_j \text{ for infinitely many } j\}$.
If $E \neq \emptyset$, $\mu(E_j) < \infty$, then $\mu(E) = 0$.

(2) Let $f \in L^1(\mathbb{R}^n)$ and denote the Lebesgue set of $f$ by $L_f$.
Let $z_0 \in \mathbb{R}^n$ and suppose $f$ is continuous at $z_0$.
Then $z_0 \in L_f$.

(3) Let $H$ be a real Hilbert space.
Let $z_k \in H$ ($k = 1, 2, \ldots$) and $z \in H$.
If $z_k \to z$ weakly in $H$ and $\|z_k\| = \|z\|$, then $\|z_k - z\| \to 0$.

(4) Let $\mathcal{S}$ denote the Schwartz space on $\mathbb{R}^n$.
Let $f, g \in \mathcal{S}$.
If $f * g = 0$ in $\mathbb{R}^n$ then either $f = 0$ in $\mathbb{R}^n$ or $g = 0$ in $\mathbb{R}^n$.

(5) Let $f(x) = |x|$ ($x \in \mathbb{R}$) and identify $f$ as a distribution on $\mathbb{R}$.
Then the second-order distributional derivative $f''$ is the zero distribution on $\mathcal{D}(\mathbb{R})$.
:::
