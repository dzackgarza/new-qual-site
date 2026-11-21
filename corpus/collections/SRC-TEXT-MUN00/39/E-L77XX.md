---
schema: qual/card@1
id: E-L77XX
kind: problem
title: A countably locally finite collection that is neither countable nor locally finite
classification:
  areas:
  - topology
  topics:
  - Local Finiteness
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
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "Feryll", *Praying For Stockholm*, "Countable Local
    Finiteness (6.39.5-6)" (26 December 2014),
    http://feryll.blogspot.com/2014/12/countable-local-finiteness-6395-6.html, read 2026-11-10; cited by
    URL and date read, since a web page has no printed page, and attributed to the handle the post
    carries. Checked against Munkres, Topology (2000), Section 39 Exercise 6, printed p. 247, and §20's
    uniform metric. The post's argument is the card's: two distinct members of the family of sets with a
    prescribed binary tail differ in some coordinate above the n-th, hence are at distance 1 in the
    uniform metric, so a small ball meets at most one of them; the family is uncountable because the
    binary tails are, and it is not locally finite at 0 because the sets R^n x prod_{i>n}{0} all contain
    0. What was corrected: the post uses the 1/2-neighbourhood and states the separation in the words
    "the 1/2-neighborhood of any element intersects at most one element", which does not follow from
    distance 1 without the triangle inequality; the card uses the ball of radius 1/3 and derives the
    uniqueness of the member met from the coordinates. The post's non-local-finiteness witness is the
    point 1^omega; the card uses 0, which is the same argument.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, and the retained set now cited in the solution
    section rather than only here. Page repair: §39 Exercise 6 is on printed p. 248, not
    p. 247 as the note of 2026-11-10 says; the folio of the page carrying it reads 248, and
    the neighbouring exercises (5 and 7) are on the same page. Citations added: the uniform
    metric of §20 on printed p. 124, and Theorem 7.8 on printed p. 50 for the
    uncountability of the power set of Z_+. Each of the three claims re-checked: the
    members of B_n are the sets R^n x prod_{i>n}{eps_i} with the tail eps, and distinct
    tails give distinct sets because the i-th projection is {eps_i}; a member meeting the
    1/3-ball about x forces |eps_i - x_i| < 1/3 for every i > n, and an interval of radius
    1/3 contains at most one of 0 and 1 since their distance is 1, so the ball meets at
    most one member; the members C_n = R^n x prod_{i>n}{0} are pairwise distinct, differ
    at the (n+1)-st coordinate, and all contain the origin. No repair to the statement.
    What was not done: the blog post itself is not in the checkout, so its wording was not
    re-read this pass; the mathematics below stands on its own check.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Issue #169 read against the published solution, Feryll, *Praying For Stockholm*, "Countable
    Local Finiteness (6.39.5-6)" (26 December 2014), fetched again this date at the URL in the
    solution. The post's three claims are the card's: each $\mathcal B_n$ is locally finite because
    two members with different binary tails are at uniform distance $1$; $\mathcal B_1$ is
    uncountable because its tails are the subsets of the integers above $1$; and the family is not
    locally finite at the constant sequence $1$, which lies in every member whose tail is constant
    $1$. The card's radius-$1/3$ ball and its witness $\mathbf 0$ are its own renderings of the
    same arguments, and both are correct. What was corrected: the sentence proving the $C_n$
    pairwise distinct said that at the $(n+1)$-st coordinate "the first is free and the second is
    $0$", which is backwards --- $C_n$ has $\{0\}$ there and $C_m$ with $m>n$ has $\RR$, since
    $n+1\le m$ --- and it now reads that way. The clause about a web page having no printed page is
    dropped from the solution. Each of the three claims stands. Citation by number: §39 Exercise 6,
    read in `tmp/sources/munkres-2000-topology.md`.

---

::: {.exercise}

Consider $\RR^\omega$ in the uniform topology.
Given $n$, let $\mathcal{B}_n$ be the collection of all subsets of $\RR^\omega$ of the form $\prod A_i$, where $A_i = \RR$ for $i \leq n$ and $A_i$ equals either $\theset{0}$ or $\theset{1}$ otherwise.
Show that the collection $\mathcal{B} = \bigcup \mathcal{B}_n$ is countably locally finite, but neither countable nor locally finite.
:::

::: {.solution}
The construction and the three claims are those of the retained published solution, **Feryll, *Praying For Stockholm*, "Countable Local Finiteness (6.39.5-6)" (26 December 2014), http://feryll.blogspot.com/2014/12/countable-local-finiteness-6395-6.html**, read 2026-11-10 and again on 2026-11-20, and cited by its URL and the date read. The steps below are its argument, with the ball of radius $1/3$ used where the post's remark speaks of the $1/2$-neighbourhood (see the audit).

Throughout, $\RR^\omega$ carries the uniform metric $\bar\rho(x,y)=\sup_i\min\{\abs{x_i-y_i},1\}$ (Munkres, *Topology* (2000), §20), the exercise is §39 Exercise 6, and $\mathcal{B}=\bigcup_{n\ge1}\mathcal{B}_n$ is the collection defined there.

::: pf

::: {.pf-step #parametrise}
For each $n$ the members of $\mathcal{B}_n$ are exactly the sets $B_\epsilon=\RR^n\times\prod_{i>n}\{\epsilon_i\}$ for $\epsilon\in\{0,1\}^{\{i>n\}}$, and $\epsilon\mapsto B_\epsilon$ is a bijection.

::: pf-proof
A member of $\mathcal{B}_n$ is $\prod_i A_i$ with $A_i=\RR$ for $i\le n$ and $A_i$ equal to $\{0\}$ or $\{1\}$ for $i>n$, which is to say $A_i=\{\epsilon_i\}$ for a unique binary tail $\epsilon$; distinct tails give distinct products, since the $i$-th coordinate projection of $B_\epsilon$ is $\{\epsilon_i\}$.
:::

:::

::: {.pf-step #lfinite}
Each $\mathcal{B}_n$ is locally finite: for every $x\in\RR^\omega$ the ball $B_{\bar\rho}(x,1/3)$ meets at most one member of $\mathcal{B}_n$.

::: pf-proof

::: {.pf-step #close}
If $B_\epsilon\in\mathcal{B}_n$ meets $B_{\bar\rho}(x,1/3)$, then $\abs{\epsilon_i-x_i}<1/3$ for every $i>n$.

::: pf-proof
Let $y\in B_\epsilon$ with $\bar\rho(x,y)<1/3$. For every $i$ we have $\min\{\abs{x_i-y_i},1\}\le\bar\rho(x,y)<1/3$, so $\abs{x_i-y_i}<1/3$; and for $i>n$ the $i$-th coordinate of $y$ is $\epsilon_i$.
:::

:::

::: {.pf-step #unique}
If $B_\epsilon$ and $B_\eta$ both meet $B_{\bar\rho}(x,1/3)$, then $B_\epsilon=B_\eta$.

::: pf-proof
By step [](#close){.pf-ref} both $\epsilon_i$ and $\eta_i$ lie in the interval $(x_i-1/3,x_i+1/3)$ for every $i>n$. That interval contains at most one of the numbers $0$ and $1$, because $\abs{0-1}=1>2/3$; so $\epsilon_i=\eta_i$ for every $i>n$ and the two tails coincide, hence $B_\epsilon=B_\eta$ by step [](#parametrise){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #clf}
$\mathcal{B}$ is countably locally finite.

::: pf-proof
Each point of $\RR^\omega$ has the neighbourhood $B_{\bar\rho}(x,1/3)$, which meets at most one member of $\mathcal{B}_n$; so $\mathcal{B}_n$ is locally finite for every $n$, and $\mathcal{B}=\bigcup_n\mathcal{B}_n$ is a countable union of locally finite collections, that is countably locally finite.
:::

:::

::: {.pf-step #uncountable}
$\mathcal{B}$ is not countable.

::: pf-proof
By step [](#parametrise){.pf-ref} the subcollection $\mathcal{B}_1$ is in bijection with the set of binary sequences indexed by the integers $i>1$, which is in bijection with the power set of $\ZZ_+$; that power set admits no surjection from $\ZZ_+$ (Theorem 7.8), so $\mathcal{B}_1$ has cardinality $2^{\aleph_0}$ and $\mathcal{B}$ is uncountable.
:::

:::

::: {.pf-step}
$\mathcal{B}$ is not locally finite.

::: pf-proof
Let $\mathbf{0}=(0,0,\ldots)$ and for each $n$ put $C_n=\RR^n\times\prod_{i>n}\{0\}$, which is the member $B_\epsilon$ of $\mathcal{B}_n$ for the tail $\epsilon$ all of whose entries are $0$. The sets $C_n$ are pairwise distinct, since $C_n$ and $C_m$ with $n<m$ differ in the $(n+1)$-st coordinate, where $C_n$ has $\{0\}$ and $C_m$ has $\RR$, as $n+1\le m$. Each $C_n$ contains $\mathbf{0}$, so every neighbourhood of $\mathbf{0}$ meets every $C_n$, that is infinitely many members of $\mathcal{B}$. Hence $\mathcal{B}$ is not locally finite.
:::

:::

:::
:::
