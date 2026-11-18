---
schema: qual/card@1
id: P-C2GOF
kind: problem
title: Continuity of a composition $g\circ f$ at a point
classification:
  areas:
  - prelim
  topics:
  - Continuity
  - Functions and Relations
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's definition and composition proof into numbered steps; the choice of eta
    from g and of delta from f is unchanged. Checked: that b = f(a) is the point at which g is
    used, and the nesting of the two epsilons. Not checked against a printed source: the UGA
    preliminary examinations are not retained in tmp/sources and the card records no page.
---

::: {.problem}
For a function $f: \RR \to \RR$, give the definition of continuity of $f$ at a point $a$.
For functions $f$ and $g$ from $\RR$ to $\RR$, prove that if $f$ is continuous at $a$ and $g$ is continuous at $b = f(a)$, then $g \circ f$ is continuous at $a$.
[The composition $g \circ f$ is defined by $(g \circ f)(x) = g(f(x))$ for $x \in \RR$.]
:::

::: {.solution}

The argument is the card's own: no solution set for this examination is retained in `tmp/sources`, so nothing below is transcribed, and the card's existing solution is restructured into numbered steps. Here $f,g:\RR\to\RR$, $a\in\RR$ and $b=f(a)$; $(g\circ f)(x)=g(f(x))$.

::: pf

::: {.pf-step #def}

The definition: $f$ is continuous at $a$ when for every $\varepsilon>0$ there is $\delta>0$ with $\abs{x-a}<\delta\Rightarrow\abs{f(x)-f(a)}<\varepsilon$.

::: pf-proof

This is the $\varepsilon$-$\delta$ definition of continuity at a point.

:::

:::

::: {.pf-step #eta}

For $\varepsilon>0$ there is $\eta>0$ with $\abs{y-b}<\eta\Rightarrow\abs{g(y)-g(b)}<\varepsilon$.

::: pf-proof

Step [](#def){.pf-ref} applied to $g$ at $b=f(a)$, which is continuous at $b$ by hypothesis.

:::

:::

::: {.pf-step #delta}

There is $\delta>0$ with $\abs{x-a}<\delta\Rightarrow\abs{f(x)-f(a)}<\eta$.

::: pf-proof

Step [](#def){.pf-ref} applied to $f$ at $a$ with the positive number $\eta$ of step [](#eta){.pf-ref}.

:::

:::

::: {.pf-step #comp}

$\abs{x-a}<\delta$ implies $\abs{(g\circ f)(x)-(g\circ f)(a)}<\varepsilon$.

::: pf-proof

By step [](#delta){.pf-ref}, $\abs{f(x)-f(a)}<\eta$, and $f(a)=b$, so step [](#eta){.pf-ref} applies with $y=f(x)$: $\abs{g(f(x))-g(f(a))}<\varepsilon$.

:::

:::

::: {.pf-step #done}

$g\circ f$ is continuous at $a$.

::: pf-proof

Steps [](#eta){.pf-ref} to [](#comp){.pf-ref} produce for every $\varepsilon>0$ a $\delta>0$ as step [](#def){.pf-ref} requires.

:::

:::

:::

:::
