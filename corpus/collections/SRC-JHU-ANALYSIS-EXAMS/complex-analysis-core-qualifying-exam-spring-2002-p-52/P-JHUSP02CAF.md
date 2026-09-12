---
schema: qual/card@1
id: P-JHUSP02CAF
kind: problem
title: "Mobius transformations carry lines and circles to lines and circles"
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Show that a Möbius transformation maps a straight line or circle onto a straight line or circle.
:::

::: solution
A generalized circle in $\widehat{\mathbb C}$ means either an ordinary circle or a straight line together with $\infty$. Such a set has an equation
\[
A|z|^2+Bz+\overline B\,\overline z+C=0,
\]
where $A,C\in\mathbb R$, $B\in\mathbb C$, and $|B|^2-AC>0$. If $A=0$, this is a line; if $A\ne0$, completing the square gives a circle.

Every Möbius map is a composition of translations, nonzero complex dilations, and inversion $z\mapsto1/z$. Indeed, for
\[
T(z)=\frac{az+b}{cz+d},\qquad ad-bc\ne0,
\]
there is nothing to prove when $c=0$, while for $c\ne0$,
\[
T(z)=\frac ac+\frac{bc-ad}{c^2}\frac1{z+d/c}.
\]
Translations and nonzero complex dilations plainly preserve generalized circles. For inversion, substitute $z=1/w$ into the equation and multiply by $|w|^2$:
\[
A+B\overline w+\overline B w+C|w|^2=0.
\]
This is again of the same form, now with coefficients $A'=C$, $B'=\overline B$, $C'=A$, and
\[
|B'|^2-A'C'=|B|^2-AC>0.
\]
Thus inversion also preserves generalized circles. Therefore every Möbius transformation maps every line or circle onto another line or circle.
:::
