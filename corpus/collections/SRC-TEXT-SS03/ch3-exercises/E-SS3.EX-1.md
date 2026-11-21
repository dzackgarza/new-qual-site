---
schema: qual/card@1
id: E-SS3.EX-1
kind: problem
title: Zeros of $\sin\pi z$ and residues of $1/\sin\pi z$
classification:
  areas:
    - complex-analysis
  topics: [Zeros of Holomorphic Functions, Residues, Trigonometric Functions]
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-10
  - event: solution-written
    by: claude
    date: 2026-11-18
    note: >-
      Restructured the prose solution into Lamport steps. The collection's provenance is the publisher's catalogue record only, with no retained text and no retained solution set, so the statement is taken as the card prints it; the argument is the card's own. Checked: the equivalence $\sin\pi z=0\iff e^{2\pi iz}=1$; that the modulus condition forces $y=0$ and then $x\in\ZZ$; that $\pi\cos\pi n=\pi(-1)^n\ne0$; and the residue formula for a simple pole of a reciprocal.
  - event: source-checked
    by: claude
    date: 2026-11-19
    note: >-
      Read in the retained book `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, at its printed folio (the scan runs nineteen pages ahead of
      the printed page): the statement is Exercise 1 at the head of the Chapter 3 Exercises,
      printed p. 103, and its printed words are the card's. The chapter, the exercise number and
      the page are now named in the solution's opening sentence. Not checked in this pass: the
      argument, which the edit does not touch.
  - event: source-corrected
    by: claude
    date: 2026-11-20
    note: >-
      The solution's opening sentence carried the printed page. It now cites the numbered statement
      alone, Chapter 3, Exercise 1, which is what the corpus rule asks for, and the page is gone
      from the rendered text. The statement is unchanged and the argument was not re-read in this
      pass.
---

::: {.exercise}
Using Euler’s formula

$$
\sin \pi z = \frac{e^{i\pi z} - e^{-i\pi z}}{2i},
$$

show that the complex zeros of $\sin \pi z$ are exactly at the integers, and that they are each of order $1$.

Calculate the residue of $1/\sin \pi z$ at $z = n \in \ZZ$.
:::

::: {.solution}
This is Exercise 1 of Chapter 3 of Stein and Shakarchi, *Complex Analysis*, retained in this repository as `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` [@SS03, ch. 3, Exercise 1]; the statement below is its wording.
No retained text and no retained solution set for this collection: its provenance is the publisher's catalogue record, so the statement is taken as the card prints it, and the argument is the card's own. Both assertions were checked: the zeros of $\sin\pi z$ are exactly the integers, each is simple, and the residue of $1/\sin\pi z$ there is $(-1)^n/\pi$.

::: pf

::: {.pf-step #zeros}
$\sin\pi z=0$ if and only if $z\in\ZZ$.

::: pf-proof
By Euler's formula $\sin\pi z=0$ exactly when $e^{i\pi z}=e^{-i\pi z}$, that is $e^{2\pi iz}=1$. Writing $z=x+iy$ gives $e^{2\pi iz}=e^{2\pi ix}e^{-2\pi y}$; for this to be $1$ its modulus must be $1$, so $e^{-2\pi y}=1$ and $y=0$, and then $e^{2\pi ix}=1$ gives $x\in\ZZ$.
:::
:::

::: {.pf-step #simple}
Each zero $n\in\ZZ$ of $\sin\pi z$ is simple.

::: pf-proof
The derivative is $\pi\cos\pi z$, whose value at $n$ is $\pi(-1)^n\ne0$.
:::
:::

::: {.pf-step #residue}
$\operatorname{Res}_{z=n}\frac{1}{\sin\pi z}=\frac{(-1)^n}{\pi}$.

::: pf-proof
For a holomorphic $g$ with a simple zero at $n$, $1/g$ has a simple pole there with residue $1/g'(n)$; applying this to $g=\sin\pi z$ and step [](#simple){.pf-ref} gives $1/(\pi\cos\pi n)=(-1)^n/\pi$.
:::
:::

::: {.pf-step}
The zeros of $\sin\pi z$ are the integers, they are simple, and the residues of the reciprocal there are $(-1)^n/\pi$.

::: pf-proof
Steps [](#zeros){.pf-ref}, [](#simple){.pf-ref} and [](#residue){.pf-ref} give the three assertions.
:::
:::

:::
:::
