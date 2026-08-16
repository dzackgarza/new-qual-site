---
schema: qual/card@1
id: P-6P6KI
kind: problem
title: Let $G$ be a finite group and $\pi_0$, $\pi_1$ be two irreducible...
classification:
  areas:
  - algebra
  topics:
  - groups
  - representation-theory
relations: []
review: draft
---

::: problem
Let $G$ be a finite group and $\pi_0$, $\pi_1$ be two irreducible representations of $G$. Prove or disprove the following assertion:
$\pi_0$ and $\pi_1$ are equivalent if and only if $\det\pi_0(g)=\det\pi_1(g)$
for all $g\in G$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

The assertion is **FALSE**.

**Counterexample:**
Consider the cyclic group $G = \ZZ_3 = \langle x \mid x^3 = 1 \rangle$.
Let $\omega = e^{2\pi i / 3} \in \CC$.
Since $G$ is abelian, all its irreducible complex representations are 1-dimensional.
Define two 1-dimensional representations $\pi_0, \pi_1: G \to \GL_1(\CC) = \CC^\times$ by:
- $\pi_0(x) = \omega$,
- $\pi_1(x) = \omega^2$.

1. **Determinants:**
   Since each $\pi_j$ is 1-dimensional, the determinant of a $1 \times 1$ matrix is the scalar itself: $\det \pi_j(g) = \pi_j(g)$.
   For $g = x$:
   $$
   \det \pi_0(x) = \omega \neq \omega^2 = \det \pi_1(x).
   $$
   (This shows that 1-dimensional representations with different determinants are not equivalent.)

2. **Higher-dimensional Counterexample (matching determinants but inequivalent):**
   To disprove the $\Longleftarrow$ direction (i.e. having identical determinants implies equivalence):
   Consider the quaternion group $G = Q_8 = \{\pm 1, \pm i, \pm j, \pm k\}$.
   $Q_8$ has four 1-dimensional irreducible representations and one 2-dimensional irreducible representation $\rho: Q_8 \to \GL_2(\CC)$.
   
   Alternatively, consider the dihedral group $D_8 = \langle r, s \mid r^4 = 1, s^2 = 1, srs = r^{-1} \rangle$.
   $D_8$ has four 1-dimensional irreducible representations $\chi_1, \chi_2, \chi_3, \chi_4$:
   - $\chi_1(r) = 1, \chi_1(s) = 1$ (trivial)
   - $\chi_2(r) = 1, \chi_2(s) = -1$
   - $\chi_3(r) = -1, \chi_3(s) = 1$
   - $\chi_4(r) = -1, \chi_4(s) = -1$

   Now consider $\pi_0 = \chi_2$ and $\pi_1 = \chi_3$.
   Since they are 1-dimensional:
   - $\det \pi_0(r) = \chi_2(r) = 1$ while $\det \pi_1(r) = \chi_3(r) = -1$.
   
   To get identical determinants:
   Consider $G = S_3$. The irreducible representations are:
   - Trivial representation $\chi_{\text{triv}}$ (dimension 1)
   - Sign representation $\chi_{\text{sgn}}$ (dimension 1)
   - Standard 2-dimensional representation $\rho$ (dimension 2)
   
   Let $\pi_0 = \rho$. For $\pi_1$, consider $\rho \otimes \chi_{\text{sgn}}$.
   On $S_3$, $\rho \cong \rho \otimes \chi_{\text{sgn}}$, so these are equivalent.
   
   For an explicit non-isomorphic pair with equal determinants:
   Let $G = A_4$ (the alternating group on 4 elements).
   $A_4$ has three 1-dimensional representations $\chi_0, \chi_1, \chi_2$ (corresponding to $A_4 / V_4 \cong \ZZ_3$) and one 3-dimensional irreducible representation $\rho$.
   Now consider $G = \SL_2(\FF_3)$ or $G = \ZZ_5 \rtimes \ZZ_4$.
   For $G = D_{10} = \langle r, s \mid r^5 = 1, s^2 = 1, srs = r^{-1} \rangle$:
   $D_{10}$ has two distinct 2-dimensional irreducible representations $\rho_1, \rho_2$:
   - $\rho_1(r) = \begin{pmatrix} \zeta & 0 \\ 0 & \zeta^{-1} \end{pmatrix}, \quad \rho_1(s) = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, where $\zeta = e^{2\pi i / 5}$.
   - $\rho_2(r) = \begin{pmatrix} \zeta^2 & 0 \\ 0 & \zeta^{-2} \end{pmatrix}, \quad \rho_2(s) = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.

   Compute determinants for all elements:
   - For any power $r^k$: $\det \rho_1(r^k) = \zeta^k \cdot \zeta^{-k} = 1$, and $\det \rho_2(r^k) = \zeta^{2k} \cdot \zeta^{-2k} = 1$.
   - For any reflection $s r^k$: $\det \rho_1(s r^k) = \det \rho_1(s) \det \rho_1(r^k) = (-1)(1) = -1$, and $\det \rho_2(s r^k) = \det \rho_2(s) \det \rho_2(r^k) = (-1)(1) = -1$.

   Thus:
   $$
   \det \rho_1(g) = \det \rho_2(g) \quad \text{for all } g \in D_{10}.
   $$
   However, their characters are:
   - $\chi_{\rho_1}(r) = \zeta + \zeta^{-1} = 2\cos(2\pi/5)$,
   - $\chi_{\rho_2}(r) = \zeta^2 + \zeta^{-2} = 2\cos(4\pi/5) \neq 2\cos(2\pi/5)$.

   Since characters determine representations over $\CC$, $\rho_1$ and $\rho_2$ are **inequivalent** irreducible representations of $D_{10}$, despite having identical determinants for every group element.
:::
