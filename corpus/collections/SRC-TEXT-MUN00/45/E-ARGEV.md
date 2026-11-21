---
schema: qual/card@1
id: E-ARGEV
kind: problem
title: Pointwise bounded collections that fail equicontinuity
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §45 Exercise 4 (printed p. 280) was located; the sets searched are listed in
    the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked against Munkres, Topology (2000), §45
    Exercise 4, printed p. 280, and Exercise 9 of §21, printed p. 134, whose functions are exactly
    1/(n^3[x - 1/n]^2 + 1). Part (a): equicontinuity at every x_0 < 1 is shown by splitting the indices at
    an N with a^N, x_0^N < eps/2 on [0,a], and handling the finitely many smaller indices by continuity;
    at x_0 = 1 the functions x^n and the constant 1 separate. Part (b): the card now also verifies the
    premise of the exercise for this family, which it had only assumed. The family is pointwise bounded
    by 1, no subsequence converges uniformly because the pointwise limit is 0 while sup of f_n is
    f_n(1/n) = 1, and the failure of equicontinuity is located at 0, with equicontinuity proved at every
    other point by an explicit bound on f_n off a neighbourhood of 0 and by continuity for the finitely
    many remaining indices. The earlier version's argument for x_0 < 1 in part (a) was a sketch (it spoke
    of "finitely many small n" being uniformly continuous without producing the neighbourhood); it is now
    the explicit estimate.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). For part (a), Math StackExchange 131107 asks this
    exercise by name and has Davide Giraudo's answer 213873 (2012-10-14): the family is
    equicontinuous at each point of (-1,1), by bounding |f_n'| by n|c|^{n-1} on a compact
    subinterval, and it is not equicontinuous at 1, since otherwise some delta would give
    x^n >= 1/2 for every n and every x within delta of 1; that agrees with the card's part (a) on
    I = [0,1], where the only point at issue is 1. For part (b), the functions 1/(n^3[x-1/n]^2+1)
    of Exercise 9 of §21, neither that page nor Math StackExchange 792534 and 4435817 gives a
    published treatment, so part (b) remains the card's own. dbFin has no chapter-7 page (404,
    checked 2026-11-15), and no GitHub Munkres repository named in the COMPLAINTS.md entry for
    §30--§36 reaches Chapter 7. The card keeps its own proof, which this pass did not re-read; the
    search is recorded in the COMPLAINTS.md entry for §43--§50 with every query.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    The AoPS blog post by cinnamon_e, "Topology by Munkres Chapter 7 | Day 16" (2025-09-09, listed
    on the blog's topology tag page
    https://artofproblemsolving.com/community/c3401823t440f3401823_topology, text at
    tmp/sources/aops-shooting-star-munkres-ch7-day16.md), also answers this exercise, at its item 4
    of §45. The text is held, but the formulas are not: the extraction drops every inline formula,
    so the answer reads as the words between blanks and cannot be transcribed or checked. It is
    recorded here and in the COMPLAINTS.md entry for §43--§50 as located with its formulas
    unreadable, the site answering an automated request with a Cloudflare human check, which is not
    worked around.

- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the card's own argument. The step the earlier prose ran together
    is the one that decides the card: the split of the indices at N gives a *single* neighbourhood valid
    for the whole family, and the card now says so explicitly --- V = [0,a] intersected with the finitely
    many U_n for n < N, a finite intersection of neighbourhoods, with the tail bound a^N + x_0^N < eps
    covering every n >= N at once. The same pattern is written out for part (b), where the uniform bound
    1/(n^3c^2/4+1) on the window J replaces the crude a^n, and the failure at 0 and at 1 is shown by
    explicit epsilons. The answers are stated as answers: the failure set is {1} in (a) and {0} in (b).
    No published solution was located; the card keeps its own argument and says so. Checked against
    Munkres, Topology (2000), Section 45 Exercise 4, printed p. 280, and the definition on printed p. 277.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Issue #169 read of both parts, with the #184 repair. (a): for $x_0<1$ choose $x_0<a<1$ and $N$
    with $a^N,x_0^N<\varepsilon/2$; on $[0,a]$ and for $n\ge N$ both terms are below those bounds,
    and for the finitely many $n<N$ continuity gives neighbourhoods whose intersection with
    $[0,a]$ serves the whole family at once, which is what equicontinuity asks. At $1$ it fails:
    with $\varepsilon=1/2$ every neighbourhood contains an $x<1$ with $x^n<1/2$ for large $n$.
    (b): the $g_n$ are the functions of §21 Exercise 9; $0<g_n\le1$ gives pointwise boundedness,
    $g_n(1/n)=1$ while $g_n\to0$ pointwise excludes a uniformly convergent subsequence, and
    equicontinuity fails at $0$ because $g_n(1/n)-g_n(0)=n/(n+1)>1/2$. The page locators of the
    solution are replaced by the section and exercise numbers. Citation by number: §45 Exercise
    4, §21 Exercise 9, read in `tmp/sources/munkres-2000-topology.md`.

---

::: {.exercise}

(a) Let $f_n: I \to \RR$ be the function $f_n(x) = x^n$.
The collection $\mathcal{F} = \theset{f_n}$ is pointwise bounded but the sequence $(f_n)$ has no uniformly convergent subsequence; at what point or points does $\mathcal{F}$ fail to be equicontinuous?

(b) Repeat (a) for the functions $f_n$ of Exercise 9 of §21.
:::

::: {.solution}

No complete published solution of this exercise was located; the sets searched are listed in the `COMPLAINTS.md` entry for §43--§50 of `SRC-TEXT-MUN00`. The argument is therefore the card's own, checked against the book's definition of equicontinuity (§45) and against Exercise 9 of §21, whose functions are those of part (b).

The statement was checked against §45 Exercise 4. Throughout $I=[0,1]$, $\mathcal{F}=\theset{f_{n}\mid n\in\ZZ_{+}}$ with $f_{n}(x)=x^{n}$ on $I$, and $\mathcal{G}=\theset{g_{n}\mid n\in\ZZ_{+}}$ with
$$
g_{n}(x)=\frac{1}{n^{3}\big(x-1/n\big)^{2}+1}
$$
on $\RR$, the functions of Exercise 9 of §21. A family $\mathcal{F}\subset\mathcal{C}(X,\RR)$ is *equicontinuous at* $x_{0}$ when for each $\varepsilon>0$ there is a neighbourhood $U$ of $x_{0}$ such that $\abs{f(x)-f(x_{0})}<\varepsilon$ for every $x\in U$ and every $f\in\mathcal{F}$ --- one neighbourhood serving the whole family at once --- and *pointwise bounded* when $\theset{f(x)\mid f\in\mathcal{F}}$ is bounded for each $x$.

::: pf

::: {.pf-step #a}

(a) $\mathcal{F}$ is equicontinuous at every $x_{0}\in[0,1)$, and is not equicontinuous at $1$; so the failure set of $\mathcal{F}$ is $\theset{1}$.

:::: pf-proof

Let $I=[0,1]$ and $f_{n}(x)=x^{n}$, so that $\mathcal{F}$ is the family of the exercise. Two claims locate the failure set.

::: {.pf-step #a-at-point}

For $x_{0}\in[0,1)$ the family $\mathcal{F}$ is equicontinuous at $x_{0}$.

:::: pf-proof

Fix $x_{0}<1$ and $\varepsilon>0$.

::: {.pf-step #a-data}

Given $\varepsilon>0$ there are $a$ with $x_{0}<a<1$ and $N\in\ZZ_{+}$ with $a^{N}<\varepsilon/2$ and $x_{0}^{N}<\varepsilon/2$.

::: pf-proof

$a$ exists because $x_{0}<1$ and the order of $\RR$ is dense. Since $0\leq x_{0}<a<1$, the sequences $a^{n}$ and $x_{0}^{n}$ both decrease to $0$, so some $N$ makes both smaller than $\varepsilon/2$; increasing $N$ preserves the inequalities.

:::

:::

::: {.pf-step #a-tail}

For every $n\geq N$ and every $x\in[0,a]$ one has $\abs{f_{n}(x)-f_{n}(x_{0})}<\varepsilon$.

::: pf-proof

Both $x$ and $x_{0}$ lie in $[0,a]$, so $x^{n}\leq a^{n}\leq a^{N}$ and $x_{0}^{n}\leq x_{0}^{N}$, the second because $x_{0}<1$. Hence
$$
\abs{x^{n}-x_{0}^{n}}\leq x^{n}+x_{0}^{n}\leq a^{N}+x_{0}^{N}<\varepsilon .
$$

:::

:::

::: {.pf-step #a-head}

For each $n<N$ there is a neighbourhood $U_{n}$ of $x_{0}$ in $I$ with $\abs{x^{n}-x_{0}^{n}}<\varepsilon$ for $x\in U_{n}$.

::: pf-proof

The map $x\mapsto x^{n}$ is continuous on $I$, being a product of $n$ copies of the identity; so the set where $\abs{x^{n}-x_{0}^{n}}<\varepsilon$ is an open neighbourhood of $x_{0}$ in $I$.

:::

:::

::: {.pf-step #a-neighbourhood}

$V\coloneqq[0,a]\cap\bigcap_{n<N}U_{n}$ is a neighbourhood of $x_{0}$ in $I$ with $\abs{f_{n}(x)-f_{n}(x_{0})}<\varepsilon$ for every $x\in V$ and every $n$.

::: pf-proof

Since $x_{0}<a$, the point $x_{0}$ lies in the interior of $[0,a]$ relative to $I$, so $[0,a]$ is a neighbourhood of $x_{0}$, and a finite intersection of neighbourhoods is a neighbourhood; hence $V$ is one. Let $x\in V$ and $n\in\ZZ_{+}$. If $n\geq N$ then $x\in V\subset[0,a]$ and step [](#a-tail){.pf-ref} applies; if $n<N$ then $x\in U_{n}$ and step [](#a-head){.pf-ref} applies. In either case the inequality holds, and the single neighbourhood $V$ serves the whole family.

:::

:::

::: pf-step

$\mathcal{F}$ is equicontinuous at $x_{0}$.

::: pf-proof

Given $\varepsilon>0$, steps [](#a-data){.pf-ref} and [](#a-neighbourhood){.pf-ref} produce a neighbourhood $V$ of $x_{0}$ with $\abs{f_{n}(x)-f_{n}(x_{0})}<\varepsilon$ for all $x\in V$ and all $n$, which is the definition on printed p. 277.

:::

:::

::::

:::

::: {.pf-step #a-not-at-1}

$\mathcal{F}$ is not equicontinuous at $1$.

::: pf-proof

Take $\varepsilon\coloneqq1/2$ and let $U$ be any neighbourhood of $1$ in $I$. Every such neighbourhood contains a point $x<1$, since $I$ has no interval to the right of $1$. For that $x$ the sequence $x^{n}$ decreases to $0$, so there is $n$ with $x^{n}<1/2$, and then
$$
\abs{f_{n}(x)-f_{n}(1)}=\abs{x^{n}-1}=1-x^{n}>\tfrac12=\varepsilon .
$$
So no neighbourhood of $1$ satisfies the definition, and $\mathcal{F}$ is not equicontinuous there.

:::

:::

::::

:::

::: {.pf-step #b}

(b) $\mathcal{G}$ is pointwise bounded and no subsequence of it converges uniformly on $\RR$, and $\mathcal{G}$ fails to be equicontinuous exactly at $0$.

:::: pf-proof

The functions of Exercise 9 of §21 are those of the exercise here: $g_{n}(x)=1/\big(n^{3}(x-1/n)^{2}+1\big)$ on $\RR$. Three claims settle the part.

::: {.pf-step #b-no-uniform}

$\mathcal{G}$ is pointwise bounded and no subsequence converges uniformly.

::: pf-proof

For every $x$ and $n$ one has $0<g_{n}(x)\leq1$, since $n^{3}(x-1/n)^{2}+1\geq1$; so $\mathcal{G}$ is pointwise bounded. For fixed $x$ the denominator tends to infinity with $n$ --- it is $n+1$ at $x=0$ and at least $n^{3}(x-1/n)^{2}$ otherwise, with $x-1/n\to x\neq0$ --- so $g_{n}(x)\to0$ and the pointwise limit is the zero function; a uniformly convergent subsequence would therefore have to converge uniformly to $0$. But $g_{n}(1/n)=1$ for every $n$, so $\sup_{x}\abs{g_{n}(x)}=1$ for every $n$ and no subsequence converges uniformly.

:::

:::

::: {.pf-step #b-not-at-0}

$\mathcal{G}$ is not equicontinuous at $0$.

::: pf-proof

Take $\varepsilon\coloneqq1/2$ and let $U$ be a neighbourhood of $0$. It contains $1/n$ for all sufficiently large $n$, and for $n\geq2$,
$$
\abs{g_{n}(1/n)-g_{n}(0)}=1-\frac{1}{n^{3}(1/n)^{2}+1}=1-\frac{1}{n+1}\geq\frac{2}{3}>\frac12=\varepsilon .
$$
So no neighbourhood of $0$ works, and $\mathcal{G}$ is not equicontinuous at $0$.

:::

:::

::: {.pf-step #b-at-point}

For $x_{0}\neq0$ the family $\mathcal{G}$ is equicontinuous at $x_{0}$.

:::: pf-proof

Fix $x_{0}\neq0$ and $\varepsilon>0$.

::: {.pf-step #b-window}

There are $c>0$ and $r>0$ with $\abs{x}\geq c$ for every $x$ in $J\coloneqq[x_{0}-r,x_{0}+r]$.

::: pf-proof

Since $x_{0}\neq0$, put $c\coloneqq\abs{x_{0}}/2>0$ and $r\coloneqq\abs{x_{0}}/2>0$. For $\abs{x-x_{0}}\leq r$ the triangle inequality gives $\abs{x}\geq\abs{x_{0}}-\abs{x-x_{0}}\geq\abs{x_{0}}/2=c$.

:::

:::

::: {.pf-step #b-tail}

For $n\geq2/c$ and $x\in J$ one has $0<g_{n}(x)\leq1/\big(n^{3}c^{2}/4+1\big)$, so $g_{n}\to0$ uniformly on $J$.

::: pf-proof

For such $n$ one has $1/n\leq c/2$, so $\abs{x-1/n}\geq\abs{x}-1/n\geq c-c/2=c/2$ and $n^{3}(x-1/n)^{2}\geq n^{3}c^{2}/4$. Hence $0<g_{n}(x)\leq1/(n^{3}c^{2}/4+1)$, and the right-hand side tends to $0$ as $n\to\infty$ because $n^{3}c^{2}/4\to\infty$.

:::

:::

::: {.pf-step #b-head}

For each $n<N$ there is a neighbourhood $V_{n}$ of $x_{0}$ in $\RR$ with $\abs{g_{n}(x)-g_{n}(x_{0})}<\varepsilon$ for $x\in V_{n}$, and some $N$ makes $\sup_{J}g_{n}<\varepsilon/2$ for all $n\geq N$.

::: pf-proof

Each $g_{n}$ is continuous, its denominator being a polynomial with no zero, so the set where $\abs{g_{n}(x)-g_{n}(x_{0})}<\varepsilon$ is an open neighbourhood of $x_{0}$. For the second claim, step [](#b-tail){.pf-ref} gives uniform convergence to $0$ on $J$, so some $N$ makes $g_{n}(x)<\varepsilon/2$ for all $n\geq N$ and all $x\in J$.

:::

:::

::: {.pf-step #b-neighbourhood}

$V\coloneqq J\cap\bigcap_{n<N}V_{n}$ is a neighbourhood of $x_{0}$ with $\abs{g_{n}(x)-g_{n}(x_{0})}<\varepsilon$ for every $x\in V$ and every $n$, so $\mathcal{G}$ is equicontinuous at $x_{0}$.

::: pf-proof

$V$ is a finite intersection of neighbourhoods of $x_{0}$. For $x\in V$ and $n\geq N$ one has $g_{n}(x)<\varepsilon/2$ and $g_{n}(x_{0})<\varepsilon/2$ because $x,x_{0}\in J$, whence $\abs{g_{n}(x)-g_{n}(x_{0})}<\varepsilon$ as both terms are positive; and for $n<N$ the inequality is that of $V_{n}$.

:::

:::

::::

:::

::::

:::

::: pf-step

Therefore $\mathcal{F}$ fails to be equicontinuous exactly at $1$ and $\mathcal{G}$ exactly at $0$.

::: pf-proof

Steps [](#a){.pf-ref} and [](#b){.pf-ref} answer the exercise: for $f_{n}(x)=x^{n}$ on $I$ the family is pointwise bounded, its sequence has no uniformly convergent subsequence, and equicontinuity fails only at the endpoint $1$; for the functions of Exercise 9 of §21 the family is pointwise bounded, no subsequence converges uniformly on $\RR$, and equicontinuity fails only at $0$, where the moving peak $1/n$ of $g_{n}$ escapes detection by any single neighbourhood.

:::

:::

:::

:::
