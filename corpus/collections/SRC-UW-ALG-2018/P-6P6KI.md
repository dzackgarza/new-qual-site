---
schema: qual/card@1
id: P-6P6KI
kind: problem
title: Equivalence of irreducible representations versus equality of determinants
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $G$ be a finite group and $\pi$, $\pi'$ be two irreducible representations of $G$.
Prove or disprove the following assertion: $\pi$ and $\pi'$ are equivalent if and only if $\det\pi(g)=\det\pi'(g)$ for all $g\in G$.
:::

::: {.solution}
The assertion is false.
The direction "equivalent implies equal determinants" holds, since equivalent representations are conjugate and the determinant is conjugation invariant; the converse fails.

**Counterexample.** Let $G = D_{10} = \langle r, s \mid r^5 = 1,\ s^2 = 1,\ srs = r^{-1} \rangle$ and $\zeta = e^{2\pi i / 5}$.
For $j = 1, 2$ define $\rho_j : G \to \GL_2(\CC)$ by
$$
\rho_j(r) = \begin{pmatrix} \zeta^j & 0 \\ 0 & \zeta^{-j} \end{pmatrix}, \qquad \rho_j(s) = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.
$$
These matrices satisfy $\rho_j(r)^5 = I$, $\rho_j(s)^2 = I$ and $\rho_j(s)\rho_j(r)\rho_j(s) = \rho_j(r)^{-1}$, so each $\rho_j$ is a representation.

1. **Each $\rho_j$ is irreducible.**
A $1$-dimensional invariant subspace would be a common eigenvector of $\rho_j(r)$ and $\rho_j(s)$.
Since $\zeta^j \ne \zeta^{-j}$, the eigenvectors of $\rho_j(r)$ are the multiples of $e_1$ and of $e_2$, and $\rho_j(s)$ swaps $e_1$ and $e_2$, so neither is an eigenvector of $\rho_j(s)$.

2. **The determinants agree.**
For every $k$, $\det \rho_j(r^k) = \zeta^{jk}\zeta^{-jk} = 1$ and $\det \rho_j(s r^k) = \det\rho_j(s)\det\rho_j(r^k) = -1$, for both $j=1$ and $j=2$.
Every element of $G$ is $r^k$ or $sr^k$, so $\det \rho_1(g) = \det \rho_2(g)$ for all $g \in G$.

3. **The representations are inequivalent.**
$\chi_{\rho_1}(r) = \zeta + \zeta^{-1} = 2\cos(2\pi/5)$ and $\chi_{\rho_2}(r) = \zeta^2 + \zeta^{-2} = 2\cos(4\pi/5)$.
These differ, because $\cos(2\pi/5) > 0 > \cos(4\pi/5)$.
Equivalent representations have equal characters, so $\rho_1 \not\cong \rho_2$.
:::
