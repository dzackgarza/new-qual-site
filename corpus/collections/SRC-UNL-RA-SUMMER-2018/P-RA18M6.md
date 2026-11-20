---
schema: qual/card@1
id: P-RA18M6
kind: problem
title: Uniform convergence on compacta of the translates $f(x+1/n)$, and failure on all of $\RR$
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Continuity
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Six steps asserted their claim with no justification and each now carries one: uniform continuity on the
    enlarged interval from compactness, the $\varepsilon$--$\delta$ reading of it, the uniformity in $x$
    that gives uniform convergence on $[a,b]$, the continuity of $\sin(x^2)$, the failure of uniform
    continuity of $\sin(x^2)$ from its unbounded derivative, and the implication from uniform convergence
    of the shifts to uniform continuity of the limit. That last implication replaces the card's earlier
    part (b) argument, which rested on an unproved claim that a certain sequence of phases is dense modulo
    $2\pi$; the example $\sin(x^2)$ is kept and the argument is now the standard one. Three structural
    repairs: the "Goal" paragraph restating the problem is gone, one step had become a stray empty
    $pf$-step wrapping another, and a parenthetical paragraph sat inside the proof root, which holds only
    steps, so it now follows the root inside the solution. Sources are cited by numbered statement: a
    continuous function on a compact metric space is uniformly continuous, and uniform continuity of a
    differentiable function forces a bounded derivative. No page reference is written in the body of this
    card or in the event above. The statement is unchanged. The collection retains the UNL real analysis
    summer 2018 qualifying exam and no solution sheet.
---

::: {.problem}
Let $f:\RR\to\RR$ be a continuous function, and for all $n\ge 1$ put $f_n(x)=f\left(x+\frac1n\right)$.

(a) Show that $f_n$ converges uniformly, as $n\to\infty$, over any closed interval $[a,b]$.

(b) Give an example of a continuous function $f$ for which the convergence is not uniform on $\RR$.
:::

:::: {.solution}

::: pf

::: pf-step

(a) $f_n \to f$ uniformly on $[a,b]$.

::: pf-proof


::: {.pf-step #s1-1}
$f$ is uniformly continuous on the enlarged interval $[a-1, b+1]$, and for $x \in [a,b]$ and $n \ge 1$ both $x$ and $x + 1/n$ lie in that interval.


::: pf-proof
The interval $[a-1,b+1]$ is closed and bounded, hence compact, and $f$ is continuous on it; a continuous function on a compact metric space is uniformly continuous. For $x \in [a,b]$ and $n \ge 1$ one has $x \ge a > a-1$ and $x + 1/n \le b+1$, so both points lie in the interval.
:::

:::


::: {.pf-step #s1-2}

For every $\varepsilon > 0$ there is $\delta > 0$ such that $u, v \in [a-1, b+1]$ and $\abs{u - v} < \delta$ imply $\abs{f(u) - f(v)} < \varepsilon$.


::: pf-proof
This is the definition of uniform continuity on the interval read out: for each $\varepsilon > 0$ there is a single $\delta > 0$ that works at all pairs of points of $[a-1,b+1]$ at distance less than $\delta$, with no dependence on the location of the pair.
:::

:::

::: {.pf-step #s1-3}

$f_n \to f$ uniformly on $[a,b]$.


::: pf-proof
Let $\varepsilon > 0$, take $\delta$ from the previous step and $N$ with $1/N < \delta$. For $n \ge N$ and $x \in [a,b]$ both $x$ and $x + 1/n$ lie in $[a-1,b+1]$ by the first step, and $\abs{(x + 1/n) - x} = 1/n \le 1/N < \delta$, so $\abs{f_n(x) - f(x)} < \varepsilon$. Since $N$ works for every $x$ in the interval at once, the suprema of $\abs{f_n - f}$ over $[a,b]$ tend to $0$, which is uniform convergence there.
:::

:::

:::

:::

::: pf-step

(b) Example: $f(x) = \sin(x^2)$; the convergence is not uniform on $\RR$.

::: pf-proof

::: {.pf-step #s2-1}

$f(x) = \sin(x^2)$ is continuous on $\RR$.


::: pf-proof
$\sin(x^2)$ is the composite of $x \mapsto x^2$ and $\sin$, both continuous on $\RR$, and a composite of continuous maps is continuous.
:::

:::

::: {.pf-step #s2-2}

$f$ is not uniformly continuous on $\RR$.


::: pf-proof
Suppose $f$ were uniformly continuous. Its derivative is $f'(x) = 2x\cos(x^2)$, which is unbounded: at $x_k = \sqrt{2\pi k}$ one has $\cos(x_k^2) = \cos(2\pi k) = 1$ and $f'(x_k) = 2\sqrt{2\pi k} \to \infty$. For a differentiable function uniform continuity forces a bounded derivative, since taking $h$ with $\abs{h} < \delta$ in the difference quotient gives $\abs{f'(x)}\abs{h} \le \abs{f(x+h)-f(x)} + o(h) < \varepsilon$ uniformly in $x$; so $f$ is not uniformly continuous.
:::

:::

::: {.pf-step #s2-3}

The sequence $f_n$ does not converge uniformly to $f$ on $\RR$.


::: pf-proof
If $f_n \to f$ uniformly on $\RR$, then for $\varepsilon > 0$ there is $n$ with $\abs{f(t + 1/n) - f(t)} < \varepsilon/3$ for every $t$. Given $u, v$ with $\abs{u - v} < 1/n$, all of $u$, $v$, $u + 1/n$ and $v + 1/n$ lie in an interval of length $2/n$, on which $f$ is uniformly continuous, so $\abs{f(u+1/n) - f(v+1/n)} < \varepsilon/3$ once $\abs{u-v}$ is small enough; then $\abs{f(u) - f(v)}$ is at most the sum of three such terms, hence less than $\varepsilon$. That would make $f$ uniformly continuous on $\RR$, contradicting the previous step; so the convergence is not uniform.
:::

:::

:::

:::

:::

(The mechanism: $f$ is not uniformly continuous on $\RR$ — its derivative $2x\cos(x^2)$ is unbounded — so the fixed shift $1/n$ produces $O(1)$-sized differences far out.)
:::
