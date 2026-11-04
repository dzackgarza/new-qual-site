---
schema: qual/card@1
id: P-AZOFF-A05
kind: problem
title: Uniform differentiability is equivalent to continuity of $f'$
classification:
  areas: [real-analysis]
  topics:
  - Differentiation
  - Uniform Continuity
  - Mean Value Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Compactness, connectedness, and functions of one real variable, Problem 5, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md. Flash emits a control character where the prime in $f'$ occurs in the final sentence; the correction is determined by the displayed uniform-differentiability definition and the stated equivalence.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Checked both recorded source appearances. For continuous f', compactness
    gives uniform continuity of f' and the mean value theorem controls every
    difference quotient uniformly. Conversely, applying uniform
    differentiability to (x,y) and to (y,x) makes the same difference
    quotient approximate both f'(y) and f'(x), proving f' uniformly
    continuous. Neither source supplies a worked proof.
- event: source-corrected
  by: claude
  date: 2026-10-31
  note: >-
    The SRC-MATH4100-6100-2020 appearance, Assignment 8 Math 6100 Bonus
    Problem 1, adds part (b), an example of a function differentiable on
    [a,b] but not uniformly differentiable there, which the card did not
    state. The statement now carries both parts; the Azoff appearance poses
    only part (a).
- event: solution-written
  by: claude
  date: 2026-10-31
  note: Rewrote the solution as a two-part structured proof and added the example for part (b).
---

::: {.problem}
Let $f$ be differentiable on $[a,b]$.
Say that $f$ is *uniformly differentiable* if for every $\varepsilon>0$ there exists $\delta>0$ such that
$$
\abs{\frac{f(x)-f(y)}{x-y}-f'(y)}<\varepsilon
$$
whenever $x,y\in[a,b]$, $x\ne y$, and $\abs{x-y}<\delta$.

(a) Prove that $f$ is uniformly differentiable on $[a,b]$ if and only if $f'$ is continuous on $[a,b]$.

(b) Give an example of a function that is differentiable on $[a,b]$ but is not uniformly differentiable on $[a,b]$.
:::

::: {.solution}
For distinct $x,y\in[a,b]$, write
$$
Q(x,y)=\frac{f(x)-f(y)}{x-y},
$$
so that $Q(y,x)=Q(x,y)$.

::: pf

::: {.pf-step}
(a) $f$ is uniformly differentiable on $[a,b]$ if and only if $f'$ is continuous on $[a,b]$.

::: pf-proof

::: {.pf-step #a-reverse}
If $f'$ is continuous on $[a,b]$, then $f$ is uniformly differentiable on $[a,b]$.

::: pf-proof
The interval $[a,b]$ is compact, so by the Heine--Cantor theorem the continuous function $f'$ is uniformly continuous on it.
Let $\varepsilon>0$ and choose $\delta>0$ such that $\abs{u-v}<\delta$ implies $\abs{f'(u)-f'(v)}<\varepsilon$ for all $u,v\in[a,b]$.
Let $x,y\in[a,b]$ be distinct with $\abs{x-y}<\delta$.
The mean value theorem applied to the interval with endpoints $x$ and $y$ gives a point $c$ strictly between them with $Q(x,y)=f'(c)$.
Since $c$ lies between $x$ and $y$, we have $\abs{c-y}<\abs{x-y}<\delta$, and therefore
$$
\abs{Q(x,y)-f'(y)}=\abs{f'(c)-f'(y)}<\varepsilon.
$$
The number $\delta$ depends only on $\varepsilon$, so $f$ is uniformly differentiable on $[a,b]$.
:::

:::

::: {.pf-step #a-forward}
If $f$ is uniformly differentiable on $[a,b]$, then $f'$ is continuous on $[a,b]$, so that with step [](#a-reverse){.pf-ref} the equivalence in (a) holds.

::: pf-proof
Let $\varepsilon>0$ and choose $\delta>0$ witnessing uniform differentiability for $\varepsilon/2$: for distinct $x,y\in[a,b]$ with $\abs{x-y}<\delta$,
$$
\abs{Q(x,y)-f'(y)}<\frac{\varepsilon}{2}.
$$
The pair $(y,x)$ satisfies the same hypotheses, and $Q(y,x)=Q(x,y)$, so
$$
\abs{Q(x,y)-f'(x)}=\abs{Q(y,x)-f'(x)}<\frac{\varepsilon}{2}.
$$
For such a pair the triangle inequality gives
$$
\abs{f'(x)-f'(y)}\le\abs{f'(x)-Q(x,y)}+\abs{Q(x,y)-f'(y)}<\varepsilon,
$$
and for $x=y$ the left-hand side is $0<\varepsilon$.
Hence $f'$ is uniformly continuous on $[a,b]$, and in particular continuous there.
:::

:::

:::

:::

::: {.pf-step}
(b)
$$
\boxed{f(x)=x^{2}\sin\left(1/x^{2}\right)\ \text{for } 0<x\le1,\qquad f(0)=0}
$$
is differentiable on $[0,1]$ and not uniformly differentiable on $[0,1]$.

::: pf-proof
On $(0,1]$ the function is built from differentiable functions by products and compositions, with
$$
f'(x)=2x\sin\left(1/x^{2}\right)-\frac{2}{x}\cos\left(1/x^{2}\right),
$$
and at the origin
$$
\frac{f(h)-f(0)}{h-0}=h\sin\left(1/h^{2}\right)\longrightarrow 0\qquad(h\to0,\ h\ne0)
$$
because $\abs{h\sin(1/h^{2})}\le\abs{h}$.
Hence $f'(0)=0$ and $f$ is differentiable on $[0,1]$.

For every integer $k\ge1$ put $x_k=1/\sqrt{2\pi k}$, an element of $(0,1]$ with $1/x_k^{2}=2\pi k$.
Then $\sin(1/x_k^{2})=0$ and $\cos(1/x_k^{2})=1$, so
$$
f'(x_k)=-\frac{2}{x_k}=-2\sqrt{2\pi k}\longrightarrow-\infty.
$$
A function continuous at a point is bounded on a neighbourhood of it, so $f'$ is not continuous at $0$, hence not continuous on $[0,1]$.
By part (a), $f$ is not uniformly differentiable on $[0,1]$.
:::

:::

:::
:::
