---
schema: qual/card@1
id: P-GRECH3-25
kind: problem
title: Line integral along a parabola
classification:
  areas:
  - real-analysis
  topics:
  - Line Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Checked against Chapter 3 review Question 25 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree. The chapter-3.pdf extraction read the starting point as (1,1); the book extraction and its solution, which integrates over t from -1 to 0, give (-1,1)."
---

::: {.problem}
If $\mathbf{F}=(3y-2x)\hat{\mathbf{i}}+(x^2+y)\hat{\mathbf{j}}$, find the value of $\int_C\mathbf{F}\cdot d\mathbf{r}$, where $C$ is the portion of the parabola $y=x^2$, directed from $(-1,1)$ to the origin.

(A) $-1$
(B) $0$
(C) $1$
(D) $2$
(E) $3$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A parametrization of $C$ with the required orientation is
$$
\mathbf{r}(t)=(t,t^2),
\qquad -1\le t\le0.
$$


::: pf-proof

The equation $y=x^2$ is satisfied by $(x,y)=(t,t^2)$. At $t=-1$ this gives $(-1,1)$, and at $t=0$ it gives the origin, so increasing $t$ follows the stated orientation.

:::

:::

::: {.pf-step #s1-2}

Along this parametrization,
$$
\mathbf{F}(\mathbf{r}(t))\cdot\mathbf{r}'(t)
=4t^3+3t^2-2t.
$$


::: pf-proof

From step [](#s1-1){.pf-ref},
$$
\mathbf{r}'(t)=(1,2t).
$$
Also,
$$
\mathbf{F}(t,t^2)
=\bigl(3t^2-2t,\ t^2+t^2\bigr)
=\bigl(3t^2-2t,\ 2t^2\bigr).
$$
Therefore
$$
\mathbf{F}(\mathbf{r}(t))\cdot\mathbf{r}'(t)
=(3t^2-2t)(1)+(2t^2)(2t)
=4t^3+3t^2-2t.
$$

:::

:::

::: {.pf-step #s1-3}

The line integral is
$$
\boxed{1},
$$
so the answer is (C).


::: pf-proof

Using step [](#s1-2){.pf-ref},
$$
\int_C\mathbf{F}\cdot d\mathbf{r}
=\int_{-1}^{0}(4t^3+3t^2-2t)\,dt
=\left[t^4+t^3-t^2\right]_{-1}^{0}.
$$
Hence
$$
\int_C\mathbf{F}\cdot d\mathbf{r}
=0-\bigl(1-1-1\bigr)
=1.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested line-integral value and corresponding choice.

:::

:::

:::
