---
schema: qual/card@1
id: P-APA17F
kind: problem
title: 'Examples: real irreducible with non-scalar endomorphism; infinite indecomposable not irreducible'
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the two examples already on the card, both of which are
    correct. Added: the explicit characteristic polynomial argument in (a) with the note that
    J's eigenvalues are +-i, and the check J != lambda I; and in (b) the case split that the
    card compressed — if the two eigenlines are distinct U would be diagonalizable, and if they
    coincide the sum is not direct — together with the explicit eigenspace computation ker(U -
    I) = C e_1. No statement was changed. Not claimed: a retained solution set; the collection's
    provenance is the examination paper only.
---

::: {.problem}
Give examples of each of the following objects.

(a) A finite group $G$, an irreducible $G$-module $V$ defined over the real numbers $\RR$, and a $G$-module homomorphism $\varphi \colon V \to V$ which is not multiplication by a scalar.

(b) An infinite group $G$ and a $G$-module $V$ defined over the complex numbers $\CC$ which is indecomposable but not irreducible.
:::

::: {.solution}
Throughout $G$ is a group, a $G$-module over a field $k$ is a $k$-vector space with a linear action of $G$, irreducible means having no nonzero proper $G$-stable subspace, and indecomposable means not being the direct sum of two nonzero $G$-stable subspaces. The collection's `provenance` is the Spring 2017 preliminary examination, and no solutions sheet accompanies it, so the examples below are the card's own.

::: pf

::: {.pf-step #a-irreducible}
(a) For $G = C_{4} = \generators{g \mid g^{4} = 1}$ and $V = \RR^{2}$ with $g$ acting as $J = \begin{pmatrix}0 & -1 \\ 1 & 0\end{pmatrix}$, the module $V$ is irreducible.

::: pf-proof
A nonzero proper subspace of $\RR^{2}$ is a line $\RR v$ with $v \ne 0$. If such a line were $G$-stable it would be stable under $J$, so $Jv = \lambda v$ for some $\lambda \in \RR$ and $v$ would be a real eigenvector of $J$. But the characteristic polynomial of $J$ is $t^{2}+1$, whose roots are $\pm i \notin \RR$, so no real eigenvector exists and no nonzero proper stable subspace exists.

:::

:::

::: {.pf-step #a-endomorphism}
(a) $\varphi \coloneqq J$ is a $G$-module homomorphism $V \to V$ that is not multiplication by a scalar.

::: pf-proof
The action of $G$ is determined by the single matrix $J$, and $J$ commutes with itself, so $\varphi(gu) = J(Ju) = J^{2}u = g(\varphi u)$ for every $u$ and the generator $g$, hence for every element of $G$ — that is the homomorphism condition. If $\varphi = \lambda I$ with $\lambda \in \RR$ then $J = \lambda I$, which is false: $J$ has zero diagonal entries and nonzero off-diagonal ones. So $\varphi$ is an endomorphism of an irreducible real module that is not a scalar, which is exactly what fails in Schur's lemma over a non-algebraically-closed field.

:::

:::

::: {.pf-step #b-reducible}
(b) For $G = \ZZ = \generators{t}$ and $V = \CC^{2}$ with $t$ acting as $U = \begin{pmatrix}1 & 1 \\ 0 & 1\end{pmatrix}$, the line $L = \CC e_{1}$ is $G$-stable, so $V$ is not irreducible.

::: pf-proof
$Ue_{1} = e_{1}$, so $L$ is stable under the generator and hence under every power of it. $L$ is nonzero and proper, so $V$ is reducible.

:::

:::

::: {.pf-step #b-indecomposable}
(b) $V$ is not the direct sum of two nonzero $G$-stable subspaces.

::: pf-proof
A $G$-stable subspace of $\CC^{2}$ is $U$-stable. Any $U$-stable subspace of dimension $1$ is spanned by an eigenvector, and any $U$-stable subspace of dimension $2$ is $V$ itself. Suppose $V = V_{1} \oplus V_{2}$ with both $V_{i}$ nonzero and stable; then each $V_{i}$ is one-dimensional, so each is spanned by an eigenvector of $U$. If the two eigenlines were distinct they would form a basis of eigenvectors, making $U$ diagonalizable; if they coincided then $V_{1} = V_{2}$, contradicting the directness of the sum. So it suffices to know that $U$ is not diagonalizable: its characteristic polynomial is $(t-1)^{2}$ and the eigenspace for $1$ is $\ker(U - I) = \CC e_{1}$, of dimension $1$, so there is no basis of eigenvectors.

:::

:::

::: pf-step
Both objects exist: (a) $C_{4}$ acting on $\RR^{2}$ by $J$, with the endomorphism $\varphi = J$ that is not scalar; (b) $\ZZ$ acting on $\CC^{2}$ by $U$, indecomposable but not irreducible.

::: pf-proof
Steps [](#a-irreducible){.pf-ref} and [](#a-endomorphism){.pf-ref} supply (a) and steps [](#b-reducible){.pf-ref} and [](#b-indecomposable){.pf-ref} supply (b), so both requested examples are given with the properties verified rather than asserted.

:::

:::

:::
:::
