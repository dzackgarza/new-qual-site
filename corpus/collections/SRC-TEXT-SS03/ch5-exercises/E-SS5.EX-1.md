---
schema: qual/card@1
id: E-SS5.EX-1
kind: problem
title: Jensen's formula via Blaschke factors
classification:
  areas:
  - complex-analysis
  topics:
  - Jensen's Formula
  - Blaschke Factors
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The collection's provenance is the publisher's catalogue record only, with no retained text and no retained solution set, so the statement is taken as the card prints it; the argument is the card's own. Checked: the pole-free denominator and the modulus identity $\abs{\alpha-z}=\abs{1-\overline\alpha z}$ on the circle; that the product of the factors cancels the zeros with multiplicity; the mean-value property for $\log\abs g$; and the two evaluations at the origin and on the boundary.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained book `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, at its printed folio (the scan runs nineteen pages ahead of
    the printed page): the statement is Exercise 1 at the head of the Chapter 5 Exercises,
    printed p. 153, and its printed words are the card's. The chapter, the exercise number and
    the page are now named in the solution's opening sentence. Not checked in this pass: the
    argument, which the edit does not touch.
---

::: {.exercise}
Give another proof of Jensen's formula in the unit disc using the functions (called Blaschke factors)
$$
\psi_\alpha(z) = \frac{\alpha - z}{1 - \overline{\alpha} z}.
$$
[Hint: The function $f/(\psi_{z_1} \cdots \psi_{z_N})$ is nowhere vanishing.]
:::

::: {.solution}
This is Exercise 1 of Chapter 5 of Stein and Shakarchi, *Complex Analysis*, retained in this repository as `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`; the statement below is its wording.
No retained text and no retained solution set for this collection: its provenance is the publisher's catalogue record, so the statement is taken as the card prints it, and the argument is the card's own. The proof is the standard Blaschke-factor argument for Jensen's formula; each property of the factor and each evaluation was checked.

::: pf

::: {.pf-step #blaschke}
For $\abs\alpha<1$ the factor $\psi_\alpha(z)=\frac{\alpha-z}{1-\overline\alpha z}$ is holomorphic and pole-free on the closed disc, has its only zero at $\alpha$, satisfies $\abs{\psi_\alpha(e^{i\theta})}=1$ and $\psi_\alpha(0)=\alpha$.

::: pf-proof
The denominator $1-\overline\alpha z$ does not vanish for $\abs z\le1$ because $\abs{\overline\alpha z}\le\abs\alpha<1$, and the numerator vanishes exactly at $z=\alpha$. On $\abs z=1$, $\abs{\alpha-z}=\abs z\abs{\overline z\alpha-1}=\abs{1-\overline\alpha z}$, so the modulus is $1$; at $0$ the factor is $\alpha$.
:::
:::

::: {.pf-step #g}
With $z_1,\dots,z_N$ the zeros of $f$ in $\DD$ counted with multiplicity, $g=f/\prod_j\psi_{z_j}$ is holomorphic and nowhere zero in a neighbourhood of the closed disc.

::: pf-proof
Each $\psi_{z_j}$ is holomorphic and pole-free on the closed disc by step [](#blaschke){.pf-ref} and has a simple zero exactly at $z_j$, so the denominator cancels the zeros of $f$ with multiplicity, leaving a holomorphic function with no zeros in a neighbourhood of the closed disc. The hypothesis that $f$ has no zeros on the unit circle keeps $g$ zero-free there.
:::
:::

::: {.pf-step #mean-value}
$\log\abs{g(0)}=\frac{1}{2\pi}\int_0^{2\pi}\log\abs{g(e^{i\theta})}d\theta$.

::: pf-proof
$g$ is zero-free near the closed disc, so $\log\abs g$ is harmonic there; the mean-value property for harmonic functions at the centre of the disc gives the identity.
:::
:::

::: {.pf-step #circle}
$\frac{1}{2\pi}\int_0^{2\pi}\log\abs{g(e^{i\theta})}d\theta=\frac{1}{2\pi}\int_0^{2\pi}\log\abs{f(e^{i\theta})}d\theta$.

::: pf-proof
By step [](#blaschke){.pf-ref} each factor has modulus $1$ on the unit circle, so $\abs{g}=\abs f$ there and the logarithms agree pointwise.
:::
:::

::: {.pf-step #origin}
$\abs{g(0)}=\abs{f(0)}/\prod_j\abs{z_j}$.

::: pf-proof
Evaluate $g$ at $0$: the denominator contributes $\prod_j\abs{\psi_{z_j}(0)}=\prod_j\abs{z_j}$ and the numerator is $f(0)$.
:::
:::

::: {.pf-step #jensen}
$\log\abs{f(0)}=\sum_j\log\abs{z_j}+\frac{1}{2\pi}\int_0^{2\pi}\log\abs{f(e^{i\theta})}d\theta$.

::: pf-proof
Combine steps [](#mean-value){.pf-ref}, [](#circle){.pf-ref} and [](#origin){.pf-ref}: $\log\abs{g(0)}=\log\abs{f(0)}-\sum_j\log\abs{z_j}$ equals the boundary integral of $\log\abs f$.
:::
:::

:::
:::
