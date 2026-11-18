---
schema: qual/card@1
id: P-4QQGN
kind: problem
title: Measurability of $f'$ and of the differentiability set of a continuous function
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    The previous solution was a sketch with a garbled sentence ("Then Module a null set, f'
    is measurable"), no hypothesis on measurability of f, and the typo "exsits"; it is
    replaced by a complete argument, and the card now states what the printed problem leaves
    implicit: measurability is Lebesgue measurability for the completed measure. Added: that
    a function differentiable off a null set is measurable (continuity on the complement,
    completeness of the measure), measurability of the difference quotients n(f(x+1/n)-f(x)),
    the derivative as their limit along h = 1/n on the differentiability set, and the
    measurability of the four Dini derivates for continuous f via a rational supremum over
    shrinking intervals, with the differentiability set written as an intersection of
    equality and finiteness conditions. Not claimed: a retained solution set, since
    `assets/attachments/a16.pdf` is the question paper only.
---

::: {.problem}
(a) Let $f(x)$ be a real valued function on the real line that is differentiable almost everywhere.
Prove that $f'(x)$ is a Lebesgue measurable function.

(b) Prove that if $f$ is a continuous real valued function on the real line, then the set of points at which $f$ is differentiable is measurable.
:::

::: {.solution}
No retained solution set covers this problem: the only retained file for this exam is `assets/attachments/a16.pdf`, which is the question paper and contains no solutions. The argument below is the card's own; the previous prose was a sketch that named no hypotheses and contained the garbled sentence "Then Module a null set", and it is replaced.

Throughout $f:\RR\to\RR$ is real valued, $m$ is Lebesgue measure, and "measurable" means Lebesgue measurable on the completion of the Borel $\sigma$-algebra, so that every subset of a null set is measurable.

::: pf

::: {.pf-step #measurable}
If $f$ is differentiable at every point of $\RR-N$ with $m(N)=0$, then $f$ is measurable.

::: pf-proof
$f$ is continuous at each point of $\RR-N$, since differentiability at a point implies continuity there. Hence for a closed set $F\subseteq\RR$ the set $f^{-1}(F)\cap(\RR-N)$ is closed in the subspace $\RR-N$, that is it equals $U\cap(\RR-N)$ for some closed $U\subseteq\RR$, and such a set is measurable. Also $f^{-1}(F)\cap N\subseteq N$ has measure zero, so it is measurable because the measure is complete. Adding the two pieces, $f^{-1}(F)$ is measurable for every closed $F$, and the closed sets generate the Borel sigma-algebra, so $f$ is measurable.

:::

:::

::: {.pf-step #difference-quotients}
For each $n\ge1$ the function $g_n(x)\coloneqq n\bigl(f(x+1/n)-f(x)\bigr)$ is measurable.

::: pf-proof
$x\mapsto f(x+1/n)$ is the composite of the measurable $f$ with the measurable translation, hence measurable; $x\mapsto f(x)$ is measurable by step [](#measurable){.pf-ref}; a difference and a scalar multiple of measurable real functions are measurable.

:::

:::

::: {.pf-step #part-a}
$f'$ is measurable.

::: pf-proof
Where $f$ is differentiable at $x$, the derivative is the limit of the difference quotients along the particular sequence $h=1/n\to0$, so
$$
f'(x)=\lim_{n\to\infty}g_n(x)\quad\text{for every }x\in\RR-N .
$$
The set $E$ on which the sequence $(g_n(x))$ converges to a finite limit is measurable, because it is the intersection of $\theset{x\mid \limsup_n g_n(x)-\liminf_n g_n(x)=0}$ with $\theset{x\mid \limsup_n\abs{g_n(x)}<\infty}$, and limsup and liminf of a sequence of measurable functions are measurable. On $E$ the limit function is $\limsup_ng_n$, which is measurable. Since $f'$ agrees on the full-measure set $(\RR-N)\cap E$ with that measurable function, it is measurable as a function defined almost everywhere, and extended by $0$ off that set it is a measurable function on $\RR$.

:::

:::

::: {.pf-step #derivates}
For continuous $f$ the four Dini derivates are measurable functions with values in $[-\infty,\infty]$:
$$
D^+f(x)=\limsup_{h\to0^+}\frac{f(x+h)-f(x)}{h},\qquad D_+f(x)=\liminf_{h\to0^+}\frac{f(x+h)-f(x)}{h},
$$
and their left-hand analogues $D^-f$, $D_-f$.

::: pf-proof
By continuity of $f$ in the increment variable, the quotient $h\mapsto(f(x+h)-f(x))/h$ is continuous on $(0,\infty)$, so its limsup as $h\to0^+$ is the supremum over $h\in(0,1/k)\cap\QQ$ for $k$ large, and
$$
D^+f(x)=\lim_{k\to\infty}\ \sup_{h\in(0,1/k)\cap\QQ}\frac{f(x+h)-f(x)}{h}.
$$
Each inner supremum is taken over a countable set of measurable functions of $x$, hence is measurable, and a limit of measurable functions is measurable. The same argument with $\inf$ gives $D_+$, and with $h<0$ gives the left-hand derivates.

:::

:::

::: {.pf-step #part-b}
If $f$ is continuous, the set of points at which $f$ is differentiable is measurable.

::: pf-proof
$f$ is differentiable at $x$ iff the four derivates are equal and finite there, because the two-sided limit of the difference quotient exists in $\RR$ exactly then. So
$$
\theset{x\mid f'(x)\text{ exists}}=\bigl(D^+f=D^-f=D_+f=D_-f\bigr)\cap\theset{x\mid \abs{D^+f(x)}<\infty},
$$
an intersection of finitely many measurable sets, each of the form $\theset{x\mid u(x)=v(x)}$ or $\theset{x\mid u(x)<\infty}$ for the measurable functions of step [](#derivates){.pf-ref}. Such a set is measurable.

:::

:::

:::
:::
