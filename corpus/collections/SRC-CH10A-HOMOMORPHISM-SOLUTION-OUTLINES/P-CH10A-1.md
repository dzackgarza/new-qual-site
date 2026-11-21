---
schema: qual/card@1
id: P-CH10A-1
kind: problem
title: The determinant is a homomorphism $GL(2,\RR)\to\RR^*$
classification:
  areas:
    - algebra
  topics:
    - Group Homomorphisms
relations: []
review: draft
audit:
  - event: source-checked
    by: claude-opus-5
    date: 2026-09-16
    note: Stated the Example 2 map (determinant on GL(2,R)) in the statement, taken from the source's own solution on page 1 of Ch10PtASltns.pdf.
  - event: solution-written
    by: claude
    date: 2026-11-19
    note: >-
      The solution was extraction residue in the outline's notation -- the function written as
      `G L ( 2 , RR )`, the determinant as `d e t ( A )`, and the image group as `RR ^ { * }`.
      Rewritten as a structured proof, and the mathematics checked: an invertible real matrix has
      nonzero determinant, so the map is well defined into $\RR^*$; the determinant is
      multiplicative and the product of invertible matrices is invertible; and
      $\GL(2,\RR)$, $\RR^*$ are groups under multiplication, so the map is a homomorphism. The
      statement, the map of Gallian's Example 2 of Chapter 10, is unchanged. The collection
      `provenance` is the textbook ISBN, so no retained solution set covers the exercise, and the
      solution says so. Not claimed: a reading of Gallian's printed Example 2, which the earlier
      event alone records.
  - event: source-corrected
    by: claude
    date: 2026-11-19
    note: >-
      The card said no retained solution set covers the exercise, and that is false: the collection's
      own outline is retained in this repository as `assets/attachments/Ch10PtASltns.pdf`, and its
      page 1 is this exercise. The rendered sentence now cites it and says what the card
      adds. Found by screening the residue's absence claims against the attachments, after two Munkres
      cards were found making the same false claim; no step of the proof changed.
  - event: source-checked
    by: claude
    date: 2026-11-19
    note: >-
      Read in the retained scan `tmp/sources/Gallian-Contemporary-Abstract-Algebra-7e.pdf`: Chapter 10
      Example 2, the determinant map from GL(2,R) to R*, is printed on p. 201 (page 215 of the file), and the
      exercise that asks for its being a homomorphism is Chapter 10 Exercise 1 on printed p. 211 (page 225 of
      the file). The pages are now named in the solution's opening sentence. Not checked in this pass: the
      two-line check, which the edit does not touch.
---

::: {.problem}
Prove that the mapping given in Example 2, the map $\phi : GL(2, \RR) \to \RR^*$ defined by $A \mapsto \det(A)$, is a homomorphism.
:::

::: {.solution}
The collection retains the source's own solution as `assets/attachments/Ch10PtASltns.pdf`, page 1, which carries this Example 2 map and its two-line check. The card states it in its own notation, and that notation is the wording below. In the seventh edition the exercise is **Chapter 10 Exercise 1**, and the Example 2 it names is Example 2 of Chapter 10; both are read in the retained scan `tmp/sources/Gallian-Contemporary-Abstract-Algebra-7e.pdf`. Write $\phi(A)=\det(A)$ for $A\in\GL(2,\RR)$, and $\RR^*$ for the group of nonzero reals under multiplication.

::: pf

::: {.pf-step #well-defined}
$\phi$ takes values in $\RR^*$.

::: pf-proof
A real $2\times2$ matrix is invertible exactly when its determinant is nonzero, so for $A\in\GL(2,\RR)$ one has $\det A\ne0$ and hence $\det A\in\RR^*$; the determinant is a real number for a real matrix.
:::

:::

::: {.pf-step #multiplicative}
$\phi(AB)=\phi(A)\phi(B)$ for all $A,B\in\GL(2,\RR)$.

::: pf-proof
The determinant is multiplicative on square matrices of the same size, $\det(AB)=\det(A)\det(B)$, and the product of two invertible matrices is invertible, so $AB\in\GL(2,\RR)$ and the identity holds there.
:::

:::

::: {.pf-step}
$\boxed{\phi\colon\GL(2,\RR)\to\RR^*,\ A\mapsto\det A,\ \text{is a homomorphism}}$.

::: pf-proof
$\GL(2,\RR)$ is a group under multiplication and $\RR^*$ is a group under multiplication, and steps [](#well-defined){.pf-ref} and [](#multiplicative){.pf-ref} show that $\phi$ is a well-defined map between them preserving the group operation, which is the definition of a homomorphism.
:::

:::

:::
:::
