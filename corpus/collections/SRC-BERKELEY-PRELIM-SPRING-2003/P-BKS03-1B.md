---
schema: qual/card@1
id: P-BKS03-1B
kind: problem
title: Measure-preserving bijections between half-spaces
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the retained sheet's argument (Spring 2003
    prelim solutions, Problem 1B, PDF p. 4, the file named in the collection's provenance),
    which the card now cites; it previously carried no citation. One repair: the sheet asserts
    that measure preservation gives |J(f)| = 1 *everywhere*, which is a two-step claim - the
    change-of-variables formula gives it almost everywhere, and continuity of J(f) together
    with connectedness of R^n upgrades it to one of the two constants everywhere; the card
    proves both steps. Added: the mean-value step f(x) = c +- x, the explicit inverse
    (u,v) -> (uv, log v), and the computation of det J(Phi) = 1. Statement unchanged.
---

::: {.problem}

(a) Prove there is no continuously differentiable measure-preserving bijection $f:\RR\to\RR_{>0}$.

(b) Find a continuously differentiable measure-preserving bijection
$$
f:\RR^2\to\RR\times\RR_{>0}.
$$
:::

::: {.solution}
The published solution is the collection's own retained sheet, **Spring 2003 prelim solutions, Problem 1B, PDF p. 4** (`assets/attachments/s03solution.pdf`, the file named in this collection's `provenance`): the reduction to $\abs{J(f)}=1$, the conclusion $f(x)=c\pm x$, and the example $(x,y)\mapsto(e^{-y}x,e^y)$ are that solution's. The card supplies what the sheet leaves implicit — that the Jacobian condition holds *everywhere* and not merely almost everywhere, and the verification that the example is a bijection with Jacobian $1$ — and it treats the two parts in the order of the printed problem.

Throughout, a map is measure preserving when $m(f^{-1}E)=m(E)$ for every measurable $E$ for which the left side is defined, $J(f)$ is the Jacobian determinant, and $\RR_{>0}=(0,\infty)$.

::: pf

::: {.pf-step #jacobian}
If $f:\RR^n\to\RR^n$ is $C^1$ and measure preserving, then $\abs{J(f)}=1$ everywhere.

::: pf-proof
If $f$ is injective and $C^1$, the change-of-variables formula gives $\int_{f(U)}\abs{J(f)}=\int_U1$ for every open set $U$ on which $f$ is injective; with $f$ measure preserving and bijective, $m(f(U))=m(U)$, so $\int_U(\abs{J(f)}-1)=0$ for every such $U$, hence $\abs{J(f)}=1$ almost everywhere. Since $f$ is $C^1$, $J(f)$ is continuous, and a continuous function equal to $\pm1$ almost everywhere equals $\pm1$ everywhere: the set where $\abs{J}=1$ is closed and dense, hence all of $\RR^n$. Finally $\RR^n$ is connected and $J(f)$ is continuous and never zero, so it takes one of the two values identically.

:::

:::

::: {.pf-step #part-a}
There is no $C^1$ measure-preserving bijection $f:\RR\to\RR_{>0}$.

::: pf-proof
Suppose $f$ is one. By step [](#jacobian){.pf-ref} with $n=1$, $f'=1$ identically or $f'=-1$ identically; so $f(x)=c+x$ or $f(x)=c-x$ for a constant $c$, by the mean value theorem. Neither maps $\RR$ into $\RR_{>0}$: $c+x$ is negative for $x<-c$, and $c-x$ is negative for $x>c$. Contradiction.

:::

:::

::: {.pf-step #part-b-bijection}
The map $\Phi(x,y)=(e^{-y}x,\ e^{y})$ is a $C^1$ bijection $\RR^2\to\RR\times\RR_{>0}$ with $C^1$ inverse.

::: pf-proof
The second coordinate $e^y$ is positive, so the image lies in $\RR\times\RR_{>0}$. The map $\Psi(u,v)=(uv,\ \log v)$, defined for $v>0$, is $C^1$, and
$$
\Phi\Psi(u,v)=\bigl(e^{-\log v}uv,\ e^{\log v}\bigr)=(u,v),\qquad \Psi\Phi(x,y)=\bigl(e^{-y}x\,e^{y},\ \log e^{y}\bigr)=(x,y),
$$
so $\Phi$ and $\Psi$ are mutually inverse bijections.

:::

:::

::: {.pf-step #part-b-jacobian}
$\det J(\Phi)=1$ everywhere, so $\Phi$ is measure preserving.

::: pf-proof
$$
J(\Phi)=\begin{pmatrix}\partial_x(e^{-y}x)&\partial_y(e^{-y}x)\\ \partial_x(e^{y})&\partial_y(e^{y})\end{pmatrix}=\begin{pmatrix}e^{-y}&-e^{-y}x\\0&e^{y}\end{pmatrix},
$$
whose determinant is $e^{-y}e^{y}-0=1$. A $C^1$ bijection whose Jacobian has absolute value $1$ everywhere preserves measure, by the change-of-variables formula applied to $\Phi$ and to its inverse $\Psi$.

:::

:::

::: {.pf-step #part-b}
There is a $C^1$ measure-preserving bijection $f:\RR^2\to\RR\times\RR_{>0}$.

::: pf-proof
Take $f=\Phi$ of steps [](#part-b-bijection){.pf-ref} and [](#part-b-jacobian){.pf-ref}.

:::

:::

:::
:::
