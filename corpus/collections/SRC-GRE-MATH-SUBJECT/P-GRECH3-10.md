---
schema: qual/card@1
id: P-GRECH3-10
kind: problem
title: Level curves of a cylindrical-coordinate surface
classification:
  areas:
  - real-analysis
  topics:
  - Level Curves
  - Cylindrical Coordinates
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Checked against Chapter 3 review Question 10 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree."
---

::: {.problem}
Which of the following depicts level curves of the surface whose equation in cylindrical coordinates is $z=r^2\cos 2\theta$?

The five graphical choices (A)–(E) appear on the source page:

![Scanned source page preserving the figure for Question 10.](../../../assets/attachments/gre-math-ch3-review/page-2.png)
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

In Cartesian coordinates the surface equation is
$$
z=x^2-y^2.
$$


::: pf-proof

Using
$$
x=r\cos\theta,\qquad y=r\sin\theta,
$$
and the identity $\cos 2\theta=\cos^2\theta-\sin^2\theta$, one obtains
$$
r^2\cos 2\theta
=r^2(\cos^2\theta-\sin^2\theta)
=(r\cos\theta)^2-(r\sin\theta)^2
=x^2-y^2.
$$
Thus $z=x^2-y^2$.

:::

:::

::: {.pf-step #s1-2}

The level curve at height $z=c$ is
$$
x^2-y^2=c.
$$


::: pf-proof

Fixing the value of $z$ in the Cartesian equation from step [](#s1-1){.pf-ref} gives exactly the displayed equation in the $xy$-plane.

:::

:::

::: {.pf-step #s1-3}

These level curves consist of the two diagonal lines when $c=0$, hyperbolas opening in the $x$-direction when $c>0$, and hyperbolas opening in the $y$-direction when $c<0$.


::: pf-proof

If $c=0$, step [](#s1-2){.pf-ref} gives
$$
x^2-y^2=(x-y)(x+y)=0,
$$
so the level set is $y=x$ together with $y=-x$. If $c>0$, division by $c$ gives
$$
\frac{x^2}{c}-\frac{y^2}{c}=1,
$$
which is a hyperbola with transverse axis on the $x$-axis. If $c<0$, writing $d=-c>0$ gives
$$
\frac{y^2}{d}-\frac{x^2}{d}=1,
$$
which is a hyperbola with transverse axis on the $y$-axis.

:::

:::

::: {.pf-step #s1-4}

Therefore the required depiction is
$$
\boxed{\text{(C)}}.
$$


::: pf-proof

Among the five source figures, choice (C) is the one showing the level-curve family characterized in step [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} identifies the requested graphical choice.

:::

:::

:::
