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

No retained solution set covers this exercise: the card's own counterexample is checked step by step — that the two maps are representations, that their determinants agree, and that they are inequivalent.

Let $G=D_{10}=\langle r,s\mid r^{5}=s^{2}=1,\ srs=r^{-1}\rangle$ and $\zeta=e^{2\pi i/5}$; for $j=1,2$ let $\rho_{j}(r)=\mathrm{diag}(\zeta^{j},\zeta^{-j})$ and $\rho_{j}(s)=\begin{pmatrix}0&1\\1&0\end{pmatrix}$.

::: pf

::: {.pf-step #representations}
Each $\rho_{j}$ is a well-defined representation $G\to\GL_{2}(\CC)$.

::: pf-proof
The relations are respected: $\rho_j(r)^{5}=\mathrm{diag}(\zeta^{5j},\zeta^{-5j})=I$, $\rho_j(s)^{2}=I$, and $\rho_j(s)\rho_j(r)\rho_j(s)=\mathrm{diag}(\zeta^{-j},\zeta^{j})=\rho_j(r)^{-1}$ (conjugating a diagonal matrix by the swap matrix interchanges the entries). A map from a group with a presentation that respects the relations factors through the group, so $\rho_{j}$ is a homomorphism.
:::

:::

::: {.pf-step #determinants}
$\det\rho_{1}(g)=\det\rho_{2}(g)$ for every $g\in G$.

::: pf-proof
Every element of $D_{10}$ is $r^{k}$ or $r^{k}s$. On $r^{k}$ both determinants are $\zeta^{jk}\zeta^{-jk}=1$; on $r^{k}s$ the matrix is $\rho_j(r)^{k}\rho_j(s)$, whose determinant is $\det\rho_j(r)^{k}\det\rho_j(s)=1\cdot(-1)=-1$.
:::

:::

::: {.pf-step #inequivalent}
$\rho_{1}$ and $\rho_{2}$ are irreducible and not equivalent.

::: pf-proof
$\rho_{j}$ is two-dimensional, and its restriction to the abelian subgroup $\langle r\rangle$ is diagonal with the two distinct characters $r\mapsto\zeta^{\pm j}$; a $\rho_j$-stable line would be an eigenline of $\rho_j(r)$, so any subrepresentation is one of the two coordinate lines, and $\rho_j(s)$ interchanges them. Hence there is no proper nonzero stable subspace and $\rho_{j}$ is irreducible. If $\rho_{1}\cong\rho_{2}$ then $\operatorname{tr}\rho_{1}(r)=\operatorname{tr}\rho_{2}(r)$, that is $\zeta+\zeta^{-1}=\zeta^{2}+\zeta^{-2}$, which is false since $2\cos(2\pi/5)\ne2\cos(4\pi/5)$.
:::

:::

::: {.pf-qed}
The implication "equivalent $\Rightarrow$ equal determinants" holds because the determinant is invariant under conjugation, but its converse fails: $\rho_{1}\nequiv\rho_{2}$ by step [](#inequivalent){.pf-ref} while their determinants agree by step [](#determinants){.pf-ref}. The assertion is therefore false.
:::

:::

:::
