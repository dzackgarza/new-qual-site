---
schema: qual/card@1
id: E-SS8.EX-4
kind: problem
title: A holomorphic surjection from the disc onto $\CC$
classification:
  areas:
    - complex-analysis
  topics:
    - Conformal Maps
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-11
  - event: solution-written
    by: claude
    date: 2026-11-19
    note: >-
      Lamport structure over the prose that was already there. The Cayley-type map is now
      verified rather than named: the real and imaginary parts of i(1+z)/(1-z) are computed,
      which both exhibits the upper half-plane as its image and proves the map is holomorphic
      on the disc, and the inverse (w-i)/(w+i) is checked to land in the disc for w in the
      upper half-plane, so the map is onto and not merely into. The choice of square root
      with nonnegative imaginary part is the step that makes the squaring surjective. Not
      checked: the book's own text of the exercise, since no copy of Stein and Shakarchi is
      retained in this checkout; the statement is as transcribed on the card. No retained
      solution set covers the exercise (the collection's provenance is a Google Books
      record), so the argument is the card's own. No statement repair.
---

::: {.exercise}
Does there exist a holomorphic surjection from the unit disc to $\CC$?

[Hint: Move the upper half-plane “down” and then square it to get $\CC$.]
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is a Google Books record, so the argument is the card's own. The answer is yes, and the map is exhibited below. Write $\DD$ for the unit disc and $\halfplane$ for the upper half-plane.

::: pf

::: {.pf-step #cayley}
$h(z)=i\dfrac{1+z}{1-z}$ is holomorphic on $\DD$ and maps $\DD$ bijectively onto $\halfplane$.

::: pf-proof
Since $\abs{z}<1$ we have $z\ne1$, so $h$ is a quotient of holomorphic functions with nonvanishing denominator, hence holomorphic on $\DD$. For $\abs{z}<1$, multiply by $\overline{1-z}$:
$$
h(z)=\frac{i(1+z)(1-\overline z)}{\abs{1-z}^2}=\frac{i\bigl(1-\abs{z}^2+z-\overline z\bigr)}{\abs{1-z}^2}=\frac{-2\operatorname{Im}z+i\bigl(1-\abs{z}^2\bigr)}{\abs{1-z}^2},
$$
using $z-\overline z=2i\operatorname{Im}z$ and $i\cdot2i\operatorname{Im}z=-2\operatorname{Im}z$. The imaginary part is $\bigl(1-\abs{z}^2\bigr)/\abs{1-z}^2>0$, so $h$ maps $\DD$ into $\halfplane$. For surjectivity let $w\in\halfplane$ and put $z=\dfrac{w-i}{w+i}$, which is defined since $\operatorname{Im}w>0$ excludes $w=-i$. Then $\abs{w-i}^2=\abs{w}^2-2\operatorname{Im}w+1<\abs{w}^2+2\operatorname{Im}w+1=\abs{w+i}^2$, so $\abs{z}<1$, and solving $w=i\frac{1+z}{1-z}$ for $z$ gives $h(z)=w$. So $h$ is a bijection onto $\halfplane$.
:::

:::

::: {.pf-step #shift}
$g=h-i$ maps $\DD$ bijectively onto $\{w:\operatorname{Im}w>-1\}$.

::: pf-proof
Subtracting the constant $i$ shifts the imaginary part down by $1$: $\operatorname{Im}\bigl(h(z)-i\bigr)=\operatorname{Im}h(z)-1$, and $\operatorname{Im}h(z)>0$ by step [](#cayley){.pf-ref}. A bijection composed with the translation $w\mapsto w-i$, itself a bijection of $\CC$, is again a bijection, onto the image of $\halfplane$ under that translation, which is $\{w:\operatorname{Im}w>-1\}$.
:::

:::

::: {.pf-step #square}
$F=g^2$ is holomorphic on $\DD$, and for every $\zeta\in\CC$ there is $w$ with $w^2=\zeta$ and $\operatorname{Im}w\ge0$.

::: pf-proof
A product of holomorphic functions is holomorphic, so $F$ is holomorphic on $\DD$. For the root: write $\zeta=re^{i\theta}$; then $w=\sqrt r\,e^{i\theta/2}$ satisfies $w^2=\zeta$, and if $\operatorname{Im}w<0$ then $-w$ is also a square root of $\zeta$ with $\operatorname{Im}(-w)>0$. So one of the two roots has nonnegative imaginary part.
:::

:::

::: {.pf-step #onto}
$F$ is surjective onto $\CC$.

::: pf-proof
Let $\zeta\in\CC$ and take $w$ with $w^2=\zeta$ and $\operatorname{Im}w\ge0$ by step [](#square){.pf-ref}. Then $\operatorname{Im}w\ge0>-1$, so $w$ lies in the image of $g$ by step [](#shift){.pf-ref}: there is $z\in\DD$ with $g(z)=w$. For that $z$, $F(z)=g(z)^2=w^2=\zeta$. So every $\zeta$ is attained, which is surjectivity.
:::

:::

::: {.pf-step}
There is a holomorphic surjection $\DD\to\CC$, namely $F(z)=\Bigl(i\dfrac{1+z}{1-z}-i\Bigr)^2$.

::: pf-proof
Steps [](#shift){.pf-ref} and [](#square){.pf-ref} give that $F$ is holomorphic on the disc, and step [](#onto){.pf-ref} gives that it is onto $\CC$. So the answer to the question is yes, with this explicit map; it is not injective, since $g$ is a bijection onto a half-plane and $w\mapsto w^2$ is two-to-one there.
:::

:::

:::

:::
