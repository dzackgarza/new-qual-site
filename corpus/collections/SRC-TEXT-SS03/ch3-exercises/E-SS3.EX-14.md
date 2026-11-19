---
schema: qual/card@1
id: E-SS3.EX-14
kind: problem
title: Injective entire functions are affine
classification:
  areas:
    - complex-analysis
  topics: [Entire Functions, Casorati-Weierstrass]
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-11
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into Lamport steps. No retained set covers this exercise, so the argument is the
      card's own and the card says so; the printed hint is followed exactly. Each step re-read: a
      removable singularity of g would make f bounded and hence constant by Liouville; an essential
      one would make the values of f near infinity accumulate at any chosen f(z_0), which injectivity
      and the nonvanishing of f'(z_0) forbid; and a pole at 0 is exactly the vanishing of all but
      finitely many Taylor coefficients of f. A slip of my own first draft is repaired before
      committing: the pole case was described as a finite sum of nonpositive powers of w, which is the
      wrong direction; the Laurent series of g = f(1/z) is sum a_n z^{-n}, so a pole means a_n = 0
      for large n, and the step now says that. The step that f'(z_0) = 0 contradicts injectivity is
      proved by counting the roots of c_k (z - z_0)^k = epsilon. Not claimed: any statement about
      injective meromorphic maps of the sphere.
---

::: {.exercise}
Prove that all entire functions that are also injective take the form $f(z) = az + b$ with $a, b \in \CC$ and $a \neq 0$.

[Hint: Apply the Casorati-Weierstrass theorem to $f(1/z)$.]
:::

::: {.solution}
The statement is Exercise 14 of [@SS03, ch. 3 (p. 105)], printed with its hint to apply the Casorati--Weierstrass theorem to $f(1/z)$.

The argument is the card's own; no retained solution set is cited on the card, and none was located for this exercise among the retained sets. It is checked against Stein and Shakarchi, Complex Analysis (2003), Chapter 3 Exercise 14, and follows the hint to apply Casorati--Weierstrass to $f(1/z)$.

::: pf

::: {.pf-step #g}
Let $g(z)=f(1/z)$ on the punctured plane; the singularity of $g$ at $0$ is removable, a pole, or essential.

::: pf-proof
$g$ is holomorphic on $\CC\setminus\{0\}$ because $f$ is entire and $z\mapsto1/z$ is holomorphic there, so $0$ is an isolated singularity of $g$ and the trichotomy applies.
:::

:::

::: {.pf-step #notremovable}
The singularity is not removable.

::: pf-proof
If it were, $g$ would extend holomorphically to a neighbourhood of $0$, so $f(z)=g(1/z)$ would have a finite limit as $z\to\infty$; then $f$ would be bounded outside a large disc and, being continuous, bounded on that disc as well, hence bounded on $\CC$. Liouville's theorem would make $f$ constant, contradicting injectivity.
:::

:::

::: {.pf-step #notessential}
The singularity is not essential.

:::: pf-proof

::: {.pf-step #casorati}
If it were essential, then for every $w$ and every punctured neighbourhood of $0$ the values of $g$ would meet every neighbourhood of $w$.

::: pf-proof
This is the Casorati--Weierstrass theorem: the image of a punctured neighbourhood of an essential singularity is dense in $\CC$.
:::

:::

::: {.pf-step #sequence}
There would be $\zeta_{n}\to0$ with $\zeta_{n}\ne1/z_{0}$ and $f(1/\zeta_{n})\to f(z_{0})$, for any fixed $z_{0}\ne0$.

::: pf-proof
Apply step [](#casorati){.pf-ref} with $w=f(z_{0})$ and with the punctured disc of radius $1/n$; choosing one point in each gives a sequence tending to $0$ whose values tend to $w$, and each point may be taken different from the single value $1/z_{0}$.
:::

:::

::: {.pf-step #local}
$f$ is injective on a neighbourhood of $z_{0}$ and has a continuous local inverse there, because $f'(z_{0})\ne0$.

::: pf-proof
If $f'(z_{0})=0$, the expansion $f(z)-f(z_{0})=c_{k}(z-z_{0})^{k}+\cdots$ has $k\ge2$ with $c_{k}\ne0$; then $f$ takes the value $f(z_{0})+\varepsilon$ at $k$ distinct points near $z_{0}$ for small $\varepsilon\ne0$ (the $k$ roots of $c_{k}(z-z_{0})^{k}=\varepsilon$), contradicting injectivity. So $f'(z_{0})\ne0$, and the inverse function theorem gives a holomorphic, in particular continuous, local inverse.
:::

:::

::: {.pf-step #contradiction}
This is impossible since $\abs{1/\zeta_{n}}\to\infty$.

::: pf-proof
$f(1/\zeta_{n})\to f(z_{0})$ and $f$ is continuous at $z_{0}$ with a continuous local inverse, so $1/\zeta_{n}\to z_{0}$ for the subsequence eventually inside the neighbourhood where the inverse is defined; but $\abs{1/\zeta_{n}}\to\infty$ because $\zeta_{n}\to0$. A sequence cannot converge to $z_{0}$ and diverge to infinity.
:::

:::

:::

:::

::: {.pf-step #pole}
$g$ has a pole at $0$, so $f$ is a polynomial.

::: pf-proof
By steps [](#notremovable){.pf-ref} and [](#notessential){.pf-ref} the singularity is a pole. If $f(w)=\sum_{n\ge0}a_{n}w^{n}$ is the Taylor expansion of the entire $f$ at $0$, then $g(z)=\sum_{n\ge0}a_{n}z^{-n}$ on the punctured plane. A pole at $0$ means that only finitely many terms of this Laurent series have negative degree, that is $a_{n}=0$ for all $n>N$ for some $N$: so $f(w)=\sum_{n=0}^{N}a_{n}w^{n}$ is a polynomial.
:::

:::

::: {.pf-step #degreeone}
An injective polynomial has degree $1$.

::: pf-proof
Let $f$ be a polynomial of degree $d\ge1$. If $d\ge2$ then $f'$ has degree $d-1\ge1$ and so has a complex root $z_{0}$ by the fundamental theorem of algebra; then $f'(z_{0})=0$ and the argument of step [](#local){.pf-ref} shows $f$ is not injective near $z_{0}$. Hence $d=1$, that is $f(z)=az+b$ with $a\ne0$.
:::

:::

::: {.pf-step}
Every injective entire function is affine.

::: pf-proof
Steps [](#pole){.pf-ref} and [](#degreeone){.pf-ref} give
$$
\boxed{f(z)=az+b,\quad a,b\in\CC,\ a\ne0.}
$$
Conversely every such map is entire and injective, so this is exactly the class asked for.
:::

:::

:::
:::
