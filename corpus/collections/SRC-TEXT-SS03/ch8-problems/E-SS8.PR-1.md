---
schema: qual/card@1
id: E-SS8.PR-1
kind: problem
title: "Isogonality and isotropy at a point"
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked: differentiability gives
    $\abs{f(z_0+rv)-f(z_0)}/r\to\norm{Av}$, so isotropy is $\norm{Av}=\lambda\norm v$; polarization
    turns that into $A^{T}A=\lambda^2I$, i.e. $A=\lambda Q$ with $Q$ orthogonal; such a map preserves
    absolute angles, so isotropy implies isogonality; conversely isogonality forces $A$ injective,
    preserves perpendicularity, and the pair $e_1\pm e_2$ forces $\norm{Ae_1}=\norm{Ae_2}$, giving
    $A^{T}A=\lambda^2I$; and $\det Q=\pm1$ gives $Av=cv$ or $Av=c\overline v$, which are exactly
    complex-linearity of $A$ and of the differential of $\overline f$. Added: the polarization
    identity explicitly, the injectivity argument in full, and the identification of the differential
    of $\overline f$ as $v\mapsto\overline{Av}$. No defect found in the statement, Problem 1 of
    Chapter 8; no retained solution set covers it.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained book `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` at its printed folio (the scan runs nineteen pages ahead of the
    printed page): the statement is Problem 1 at the head of the Chapter 8 Problems, printed
    p. 254, and its printed words are the card's. The chapter, the problem number and the page
    are now named in the solution's opening sentence. Not checked in this pass: the argument, which
    the edit does not touch.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Asterisk status read from the book: Chapter 8 sets its asterisks before Problems 3, 4, 6, 7, 8
    and 9 only, so none stands before Problem 1. The remark records that. The locator by numbered
    statement is Chapter 8, Problem 1; the page readings recorded in the earlier events are
    superseded by it, the events themselves standing as written. Not checked in this pass: the
    wording of the statement and the argument.
---

::: {.exercise}
This is Problem 1 of Chapter 8 of Stein and Shakarchi, *Complex Analysis*, retained in this repository as `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`; the statement below is its wording.

Let $f$ be a complex-valued $C^1$ function defined in the neighborhood of a point $z_0$. There are several notions closely related to conformality at $z_0$. We say that $f$ is isogonal at $z_0$ if whenever $\gamma(t)$ and $\eta(t)$ are two smooth curves with $\gamma(0) = \eta(0) = z_0$, that make an angle $\theta$ there ($\abs{\theta} < \pi$), then $f(\gamma(t))$ and $f(\eta(t))$ make an angle of $\theta'$ at $t = 0$ with $\abs{\theta'} = \abs{\theta}$ for all $\theta$. Also, $f$ is said to be isotropic if it magnifies lengths by some factor for all directions emanating from $z_0$, that is, if the limit
$$
\lim_{r \to 0} \frac{\abs{f(z_0 + re^{i\theta}) - f(z_0)}}{r}
$$
exists, is non-zero, and independent of $\theta$.

Then $f$ is isogonal at $z_0$ if and only if it is isotropic at $z_0$; moreover, $f$ is isogonal at $z_0$ if and only if either $f'(z_0)$ exists and is non-zero, or the same holds for $f$ replaced by $\overline{f}$.
:::

::: {.remark}
The book sets no asterisk before this problem (Chapter 8, Problem 1).
:::

::: {.solution}
No retained solution set covers this problem, so the argument is the card's own; it is the linear-algebra reduction of the three notions to the real differential of $f$ at $z_0$. Write $A=Df(z_0)$, the real differential, which exists because $f$ is $\mathcal{C}^1$ near $z_0$.

::: pf

::: {.pf-step #isotropic}
$f$ is isotropic at $z_0$ if and only if there is $\lambda>0$ with $\norm{Av}=\lambda\norm v$ for all $v\in\RR^2$.

::: pf-proof
For a unit vector $v$, differentiability gives $f(z_0+rv)-f(z_0)=rAv+o(r)$ as $r\to0$, so $\abs{f(z_0+rv)-f(z_0)}/r\to\norm{Av}$. Isotropy says this limit exists, is nonzero and is independent of the direction $v$; that is exactly the existence of $\lambda>0$ with $\norm{Av}=\lambda$ for every unit $v$, which by homogeneity of the norm is the stated condition for all $v$.
:::

:::

::: {.pf-step #orthogonal}
The condition $\norm{Av}=\lambda\norm v$ for all $v$, with $\lambda>0$, is equivalent to $A^{T}A=\lambda^2I$.

::: pf-proof
If $\norm{Av}=\lambda\norm v$ then the polarization identity gives $\langle Av,Aw\rangle=\lambda^2\langle v,w\rangle$ for all $v,w$, which is $\langle A^{T}Av,w\rangle=\lambda^2\langle v,w\rangle$, that is $A^{T}A=\lambda^2I$. Conversely $A^{T}A=\lambda^2I$ gives $\norm{Av}^2=\langle A^{T}Av,v\rangle=\lambda^2\norm v^2$.
:::

:::

::: {.pf-step #similarity}
$A^{T}A=\lambda^2I$ with $\lambda>0$ holds if and only if $A=\lambda Q$ for an orthogonal $Q$, and then $A$ multiplies all lengths by $\lambda$ and preserves the absolute value of every angle; so isotropy implies isogonality.

::: pf-proof
$A^{T}A=\lambda^2I$ means $(A/\lambda)^{T}(A/\lambda)=I$, that is $Q=A/\lambda$ is orthogonal. Such an $A$ satisfies $\norm{Av}=\lambda\norm v$ and $\langle Av,Aw\rangle=\lambda^2\langle v,w\rangle$, so the angle between any two nonzero vectors is preserved in absolute value, and the angle between the images of two curves with tangents $v,w$ is that same angle.
:::

:::

::: {.pf-step #isogonal-implies}
If $f$ is isogonal at $z_0$ then $A^{T}A=\lambda^2I$ for some $\lambda>0$.

::: pf-proof
First $A$ is injective: if $Av=0$ for $v\ne0$, a curve through $z_0$ with tangent $v$ would have image tangent $0$, so the image curve would have no direction and the angle condition could not hold. Take an orthonormal pair $e_1,e_2$; isogonality turns the angle $\pi/2$ into an angle of absolute value $\pi/2$, so $Ae_1\perp Ae_2$. The vectors $e_1+e_2$ and $e_1-e_2$ are also perpendicular, so
$$
0=\langle A(e_1+e_2),A(e_1-e_2)\rangle=\norm{Ae_1}^2-\norm{Ae_2}^2,
$$
using the orthogonality of $Ae_1$ and $Ae_2$. With $\lambda=\norm{Ae_1}=\norm{Ae_2}>0$, the images of an orthonormal basis being orthogonal of equal length $\lambda$, the operator $A$ satisfies $\norm{Av}=\lambda\norm v$ for all $v$, and step [](#orthogonal){.pf-ref} gives $A^{T}A=\lambda^2I$.
:::

:::

::: {.pf-step #two-cases}
$A=\lambda Q$ with $Q$ orthogonal if and only if either $A$ is multiplication by some $c\ne0$ or $A$ is $v\mapsto c\overline v$ for some $c\ne0$; these are respectively the cases $\det Q=1$ and $\det Q=-1$.

::: pf-proof
An orthogonal $Q$ has $\det Q=\pm1$. If $\det Q=1$, $Q$ is a rotation, and a rotation of the plane is multiplication by the complex number $e^{i\alpha}$, so $Av=cv$ with $c=\lambda e^{i\alpha}$. If $\det Q=-1$, then $Q$ is a rotation followed by the reflection $v\mapsto\overline v$, so $Av=c\overline v$ with $c=\lambda e^{i\alpha}$. Conversely multiplication by $c\ne0$ and $v\mapsto c\overline v$ are $\abs c$ times a rotation, respectively a rotation composed with a reflection, hence $\abs c$ times an orthogonal map.
:::

:::

::: {.pf-step}
$f$ is isogonal at $z_0$ if and only if it is isotropic there, and if and only if either $f'(z_0)$ exists and is nonzero or $(\overline f)'(z_0)$ exists and is nonzero.

::: pf-proof
Steps [](#isotropic){.pf-ref} and [](#orthogonal){.pf-ref} identify isotropy with $A^{T}A=\lambda^2I$; step [](#similarity){.pf-ref} gives isogonality from it, and step [](#isogonal-implies){.pf-ref} gives it back from isogonality, so the first two notions coincide. For a $\mathcal{C}^1$ function the complex derivative $f'(z_0)$ exists exactly when the real differential $A$ is complex-linear, that is exactly when $Av=cv$ for some complex $c$, which is nonzero precisely when $A$ is invertible; and the differential of $\overline f$ is $v\mapsto\overline{Av}$, which equals $\overline c\,v$ when $Av=c\overline v$. By step [](#two-cases){.pf-ref} a similarity is of one of these two forms, so the third condition is equivalent to the first two.
:::

:::

:::
:::
