---
schema: qual/card@1
id: P-KVE3S
kind: problem
title: $C^1([a,b])$ is Banach under $\sup\abs{f}+\sup\abs{f'}$
classification:
  areas: [real-analysis]
  topics:
    - Banach Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against the UGA Spring 2017 real-analysis qualifying exam recorded by SRC-UGA-RA-SPRING-2017.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against the retained exam assets/attachments/Real_Analysis_Spring_2017.docx, whose
    problem set asks for C^1([a,b]) to be shown a Banach space in the norm given; the card's
    statement is that problem with the norm written out. The retained file is the Word
    document the collection lists as its provenance.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured the card's own argument into numbered steps; no retained solution set for
    this exam covers it. Two things the prose leaves implicit are now steps: that the
    displayed expression is a norm on C^1([a,b]) at all (the suprema are finite and
    attained for continuous functions on a compact interval, and the axioms are checked),
    and that the limit passage in the Fundamental Theorem of Calculus identity is justified
    by uniform convergence of the derivatives, with the bound on the integral difference
    written out.
---

::: {.problem}
Show that the space $C^1([a,b])$ is a Banach space when equipped with the norm
$$\norm{f}:=\sup_{x\in[a,b]}\abs{f(x)}+\sup_{x\in[a,b]}\abs{f'(x)}.$$
:::

::: {.solution}

The problem is the one recorded for the UGA Spring 2017 real-analysis qualifying exam, whose
retained source is `assets/attachments/Real_Analysis_Spring_2017.docx`. No retained solution
set covers it; the argument below is the card's own, restructured as numbered steps.

Write $\norm{f}_{\infty}=\sup_{[a,b]}\abs{f}$ and $\norm{f}=\norm{f}_{\infty}
+\norm{f'}_{\infty}$ for $f\in C^{1}([a,b])$, and let $C([a,b])$ carry the supremum norm,
under which it is complete.

::: pf

::: {.pf-step #norm}

$\norm{\cdot}$ is a norm on $C^{1}([a,b])$.

::: pf-proof

For $f\in C^{1}([a,b])$ both $f$ and $f'$ are continuous on the compact interval, so
$\abs{f}$ and $\abs{f'}$ are bounded and the two suprema are finite real numbers; hence
$\norm{f}$ is a nonnegative real. It is $0$ only for $f=0$, since $\norm{f}=0$ forces
$\norm{f}_{\infty}=0$. Homogeneity and the triangle inequality hold because both suprema have
them: $\norm{cf}_{\infty}=\abs{c}\norm{f}_{\infty}$ and
$\norm{f+g}_{\infty}\le\norm{f}_{\infty}+\norm{g}_{\infty}$, and likewise for the derivatives.

:::

:::

::: {.pf-step #cauchy}

If $(f_{n})$ is Cauchy in $\norm{\cdot}$, then $(f_{n})$ and $(f_{n}')$ are Cauchy in
$\norm{\cdot}_{\infty}$.

::: pf-proof

$\norm{f_{n}-f_{m}}_{\infty}\le\norm{f_{n}-f_{m}}$ and
$\norm{f_{n}'-f_{m}'}_{\infty}\le\norm{f_{n}-f_{m}}$ because both terms of the sum are
nonnegative. So for $\varepsilon>0$, indices beyond the Cauchy threshold satisfy both bounds.

:::

:::

::: {.pf-step #limits}

There are $f,g\in C([a,b])$ with $f_{n}\to f$ and $f_{n}'\to g$ uniformly on $[a,b]$.

::: pf-proof

By step [](#cauchy){.pf-ref} both sequences are Cauchy in the supremum norm, and $C([a,b])$
with that norm is complete, so each converges uniformly to a continuous limit.

:::

:::

::: {.pf-step #ftc}

$f(x)-f(a)=\int_{a}^{x}g(t)\,dt$ for every $x\in[a,b]$.

::: pf-proof

Fix $x$. For each $n$, the Fundamental Theorem of Calculus gives
$f_{n}(x)-f_{n}(a)=\int_{a}^{x}f_{n}'(t)\,dt$. The left side tends to $f(x)-f(a)$ by step
[](#limits){.pf-ref}. For the right side,
$\abs{\int_{a}^{x}f_{n}'-\int_{a}^{x}g}\le\abs{x-a}\norm{f_{n}'-g}_{\infty}\to0$, so the
integrals converge to $\int_{a}^{x}g$.

:::

:::

::: {.pf-step #derivative}

$f\in C^{1}([a,b])$ and $f'=g$.

::: pf-proof

By step [](#ftc){.pf-ref}, $f(x)=f(a)+\int_{a}^{x}g$ for all $x$, and $g$ is continuous by
step [](#limits){.pf-ref}. The Fundamental Theorem of Calculus then says that
$x\mapsto\int_{a}^{x}g$ is differentiable with derivative $g$; so $f$ is differentiable with
$f'=g$, and $f'$ is continuous.

:::

:::

::: {.pf-step #convergence}

$\norm{f_{n}-f}\to0$.

::: pf-proof

By steps [](#limits){.pf-ref} and [](#derivative){.pf-ref},
$\norm{f_{n}-f}=\norm{f_{n}-f}_{\infty}+\norm{f_{n}'-g}_{\infty}$, and both terms tend to $0$
by uniform convergence.

:::

:::

::: {.pf-step #banach}

$C^{1}([a,b])$ is complete in $\norm{\cdot}$.

::: pf-proof

An arbitrary Cauchy sequence converges by steps [](#cauchy){.pf-ref} to
[](#convergence){.pf-ref}, with limit $f\in C^{1}([a,b])$ by step [](#derivative){.pf-ref}.
A normed space in which every Cauchy sequence converges is a Banach space.

:::

:::

:::

:::
