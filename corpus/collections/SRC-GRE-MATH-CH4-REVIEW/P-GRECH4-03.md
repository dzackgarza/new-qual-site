---
schema: qual/card@1
id: P-GRECH4-03
kind: problem
title: Family of curves from an area condition
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
  note: Re-transcribed from Chapter 4 review Question 3 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch4-review/, replacing the earlier chapter-4.pdf transcription.
---

::: {.problem}
Every curve in a certain family, $y = f(x, c)$, has the following property: the area of the region in the first quadrant bounded above by the curve from $(0, 0)$ to $(x, y)$ and bounded below by the $x$-axis is $\frac{1}{3}$ the area of the rectangle with opposite vertices at $(0, 0)$ and $(x, y)$. Find $f(x, c)$.

(A) $cx^3$
(B) $cx^3 + x$
(C) $cx^3 - x$
(D) $cx^2$
(E) $c\sqrt{x}$
:::

::: {.solution}
<1>1. Every curve in the family satisfies
$$
\int_0^x f(t,c)\,dt
=\frac13 x f(x,c).
$$

::: {.proof}
For the point $(x,y)$ on a curve, one has $y=f(x,c)$. The area under the curve from $0$ to $x$ is
$$
\int_0^x f(t,c)\,dt,
$$
while the rectangle with opposite vertices $(0,0)$ and $(x,y)$ has area $xy=x f(x,c)$. The stated area relation gives the displayed identity.
:::

<1>2. Writing $y=f(x,c)$, every such curve satisfies
$$
xy'=2y
$$
for $x>0$.

::: {.proof}
Differentiate the identity in step <1>1 with respect to $x$. The fundamental theorem of calculus gives
$$
y
=\frac13(xy)'
=\frac13(y+xy').
$$
Multiplying by $3$ and rearranging yields $xy'=2y$.
:::

<1>3. The family is
$$
\boxed{f(x,c)=cx^2},
$$
so the answer is (D).

::: {.proof}
For a nonzero solution of the equation in step <1>2,
$$
\frac{y'}{y}=\frac2x,
$$
so integration on $x>0$ gives
$$
\log|y|=2\log x+C,
$$
and hence $y=cx^2$ for a constant $c$. The zero solution is obtained by taking $c=0$, so the same formula describes the full family.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested family and corresponding choice.
:::
:::
