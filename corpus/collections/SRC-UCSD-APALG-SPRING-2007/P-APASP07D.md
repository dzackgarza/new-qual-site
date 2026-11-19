---
schema: qual/card@1
id: P-APASP07D
kind: problem
title: "Trace and computation of the averaged conjugate of a matrix over a finite group"
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-18
  note: >-
    The collection's provenance is the examination paper alone,
    assets/attachments/SP07_202_Applied_Algebra_Qual.pdf, so no retained solution set covers the
    problem and the argument is the card's own. The statement is the printed one and both parts were
    re-checked: trace of the displayed B is 6, and the answer C = 2I is forced by Schur's lemma plus
    the trace.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the prose solution into a Lamport proof with the four ingredients as separate steps:
    invariance of C under conjugation by each A_h (with the reindexing by g -> hg written), Schur's
    lemma applied to an endomorphism of the irreducible module, the trace identity, and the two
    answers. The prose derived part (b) from part (a) in one line; the card records why the scalar
    exists before using the trace, so part (b) does not depend on the particular group or action.
    Nothing in the original argument was wrong and both answers 6 and 2I_3 are unchanged.
---

::: {.problem}
Let
$$
B = \begin{bmatrix}
2 & 3 & 1 \\
1 & 1 & 1 \\
27 & 0 & 3
\end{bmatrix},
$$
and let $V' = \CC^3$ be an irreducible $G$-module for a finite group $G$, with $g \in G$ acting via the matrix $A_g$.
Let $$C = \frac{1}{\cardinality{G}} \sum_{g} A_g B A_g^{-1}.$$

(a) Calculate $\operatorname{Tr}(C)$, where $\operatorname{Tr}$ is the usual trace.

(b) Calculate $C$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers the problem; the argument is the card's own. Write $n=\cardinality{G}$ and note that $\Tr$ is linear and satisfies $\Tr(XY)=\Tr(YX)$.

::: pf

::: {.pf-step #invariant}
$A_{h}CA_{h}^{-1}=C$ for every $h\in G$.

::: pf-proof
Since $g\mapsto hg$ is a bijection of $G$, and $A_{h}A_{g}=A_{hg}$ while $A_{g}^{-1}A_{h}^{-1}=(A_{h}A_{g})^{-1}=A_{hg}^{-1}$, we get $A_{h}CA_{h}^{-1}=\frac{1}{n}\sum_{g}A_{hg}BA_{hg}^{-1}=\frac{1}{n}\sum_{g'}A_{g'}BA_{g'}^{-1}=C$ after reindexing by $g'=hg$.
:::

:::

::: {.pf-step #scalar}
$C=\lambda I_{3}$ for some $\lambda\in\CC$.

::: pf-proof
Step [](#invariant){.pf-ref} says $A_{h}C=CA_{h}$ for all $h$, so $C$ is a homomorphism of $G$-modules $\CC^{3}\to\CC^{3}$ for the given action. As $\CC^{3}$ is an irreducible complex $G$-module, Schur's lemma says every such endomorphism is a scalar, that is $C=\lambda I_{3}$.
:::

:::

::: {.pf-step #trace}
$\Tr(C)=\Tr(B)=6$.

::: pf-proof
Trace is unchanged under conjugation, $\Tr(A_{g}BA_{g}^{-1})=\Tr(B)$, and is linear, so $\Tr(C)=\frac{1}{n}\sum_{g}\Tr(B)=\Tr(B)$. For the given $B$ the diagonal entries are $2,1,3$, so $\Tr(B)=2+1+3=6$.
:::

:::

::: {.pf-step #answer-a}
(a) $\boxed{\Tr(C)=6}$.

::: pf-proof
This is step [](#trace){.pf-ref}; it uses only that the average is over the whole group, not the value of $n$ or the entries of $B$ off the diagonal.
:::

:::

::: {.pf-step #answer-b}
(b) $\boxed{C=2I_{3}}$.

::: pf-proof
By step [](#scalar){.pf-ref} $C=\lambda I_{3}$, whose trace is $3\lambda$; step [](#trace){.pf-ref} gives $3\lambda=6$, so $\lambda=2$ and $C=2I_{3}$, whatever the group and its action.
:::

:::

:::
:::
