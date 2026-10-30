---
schema: qual/card@1
id: P-GRECH3-17
kind: problem
title: Implicit partial derivative of a surface
classification:
  areas:
  - real-analysis
  topics:
  - Implicit Differentiation
  - Partial Derivatives
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Checked against Chapter 3 review Question 17 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree."
---

::: {.problem}
The equation $x^3z^5-y^2z^3-3xy=1$ defines an implicit function $z=f(x,y)$. What's the value of $\frac{\partial f}{\partial y}$ at the point $(x,y)=(-1,1)$?

(A) $-8$
(B) $-1$
(C) $-\frac{1}{8}$
(D) $\frac{1}{8}$
(E) $8$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

At $(x,y)=(-1,1)$, the implicit equation has the unique real solution
$$
z=1.
$$


::: pf-proof

Substituting $x=-1$ and $y=1$ into
$$
x^3z^5-y^2z^3-3xy=1
$$
gives
$$
-z^5-z^3+3=1,
$$
or equivalently
$$
z^5+z^3=2.
$$
The value $z=1$ satisfies this equation. If $z\le0$, then $z^5+z^3\le0$; if $0<z<1$, then $z^5+z^3<2$; and if $z>1$, then $z^5+z^3>2$. Thus no other real value is possible.

:::

:::

::: {.pf-step #s1-2}

Implicit differentiation with respect to $y$, holding $x$ fixed, gives
$$
\frac{\partial z}{\partial y}
=
\frac{2yz^3+3x}{5x^3z^4-3y^2z^2}.
$$


::: pf-proof

Differentiating the defining equation yields
$$
5x^3z^4\frac{\partial z}{\partial y}
-2yz^3
-3y^2z^2\frac{\partial z}{\partial y}
-3x
=0.
$$
Collecting the terms containing $\partial z/\partial y$ gives
$$
\left(5x^3z^4-3y^2z^2\right)\frac{\partial z}{\partial y}
=2yz^3+3x,
$$
which gives the displayed formula whenever the coefficient on the left is nonzero.

:::

:::

::: {.pf-step #s1-3}

At $(x,y,z)=(-1,1,1)$,
$$
\boxed{\frac{\partial f}{\partial y}=\frac18},
$$
so the answer is (D).


::: pf-proof

By step [](#s1-1){.pf-ref}, the relevant point on the surface has $z=1$. Substitution into step [](#s1-2){.pf-ref} gives
$$
\frac{\partial f}{\partial y}
=\frac{2(1)(1)^3+3(-1)}
{5(-1)^3(1)^4-3(1)^2(1)^2}
=\frac{-1}{-8}
=\frac18.
$$
The denominator is $-8\ne0$, so the implicit derivative is well-defined there.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested partial derivative and corresponding choice.

:::

:::

:::
