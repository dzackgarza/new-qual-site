---
schema: qual/card@1
id: P-GRECH6-01
kind: problem
title: Integer solution of $42x+55y=1$
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
  note: "Re-transcribed from Chapter 6 review Question 1 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), compared with assets/attachments/chapter-6_extracted.md, replacing the earlier paraphrased transcription."
---

::: {.problem}
There is only one integer, $x$, between $100$ and $200$ such that integer pair $(x, y)$ satisfies the equation $42x + 55y = 1$. What's the value of $x$ in this integer pair?

(A) $127$
(B) $148$
(C) $158$
(D) $167$
(E) $183$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The Euclidean algorithm gives
$$
1=42(-17)+55(13).
$$


::: pf-proof

Compute
$$
55=42+13,
\qquad
42=3\cdot13+3,
\qquad
13=4\cdot3+1.
$$
Back-substitution yields
$$
\begin{aligned}
1
&=13-4(42-3\cdot13)\\
&=13\cdot13-4\cdot42\\
&=13(55-42)-4\cdot42\\
&=55\cdot13-42\cdot17.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-2}

All integer solutions of $42x+55y=1$ have the form
$$
x=-17+55t,
\qquad
y=13-42t,
\qquad t\in\ZZ.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} gives one solution $(x_0,y_0)=(-17,13)$. If $(x,y)$ is any other solution, subtracting the two equations gives
$$
42(x+17)+55(y-13)=0.
$$
Hence $42(x+17)=-55(y-13)$. Since $\gcd(42,55)=1$, one has $55\mid x+17$, so $x+17=55t$ for some $t\in\ZZ$. Substitution then gives $y-13=-42t$. Conversely, every pair of the displayed form satisfies the equation.

:::

:::

::: {.pf-step #s1-3}

The unique solution with $100<x<200$ has
$$
\boxed{x=148},
$$
so the answer is (B).


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
100<-17+55t<200,
$$
equivalently
$$
117<55t<217.
$$
Dividing by $55$ gives
$$
\frac{117}{55}<t<\frac{217}{55}.
$$
Since
$$
2<\frac{117}{55}<3<\frac{217}{55}<4,
$$
the only integer possibility is $t=3$. Then $x=-17+3\cdot55=148$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested integer.

:::

:::

:::
