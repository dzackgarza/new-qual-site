---
schema: qual/card@1
id: P-GRECH4-14
kind: problem
title: Recovering an exact differential equation coefficient
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 4 review Question 14 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch4-review/, replacing the earlier chapter-4.pdf transcription.
---

::: {.problem}
Let $g(x, y)$ be the function defined for all $x$ and all nonzero $y$ such that the differential equation

$$
(\sin xy)\,dx + g(x, y)\,dy = 0
$$

is exact and $g(0, y) = 0$ for all $y \neq 0$. What is $g(x, 1)$?

(A) $\sin x + \cos x - 1$
(B) $x\sin x + \cos x - 1$
(C) $x\sin x - \cos x + 1$
(D) $x\sin x + \cos x$
(E) $\sin x - x\cos x + 1$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Exactness requires
$$
\frac{\partial g}{\partial x}
=x\cos(xy).
$$


::: pf-proof

For
$$
M(x,y)=\sin(xy),
\qquad
N(x,y)=g(x,y),
$$
exactness means $M_y=N_x$. Since
$$
M_y=x\cos(xy),
$$
the displayed identity follows.

:::

:::

::: {.pf-step #s1-2}

For $y\ne0$,
$$
g(x,y)
=\frac{x}{y}\sin(xy)
+\frac{1}{y^2}\cos(xy)
+h(y)
$$
for some function $h$.


::: pf-proof

Integrating step [](#s1-1){.pf-ref} with respect to $x$, set $u=xy$. Then
$$
\int x\cos(xy)\,dx
=\frac1{y^2}\int u\cos u\,du.
$$
Integration by parts gives
$$
\int u\cos u\,du
=u\sin u+\cos u.
$$
Substituting back yields
$$
\frac{x}{y}\sin(xy)+\frac1{y^2}\cos(xy),
$$
and the constant of integration may depend on $y$.

:::

:::

::: {.pf-step #s1-3}

The condition $g(0,y)=0$ forces
$$
h(y)=-\frac1{y^2}.
$$


::: pf-proof

Putting $x=0$ into step [](#s1-2){.pf-ref} gives
$$
0=g(0,y)=\frac1{y^2}+h(y)
$$
for every nonzero $y$.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{g(x,1)=x\sin x+\cos x-1},
$$
so the answer is (B).


::: pf-proof

Substitute $y=1$ and the function $h$ from step [](#s1-3){.pf-ref} into step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested function and corresponding choice.

:::

:::

:::
