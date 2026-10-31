---
schema: qual/card@1
id: P-PRACT20-W4-04
kind: problem
title: The solution of $x\,dy+(y-xe^x)\,dx=0$ through $(1,0)$
classification:
  areas:
  - prelim
  topics:
  - Ordinary Differential Equations
relations: []
review: draft
---

::: {.problem}
Find the solution of $x\, dy + (y - x e^{x})\, dx = 0$ which passes through the point $(1, 0)$.
:::

::: {.solution}
This problem can be re-phrased

$$
x\frac{dy}{dx}+y=xe^x.
$$

The left-hand side is already a perfect derivative:

$$
\frac{d}{dx}\left[xy(x)\right]=xe^x\Longrightarrow xy(x)=xe^x-e^x+C\Longrightarrow y(x)=e^x-\frac{e^x}{x}+\frac{C}{x}.
$$

Now $y(1)=0$ gives $C=0$, so $\boxed{y(x)=e^x-e^x/x}$ for $x>0$.
:::
