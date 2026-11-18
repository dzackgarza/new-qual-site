---
schema: qual/card@1
id: E-9V5EM
kind: problem
title: Powers converge pointwise but not uniformly on $[0,1]$
classification:
  areas:
  - topology
  topics:
  - Uniform Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §21 Exercise 6, printed p. 134, with the
    definitions of pointwise and uniform convergence and Theorem 21.6; the stored statement
    is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 21.6, PDF p. 25. The pointwise limit is 0 off 1
    and 1 at 1, and the convergence is not uniform: at x = epsilon^{1/N} the N-th function
    is epsilon away from the limit. One misprint in the published answer is corrected: its
    limit function names 0 only at 0 instead of on [0,1). (tmp/sources/munkres-solutions-
    positron-ch2.pdf).
---

::: {.exercise}

Define $f_n: [0,1] \to \RR$ by the equation $f_n(x) = x^n$.
Show that the sequence $(f_n(x))$ converges for each $x \in [0,1]$, but that the sequence $(f_n)$ does not converge uniformly.
:::

::: {.solution}

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 21.6, PDF p. 25** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); both halves are theirs. Their printed limit function is corrected on this card: it is $f(x)=0$ for $0\le x<1$ and $f(1)=1$, as computed in step [](#pointwise){.pf-ref}.

Let $f_{n}(x)=x^{n}$ on $[0,1]$.

::: pf

::: {.pf-step #pointwise}
$(f_{n}(x))$ converges for every $x\in[0,1]$, with limit $f(x)=0$ for $0\le x<1$ and $f(1)=1$.

::: pf-proof
$f_{n}(0)=0$ for every $n$, so the sequence converges to $0$. For $0<x<1$ one has $x^{n}\to0$, since $x^{n}$ is decreasing and bounded below by $0$ and $x^{n+1}=x\cdot x^{n}$ forces the limit $\ell$ to satisfy $\ell=x\ell$, hence $\ell=0$; alternatively $x=1/(1+h)$ with $h>0$ and $x^{n}\le1/(1+nh)\to0$ by the binomial estimate. And $f_{n}(1)=1$ for every $n$.
:::

:::

::: {.pf-step #not-uniform}
The convergence is not uniform.

::: pf-proof
Let $0<\varepsilon<1$ and let $N\ge1$. Put $x=\varepsilon^{1/N}$, which lies in $(0,1)$ because $0<\varepsilon<1$. Then $\abs{f_{N}(x)-f(x)}=\abs{x^{N}-0}=\varepsilon$, since $f(x)=0$ for $x<1$ by step [](#pointwise){.pf-ref}. So for every $N$ there is a point of $[0,1]$ at distance at least $\varepsilon$ from the limit, and the convergence is not uniform.
:::

:::

::: {.pf-step #continuity-test}
Equivalently, the limit function is not continuous, while every $f_{n}$ is.

::: pf-proof
Each $f_{n}$ is continuous. The function $f$ of step [](#pointwise){.pf-ref} satisfies $f(x)=0\to0$ as $x\to1^{-}$ while $f(1)=1$, so it is discontinuous at $1$. A uniformly convergent sequence of continuous functions has continuous limit (Theorem 21.6, printed p. 132), so the convergence cannot be uniform.
:::

:::

::: {.pf-qed}
The sequence converges pointwise by step [](#pointwise){.pf-ref} and not uniformly by steps [](#not-uniform){.pf-ref} and [](#continuity-test){.pf-ref}.
:::

:::

:::
