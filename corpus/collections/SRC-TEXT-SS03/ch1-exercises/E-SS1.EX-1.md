---
schema: qual/card@1
id: E-SS1.EX-1
kind: problem
title: Geometric loci in the complex plane
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Numbers
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.exercise}
Describe geometrically the sets of points $z$ in the complex plane defined by the following relations:

(a) $|z-z_1|=|z-z_2|$, where $z_1,z_2\in\mathbb C$.

(b) $1/z=\overline z$.

(c) $\operatorname{Re}(z)=3$.

(d) $\operatorname{Re}(z)>c$ (respectively, $\operatorname{Re}(z)\ge c$), where $c\in\mathbb R$.

(e) $\operatorname{Re}(az+b)>0$, where $a,b\in\mathbb C$.

(f) $|z|=\operatorname{Re}(z)+1$.

(g) $\operatorname{Im}(z)=c$, where $c\in\mathbb R$.
:::

::: {.solution}

::: pf

::: pf-step

For (a), if $z_1\ne z_2$, the locus is the perpendicular bisector of the line segment joining $z_1$ and $z_2$; if $z_1=z_2$, the locus is all of $\mathbb C$.

::: pf-proof

Squaring both sides gives
\[
|z-z_1|^2=|z-z_2|^2
\iff
2\operatorname{Re}\!\bigl(z(\overline{z_2}-\overline{z_1})\bigr)=|z_2|^2-|z_1|^2.
\]
If $z_1\ne z_2$, this is the equation of a real affine line. It consists exactly of the points equidistant from $z_1$ and $z_2$, hence is their perpendicular bisector. If $z_1=z_2$, the original equality is tautological for every $z$.

:::

:::

::: pf-step

For (b), the locus is the unit circle $\{z\in\mathbb C:|z|=1\}$.

::: pf-proof

The equation is defined only for $z\ne0$. Multiplying by $z$ gives
\[
1=z\overline z=|z|^2,
\]
which is equivalent to $|z|=1$. Conversely every point of the unit circle satisfies $1/z=\overline z$.

:::

:::

::: pf-step

For (c), the locus is the vertical line $\{x+iy:x=3\}$.

::: pf-proof

Writing $z=x+iy$, one has $\operatorname{Re}(z)=x$, so the equation is exactly $x=3$.

:::

:::

::: pf-step

For (d), the loci are respectively the open and closed right half-planes bounded by the vertical line $x=c$.

::: pf-proof

Again writing $z=x+iy$, the inequalities become $x>c$ and $x\ge c$.

:::

:::

::: pf-step

For (e), if $a\ne0$ the locus is an open half-plane; if $a=0$, it is all of $\mathbb C$ when $\operatorname{Re}(b)>0$ and is empty when $\operatorname{Re}(b)\le0$.

::: pf-proof

Write $a=\alpha+i\beta$, $b=u+iv$, and $z=x+iy$. Then
\[
\operatorname{Re}(az+b)=\alpha x-\beta y+u.
\]
If $a\ne0$, then $(\alpha,-\beta)\ne(0,0)$, so
\[
\alpha x-\beta y+u>0
\]
defines one of the two open half-planes bounded by the line $\alpha x-\beta y+u=0$. If $a=0$, the inequality is the constant condition $u>0$, giving the two stated possibilities.

:::

:::

::: pf-step

For (f), the locus is the parabola
\[
y^2=2x+1,
\]
which opens to the right and has vertex $(-1/2,0)$.

::: pf-proof

Write $z=x+iy$. The equation $|z|=x+1$ implies
\[
x^2+y^2=(x+1)^2,
\]
hence $y^2=2x+1$. Conversely, on this parabola,
\[
x+1=\frac{y^2+1}{2}>0,
\]
so squaring introduced no extraneous points and $|z|=x+1$ indeed holds.

:::

:::

::: pf-step

For (g), the locus is the horizontal line $\{x+iy:y=c\}$.

::: pf-proof

For $z=x+iy$, one has $\operatorname{Im}(z)=y$, so the equation is exactly $y=c$.

:::

:::

:::

:::
