---
schema: qual/card@1
id: P-CAF08A
kind: problem
title: "Harnack inequality bound for a nonnegative harmonic function"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
---

::: {.problem}
Let $u$ be a nonnegative real-valued harmonic function defined in $B(1; 2)$ with $u(1) = 1/3$.
Prove that $$u(i) \leq 1 + \frac{2}{3}\sqrt{2}.$$
:::

::: {.solution}

No retained solution set covers this exercise: the card's own application of Harnack's inequality follows, with the value of $r$, the algebra of the Harnack factor and the conclusion separated.

::: pf

::: {.pf-step #harnack}
For $u$ nonnegative and harmonic in $B(1;2)$ and $\abs{z-1}=r<2$, one has $u(z)\le\dfrac{2+r}{2-r}\,u(1)$.

::: pf-proof
Harnack's inequality in the disc $B(a;R)$ states, for $u\ge0$ harmonic there and $\abs{z-a}=r<R$, that $\dfrac{R-r}{R+r}u(a)\le u(z)\le\dfrac{R+r}{R-r}u(a)$; take $a=1$ and $R=2$ and use the upper bound.
:::

:::

::: {.pf-step #radius}
For $z=i$ the radius is $r=\abs{i-1}=\sqrt{2}<2$.

::: pf-proof
$\abs{i-1}^{2}=1^{2}+(-1)^{2}=2$, so $r=\sqrt2\approx1.414<2$.
:::

:::

::: {.pf-step #algebra}
$\dfrac{2+\sqrt2}{2-\sqrt2}=3+2\sqrt2$.

::: pf-proof
Multiply numerator and denominator by $2+\sqrt2$: the denominator becomes $4-2=2$ and the numerator $(2+\sqrt2)^{2}=4+4\sqrt2+2=6+4\sqrt2$; the quotient is $3+2\sqrt2$.
:::

:::

::: {.pf-qed}
$u(i)\le\dfrac{2+\sqrt2}{2-\sqrt2}\,u(1)=(3+2\sqrt2)\cdot\tfrac13=1+\tfrac23\sqrt2$, by steps [](#harnack){.pf-ref}, [](#radius){.pf-ref}, [](#algebra){.pf-ref} and the hypothesis $u(1)=\tfrac13$.
:::

:::

:::
