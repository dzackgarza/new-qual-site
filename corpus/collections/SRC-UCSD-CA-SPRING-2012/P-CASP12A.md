---
schema: qual/card@1
id: P-CASP12A
kind: problem
title: "True or False: entire functions with prescribed derivatives, maximum modulus, Picard's theorem, fixed points, and complex structures"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Determine if each statement is true or false.
If false, provide a counterexample.
If true, give a brief proof.

1. If $f$ is an entire function satisfying $f(0) = 1$ and $f'(1/n) = f(1/n)$ for all integers $n \geq 1$, then $f(z) = e^z$ for all $z \in \CC$.

2. If $f$ is an entire function satisfying $f(0) = 1$ and $f'(n) = f(n)$ for all integers $n \geq 1$, then $f(z) = e^z$ for all $z \in \CC$.

3. If $f$ and $g$ are analytic functions defined on a neighborhood of $\abs{z} \leq 1$, $g \neq 0$ on $\abs{z} \leq 1$, and $\abs{f} \leq \abs{g}$ on $\abs{z} = 1$, then $\abs{f} \leq \abs{g}$ on $\abs{z} \leq 1$.

4. There exists a nonconstant analytic function $f$ on $\CC$ such that $\operatorname{ran} f \cap \DD = \emptyset$.

5. If $f$ is analytic on a neighborhood of $\abs{z} \leq 1$ and $\abs{f(z)} < 1$ for $\abs{z} \leq 1$, then $f$ when viewed as a mapping of $\overline{\DD}$ into $\overline{\DD}$ has a unique fixed point.

6. There is no complex structure on $\RR^2$ such that the function $f: \RR^2 \to \CC$ defined by $f(x, y) = x - iy$ is analytic.
:::

::: {.solution}

No retained solution set covers this exercise: the six answers are settled here, one step each, and item 2's counterexample is replaced — the card's own attempts, $e^{z}+\sin(\pi z)$ and $e^{z}\sin(2\pi z)$, fail the hypothesis $f'(n)=f(n)$.

::: pf

::: {.pf-step #one}
1. True.

::: pf-proof
$h=f'-f$ is entire and vanishes at every $1/n$, $n\ge1$; these points have the accumulation point $0$ in $\CC$, so the identity theorem gives $h\equiv0$. Then $(e^{-z}f)'=e^{-z}(f'-f)=0$, so $f=Ce^{z}$ with $C=f(0)=1$.
:::

:::

::: {.pf-step #two}
2. False.

::: pf-proof
Set $f(z)=e^{z}+\sin^{2}(\pi z)$, which is entire with $f(0)=1+0=1$. Since $f'=e^{z}+2\pi\sin(\pi z)\cos(\pi z)=e^{z}+\pi\sin(2\pi z)$ and $\sin(2\pi n)=0$, for every integer $n\ge1$ one has $f'(n)=e^{n}=f(n)$. But $f\ne e^{z}$. So the hypothesis at the discrete set $\{1,2,3,\dots\}$, which has no accumulation point in $\CC$, does not force $f=e^{z}$.
:::

:::

::: {.pf-step #three}
3. True.

::: pf-proof
$g$ is nonzero on the closed disc, so $h=f/g$ is analytic on a neighbourhood of it, and on $\abs z=1$ we have $\abs h=\abs f/\abs g\le1$. The maximum modulus principle gives $\abs h\le1$ on the disc, that is $\abs f\le\abs g$.
:::

:::

::: {.pf-step #four}
4. False.

::: pf-proof
If a nonconstant entire $f$ had range disjoint from $\DD$, its range would omit every point of the open disc, in particular two distinct values; Picard's little theorem says an entire function omitting two values is constant. So no such nonconstant $f$ exists.
:::

:::

::: {.pf-step #five}
5. True.

::: pf-proof
On $\abs z=1$ one has $\abs{f(z)}<1=\abs z$, so $\abs{f(z)-z}$ differs from $\abs z$ in the strict Rouché comparison: $\abs{f(z)-z-(-z)}=\abs{f(z)}<\abs z$. Hence $f(z)-z$ and $-z$ have the same number of zeros in $\DD$, namely one, and that zero is the unique fixed point.
:::

:::

::: {.pf-step #six}
6. False.

::: pf-proof
Take the complex structure on $\RR^{2}$ with the single global chart $\phi:\RR^{2}\to\CC$, $\phi(x,y)=x-iy$; the atlas has no transition maps to check, so it makes $\RR^{2}$ a complex analytic manifold. In that structure $f=\phi$ is a chart, hence analytic (indeed biholomorphic onto $\CC$). So such a complex structure does exist.
:::

:::

::: {.pf-qed}
1, 3, 5 are true by steps [](#one){.pf-ref}, [](#three){.pf-ref}, [](#five){.pf-ref}; 2, 4, 6 are false by steps [](#two){.pf-ref}, [](#four){.pf-ref}, [](#six){.pf-ref}.
:::

:::

:::
