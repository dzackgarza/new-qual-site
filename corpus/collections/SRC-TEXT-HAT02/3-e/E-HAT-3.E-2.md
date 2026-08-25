---
schema: qual/card@1
id: E-HAT-3.E-2
kind: exercise
title: "Homotopy classification of lens spaces"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
---

In this problem we will derive one half of the classification of lens spaces up to homotopy equivalence, by showing that if $L_m(\ell_1, \dots, \ell_n) \simeq L_m(\ell_1', \dots, \ell_n')$ then $\ell_1 \cdots \ell_n \equiv \pm \ell_1' \cdots \ell_n' k^n \pmod{m}$ for some integer $k$. The converse is Exercise 29 for §4.2.

(a) Let $L = L_m(\ell_1, \dots, \ell_n)$ and let $\mathbb{Z}_m^*$ be the multiplicative group of invertible elements of $\mathbb{Z}_m$. Define $t \in \mathbb{Z}_m^*$ by the equation $xy^{n-1} = tz$ where $x$ is a generator of $H^1(L; \mathbb{Z}_m)$, $y = \beta(x)$, and $z \in H^{2n-1}(L; \mathbb{Z}_m)$ is the image of a generator of $H^{2n-1}(L; \mathbb{Z})$. Show that the image $\tau(L)$ of $t$ in the quotient group $\mathbb{Z}_m^* / \pm(\mathbb{Z}_m^*)^n$ depends only on the homotopy type of $L$.

(b) Given nonzero integers $k_1, \dots, k_n$, define a map $\tilde{f}: S^{2n-1} \to S^{2n-1}$ sending the unit vector $(r_1 e^{i\theta_1}, \dots, r_n e^{i\theta_n})$ in $\mathbb{C}^n$ to $(r_1 e^{ik_1\theta_1}, \dots, r_n e^{ik_n\theta_n})$. Show:
  (i) $\tilde{f}$ has degree $k_1 \cdots k_n$.
  (ii) $\tilde{f}$ induces a quotient map $f: L \to L'$ for $L' = L_m(\ell_1', \dots, \ell_n')$ provided that $k_j \ell_j \equiv \ell_j' \pmod{m}$ for each $j$.
  (iii) $f$ induces an isomorphism on $\pi_1$, hence on $H^1(-; \mathbb{Z}_m)$.
  (iv) $f$ has degree $k_1 \cdots k_n$, i.e., $f_*$ is multiplication by $k_1 \cdots k_n$ on $H_{2n-1}(-; \mathbb{Z})$.

(c) Using the $f$ in (b), show that $\tau(L) = k_1 \cdots k_n \tau(L')$.

(d) Deduce that if $L_m(\ell_1, \dots, \ell_n) \simeq L_m(\ell_1', \dots, \ell_n')$, then $\ell_1 \cdots \ell_n \equiv \pm \ell_1' \cdots \ell_n' k^n \pmod{m}$ for some integer $k$.

