---
schema: qual/card@1
id: P-CH37V
kind: problem
title: Equidistribution of $n\alpha\bmod 1$ for continuous functions and for interval
  indicators
classification:
  areas:
  - real-analysis
  topics:
  - Density
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the argument already on the card, whose two routes
    (trigonometric polynomials plus Stone--Weierstrass, and a continuous sandwich for an
    interval) are correct. Added: the geometric-sum bound |A_N(e_k)| <= 2/(N|1-q|) with the
    check that q != 1 by irrationality of alpha; the evaluation of I(e_k); the description of
    the approximating subalgebra that the complex Stone--Weierstrass theorem needs (conjugation-
    closed via e_k-bar = e_{-k}, separating through e_1); and in (b) the three cases of the
    sandwich construction, including the single-point and full-torus cases the card only
    parenthesised, together with the point that the tents are continuous on the torus. The
    card's `\square` markers are gone, as the filter prints QED. Not claimed: a retained
    solution set; the collection's provenance is the examination paper only.
---

::: {.problem}
Let $\RR/\ZZ$ denote the torus (whose elements we write as cosets) and fix an irrational $\alpha>0$.

(a) Show that $$\lim_{N\to\infty} \frac{1}{N}\sum_{n=0}^{N-1} f(n\alpha+\ZZ) = \int_0^1 f(x+\ZZ)\,dx$$ for all continuous functions $f:\RR/\ZZ\to\RR$.

(b) Show that the conclusion is also true when $f$ is the characteristic function of a closed interval.
:::

::: {.solution}
Throughout $\TT \coloneqq \RR/\ZZ$ is the torus, $\alpha > 0$ is irrational, $e_{k}(x + \ZZ) \coloneqq e^{2\pi i k x}$ for $k \in \ZZ$, $A_{N}(f) \coloneqq \frac{1}{N}\sum_{n=0}^{N-1}f(n\alpha + \ZZ)$ and $I(f) \coloneqq \int_{0}^{1}f(x + \ZZ)\,dx$; a trigonometric polynomial is a finite sum $\sum_{k}c_{k}e_{k}$ with complex coefficients. The collection's `provenance` is the Fall 2010 examination paper, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #characters}
For every $k \in \ZZ$ one has $A_{N}(e_{k}) \to I(e_{k})$ as $N \to \infty$.

::: pf-proof
For $k = 0$ the function $e_{0} \equiv 1$, so $A_{N}(e_{0}) = \frac{1}{N}\sum_{n}1 = 1$ and $I(e_{0}) = \int_{0}^{1}1\\,dx = 1$, and the two agree for every $N$. For $k \ne 0$ put $q \coloneqq e^{2\pi i k\alpha}$; then $q \ne 1$, because $q = 1$ would give $k\alpha \in \ZZ$ with $k \ne 0$, contradicting the irrationality of $\alpha$. So $A_{N}(e_{k}) = \frac{1}{N}\sum_{n=0}^{N-1}q^{n} = \frac{1}{N}\cdot\frac{1 - q^{N}}{1 - q}$, whose modulus is at most $\frac{2}{N\abs{1-q}}$ and hence tends to $0$; and $I(e_{k}) = \int_{0}^{1}e^{2\pi i k x}dx = \frac{e^{2\pi i k} - 1}{2\pi i k} = 0$.

:::

:::

::: {.pf-step #polynomial}
For every trigonometric polynomial $P$ one has $A_{N}(P) \to I(P)$.

::: pf-proof
Both $A_{N}$ and $I$ are linear in $f$, so it suffices to treat $P = \sum_{k=c}^{d}c_{k}e_{k}$: $A_{N}(P) - I(P) = \sum_{k}c_{k}\bigl(A_{N}(e_{k}) - I(e_{k})\bigr)$, a finite sum whose every term tends to $0$ by step [](#characters){.pf-ref}. A finite sum of sequences tending to $0$ tends to $0$.

:::

:::

::: {.pf-step #dense}
For every $f \in C(\TT)$ and every $\varepsilon > 0$ there is a trigonometric polynomial $P$ with $\norm{f - P}_{\infty} < \varepsilon$.

::: pf-proof
The trigonometric polynomials form a subalgebra of the complex-valued continuous functions on the compact space $\TT$ that contains the constants, is closed under complex conjugation because $\overline{e_{k}} = e_{-k}$, and separates points: $e_{1}$ takes distinct values at distinct points of $\TT$. The complex Stone--Weierstrass theorem therefore makes it dense in $C(\TT)$ with the supremum norm, which is the assertion.

:::

:::

::: {.pf-step #part-a}
(a) $A_{N}(f) \to I(f)$ for every $f \in C(\TT)$.

::: pf-proof
Given $\varepsilon > 0$ choose $P$ as in step [](#dense){.pf-ref}. Then $\abs{A_{N}(f) - A_{N}(P)} \le \frac{1}{N}\sum_{n}\abs{f - P} \le \varepsilon$ because $A_{N}$ is an average, and $\abs{I(P) - I(f)} \le \int_{0}^{1}\abs{P - f} \le \varepsilon$; hence $\abs{A_{N}(f) - I(f)} \le 2\varepsilon + \abs{A_{N}(P) - I(P)}$, so $\limsup_{N}\abs{A_{N}(f) - I(f)} \le 2\varepsilon$ by step [](#polynomial){.pf-ref}. As $\varepsilon > 0$ is arbitrary, the limsup is $0$ and the sequence converges to $I(f)$.

:::

:::

::: {.pf-step #sandwich-functions}
(b) For the characteristic function $f$ of a closed interval there are continuous $g_{k}, h_{k}$ on $\TT$ with $0 \le g_{k} \le f \le h_{k} \le 1$ at every point and $g_{k} \to f$, $h_{k} \to f$ almost everywhere.

::: pf-proof
Write the interval as the image of $[a,b]$ with $a \le b \le a+1$. If $b - a \ge 1$ then $f \equiv 1$ and $g_{k} = h_{k} \equiv 1$ serve. If $a = b$ then $f$ is the indicator of a single point and $h_{k}$ the continuous tent of height $1$ supported on $[a-1/k, a+1/k]$, with $g_{k} = 0$, serves. Otherwise $0 < b - a < 1$ and, for $k$ with $2/k < b - a$, let $g_{k}$ equal $1$ on $[a+1/k, b-1/k]$, $0$ outside $[a,b]$, and be linear on the two end intervals, and $h_{k}$ equal $1$ on $[a,b]$, $0$ outside $[a-1/k, b+1/k]$, and linear on $[a-1/k,a]$ and $[b,b+1/k]$; these are continuous on $\RR$, invariant under $x \mapsto x+1$ once read modulo $1$ on an interval of length below $1$, hence continuous on $\TT$, and they satisfy the displayed inequalities with $g_{k}(x) \to f(x)$ off the two endpoints and $h_{k}(x) \to f(x)$ everywhere.

:::

:::

::: {.pf-step #sandwich}
(b) For such $f$ one has $A_{N}(f) \to I(f)$.

::: pf-proof
Fix $k$. Since $g_{k} \le f \le h_{k}$ pointwise, averaging and integrating give $A_{N}(g_{k}) \le A_{N}(f) \le A_{N}(h_{k})$ and $I(g_{k}) \le I(f) \le I(h_{k})$ for every $N$. The functions $g_{k}, h_{k}$ are continuous, so step [](#part-a){.pf-ref} applies to them, and taking $N \to \infty$ in the first chain yields $I(g_{k}) \le \liminf_{N}A_{N}(f) \le \limsup_{N}A_{N}(f) \le I(h_{k})$. Now let $k \to \infty$: the functions $h_{k} - g_{k}$ are nonnegative, bounded by $2$, and tend to $0$ almost everywhere by step [](#sandwich-functions){.pf-ref}, so $I(h_{k}) - I(g_{k}) \to 0$ by dominated convergence, while $I(g_{k}) \to I(f)$ and $I(h_{k}) \to I(f)$. Hence $\liminf = \limsup = I(f)$.

:::

:::

::: pf-step
Both parts hold: $A_{N}(f) \to I(f)$ for every continuous $f$, and also for $f$ the characteristic function of a closed interval.

::: pf-proof
Step [](#part-a){.pf-ref} is part (a) and step [](#sandwich){.pf-ref} is part (b), whose hypotheses are supplied by step [](#sandwich-functions){.pf-ref}.

:::

:::

:::
:::
