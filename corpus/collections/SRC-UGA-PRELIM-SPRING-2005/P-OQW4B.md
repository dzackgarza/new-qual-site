---
schema: qual/card@1
id: P-OQW4B
kind: problem
title: The cube roots of $2-2i$
classification:
  areas:
  - prelim
  topics:
  - Roots of Unity
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. The card's first step had no proof and stated the polar form as
    an instruction ('Write 2-2i in polar form as ...'), the second gave the candidate roots with
    a one-line reason, and the third asserted completeness. It is now four proved steps: the
    modulus and argument computed; the candidates derived by comparing modulus and argument in
    z^3 = 2-2i, with the note that the three listed arguments are distinct modulo 2 pi and that
    each does give a root; the completeness from the degree bound; and the three values listed.
    The answers are unchanged. Not claimed: a retained solution set; the collection's provenance
    is the examination paper only.
---

::: {.problem}
Find all cube roots of $2-2i$ and express them in the standard form $a + bi$.
:::

::: {.solution}
Throughout $2-2i$ is written in polar form $re^{i\theta}$ with $r = \abs{2-2i} > 0$ and $\theta$ its principal argument, and a cube root of a complex number means a solution of $z^{3} = 2-2i$. The collection's `provenance` is the Spring 2005 examination paper, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #polar}
$2-2i = 2\sqrt{2}\\,e^{-i\pi/4}$.

::: pf-proof
$\abs{2-2i} = \sqrt{2^{2} + (-2)^{2}} = \sqrt{8} = 2\sqrt{2}$, and the point $(2,-2)$ lies in the fourth quadrant on the bisector, so its argument is $-\pi/4$: indeed $2\sqrt2\cos(-\pi/4) = 2\sqrt2\cdot\frac{\sqrt2}{2} = 2$ and $2\sqrt2\sin(-\pi/4) = -2$.

:::

:::

::: {.pf-step #candidates}
Every cube root has the form $z_{k} = \sqrt2\\,e^{i(-\pi/12 + 2\pi k/3)}$ for $k = 0, 1, 2$.

::: pf-proof
If $z = \rho e^{i\varphi}$ satisfies $z^{3} = 2-2i = 2\sqrt2\\,e^{-i\pi/4}$, then $\rho^{3} = 2\sqrt2$ gives $\rho = \sqrt2$ because $\rho > 0$ is real, and $3\varphi \equiv -\pi/4 \pmod{2\pi}$, that is $\varphi = -\pi/12 + 2\pi k/3$ for an integer $k$; the arguments for $k = 0, 1, 2$ differ by $2\pi/3$ and those for other $k$ repeat one of them, and each of the three values does give a root, since $\rho^{3}e^{3i\varphi} = 2\sqrt2\\,e^{-i\pi/4}$.

:::

:::

::: {.pf-step #all}
These three are all the cube roots of $2-2i$.

::: pf-proof
The polynomial $z^{3} - (2-2i)$ has degree $3$, so it has at most three roots in $\CC$, and step [](#candidates){.pf-ref} exhibits three distinct ones (their arguments are distinct modulo $2\pi$); hence they are exactly the roots.

:::

:::

::: pf-step
The three cube roots are $\boxed{\sqrt2\\,e^{-i\pi/12},\\ \sqrt2\\,e^{7i\pi/12},\\ \sqrt2\\,e^{15i\pi/12}}$, that is $\sqrt2\\,e^{i(-\pi/12 + 2\pi k/3)}$ for $k = 0,1,2$.

::: pf-proof
Substituting $k = 0, 1, 2$ in step [](#candidates){.pf-ref} gives the arguments $-\pi/12$, $-\pi/12 + 2\pi/3 = 7\pi/12$ and $-\pi/12 + 4\pi/3 = 15\pi/12$; step [](#all){.pf-ref} says there are no others.

:::

:::

:::
:::
