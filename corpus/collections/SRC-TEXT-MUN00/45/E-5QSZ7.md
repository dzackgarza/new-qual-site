---
schema: qual/card@1
id: E-5QSZ7
kind: problem
title: Finite families, uniform limits, and families with bounded derivatives are equicontinuous
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §45 Exercise 2 (printed p. 280) was located; the sets searched are listed in
    the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked line by line against the book's
    definition of equicontinuity in §45 (equicontinuous at x_0 if for every eps there is a neighbourhood U
    of x_0 with d(f(x), f(x_0)) < eps for all x in U and all f in the family). Part (a) is the finite
    intersection of the finitely many neighbourhoods given by continuity. Part (b) is the standard eps/3
    argument: the uniform limit f is continuous by Theorem 21.6, the finitely many functions with index
    below N are handled by continuity at x_0 and the rest by the triangle inequality through f. Part (c)
    is the mean value theorem, a calculus fact the book does not number, applied on the interval between
    x and x_0 inside the neighbourhood on which the derivatives are bounded. What was corrected: part (c) divided by the
    bound M, which may be 0 when every function of the family is constant; the card now uses max{M,1}.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout for a published solution of this exercise and found none
    (issue #144). Math StackExchange through the API, site math, with the queries "equicontinuous
    uniformly convergent sequence", "uniform limit equicontinuous", "equicontinuity compactness
    uniform convergence" and "Arzela Ascoli theorem equicontinuous" returns questions 792534,
    1315747, 1293329 and 4435817; 792534 proves that a family that is not equicontinuous has a
    sequence x_n -> x_0 and functions f_n with |f_n(x_n) - f_n(x_0)| bounded below, which is not
    one of the three parts, and none of the others treats a finite family, a uniformly convergent
    sequence, or derivatives bounded on a neighbourhood uniformly. dbFin has no chapter-7 page
    (404, checked 2026-11-15), and no GitHub Munkres repository named in the COMPLAINTS.md entry
    for §30--§36 reaches Chapter 7. The card keeps its own proof, which this pass did not re-read;
    the search is recorded in the COMPLAINTS.md entry for §43--§50 with every query.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    The AoPS blog post by cinnamon_e, "Topology by Munkres Chapter 7 | Day 16" (2025-09-09, listed
    on the blog's topology tag page
    https://artofproblemsolving.com/community/c3401823t440f3401823_topology, text at
    tmp/sources/aops-shooting-star-munkres-ch7-day16.md), also answers this exercise, at its item 2
    of §45. The text is held, but the formulas are not: the extraction drops every inline formula,
    so the answer reads as the words between blanks and cannot be transcribed or checked. It is
    recorded here and in the COMPLAINTS.md entry for §43--§50 as located with its formulas
    unreadable, the site answering an automated request with a Cloudflare human check, which is not
    worked around.

---

::: {.exercise}

Let $(Y, d)$ be a metric space; let $\mathcal{F}$ be a subset of $\mathcal{C}(X, Y)$.

(a) Show that if $\mathcal{F}$ is finite, then $\mathcal{F}$ is equicontinuous.

(b) Show that if $f_n$ is a sequence of elements of $\mathcal{C}(X, Y)$ that converges uniformly, then the collection $\theset{f_n}$ is equicontinuous.

(c) Suppose that $\mathcal{F}$ is a collection of differentiable functions $f: \RR \to \RR$ such that each $x \in \RR$ lies in a neighborhood $U$ on which the derivatives of the functions in $\mathcal{F}$ are uniformly bounded.
[This means that there is an $M$ such that $\abs{f'(x)} \leq M$ for all $f$ in $\mathcal{F}$ and all $x \in U$.] Show that $\mathcal{F}$ is equicontinuous.
:::

::: {.solution}

::: pf

::: pf-step

Part (a): Finite collections are equicontinuous.
    *Proof:*

::: pf-proof

::: pf-step

Let $\mathcal{F} = \{f_1, \dots, f_k\}$ be finite, and let $x_0 \in X, \varepsilon > 0$.

:::

::: pf-step

For each $i \in \{1, \dots, k\}$, continuity of $f_i$ at $x_0$ guarantees an open neighborhood $U_i \subseteq X$ of $x_0$ such that $d(f_i(x), f_i(x_0)) < \varepsilon$ for all $x \in U_i$.

:::

::: pf-step

Define $U = \bigcap_{i=1}^k U_i$. As a finite intersection of open neighborhoods of $x_0$, $U$ is an open neighborhood of $x_0$.

:::

::: pf-step

For all $x \in U$ and all $f \in \mathcal{F}$, $d(f(x), f(x_0)) < \varepsilon$. Thus $\mathcal{F}$ is equicontinuous.

:::

:::

:::

::: pf-step

Part (b): Uniformly convergent sequences $\{f_n\}$ are equicontinuous.
    *Proof:*

::: pf-proof

::: pf-step

Let $f_n \to f$ uniformly on $X$, with $x_0 \in X$ and $\varepsilon > 0$. By the uniform limit theorem, $f: X \to Y$ is continuous.

:::

::: pf-step

Choose an integer $N \ge 1$ such that $d(f_n(x), f(x)) < \frac{\varepsilon}{3}$ for all $n \ge N$ and all $x \in X$.

:::

::: pf-step

By continuity of $f$ at $x_0$, choose an open neighborhood $U_0 \subseteq X$ of $x_0$ such that $d(f(x), f(x_0)) < \frac{\varepsilon}{3}$ for all $x \in U_0$.

:::

::: pf-step

For each $n \in \{1, \dots, N-1\}$, choose an open neighborhood $U_n$ of $x_0$ such that $d(f_n(x), f_n(x_0)) < \varepsilon$ for all $x \in U_n$.

:::

::: pf-step

Set $U = \bigcap_{n=0}^{N-1} U_n$, which is an open neighborhood of $x_0$.

:::

::: pf-step

For any $n < N$ and $x \in U$, $d(f_n(x), f_n(x_0)) < \varepsilon$ since $x \in U_n$.

:::

::: pf-step

For any $n \ge N$ and $x \in U$, the triangle inequality gives:
        $$d(f_n(x), f_n(x_0)) \le d(f_n(x), f(x)) + d(f(x), f(x_0)) + d(f(x_0), f_n(x_0)) < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon.$$

:::

::: pf-step

Thus $\{f_n\}_{n=1}^\infty$ is equicontinuous at $x_0$, hence equicontinuous on $X$.

:::

:::

:::

::: pf-step

Part (c): Locally uniformly bounded derivatives imply equicontinuity.
    *Proof:*

::: pf-proof

::: pf-step

Let $x_0 \in \RR$ and $\varepsilon > 0$.

:::

::: pf-step

By hypothesis, there exists an open neighborhood $U_0 \ni x_0$ and a constant $M > 0$ such that $\abs{f'(t)} \le M$ for all $f \in \mathcal{F}$ and all $t \in U_0$.

:::

::: pf-step

Replacing $M$ by $\max\{M,1\}$, which is still a bound for the derivatives on $U_0$ and is positive, choose $\delta > 0$ such that the interval $U = (x_0 - \delta, x_0 + \delta) \subseteq U_0$ and $\delta < \frac{\varepsilon}{M}$.

:::

::: pf-step

For any $x \in U$ and any $f \in \mathcal{F}$, by the Mean Value Theorem, there exists a point $c$ strictly between $x$ and $x_0$ such that:
        $$\abs{f(x) - f(x_0)} = \abs{f'(c)} \abs{x - x_0}.$$

:::

::: pf-step

Since $c \in U \subseteq U_0$, $\abs{f'(c)} \le M$.

:::

::: pf-step

Consequently, $\abs{f(x) - f(x_0)} \le M \abs{x - x_0} < M \delta < \varepsilon$.

:::

::: pf-step

Thus $\mathcal{F}$ is equicontinuous at $x_0$, and therefore on $\RR$. Q.E.D.

:::

:::

:::

:::

:::
