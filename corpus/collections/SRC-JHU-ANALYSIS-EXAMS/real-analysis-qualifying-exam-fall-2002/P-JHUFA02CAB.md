---
schema: qual/card@1
id: P-JHUFA02CAB
kind: problem
title: Monotone convergence for an increasing sequence with bounded integrals
classification:
  areas:
  - real-analysis
  topics:
  - Monotone Convergence
  - Interchange of Limits
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 2 of the preserved JHU Fall 2002 Real Analysis qualifying exam packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Added the two points the prose used
    silently: that the subtraction int f_n - int f_1 is legitimate because both integrals are finite,
    the hypothesis giving int f_1 <= M as well; and that a nonnegative function with finite integral
    is finite almost everywhere, which is what turns the finiteness of int g into the pointwise
    finiteness of the limit. The final identification of int f with int f_1 + int g is now a step
    using f = f_1 + g almost everywhere. Not checked: the printed exam page, which was not re-read in
    this pass.
---

::: {.problem}
Let $f_1(x)\le f_2(x)\le\cdots\le f_n(x)\le\cdots$ on a set $A$, where the functions $f_n$ are integrable and $\int_A f_n(x)\,dx\le M$ for some constant $M$.
Show that the limit
$$
f(x)=\lim_{n\to\infty}f_n(x)
$$
exists and is finite almost everywhere on $A$, and that
$$
\lim_{n\to\infty}\int_A f_n(x)\,dx=\int_A f(x)\,dx.
$$
:::

::: {.solution}
This is a problem of the JHU real-analysis qualifying examination of Fall 2002, as printed in the retained compilation (`SRC-JHU-ANALYSIS-EXAMS`). No published solution set is transcribed: the argument is the card's own, and it is the standard reduction to monotone convergence.

::: pf

::: {.pf-step #normalise}
With $g_{n}=f_{n}-f_{1}$ the sequence $(g_{n})$ is nonnegative, increasing, measurable, and $\int_{A}g_{n}\leq M-\int_{A}f_{1}<\infty$ for every $n$.

::: pf-proof
$g_{n}\geq0$ because $f_{n}\geq f_{1}$ by hypothesis, and $g_{1}=0$. It is increasing because $f_{n}$ is, and measurable as a difference of integrable, hence measurable, functions. Finally $\int_{A}g_{n}=\int_{A}f_{n}-\int_{A}f_{1}\leq M-\int_{A}f_{1}$, the subtraction being legitimate because both integrals are finite, and the right side is finite because $\int_{A}f_{1}\leq M$ as well.
:::
:::

::: {.pf-step #limit}
$g=\lim_{n}g_{n}$ exists in $[0,\infty]$ and $\int_{A}g=\lim_{n}\int_{A}g_{n}\leq M-\int_{A}f_{1}$.

::: pf-proof
An increasing sequence in $[0,\infty]$ has a limit in $[0,\infty]$, namely its supremum, and $g$ is measurable as a limit of measurable functions. Since the $g_{n}$ are nonnegative, increasing and measurable, the monotone convergence theorem gives $\int_{A}g=\lim_{n}\int_{A}g_{n}$, and this limit is at most $M-\int_{A}f_{1}$ by step [](#normalise){.pf-ref}.
:::
:::

::: {.pf-step #finite}
$g<\infty$ almost everywhere on $A$, so $f=\lim_{n}f_{n}=f_{1}+g$ exists and is finite almost everywhere.

::: pf-proof
$\int_{A}g\leq M-\int_{A}f_{1}<\infty$, and a nonnegative function with finite integral is finite almost everywhere: if $g=+\infty$ on a set of positive measure, the integral would be infinite. On the complement, $f_{n}=f_{1}+g_{n}\to f_{1}+g$ with both terms finite, so the limit exists there and equals $f_{1}+g$.
:::
:::

::: {.pf-step #integrals}
$\lim_{n}\int_{A}f_{n}=\int_{A}f$.

::: pf-proof
$\int_{A}f_{n}=\int_{A}f_{1}+\int_{A}g_{n}$ for every $n$, and $\int_{A}g_{n}\to\int_{A}g$ by step [](#limit){.pf-ref}, so the limit of the left sides is $\int_{A}f_{1}+\int_{A}g$. On the other hand $\int_{A}f=\int_{A}(f_{1}+g)=\int_{A}f_{1}+\int_{A}g$, since $f=f_{1}+g$ almost everywhere and $f_{1}$ is integrable. So the two sides agree.
:::
:::
:::

:::
