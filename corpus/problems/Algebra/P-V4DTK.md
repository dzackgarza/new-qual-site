---
schema: qual/card@1
id: P-V4DTK
kind: problem
title: What do you know about representations of $\SO(2)$? $\SO(3)$?
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Matrix Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Describe the irreducible representations of the compact Lie groups $\operatorname{SO}(2)$ and $\operatorname{SO}(3)$ over $\mathbb{C}$ and $\mathbb{R}$.
:::

::: solution
**Goal:** Classify the finite-dimensional irreducible representations of $\operatorname{SO}(2)$ and $\operatorname{SO}(3)$.

<1>1. Representations of $\operatorname{SO}(2) \cong S^1 \cong \mathbb{R}/2\pi\mathbb{Z}$:
    *Proof:*
    <2>1. $\operatorname{SO}(2)$ is an abelian compact Lie group consisting of rotation matrices $R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$.
    <2>2. **Complex Irreducible Representations:**
        - By Schur's Lemma, every complex irreducible representation of an abelian group is 1-dimensional: $\rho: \operatorname{SO}(2) \to \mathbb{C}^\times \cong \operatorname{GL}_1(\mathbb{C})$.
        - Group homomorphisms must satisfy $\rho(\theta_1 + \theta_2) = \rho(\theta_1)\rho(\theta_2)$ and periodicity $\rho(\theta + 2\pi) = \rho(\theta)$.
        - These are the characters $\chi_n(R(\theta)) = e^{i n \theta}$ for each integer $n \in \mathbb{Z}$.
        - Thus, the irreducible complex representations are indexed by $\mathbb{Z}$:
            $$\rho_n: R(\theta) \mapsto (e^{in\theta}) \in \operatorname{GL}_1(\mathbb{C}), \quad n \in \mathbb{Z}.$$
    <2>3. **Real Irreducible Representations:**
        - The trivial 1-dimensional representation $\rho_0(R(\theta)) = [1]$.
        - For each $m \ge 1$, the 2-dimensional real representation by standard frequency-$m$ rotations:
            $$\rho_m(R(\theta)) = \begin{pmatrix} \cos(m\theta) & -\sin(m\theta) \\ \sin(m\theta) & \cos(m\theta) \end{pmatrix} \in \operatorname{GL}_2(\mathbb{R}).$$

<1>2. Representations of $\operatorname{SO}(3)$:
    *Proof:*
    <2>1. **Lie Algebra $\mathfrak{so}(3)$ and Universal Cover $\operatorname{SU}(2)$:**
        - $\operatorname{SO}(3) \cong \operatorname{SU}(2) / \{\pm I\}$ has fundamental group $\pi_1(\operatorname{SO}(3)) \cong \mathbb{Z}_2$.
        - The complexified Lie algebra is $\mathfrak{so}(3)_\mathbb{C} \cong \mathfrak{sl}_2(\mathbb{C})$.
        - Irreducible representations of $\mathfrak{sl}_2(\mathbb{C})$ correspond to highest weights $j \in \{0, \frac{1}{2}, 1, \frac{3}{2}, 2, \dots\}$ with dimension $2j + 1$.
    <2>2. **Descent from $\operatorname{SU}(2)$ to $\operatorname{SO}(3)$:**
        - A representation of $\operatorname{SU}(2)$ descends to $\operatorname{SO}(3)$ if and only if the central element $-I \in \operatorname{SU}(2)$ acts trivially ($(-1)^{2j} = 1$).
        - This requires $2j$ to be even, so **$j = \ell \in \mathbb{Z}_{\ge 0}$ must be an integer**.
    <2>3. **Classification of Complex Irreps:**
        - For each integer $\ell = 0, 1, 2, \dots$, there is a unique irreducible complex representation $V_\ell$ of dimension:
            $$\dim(V_\ell) = 2\ell + 1.$$
        - Explicit model: $V_\ell = \mathcal{H}_\ell(\mathbb{R}^3)$ is the space of **spherical harmonics** of degree $\ell$ (homogeneous harmonic polynomials of degree $\ell$ on $\mathbb{R}^3$).
        - The character on a rotation by angle $\theta$ is the Dirichlet kernel:
            $$\chi_\ell(\theta) = \sum_{m=-\ell}^\ell e^{im\theta} = \frac{\sin\left(\left(\ell + \frac{1}{2}\right)\theta\right)}{\sin(\theta/2)}.$$
    <2>4. **Real Irreducible Representations:**
        - Since spherical harmonics are defined over $\mathbb{R}$, each complex irrep $V_\ell$ is the complexification of a real $(2\ell+1)$-dimensional irreducible representation $\mathcal{H}_\ell(\mathbb{R}^3)_{\mathbb{R}}$ (real orthogonal representations).

<1>3. Conclusion:
    $\operatorname{SO}(2)$ has 1D complex irreps $\chi_n(\theta) = e^{in\theta}$ ($n \in \mathbb{Z}$); $\operatorname{SO}(3)$ has unique irreps $V_\ell$ of odd dimensions $2\ell + 1$ ($\ell \in \mathbb{Z}_{\ge 0}$) realized by spherical harmonics. Q.E.D.
:::
