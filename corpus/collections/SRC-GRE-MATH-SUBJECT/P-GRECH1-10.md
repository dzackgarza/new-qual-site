---
schema: qual/card@1
id: P-GRECH1-10
kind: problem
title: Focus of a parabola from its directrix
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 1 review Question 10 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription.
---

::: {.problem}
Every point on the parabola $y = \sqrt{2x - 1}$ is equidistant from the $y$-axis and which of the following points?

(A) $(\frac{1}{2}, 0)$
(B) $(1, 0)$
(C) $(\frac{3}{2}, 0)$
(D) $(2, 0)$
(E) $(\frac{5}{2}, 0)$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Every point $(x,y)$ on the given graph is equidistant from the $y$-axis and $(1,0)$.


::: pf-proof

On the graph,
$$
y^2=2x-1,
$$
so $x=(y^2+1)/2>0$. Hence the distance from $(x,y)$ to the $y$-axis is $x$. Its squared distance to $(1,0)$ is
$$
(x-1)^2+y^2
=(x-1)^2+(2x-1)
=x^2.
$$
Because $x>0$, the distance to $(1,0)$ is also $x$.

:::

:::

::: {.pf-step #s1-2}

The required point is uniquely
$$
\boxed{(1,0)},
$$
so the answer is (B).


::: pf-proof

The graph contains $(1,1)$. If a point $(p,0)$ is equidistant from every point of the graph and the $y$-axis, then at $(1,1)$ its distance must equal $1$. Thus
$$
(1-p)^2+1=1,
$$
so $p=1$. Step [](#s1-1){.pf-ref} shows that this value indeed works for every point on the graph.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} identifies the unique listed point with the required property.

:::

:::

:::
