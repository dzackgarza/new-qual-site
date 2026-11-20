---
schema: qual/card@1
id: E-1FRQL
kind: problem
title: Thomae-type function continuous at each irrational
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
  - Continuous Functions
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
    No complete published solution of Munkres §48 Exercise 9 (printed p. 299) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked line by line against the book: continuity at an
    irrational x_0 takes the finitely many rationals x_1,...,x_N with 1/n >= eps and a radius avoiding them;
    discontinuity at the rational x_m = f^{-1}(1/m) uses the density of the irrationals, where f vanishes, at
    distance 1/m from f(x_m). The second question is answered yes, with an explicit sequence of continuous
    functions: at stage k one places a tent of height 1/n on a small interval about each of x_1,...,x_k, with
    pairwise disjoint supports of width less than 1/k; then f_k(x_m) = 1/m for k >= m while f_k(x) is eventually
    at most 1/n for each fixed n at an irrational x, because the supports of the first N tents are eventually
    avoided there. The supports are disjoint so at most one tent contributes at an irrational point. Nothing
    needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Yougi, *Munkres Topology Solution: Chapter 8* (Nocturne blog,
    2025-07-10, https://hexo.yougi.top/2025/07/10/Munkres-Topology-Solution-Chapter-8/, text at
    tmp/sources/yougi-2025-munkres-chapter-8.md), answers Munkres §48 Exercise 9 (printed p. 299) at its Ex.
    48.9 for the first question only, in one sentence ("a standard fact in analysis"), and says in the post
    itself that it has neither proved nor disproved the existence of the sequence $f_n$: the second question
    of the exercise is unanswered there. Math StackExchange 1114745, "Thomae function is continuous at
    $x\notin\QQ$, discontinuous at $x\in\QQ$" (2015-03-23), is the first question and has no
    answer, the text kept at tmp/sources/mse-1114745-munkres-48-9.md; the other Thomae questions returned by
    the search are about integrability, limits or inverse images and not about this exercise. The card
    therefore keeps both halves as its own: the $\varepsilon$-$\delta$ proof at an irrational and the density
    argument at a rational, and the explicit sequence of tents with pairwise disjoint supports of width below
    $1/k$, which answers the second question yes. Nothing needed correction.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Rewrote the solution's frame on 2026-11-19, leaving every argument as it was.
    The three steps opened with run-in titles ("Continuity at every irrational
    point", "Discontinuity at every rational point", "Construction of continuous
    functions f_k -> f pointwise") instead of claims, which STYLE-07 and STYLE-08
    do not allow. They are now labelled steps s1 to s3 whose first paragraphs are
    the claims that f is continuous at every irrational, discontinuous at every
    rational, and the pointwise limit of continuous functions. The exercise is
    Section 48 Exercise 3 at printed p. 299, as the page already on the card has
    it. No statement, argument or citation changes.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Twenty steps asserted their claim with no justification; the three parts are now proved by steps that
    state one claim and derive it in a pf-proof. Continuity at an irrational: the integer $N$ with
    $1/N < \varepsilon$ and the radius $\delta$ that avoids $x_1, \dots, x_N$ are now one step, whose proof
    notes that the minimum of finitely many positive distances is positive, and the two cases of the
    estimate are the second step. Discontinuity at the rational $x_m$: the value and the density of the
    irrationals in every interval form one step, and the choice $\varepsilon_0 = 1/(2m)$ with the negation
    of the $\varepsilon$-$\delta$ condition the second. The sequence of continuous functions: the disjoint
    tents are now justified by taking $\delta_{n,k} = \min\{1/k, d_k/2\}$ with $d_k$ the minimum distance
    between the first $k$ rationals, which the card had asserted without saying how; the tent's continuity,
    its range and its support are derived from the formula; the continuity of $f_k$ and its eventual
    constancy at each rational are one step; and the pointwise vanishing at an irrational is the last, with
    the two range conditions $k > N$ and $1/k < \eta$ that it needs. Sources are cited by numbered
    statement: the density of the irrationals in $\RR$, and the archimedean property. No page reference is
    written in the body of this card or in the event above. The statement is unchanged. Both questions are
    answered by the card's own argument; no retained solution set covers the exercise.

---

::: {.exercise}

Let $g: \ZZ_+ \to \QQ$ be a bijective function; let $x_n = g(n)$.
Define $f: \RR \to \RR$ as follows:

$$
\begin{array}{ll}
f(x_n) = 1/n & \text{for } x_n \in \QQ, \\
f(x) = 0 & \text{for } x \notin \QQ.
\end{array}
$$

Show that $f$ is continuous at each irrational and discontinuous at each rational.
Can you find a sequence of continuous functions $f_n$ converging to $f$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
$f$ is continuous at every irrational point.

::: pf-proof

::: {.pf-step #delta-choice}

At an irrational $x_0$ and for every $\varepsilon > 0$ there is $\delta > 0$ such that the interval $(x_0 - \delta, x_0 + \delta)$ contains none of the rationals $x_1, \dots, x_N$, where $N$ is chosen with $1/N < \varepsilon$.

::: pf-proof
The value $f(x_0) = 0$ because $x_0$ is irrational. Fix $\varepsilon > 0$ and an integer $N$ with $1/N < \varepsilon$, which exists by the archimedean property. The set $S_N = \{x_1, \dots, x_N\}$ is finite and consists of rationals, so $x_0 \notin S_N$; hence the finitely many numbers $\abs{x_0 - x_n}$ for $1 \le n \le N$ are positive, and their minimum $\delta > 0$ is attained and positive. If $\abs{x - x_0} < \delta$ then $\abs{x - x_0} \ne \abs{x_0 - x_n}$ for every $n \le N$, so $x \ne x_n$ for every $n \le N$ and $x \notin S_N$.
:::

:::

::: pf-step

$\abs{f(x) - f(x_0)} < \varepsilon$ for every $x \in (x_0 - \delta, x_0 + \delta)$, so $f$ is continuous at $x_0$.

::: pf-proof
Let $x$ lie in that interval. If $x$ is irrational then $f(x) = 0 = f(x_0)$ and the difference is $0 < \varepsilon$. If $x$ is rational then $x = x_k$ for exactly one $k$, since $g$ is a bijection, and $x \notin S_N$ gives $k > N$; therefore $\abs{f(x) - f(x_0)} = 1/k < 1/N < \varepsilon$. Both cases give the bound, which is the $\varepsilon$-$\delta$ definition of continuity at $x_0$.
:::

:::

:::

:::

::: {.pf-step #s2}
$f$ is discontinuous at every rational point.

::: pf-proof

::: pf-step

$f(x_m) = 1/m$, and every interval about $x_m$ contains an irrational point at which $f$ vanishes.

::: pf-proof
The first statement is the definition of $f$ at the rational $x_m$. For the second, the irrationals are dense in $\RR$, so $(x_m - \delta, x_m + \delta)$ contains an irrational $y$ for every $\delta > 0$, and $f(y) = 0$ by the definition of $f$ off $\QQ$.
:::

:::

::: pf-step

$f$ is discontinuous at $x_m$.

::: pf-proof
Put $\varepsilon_0 = 1/(2m) > 0$. Given any $\delta > 0$, the previous step supplies an irrational $y$ with $\abs{y - x_m} < \delta$, and then $\abs{f(y) - f(x_m)} = \abs{0 - 1/m} = 1/m > \varepsilon_0$. So no $\delta$ makes the values within $\varepsilon_0$ on that interval, which is the negation of continuity at $x_m$.
:::

:::

:::

:::

::: {.pf-step #s3}
$f$ is the pointwise limit of continuous functions $f_k\colon\RR\to\RR$.

::: pf-proof

::: {.pf-step #disjoint-supports}

For each $k$ there are $\delta_{n,k} > 0$, $n = 1, \dots, k$, with $\delta_{n,k} < 1/k$ and the intervals $(x_n - \delta_{n,k}, x_n + \delta_{n,k})$ pairwise disjoint.

::: pf-proof
The points $x_1, \dots, x_k$ are distinct because $g$ is injective, so the minimum $d_k$ of the finitely many distances $\abs{x_i - x_j}$ with $i \ne j$ is positive. Set $\delta_{n,k} = \min\{1/k, d_k/2\}$, which is positive and below $1/k$. Two intervals centred at points at distance at least $d_k$ with radii at most $d_k/2$ are disjoint, since a common point would be within $d_k/2$ of each centre and the centres would then be less than $d_k$ apart.
:::

:::

::: pf-step

The tent $\phi_{n,k}$ is continuous, takes the value $1/n$ at $x_n$, and vanishes off $[x_n - \delta_{n,k}, x_n + \delta_{n,k}]$, with values in $[0, 1/n]$.

::: pf-proof
The formula $\phi_{n,k}(x) = \max\{0, (1/n)(1 - \abs{x - x_n}/\delta_{n,k})\}$ defines a continuous function, being the maximum of the zero function and a function that is a composite of continuous maps, and the absolute value is bounded below by $0$, so the values lie in $[0, 1/n]$. At $x = x_n$ the bracket equals $1$ and the value is $1/n$. If $\abs{x - x_n} \ge \delta_{n,k}$ the bracket is at most $0$ and the max is $0$.
:::

:::

::: pf-step

$f_k = \sum_{n=1}^{k} \phi_{n,k}$ is continuous, and $f_k(x_m) = 1/m$ for every $k \ge m$.

::: pf-proof
A finite sum of continuous functions is continuous. For $k \ge m$ the point $x_m$ is one of the centres, so $\phi_{m,k}(x_m) = 1/m$; the other tents vanish at $x_m$ by the disjointness of the supports, since $x_m$ lies on none of their intervals. Hence $f_k(x_m) = 1/m = f(x_m)$, and the sequence of values is eventually constant at $f(x_m)$.
:::

:::

::: pf-step

$f_k(x) \to 0$ for every irrational $x$.

::: pf-proof
Let $\varepsilon > 0$ and $N$ with $1/N < \varepsilon$, and put $\eta = \min_{1 \le n \le N}\abs{x - x_n} > 0$, which is positive because $x$ is irrational and the $x_n$ are rational. For $k > \max(N, 1/\eta)$ one has $\delta_{n,k} < 1/k < \eta$ for every $n$, so $x$ lies outside the support of $\phi_{n,k}$ whenever $n \le N$ and those tents contribute $0$. The supports are pairwise disjoint, so at most one of the remaining tents is nonzero at $x$, and every tent has values at most $1/n$ for its index $n$; a nonzero value therefore comes from some $n > N$ and is at most $1/n < 1/N < \varepsilon$. Hence $f_k(x) < \varepsilon$ for all large $k$, that is $f_k(x) \to 0 = f(x)$.
:::

:::

:::

:::

:::

:::
