---
schema: qual/card@1
id: E-SS8.PR-3
kind: exercise
title: Hyperbolic metric on the disc and the Schwarz-Pick lemma
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
relations: []
review: draft
solved: false
---

::: exercise
3.* The Schwarz-Pick lemma (see Exercise 13) is the infinitesimal version of an important observation in complex analysis and geometry.

For complex numbers $w \in \mathbb{C}$ and $z \in \mathbb{D}$ we define the hyperbolic length of $w$ at $z$ by

$$

\| w \| _ {z} = \frac{| w |}{1 - | z | ^ {2}},

$$

where $|w|$ and $|z|$ denote the usual absolute values. This length is sometimes referred to as the Poincaré metric, and as a Riemann metric it is written as

$$

d s ^ {2} = \frac{| d z | ^ {2}}{(1 - | z | ^ {2}) ^ {2}}.

$$

The idea is to think of $w$ as a vector lying in the tangent space at $z$. Observe that for a fixed $w$, its hyperbolic length grows to infinity as $z$ approaches the boundary of the disc. We pass from the infinitesimal hyperbolic length of tangent vectors to the global hyperbolic distance between two points by integration.

(a) Given two complex numbers $z_1$ and $z_2$ in the disc, we define the hyperbolic distance between them by

$$

d (z_1, z_2) = \inf_ {\gamma} \int_ {0} ^ {1} \| \gamma' (t) \| _ {\gamma (t)} d t,

$$

where the infimum is taken over all smooth curves $\gamma : [0, 1] \to \mathbb{D}$ joining $z_1$ and $z_2$. Use the Schwarz-Pick lemma to prove that if $f : \mathbb{D} \to \mathbb{D}$ is holomorphic, then

$$

d (f (z_1), f (z_2)) \leq d (z_1, z_2) \quad \text{for any } z_1, z_2 \in \mathbb{D}.

$$

In other words, holomorphic functions are distance-decreasing in the hyperbolic metric.

(b) Prove that automorphisms of the unit disc preserve the hyperbolic distance, namely

$$

d (\varphi (z_1), \varphi (z_2)) = d (z_1, z_2), \quad \text{for any } z_1, z_2 \in \mathbb{D}

$$

and any automorphism $\varphi$. Conversely, if $\varphi : \mathbb{D} \to \mathbb{D}$ preserves the hyperbolic distance, then either $\varphi$ or $\overline{\varphi}$ is an automorphism of $\mathbb{D}$.

(c) Given two points $z_1, z_2 \in \mathbb{D}$, show that there exists an automorphism $\varphi$ such that $\varphi(z_1) = 0$ and $\varphi(z_2) = s$ for some $s$ on the segment $[0, 1)$ on the real line.

(d) Prove that the hyperbolic distance between $0$ and $s \in [0, 1)$ is

$$

d (0, s) = \frac{1}{2} \log \frac{1 + s}{1 - s}.

$$

(e) Find a formula for the hyperbolic distance between any two points in the unit disc.
:::
