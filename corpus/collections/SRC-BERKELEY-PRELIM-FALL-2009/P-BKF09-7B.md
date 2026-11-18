---
schema: qual/card@1
id: P-BKF09-7B
kind: problem
title: Evaluation of $\int_0^{2\pi} d\theta/(1-2\alpha\cos\theta+\alpha^2)$
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the retained sheet's argument (Fall 2009
    solutions, Problem 7B, PDF p. 7, the file named in the collection's provenance), now cited
    on the body. Added: the partial-fraction identity
    $1-2\alpha\cos\theta+\alpha^2=-\frac{\alpha}{z}(z-\alpha)(z-\alpha^{-1})$ is proved rather
    than asserted, $\alpha=0$ is separated before the residue formula (the sheet separates it
    too, but after writing $\alpha^{-1}$), the residues are computed in both cases, and the
    three cases are collected into the single answer $2\pi/\abs{1-\alpha^2}$, where the
    sheet's last display is $2\pi(\abs\alpha-1)/((\alpha^2-1)\abs{\abs\alpha-1})$ and
    leaves the sign implicit. The value of the integral is unchanged.
---

::: {.problem}
Suppose $\alpha$ is a complex number, $\abs{\alpha}\neq1$.
Compute
$$
\int_0^{2\pi}\frac{d\theta}{1-2\alpha\cos\theta+\alpha^2}
$$
by integrating $(z-\alpha)^{-1}(z-\alpha^{-1})^{-1}$ over the unit circle.
:::

::: {.solution}
The published solution is the collection's own retained sheet, **Fall 2009 preliminary examination solutions, Problem 7B, PDF p. 7** (`assets/attachments/f09solutions.pdf`, the file named in this collection's `provenance`): the parametrization, the residue computation in the two cases, and the separate treatment of $\alpha=0$ are that solution's. The card writes the answer in the single form $2\pi/\abs{1-\alpha^2}$, where the sheet's final display is the product $2\pi(\abs\alpha-1)/((\alpha^2-1)\abs{\abs\alpha-1})$ and so hides the sign it is computing.

Throughout $\alpha\in\CC$ with $\abs\alpha\ne1$, $C$ is the unit circle traversed once counterclockwise, and
$$
J(\alpha)\coloneqq\int_0^{2\pi}\frac{d\theta}{1-2\alpha\cos\theta+\alpha^2}.
$$

::: pf

::: {.pf-step #parametrize}
$J(\alpha)=\dfrac{i}{\alpha}\displaystyle\oint_C\frac{dz}{(z-\alpha)(z-\alpha^{-1})}$ for $\alpha\ne0$.

::: pf-proof
Put $z=e^{i\theta}$, so $dz=iz\,d\theta$, $d\theta=dz/(iz)$, and $\cos\theta=(z+z^{-1})/2$. Then
$$
1-2\alpha\cos\theta+\alpha^2=1-\alpha(z+z^{-1})+\alpha^2=-\frac{\alpha}{z}(z-\alpha)(z-\alpha^{-1}),
$$
and that identity is the expansion
$$
-\frac{\alpha}{z}(z-\alpha)(z-\alpha^{-1})
=-\frac{\alpha}{z}\bigl(z^2-z(\alpha+\alpha^{-1})+1\bigr)
=-\alpha z+\alpha(\alpha+\alpha^{-1})-\frac{\alpha}{z}
=1-\alpha z-\frac{\alpha}{z}+\alpha^2,
$$
whose right-hand side is $1-\alpha(z+z^{-1})+\alpha^2$. Hence
$$
\frac{d\theta}{1-2\alpha\cos\theta+\alpha^2}=\frac{dz}{iz}\cdot\frac{-z}{\alpha(z-\alpha)(z-\alpha^{-1})}=\frac{i\,dz}{\alpha(z-\alpha)(z-\alpha^{-1})} .
$$

:::

:::

::: {.pf-step #alpha-zero}
$J(0)=2\pi$.

::: pf-proof
At $\alpha=0$ the integrand is the constant $1$ and the integral is $2\pi$. The residue formula of step [](#parametrize){.pf-ref} does not apply, because $\alpha^{-1}$ is undefined.

:::

:::

::: {.pf-step #inside}
For $0<\abs\alpha<1$, $J(\alpha)=2\pi/(1-\alpha^2)$.

::: pf-proof
The integrand $(z-\alpha)^{-1}(z-\alpha^{-1})^{-1}$ has its only pole inside $C$ at $z=\alpha$, since $\abs{\alpha^{-1}}>1$. That pole is simple with residue $1/(\alpha-\alpha^{-1})$, so by the residue theorem
$$
\oint_C\frac{dz}{(z-\alpha)(z-\alpha^{-1})}=2\pi i\cdot\frac{1}{\alpha-\alpha^{-1}},
$$
and step [](#parametrize){.pf-ref} gives
$$
J(\alpha)=\frac{i}{\alpha}\cdot\frac{2\pi i}{\alpha-\alpha^{-1}}=\frac{-2\pi}{\alpha^2-1}=\frac{2\pi}{1-\alpha^2}.
$$

:::

:::

::: {.pf-step #outside}
For $\abs\alpha>1$, $J(\alpha)=2\pi/(\alpha^2-1)$.

::: pf-proof
Now $\abs{\alpha^{-1}}<1$ and $\abs\alpha>1$, so the only pole inside $C$ is $z=\alpha^{-1}$, with residue $1/(\alpha^{-1}-\alpha)$. Hence
$$
J(\alpha)=\frac{i}{\alpha}\cdot\frac{2\pi i}{\alpha^{-1}-\alpha}=\frac{-2\pi}{\alpha(\alpha^{-1}-\alpha)}=\frac{-2\pi}{1-\alpha^2}=\frac{2\pi}{\alpha^2-1}.
$$

:::

:::

::: {.pf-step #conclusion}
$J(\alpha)=\dfrac{2\pi}{\abs{1-\alpha^2}}$ for every $\alpha$ with $\abs\alpha\ne1$.

::: pf-proof
For $0<\abs\alpha<1$ step [](#inside){.pf-ref} gives $2\pi/(1-\alpha^2)$ and $1-\alpha^2>0$, so this is $2\pi/\abs{1-\alpha^2}$. For $\abs\alpha>1$ step [](#outside){.pf-ref} gives $2\pi/(\alpha^2-1)$ and $\alpha^2-1>0$, which is again $2\pi/\abs{1-\alpha^2}$. For $\alpha=0$ step [](#alpha-zero){.pf-ref} gives $2\pi=2\pi/\abs{1-0}$. The integrand is real and positive throughout, so the single positive expression is consistent with all three cases.

:::

:::

:::
:::
