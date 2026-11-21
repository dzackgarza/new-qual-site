---
schema: qual/card@1
id: E-MUN-2-1
kind: problem
title: Preimage and image under injective and surjective maps
classification:
  areas:
  - topology
  topics:
  - Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 2, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §2 Exercise 1, printed p. 20; the two parts
    are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 2.1,
    printed p. 11 (tmp/sources/munkres-solutions-whitman.pdf), whose two arguments are
    the card's. No defect found.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The statement was checked against Munkres, *Topology* (2000), §2 Exercise 1, printed p. 20, and the argument is transcribed from the retained set: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 2.1, printed p. 11, whose two directions in each part are the card's. The inclusion in (a) and in (b) is proved for an arbitrary element; the equality in each part uses the corresponding injectivity or surjectivity hypothesis exactly once.
---

::: {.exercise}

Let $f: A \to B$ . Let $A_0 \subset A$ and $B_0 \subset B$ .

(a) Show that $A_0 \subset f^{-1}(f(A_0))$ and that equality holds if $f$ is injective.

(b) Show that $f(f^{-1}(B_0)) \subset B_0$ and that equality holds if $f$ is surjective.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 2.1** (`tmp/sources/munkres-solutions-whitman.pdf`), whose two arguments are the steps below; the statement is Munkres, *Topology* (2000), §2 Exercise 1.

::: pf

::: {.pf-step #a-inclusion}
$A_0\subset f^{-1}(f(A_0))$.

::: pf-proof
Let $x\in A_0$ and put $y=f(x)$. Then $y\in f(A_0)$ by the definition of the image, so $x\in f^{-1}(f(A_0))$ by the definition of the preimage. As $x$ was arbitrary, $A_0\subset f^{-1}(f(A_0))$.
:::
:::

::: {.pf-step #a-equality}
If $f$ is injective then $f^{-1}(f(A_0))\subset A_0$, hence $f^{-1}(f(A_0))=A_0$.

::: pf-proof
Let $x\in f^{-1}(f(A_0))$. Then $f(x)\in f(A_0)$, so $f(x)=f(x')$ for some $x'\in A_0$. Injectivity gives $x=x'\in A_0$. So $f^{-1}(f(A_0))\subset A_0$, and with the inclusion of step [](#a-inclusion){.pf-ref} the two sets are equal.
:::
:::

::: {.pf-step #b-inclusion}
$f(f^{-1}(B_0))\subset B_0$.

::: pf-proof
Let $y\in f(f^{-1}(B_0))$. Then $y=f(x)$ for some $x\in f^{-1}(B_0)$, and $x\in f^{-1}(B_0)$ means $f(x)\in B_0$; so $y\in B_0$.
:::
:::

::: {.pf-step #b-equality}
If $f$ is surjective then $B_0\subset f(f^{-1}(B_0))$, hence $f(f^{-1}(B_0))=B_0$.

::: pf-proof
Let $y\in B_0$. Since $B_0\subset B$ and $f$ is surjective, $y=f(x)$ for some $x\in A$; then $f(x)\in B_0$, so $x\in f^{-1}(B_0)$ and $y=f(x)\in f(f^{-1}(B_0))$. So $B_0\subset f(f^{-1}(B_0))$, and with step [](#b-inclusion){.pf-ref} the two sets are equal.
:::
:::

::: {.pf-step}
Both assertions of the exercise hold, with equality exactly under the stated hypothesis in each part.

::: pf-proof
Steps [](#a-inclusion){.pf-ref} and [](#a-equality){.pf-ref} give (a) and steps [](#b-inclusion){.pf-ref} and [](#b-equality){.pf-ref} give (b).
:::
:::

:::
:::
