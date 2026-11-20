---
schema: qual/card@1
id: E-SS2.EX-1
kind: problem
title: The Fresnel integrals $\int_0^\infty\sin(x^2)\,dx=\int_0^\infty\cos(x^2)\,dx=\frac{\sqrt{2\pi}}4$
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Integrals
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
    Restructured the prose solution into Lamport steps. The collection's provenance is the publisher's catalogue record only, with no retained text and no retained solution set, so the statement is taken as the card prints it; the argument is the card's own. Checked: the contour and the parametrisation of its three pieces; the modulus $\abs{e^{-z^2}}=e^{-R^2\cos2\theta}=e^{-R^2\sin2u}$; the concavity bound $\sin2u\ge4u/\pi$; the resulting estimate $\pi/(4R)$; and the passage to real and imaginary parts, which gives the two values $\sqrt{2\pi}/4$.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained book `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, at its printed folio (the scan runs nineteen pages ahead of
    the printed page): the statement is Exercise 1 at the head of the Chapter 2 Exercises,
    printed p. 64, and its printed words are the card's. The chapter, the exercise number and
    the page are now named in the solution's opening sentence. Not checked in this pass: the
    argument, which the edit does not touch.
---

::: {.exercise}
Prove that
$$
\int_0^{\infty} \sin(x^2)\, dx = \int_0^{\infty} \cos(x^2)\, dx = \frac{\sqrt{2\pi}}{4}.
$$
These are the Fresnel integrals. Here, $\int_0^{\infty}$ is interpreted as $\lim_{R \to \infty} \int_0^R$.

[Hint: Integrate the function $e^{-z^2}$ over the path in Figure 14. Recall that $\int_{-\infty}^{\infty} e^{-x^2}\, dx = \sqrt{\pi}$.]
:::

::: {.solution}
This is Exercise 1 of Chapter 2 of Stein and Shakarchi, *Complex Analysis*, retained in this repository as `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`; the statement below is its wording.
No retained text and no retained solution set for this collection: its provenance is the publisher's catalogue record, so the statement is taken as the card prints it, and the argument is the card's own. The standard sector-contour proof was checked step by step, including the arc estimate.

::: pf

::: {.pf-step #contour}
For $R>0$, integrating the entire function $e^{-z^2}$ over the boundary of the sector $0\le\abs z\le R$, $0\le\arg z\le\pi/4$ gives $\int_0^R e^{-x^2}dx+\int_{\Gamma_R}e^{-z^2}dz-e^{i\pi/4}\int_0^Re^{-ir^2}dr=0$.

::: pf-proof
$e^{-z^2}$ is entire, so its integral over the closed contour vanishes by Cauchy's theorem. The contour consists of the segment $[0,R]$ on the real axis, the arc $\Gamma_R$ of radius $R$ from angle $0$ to $\pi/4$, and the ray at angle $\pi/4$ traversed back to $0$, on which $z=e^{i\pi/4}r$ and $dz=e^{i\pi/4}dr$, so $z^2=ir^2$.
:::
:::

::: {.pf-step #arc}
$\abs{\int_{\Gamma_R}e^{-z^2}dz}\le\pi/(4R)$, so the arc integral tends to $0$.

::: pf-proof
On $\Gamma_R$ we have $z=Re^{i\theta}$ and $z^2=R^2e^{2i\theta}$, so $\abs{e^{-z^2}}=e^{-R^2\cos2\theta}$. With $u=\pi/4-\theta$ this is $e^{-R^2\sin2u}$, and concavity of $\sin$ on $[0,\pi/2]$ gives $\sin2u\ge4u/\pi$ for $0\le u\le\pi/4$. Hence the modulus of the arc integral is at most $R\int_0^{\pi/4}e^{-4R^2u/\pi}du\le R\cdot\pi/(4R^2)=\pi/(4R)$.
:::
:::

::: {.pf-step #limit}
Letting $R\to\infty$: $\int_0^\infty e^{-ir^2}dr=e^{-i\pi/4}\frac{\sqrt\pi}{2}=\frac{\sqrt{2\pi}}{4}(1-i)$.

::: pf-proof
The arc term tends to $0$ by step [](#arc){.pf-ref} and the Gaussian integral is $\int_0^\infty e^{-x^2}dx=\sqrt\pi/2$; passing to the limit in the identity of step [](#contour){.pf-ref} gives $\sqrt\pi/2=e^{i\pi/4}\int_0^\infty e^{-ir^2}dr$, and multiplying by $e^{-i\pi/4}=\frac{\sqrt2}{2}(1-i)$ gives the displayed value.
:::
:::

::: {.pf-step #parts}
$\int_0^\infty\cos(x^2)dx=\frac{\sqrt{2\pi}}{4}$ and $\int_0^\infty\sin(x^2)dx=\frac{\sqrt{2\pi}}{4}$.

::: pf-proof
By step [](#limit){.pf-ref}, $\int_0^\infty e^{-ir^2}dr=\int_0^\infty\cos(r^2)dr-i\int_0^\infty\sin(r^2)dr$ equals $\frac{\sqrt{2\pi}}{4}(1-i)$; comparing real and imaginary parts gives both integrals equal to $\frac{\sqrt{2\pi}}{4}$.
:::
:::

:::
:::
