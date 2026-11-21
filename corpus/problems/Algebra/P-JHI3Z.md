---
schema: qual/card@1
id: P-JHI3Z
kind: problem
title: Nilpotent matrix
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Reviewed against the Lamport standard. What was found: the question asks what
    a nilpotent matrix is, so its answer is a definition, not a proposition, and
    a structured proof has nothing to prove — no `pf` block was added, because
    one here would be invented structure rather than a proof. What was checked:
    the definition in the solution agrees with the one on the definition card
    D-GIGM2 (nilpotent element: r^n = 0 for some n >= 1), so the solution adds
    no second defining occurrence; the least such r is the nilpotency index, and
    that is a definition rather than a claim; the remark's assertions (minimal
    polynomial x^r, eigenvalues 0, Jordan blocks J_s(0), and A^n = 0 by
    Cayley-Hamilton) are standard and are stated as a remark, not as part of the
    solution. What was not checked: no source solution exists for this card and
    none was compared; the remark's equivalences were not proved here, since they
    are outside the solution section.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof: the definition is stated as the answer, and the equivalences
    recorded in the card's remark are proved rather than only listed — nilpotent implies a zero
    spectrum; the characteristic polynomial is x^n by triangularization over an algebraic
    closure, so Cayley-Hamilton gives A^n = 0; the minimal polynomial is x^s with s the
    nilpotency index; the Jordan form consists of blocks J_s(0); and the three converses. Added
    the reason the index exists and is at most n. Not claimed: a retained solution set; the
    defining link to D-GIGM2 in the previous text is kept in the remark's neighbourhood.
---

::: {.problem}
What is a nilpotent matrix?
:::

::: {.solution}
The question asks for a definition; the numbered steps state it and then justify the equivalence recorded in the card's remark, which is the mathematical content of the answer. No retained solution set covers it. Throughout $A$ is an $n\times n$ matrix over a field $k$ and $\overline k$ is an algebraic closure of $k$.

::: pf

::: {.pf-step #definition}
$A$ is **nilpotent** if $A^r=0$ for some integer $r\ge1$; the least such $r$ is the **nilpotency index** of $A$.

::: pf-proof
A definition, needing no proof. The zero matrix is nilpotent with index $1$; the index exists by well-ordering when $A$ is nilpotent, and is at most $n$ for an $n\times n$ matrix by step [](#annihilates){.pf-ref}.

:::

:::

::: {.pf-step #spectrum}
If $A$ is nilpotent then every eigenvalue of $A$ in $\overline k$ is $0$.

::: pf-proof
Let $Av=\lambda v$ with $v\ne0$. Then $0=A^rv=\lambda^rv$, so $\lambda^r=0$ and hence $\lambda=0$.

:::

:::

::: {.pf-step #charpoly}
If $A$ is nilpotent with $A^r=0$, its characteristic polynomial is $x^n$, and consequently $A^n=0$.

::: pf-proof
Over $\overline k$ the matrix $A$ is conjugate to an upper triangular matrix with the eigenvalues on the diagonal (every matrix is triangularizable over an algebraically closed field). By step [](#spectrum){.pf-ref} all the entries on the diagonal are $0$, so the characteristic polynomial, which is the product of the diagonal entries of $xI-A$ in triangular form, is $x^n$. By the Cayley–Hamilton theorem $A$ satisfies its characteristic polynomial, so $A^n=0$.

:::

:::

::: {.pf-step #polynomial}
If $A$ is nilpotent with $A^r=0$, its minimal polynomial is $x^s$ for some $1\le s\le r$, namely the least $s$ with $A^s=0$.

::: pf-proof
The minimal polynomial $m$ divides every polynomial annihilating $A$, in particular $x^r$, so it is $x^s$ with $s\le r$; and $m$ is the monic generator of the annihilator ideal, so $s$ is the least exponent with $A^s=0$, which is the nilpotency index.

:::

:::

::: {.pf-step #jordan}
If $A$ is nilpotent then its Jordan form consists of blocks $J_s(0)$, $s\ge1$.

::: pf-proof
The Jordan form of $A$ over $\overline k$ is block diagonal with blocks $J_s(\lambda)$ for the eigenvalues $\lambda$ and the sizes $s$ of the elementary divisors. By step [](#spectrum){.pf-ref} every $\lambda$ is $0$, so every block is $J_s(0)$, which is nilpotent; conversely a direct sum of such blocks is nilpotent, with index the largest $s$.

:::

:::

::: {.pf-step #converse}
Conversely, if every eigenvalue of $A$ over $\overline k$ is $0$, or if the minimal polynomial is $x^s$, or if the Jordan form consists of blocks $J_s(0)$, then $A$ is nilpotent.

::: pf-proof
If the Jordan form is a direct sum of blocks $J_s(0)$ then $A$ is conjugate to a nilpotent matrix, hence nilpotent, with index the largest block size. If the minimal polynomial is $x^s$ then $A^s=0$ by definition of the minimal polynomial. If every eigenvalue is $0$, then the characteristic polynomial is $x^n$ by the triangular-form argument of step [](#charpoly){.pf-ref}, so the minimal polynomial divides $x^n$ and is $x^s$, and $A^s=0$.

:::

:::

::: {.pf-step #annihilates}
For an $n\times n$ matrix over a field, nilpotent is equivalent to each of: minimal polynomial $x^s$; all eigenvalues $0$; Jordan form a sum of blocks $J_s(0)$; and then $A^n=0$.

::: pf-proof
The forward implications are steps [](#spectrum){.pf-ref}, [](#charpoly){.pf-ref}, [](#polynomial){.pf-ref} and [](#jordan){.pf-ref}, and the reverse ones step [](#converse){.pf-ref}; $A^n=0$ is step [](#charpoly){.pf-ref}.

:::

:::

:::
:::

::: {.remark}
For an $n\times n$ matrix $A$ over a field, the following are equivalent: $A$ is nilpotent; the minimal polynomial of $A$ is $x^r$ for some $r\ge1$; every eigenvalue of $A$ in an algebraic closure is $0$; the Jordan form of $A$ consists of blocks $J_s(0)$. In particular, a nilpotent $n\times n$ matrix over a field satisfies $A^n=0$, by the Cayley--Hamilton theorem applied to its characteristic polynomial $x^n$.
:::
