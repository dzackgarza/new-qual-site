---
schema: qual/card@1
id: P-APAS19G
kind: problem
title: Real irreducible endomorphisms need not be scalar; complexification
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
    Lamport structure. The meaning of "T is an endomorphism of X" is stated (real-linear and commuting with the action), part (a)'s irreducibility is proved by the absence of a real eigenline (with the determinant t^2 + 1 computed) and the non-scalarness by the (1,1) entry, and part (b) is run as a proof by contradiction with Schur's lemma over C, including why the constant is real (compare (1,1) entries). The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. No statement repair; the answers (an example for (a), no for (b)) are correct.
---

::: {.problem}
Let $G$ be a finite group and let $X\colon G\to\mathrm{GL}_d(\RR)$ be an irreducible matrix representation of $G$ over the field of real numbers.
Let $T\colon\RR^d\to\RR^d$ be an endomorphism of $X$.

(a) Give an example to show that $T$ is not necessarily a scalar transformation.

(b) Suppose that $T$ is not a scalar transformation.
Consider the representation $X'\colon G\to\mathrm{GL}_d(\CC)$ given by viewing real matrices as complex matrices:
$$
X'(g):=X(g)\qquad\text{for all }g\in G.
$$
Is it possible for $X'$ to be irreducible (as a complex matrix representation)?
Justify your answer.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

"$T$ is an endomorphism of $X$" is read as: $T$ is $\RR$-linear and $T X(g)=X(g)T$ for every $g\in G$.

::: pf

::: {.pf-step #parta}
For $G=C_4$ and $X(g)=J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ the representation is irreducible over $\RR$ and the endomorphism $T=J$ is not a scalar transformation.

::: pf-proof
$J^2=-I$, so $J^4=I$ and $g\mapsto J^k$ ($g^k\mapsto J^k$) is a representation of $C_4=\langle g:g^4=1\rangle$ on $\RR^2$. A nonzero proper invariant subspace of $\RR^2$ would be a line $\RR v$ with $Jv=\lambda v$ for some real $\lambda$, i.e. a real eigenvalue; but $\det(tI-J)=t^2+1$ has no real root, so no such line exists and the representation is irreducible. The matrix $J$ commutes with $J^k$ for every $k$, so $T=J$ is an endomorphism, and it is not $\lambda I$ for any $\lambda\in\RR$, since $J$ has $0$ in its first diagonal entry while $\lambda I$ has $\lambda$ there.
:::

:::

::: {.pf-step #partb}
If $T$ is a non-scalar endomorphism then $X'$ is not irreducible over $\CC$.

::: pf-proof
Suppose, for contradiction, that $X'$ is irreducible over $\CC$. Regard $T$ as a complex matrix; since $TX(g)=X(g)T$ for all $g$ with real matrices, the same identity holds after viewing entries in $\CC$, so $T$ commutes with $X'(g)$ for all $g$. Schur's lemma over $\CC$ then gives $T=cI$ for some $c\in\CC$. Comparing the $(1,1)$ entries, $c=T_{11}\in\RR$ because $T$ has real entries; so $T=cI$ is a real scalar transformation, contradicting the hypothesis. Hence $X'$ is not irreducible.
:::

:::

::: {.pf-step}
Answers: (a) $G=C_4$ with $X(g)=J$ and $T=J$; (b) no.

::: pf-proof
Step [](#parta){.pf-ref} is the example for (a) and step [](#partb){.pf-ref} is the negative answer to (b).
:::

:::

:::
:::
