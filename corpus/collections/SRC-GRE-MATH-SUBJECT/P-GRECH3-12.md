---
schema: qual/card@1
id: P-GRECH3-12
kind: problem
title: Slope on a planar slice of a surface
classification:
  areas:
  - real-analysis
  topics:
  - Partial Derivatives
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Checked against Chapter 3 review Question 12 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree."
---

::: {.problem}
The plane $y=1$ slices the surface
$$
z=\arctan\frac{x+y}{1-xy}
$$
in a curve, $C$. Find the slope of the tangent line to $C$ at the point where $x=2$.

(A) $-3$
(B) $-1$
(C) $\frac{1}{5}$
(D) $\frac{1}{3}$
(E) $\frac{1}{2}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

On the slice $y=1$, the curve $C$ is the graph
$$
z=\arctan\frac{x+1}{1-x}.
$$


::: pf-proof

Substituting $y=1$ into the given surface equation gives the displayed one-variable relation between $x$ and $z$.

:::

:::

::: {.pf-step #s1-2}

Along $C$,
$$
\frac{dz}{dx}=\frac{1}{1+x^2}.
$$


::: pf-proof

Set
$$
u(x)=\frac{x+1}{1-x}.
$$
Then, for $x\ne1$,
$$
u'(x)
=\frac{(1-x)+(x+1)}{(1-x)^2}
=\frac{2}{(1-x)^2}.
$$
By step [](#s1-1){.pf-ref} and the derivative of $\arctan$,
$$
\frac{dz}{dx}
=\frac{u'(x)}{1+u(x)^2}
=\frac{\frac{2}{(1-x)^2}}
{1+\frac{(x+1)^2}{(1-x)^2}}
=\frac{2}{(1-x)^2+(x+1)^2}
=\frac{1}{1+x^2}.
$$

:::

:::

::: {.pf-step #s1-3}

At $x=2$, the tangent slope is
$$
\boxed{\frac15},
$$
so the answer is (C).


::: pf-proof

Substituting $x=2$ into the derivative from step [](#s1-2){.pf-ref} gives
$$
\evaluated{\frac{dz}{dx}}_{x=2}
=\frac{1}{1+2^2}
=\frac15.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested tangent slope and corresponding choice.

:::

:::

:::
