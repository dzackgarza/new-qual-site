---
schema: qual/card@1
id: E-AMD-H4KPWJ75
kind: problem
title: The minimal polynomial divides the characteristic polynomial
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured the prose solution into a structured proof under #2 and re-checked it: the
    annihilator set $I$ is an ideal because evaluation at $A$ is a ring homomorphism; $F[t]$ is a
    principal ideal domain, so $I=(m_A)$ for the monic minimal polynomial; and $\chi_A\in I$ by
    Cayley--Hamilton, whence $m_A\mid\chi_A$. The prose's remainder argument is kept as the
    equivalent form of the same step. No defect was found in the statement or in the prose. The
    card carries no collection and no retained solution set covers this exercise, so the argument
    is the card's own. Not claimed: a citation to a publication, and no separate proof of
    Cayley--Hamilton is given, that theorem being used as a known result.
---

::: {.exercise}
Prove that the minimal polynomial divides the characteristic polynomial.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own. Fix an $n\times n$ matrix $A$ over $F$, write $\chi_A(t)=\det(tI-A)$ for its characteristic polynomial, and let
$$
I=\{p\in F[t]:p(A)=0\}
$$
be the set of polynomials that annihilate $A$. The minimal polynomial $m_A$ is the monic generator of $I$.

::: pf

::: {.pf-step #ideal}
$I$ is an ideal of $F[t]$.

::: pf-proof
Let $p,q\in I$ and $s\in F[t]$. Then $(p+q)(A)=p(A)+q(A)=0$ because evaluation at $A$ is a ring homomorphism $F[t]\to M_n(F)$; and $(sp)(A)=s(A)p(A)=0$. So $I$ is closed under addition and under multiplication by elements of $F[t]$, and $0\in I$; that is an ideal.
:::

:::

::: {.pf-step #nonzero}
$I\ne\{0\}$, so it has a monic generator $m_A$, and $m_A\ne0$.

::: pf-proof
$F[t]$ is a principal ideal domain, so $I=(g)$ for some $g$, and multiplying $g$ by a nonzero scalar makes it monic. By the Cayley--Hamilton theorem $\chi_A(A)=0$, so $\chi_A\in I$; since $\chi_A$ is monic of degree $n$, it is nonzero, hence $I\ne\{0\}$ and $g\ne0$.
:::

:::

::: {.pf-step}
$\boxed{m_A\mid\chi_A}$.

::: pf-proof
By step [](#nonzero){.pf-ref} the ideal $I$ equals $(m_A)$, so every element of $I$ is a multiple of $m_A$; and $\chi_A\in I$ by step [](#nonzero){.pf-ref}. Hence $\chi_A=q\,m_A$ for some $q\in F[t]$, which is the assertion. Equivalently, dividing $\chi_A$ by $m_A$ with remainder and evaluating at $A$ gives $r(A)=0$ with $\deg r<\deg m_A$, so $r\in I$ is a multiple of $m_A$ of smaller degree and $r=0$.
:::

:::

:::
:::
