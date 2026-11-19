---
schema: qual/card@1
id: P-PRACT20-W4-15
kind: problem
title: Evaluating a linear functional on $\RR^2$ from two values
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
  - Linear Transformations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the retained solution booklet of the collection,
    assets/attachments/Week4_solns.pdf, page 6, where Problem 15 reads: "Suppose
    that f: R^2 -> R is linear. If f(1,1) = 1 and f(-1,0) = 2, what is f(3,5)?"
    The card states exactly this, and the retained solution there is the single
    line "By linearity f(3,5) = f(5(1,1) + 2(-1,0)) = 5f(1,1) + 2f(-1,0) = 9",
    which is the card's solution word for word. The proof is complete for the
    problem: the linear combination 5(1,1) + 2(-1,0) = (3,5) is a direct
    arithmetic identity, and linearity is applied once to that identity. Nothing
    is left unproved, so nothing was written.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the one-line answer into a Lamport proof, quoting the retained solution itself:
    Christian Parkinson, GRE Prep: Diff. Eq. and Lin. Alg. Practice Problem Solutions, Problem 15,
    page 6 of assets/attachments/Week4_solns.pdf, whose solution reads "By linearity f(3,5) =
    f(5·(1,1) + 2·(-1,0)) = 5f(1,1) + 2f(-1,0) = 9". The steps are that computation with the
    coefficient identity (3,5) = 5(1,1) + 2(-1,0) proved rather than asserted, additivity and
    homogeneity used separately, and a closing step recording that the two given vectors are a basis
    of R^2, so the data are consistent and the value is forced rather than one of several
    possibilities. The answer 9 is unchanged.
---

::: {.problem}
Suppose that $f \colon \RR^{2} \to \RR$ is linear.
If $f(1, 1) = 1$ and $f(-1, 0) = 2$, what is $f(3, 5)$?
:::

::: {.solution}
The retained solution booklet answers this problem — **Christian Parkinson, *GRE Prep: Diff. Eq. & Lin. Alg. Practice Problem Solutions*, Problem 15, page 6 of `assets/attachments/Week4_solns.pdf`**: "By linearity $f(3,5)=f(5\cdot(1,1)+2\cdot(-1,0))=5f(1,1)+2f(-1,0)=9$." The steps below are that computation with the coefficient identity checked.

::: pf

::: {.pf-step #combination}
$(3,5)=5(1,1)+2(-1,0)$.

::: pf-proof
Coordinatewise: $5\cdot1+2\cdot(-1)=5-2=3$ and $5\cdot1+2\cdot0=5$. Both coordinates agree, so the identity holds.
:::

:::

::: {.pf-step #linearity}
$f(5(1,1)+2(-1,0))=5f(1,1)+2f(-1,0)$.

::: pf-proof
A linear map satisfies $f(u+v)=f(u)+f(v)$ and $f(cu)=cf(u)$. Applying additivity to the sum of the two scaled vectors and then homogeneity to each term gives the identity.
:::

:::

::: {.pf-step #answer}
$\boxed{f(3,5)=9}$.

::: pf-proof
By step [](#combination){.pf-ref} the vector $(3,5)$ is that combination, so $f(3,5)=5f(1,1)+2f(-1,0)$ by step [](#linearity){.pf-ref}; substituting $f(1,1)=1$ and $f(-1,0)=2$ gives $5\cdot1+2\cdot2=9$.
:::

:::

::: {.pf-step #well-posed}
The two given values are consistent, so the answer is forced.

::: pf-proof
The vectors $(1,1)$ and $(-1,0)$ are linearly independent, since $a(1,1)+b(-1,0)=(a-b,a)=(0,0)$ forces $a=0$ and then $b=0$, and two independent vectors in $\RR^{2}$ form a basis. A linear map is determined by its values on a basis, so the two prescribed values extend to exactly one linear $f$, and every such $f$ takes the value computed in step [](#answer){.pf-ref} at $(3,5)$.
:::

:::

:::
:::
