---
schema: qual/card@1
id: P-HCAO41
kind: problem
title: A Noetherian valuation ring which is not a field is a discrete valuation ring
classification:
  areas:
  - algebra
  topics:
  - Valuation Rings
  - Noetherian Rings
  - Discrete Valuation Rings
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard commutative-algebra oral extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained sheet `assets/attachments/MGSA_Commutative_Algebra_Oral_Questions.pdf`: the statement is the item "Let A be a noetherian valuation ring which is not a field. Show that A is a dvr.",
    and its printed words are the card's. The sheet numbers nothing and prints no folios, so the
    item is identified by its position and its opening words rather than by a number. Both are now
    named in the solution's opening sentence. Not checked in this pass: the argument, which the
    edit does not touch.
---

::: {.problem}
Let $A$ be a Noetherian valuation ring which is not a field.
Show that $A$ is a discrete valuation ring.
:::


::: {.solution}
This is the sheet `assets/attachments/MGSA_Commutative_Algebra_Oral_Questions.pdf`, Commutative Algebra section, item "Let A be a noetherian valuation ring which is not a field. Show that A is a dvr."; the statement below is its wording.
Let $\mathfrak m$ be the maximal ideal of the valuation ring $A$. Since $A$
is not a field, $\mathfrak m\ne0$.

::: pf

::: {.pf-step #maximal-ideal-principal}
The maximal ideal $\mathfrak m$ is principal.

::: pf-proof
Because $A$ is Noetherian, write
$$
\mathfrak m=(a_1,\ldots,a_r).
$$
Ideals in a valuation ring are totally ordered by inclusion, so among the
principal ideals $(a_i)$ there is a largest one, say $(a_j)$. Then every
$a_i\in(a_j)$, hence
$$
\mathfrak m=(a_j).
$$
Set $\pi=a_j$.
:::

:::

::: {.pf-step #every-ideal-is-power-of-m}
Every nonzero ideal of $A$ is a power of $\mathfrak m=(\pi)$.

::: pf-proof
Let $0\ne I\subseteq A$. Since $A$ is Noetherian, $I$ is finitely
generated, hence principal by the same total-order argument: $I=(x)$.
If $x$ is a unit then $I=A=\mathfrak m^0$. Otherwise $x\in\mathfrak m$,
so $x=\pi x_1$. If $x_1$ is not a unit, repeat.

This process must terminate. Otherwise $x\in(\pi^n)$ for every $n$, so
$$
(x)\subseteq\bigcap_{n\ge1}(\pi^n).
$$
But in the Noetherian local domain $A$, Krull's intersection theorem gives
$$
\bigcap_{n\ge1}\mathfrak m^n=0,
$$
contradicting $x\ne0$. Hence $x=u\pi^n$ for a unit $u$, and therefore
$$
I=(\pi^n)=\mathfrak m^n.
$$
:::

:::

::: pf-step
$A$ is a discrete valuation ring.

::: pf-proof
A Noetherian local domain that is not a field is a DVR precisely when its
nonzero maximal ideal is principal; equivalently, every nonzero ideal is a
power of that maximal ideal. Both conditions were established in step [](#maximal-ideal-principal){.pf-ref} and
step [](#every-ideal-is-power-of-m){.pf-ref}. Thus $A$ is a DVR with uniformizer $\pi$.
:::

:::

:::
:::
