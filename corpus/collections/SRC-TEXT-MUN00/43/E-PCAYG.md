---
schema: qual/card@1
id: E-PCAYG
kind: problem
title: Banach fixed point theorem for contractions of complete metric spaces
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: gpt-6.1-sol
  date: 2026-10-31
  note: 'The printed fixed-point claim needs X nonempty; the empty metric space is complete and has no fixed point.'
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §43 Exercise 5 (printed p. 270) was located in any set searched; the search
    is recorded in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00, and the proof on the card is
    checked line by line against the book. Checked against Munkres, Topology (2000), §43 Exercise 5,
    printed p. 270, with the definition of a contraction stated in the exercise, the definition of
    completeness in §43, the triangle inequality, and the convergence of the geometric series in R
    (Theorem 43.2 for the completeness of R). The steps are the standard ones: d(x_{n+1},x_n) <=
    alpha^n d(x_1,x_0) by induction on the contraction inequality, the triangle inequality bounds
    d(x_m,x_n) for m > n by c alpha^n/(1-alpha), completeness gives the limit x, continuity of the
    Lipschitz map f gives f(x) = x, and uniqueness follows from d(x,y) <= alpha d(x,y) with alpha < 1.
    The hypothesis "nonempty" retained in the statement is the repair recorded in the source-corrected
    event above: without it the theorem is false at the empty metric space, which is complete and
    carries the unique map, and that map has no fixed point.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout for a published solution of this exercise and found none
    (issue #144). Math StackExchange through the API, site math: the queries "contraction
    mapping theorem", "Banach fixed point", "Banach fixed point theorem complete", "contraction
    mapping principle proof", "contraction mapping theorem complete metric space unique fixed
    point proof" and "Picard iteration contraction fixed point" return questions 916717, 2208010,
    3106473, 3634815, 1404632 and 3137955; none proves the theorem, the ones that use it taking it
    as known, and 3137955 is the exercise of §28 on a compact space that this card compares with,
    not this one. dbFin has no chapter-7 page (404, checked 2026-11-15), and no GitHub Munkres
    repository named in the COMPLAINTS.md entry for §30--§36 reaches Chapter 7. The card keeps its
    own proof, which this pass did not re-read; the search is recorded in the COMPLAINTS.md entry
    for §43--§50 with every query.

- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). The AoPS blog post by cinnamon_e, "Topology by
    Munkres Chapter 6 + 7 | Day 15" (2025-09-08,
    https://artofproblemsolving.com/community/c3401823h3645909, text at
    tmp/sources/aops-shooting-star-munkres-ch6-7-day15.md), answers this exercise, at its item 5 of
    §43. The text is held, but the formulas are not: the extraction drops every inline formula, so
    the answer reads as the words between blanks and cannot be transcribed or checked. It is
    recorded here and in the COMPLAINTS.md entry for §43--§50 as located with its formulas
    unreadable, the site answering an automated request with a Cloudflare human check, which is not
    worked around. The card keeps its own proof.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked the geometric decay of the successive distances
    by induction, the Cauchy estimate with the geometric tail bounded by alpha^n/(1-alpha),
    convergence by completeness, continuity of f from the Lipschitz bound, the fixed point
    identity, and uniqueness from (1-alpha)d(x,y) <= 0. The argument is the card's own; no
    retained set is cited on it. No repair needed to the statement.
---

::: {.exercise}

If $(X, d)$ is a metric space, recall that a map $f: X \to X$ is called a contraction if there is a number $\alpha < 1$ such that

$$
d(f(x), f(y)) \leq \alpha \, d(x, y)
$$

for all $x, y \in X$.
Show that if $f$ is a contraction of a nonempty complete metric space, then there is a unique point $x \in X$ such that $f(x) = x$.
Compare [[E-70TGS]].
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on it. This is the Banach fixed point theorem, Munkres §43, and the card records the comparison with [[E-70TGS]], where compactness replaces completeness and the map need only be shrinking.

::: pf

::: {.pf-step #geometric}
With $x_{0}\in X$ arbitrary and $x_{n+1}=f(x_{n})$, one has $d(x_{n+1},x_{n})\le\alpha^{n}c$ for all $n\ge0$, where $c=d(x_{1},x_{0})$.

::: pf-proof
For $n=0$ this reads $d(x_{1},x_{0})\le c$, an equality. If it holds for $n$, then $d(x_{n+2},x_{n+1})=d\big(f(x_{n+1}),f(x_{n})\big)\le\alpha\,d(x_{n+1},x_{n})\le\alpha^{n+1}c$; so it holds for all $n$ by induction.
:::

:::

::: {.pf-step #cauchy}
$(x_{n})$ is Cauchy.

::: pf-proof
For $m>n$, the triangle inequality and step [](#geometric){.pf-ref} give
$$
d(x_{m},x_{n})\le\sum_{k=n}^{m-1}d(x_{k+1},x_{k})\le c\sum_{k=n}^{m-1}\alpha^{k}\le\frac{c\,\alpha^{n}}{1-\alpha},
$$
the last because the geometric tail is bounded by $\alpha^{n}/(1-\alpha)$ when $0\le\alpha<1$. The bound tends to $0$ as $n\to\infty$, so for every $\varepsilon>0$ there is $N$ with $d(x_{m},x_{n})<\varepsilon$ for all $m>n\ge N$.
:::

:::

::: {.pf-step #limit}
$(x_{n})$ converges, say to $x$, and $f$ is continuous.

::: pf-proof
$X$ is complete and $(x_{n})$ is Cauchy, so $x_{n}\to x$ for some $x\in X$. The contraction inequality gives $d\big(f(u),f(v)\big)\le\alpha d(u,v)\le d(u,v)$ for all $u,v$, so $f$ is Lipschitz with constant $\alpha$ and in particular continuous.
:::

:::

::: {.pf-step #fixed}
$f(x)=x$.

::: pf-proof
By continuity of $f$ and step [](#limit){.pf-ref},
$$
f(x)=f\Big(\lim_{n}x_{n}\Big)=\lim_{n}f(x_{n})=\lim_{n}x_{n+1}=x .
$$
:::

:::

::: {.pf-step #unique}
The fixed point is unique.

::: pf-proof
If $f(x)=x$ and $f(y)=y$ then $d(x,y)=d\big(f(x),f(y)\big)\le\alpha\,d(x,y)$, so $(1-\alpha)d(x,y)\le0$; since $1-\alpha>0$ and $d(x,y)\ge0$, this gives $d(x,y)=0$ and hence $x=y$.
:::

:::

::: {.pf-step}
A contraction of a nonempty complete metric space has exactly one fixed point.

::: pf-proof
Steps [](#cauchy){.pf-ref}, [](#limit){.pf-ref} and [](#fixed){.pf-ref} produce a fixed point, and step [](#unique){.pf-ref} shows it is the only one.
:::

:::

:::
:::
