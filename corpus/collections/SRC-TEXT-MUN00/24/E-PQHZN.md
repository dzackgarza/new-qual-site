---
schema: qual/card@1
id: E-PQHZN
kind: problem
title: The long line
classification:
  areas:
  - topology
  topics:
  - Order Topology
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §24 Exercise 12, printed p. 158, with Theorem
    24.1, Theorem 24.3 and Exercise 24.7; the six parts and the theorem are stored as
    printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 24.12, PDF pp. 6-7. All six parts are theirs: the
    splitting and gluing of intervals of the order type of [0,1), the sequence form, the
    transfinite induction over S_Omega, path connectedness of L through the successor of the
    least element, the local homeomorphism at each point, and the failure of second
    countability, which is stated on the card as the counting lemma about disjoint open sets
    in a space with a countable basis. (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose, part by part, without changing the
    citation: the argument is positron0802's, read again at PDF pp. 6--7 of
    tmp/sources/munkres-solutions-positron-ch3.pdf. Two repairs came out of the reading. The
    source's (c) splits off the base case a = a_0^+ explicitly ("The base case is when a is the
    successor of a_0"), which the card's prose had dropped by writing b >= a_0 in the successor
    case, where b = a_0 would give the empty interval [a_0 x 0, a_0 x 0) and no induction
    hypothesis applies; the base case is now its own step. In (d) the prose joined a_0 x t to
    a_1 x 0 by a path inside the half-open interval [a_0 x 0, a_1 x 0), which does not contain
    a_1 x 0; the step now uses [a_0 x 0, a_2 x 0), which has the order type of [0,1) by (c) and
    contains both points. Also dropped, as not needed and not proved there, the closing clause of
    (e) that (a_0 x 0, b x t) is again homeomorphic with an open interval. Checked in (b) that the
    intervals [x_i, x_{i+1}) partition [x_0, b) when b is the supremum, so that the gluing is
    well defined, and in (f) that {b} x (0,1) is the open interval (b x 0, b^+ x 0) of L. What was
    not checked: the printed page is taken from the card's own audit, not re-read here.
---

::: {.exercise}

Recall that $S_\Omega$ denotes the minimal uncountable well-ordered set.
Let $L$ denote the ordered set $S_\Omega \times [0, 1)$ in the dictionary order, with its smallest element deleted.
The set $L$ is a classical example in topology called the long line.

Theorem.
The long line is path connected and locally homeomorphic to $\RR$, but it cannot be imbedded in $\RR$.

(a) Let $X$ be an ordered set; let $a < b < c$ be points of $X$.
Show that $[a, c)$ has the order type of $[0, 1)$ if and only if both $[a, b)$ and $[b, c)$ have the order type of $[0, 1)$.

(b) Let $X$ be an ordered set.
Let $x_0 < x_1 < \cdots$ be an increasing sequence of points of $X$; suppose $b = \sup\theset{x_i}$.
Show that $[x_0, b)$ has the order type of $[0, 1)$ if and only if each interval $[x_i, x_{i+1})$ has the order type of $[0, 1)$.

(c) Let $a_0$ denote the smallest element of $S_\Omega$.
For each element $a$ of $S_\Omega$ different from $a_0$, show that the interval $[a_0 \times 0, a \times 0)$ of $S_\Omega \times [0, 1)$ has the order type of $[0, 1)$.
[Hint: Proceed by transfinite induction. Either $a$ has an immediate predecessor in $S_\Omega$, or there is an increasing sequence $a_i$ in $S_\Omega$ with $a = \sup\theset{a_i}$.]

(d) Show that $L$ is path connected.

(e) Show that every point of $L$ has a neighborhood homeomorphic with an open interval in $\RR$.

(f) Show that $L$ cannot be imbedded in $\RR$, or indeed in $\RR^n$ for any $n$.
[Hint: Any subspace of $\RR^n$ has a countable basis for its topology.]
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 24.12, PDF pp. 6--7** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); all six parts are theirs. Part (f) is stated on the card through the counting lemma behind the second countability of subspaces of $\RR^{n}$, which is the book's hint, rather than through Theorem 30.3, which comes later in the book.

Let $S_{\Omega}$ be the minimal uncountable well-ordered set, $a_{0}$ its least element, and $L$ the long line, that is, $S_{\Omega}\times[0,1)$ in the dictionary order with its least element $a_{0}\times0$ removed.

(a) If $[a,c)$ has the order type of $[0,1)$ via an order-preserving bijection $f$, then $f$ restricts to order-preserving bijections $[a,b)\to[0,f(b))$ and $[b,c)\to[f(b),1)$, and $[0,t)$ has the order type of $[0,1)$ for every $t\in(0,1)$ (via $s\mapsto s/t$). Conversely, order-preserving bijections $[a,b)\to[0,1/2)$ and $[b,c)\to[1/2,1)$ glue to an order-preserving bijection $[a,c)\to[0,1)$.

(b) If $[x_{0},b)$ has the order type of $[0,1)$, then by (a) applied repeatedly each $[x_{i},x_{i+1})$ does. Conversely, if each $[x_{i},x_{i+1})$ has the order type of $[0,1)$, choose order-preserving bijections $f_{i}:[x_{i},x_{i+1})\to[1-2^{-i},\,1-2^{-i-1})$; they agree on the overlaps (each $x_{i}$ is the last point of nothing and the first point of $[x_{i},\dots)$), and together they give an order-preserving bijection $[x_{0},b)\to[0,1)$ because $\sup_{i}x_{i}=b$ corresponds to $\sup_{i}(1-2^{-i})=1$.

(c) By transfinite induction on $a\ne a_{0}$ in $S_{\Omega}$, one shows that $[a_{0}\times0,\ a\times0)$ has the order type of $[0,1)$. If $a$ is the successor of an element $b$ (with $b\ge a_{0}$), then $[a_{0}\times0,b\times0)$ has the order type of $[0,1)$ by induction, and so does $[b\times0,a\times0)=\{b\}\times[0,1)$, which is order isomorphic to $[0,1)$; by (a) the same holds for $[a_{0}\times0,a\times0)$. If $a$ is not a successor, there is a strictly increasing sequence $a_{i}$ in $S_{\Omega}$ with $a=\sup_{i}a_{i}$; each $[a_{0}\times0,a_{i}\times0)$ has the order type of $[0,1)$ by induction, and by (b) so does $[a_{0}\times0,a\times0)$.

(d) *$L$ is path connected.* Let $a_{1}$ be the successor of $a_{0}$. Every point of $[a_{0}\times0,a_{1}\times0)$ can be joined to $a_{1}\times0$ by a path, since that interval has the order type of $[0,1)$ (part (c)) and the order topology on it is the usual one (Theorem 24.1 and Exercise 24.7(a)). For $b\ge a_{1}$ and $t\in[0,1)$, the point $b\times t$ can be joined to $b\times0$ within $\{b\}\times[0,1)$, and $b\times0$ can be joined to $a_{1}\times0$ by (a) and (b), since $[a_{1}\times0,b\times0)$ is a union of intervals each of the order type of $[0,1)$ (part (c)); the union of those two paths joins $b\times t$ to $a_{1}\times0$. So every point of $L$ is joined to $a_{1}\times0$.

(e) Every point of $L$ has a neighbourhood homeomorphic with an open interval of $\RR$. For $a_{0}\times t$ with $t\in(0,1)$ the interval $\{a_{0}\}\times(0,1)$ is such a neighbourhood, and so is $[a_{0}\times0,a_{1}\times0)$ (which is open in $L$ because $a_{0}\times0$ has been deleted and contained in the interval that has the order type of $[0,1)$). For $b>a_{0}$ and $t\in[0,1)$ the interval $(a_{0}\times0,\ b'\times0)$ with $b'$ the successor of $b$ is homeomorphic with $(0,1)$ by part (c) and Exercise 24.7(a), and it contains $b\times t$; so does the smaller open interval $(a_{0}\times0,\ b\times t)$ when $t>0$.

(f) *$L$ cannot be imbedded in $\RR^{n}$.* Any subspace of $\RR^{n}$ has a countable basis for its topology (the balls with rational centre and rational radius), and in a space with a countable basis every family of pairwise disjoint nonempty open sets is countable: each member contains a basis element, and distinct members contain distinct basis elements. But the sets $\{b\}\times(0,1)$, for $b$ ranging over the uncountably many elements of $S_{\Omega}$ other than $a_{0}$, are pairwise disjoint nonempty open subsets of $L$. So $L$ has no countable basis and cannot be a subspace of $\RR^{n}$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 24.12, PDF pp. 6--7** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); all six parts are theirs, and each step below is theirs unless it says otherwise. Part (f) is stated on the card through the counting lemma behind the second countability of subspaces of $\RR^{n}$, which is the book's hint, rather than through Theorem 30.3, which comes later in the book.

Throughout, $S_{\Omega}$ is the minimal uncountable well-ordered set, $a_{0}$ its least element, and $L$ is the long line: $S_{\Omega}\times[0,1)$ in the dictionary order with its least element $a_{0}\times0$ deleted.

::: pf

::: {.pf-step #parta}
(a) For $a<b<c$ in an ordered set $X$, the interval $[a,c)$ has the order type of $[0,1)$ if and only if both $[a,b)$ and $[b,c)$ do.

::: pf-proof
Let $f\colon[a,c)\to[0,1)$ be an order-preserving bijection. Its restriction to $[a,b)$ is an order-preserving bijection onto $[0,f(b))$, and $[0,t)$ has the order type of $[0,1)$ for every $t\in(0,1)$ via $s\mapsto s/t$, so $[a,b)$ has the order type of $[0,1)$. Its restriction to $[b,c)$ is an order-preserving bijection onto $[f(b),1)$, and $[t,1)$ has the order type of $[0,1)$ for every $t\in(0,1)$ via $s\mapsto(s-t)/(1-t)$; so $[b,c)$ does too.

Conversely, given order-preserving bijections $[a,b)\to[0,1)$ and $[b,c)\to[0,1)$, compose them with $s\mapsto s/2$ and $s\mapsto(s+1)/2$ to get order-preserving bijections $g\colon[a,b)\to[0,1/2)$ and $h\colon[b,c)\to[1/2,1)$. Every point of $[a,b)$ precedes every point of $[b,c)$, and every value below $1/2$ precedes every value from $1/2$ on, so $g$ and $h$ together give an order-preserving bijection $[a,c)\to[0,1)$.
:::
:::

::: {.pf-step #partb}
(b) If $x_{0}<x_{1}<\cdots$ and $b=\sup_{i}x_{i}$, then $[x_{0},b)$ has the order type of $[0,1)$ if and only if each $[x_{i},x_{i+1})$ does.

::: pf-proof
Suppose first that $[x_{0},b)$ has the order type of $[0,1)$. Since the sequence is strictly increasing with supremum $b$, one has $x_{i}<x_{i+1}<b$ for every $i$. Starting from $[x_{0},b)$, part [](#parta){.pf-ref} applied to the triple $x_{0}<x_{1}<b$ gives that $[x_{0},x_{1})$ and $[x_{1},b)$ have the order type of $[0,1)$; applying it again to $x_{i}<x_{i+1}<b$ with $[x_{i},b)$ in hand gives $[x_{i},x_{i+1})$, and induction on $i$ gives every $[x_{i},x_{i+1})$.

Conversely, suppose each $[x_{i},x_{i+1})$ has the order type of $[0,1)$, and choose order-preserving bijections $f_{i}\colon[x_{i},x_{i+1})\to[1-2^{-i},1-2^{-i-1})$. The intervals $[x_{i},x_{i+1})$ for $i\in\NN$ are pairwise disjoint with union $[x_{0},b)$: a point $x$ of $[x_{0},b)$ satisfies $x<b=\sup_{i}x_{i}$, so $x<x_{i+1}$ for some $i$, and taking $i$ least with $x<x_{i+1}$ gives $x\geq x_{i}$, so $x\in[x_{i},x_{i+1})$; and $b\notin[x_{i},x_{i+1})$ for every $i$. The intervals $[1-2^{-i},1-2^{-i-1})$ likewise partition $[0,1)$. So the $f_{i}$ fit together into a bijection $f\colon[x_{0},b)\to[0,1)$. It preserves order: for $x<y$ in the same piece this is the corresponding $f_{i}$, and for $x\in[x_{i},x_{i+1})$ and $y\in[x_{j},x_{j+1})$ with $x<y$ one has $i<j$ and hence $f(x)<1-2^{-i-1}\leq 1-2^{-j}\leq f(y)$.
:::
:::

::: {.pf-step #partc}
(c) $[a_{0}\times0,\ a\times0)$ has the order type of $[0,1)$ for every $a\in S_{\Omega}$ with $a\neq a_{0}$.

::: pf-proof
This is transfinite induction on $a\in S_{\Omega}$, $a>a_{0}$. In the base case $a$ is the successor $a_{0}^{+}$ of $a_{0}$, and the interval is $\{a_{0}\}\times[0,1)$, which is $[0,1)$ in the dictionary order; no induction hypothesis is needed here, and this base case is what the source's proof records.

If $a=b^{+}$ is a successor with $b>a_{0}$, then $[a_{0}\times0,\ b\times0)$ has the order type of $[0,1)$ by induction, and $[b\times0,\ a\times0)=\{b\}\times[0,1)$ does as well; part [](#parta){.pf-ref} applied to $a_{0}\times0<b\times0<a\times0$ gives the order type of $[a_{0}\times0,\ a\times0)$.

If $a$ is not a successor, there is a strictly increasing sequence $a_{i}$ in $S_{\Omega}$ with $a=\sup_{i}a_{i}$. Each $[a_{0}\times0,\ a_{i}\times0)$ has the order type of $[0,1)$ by induction, so part [](#parta){.pf-ref} applied to $a_{0}\times0<a_{i}\times0<a_{i+1}\times0$ gives the same for each $[a_{i}\times0,\ a_{i+1}\times0)$, and $a\times0=\sup_{i}(a_{i}\times0)$ in the dictionary order, so part [](#partb){.pf-ref} gives it for $[a_{0}\times0,\ a\times0)$.

Transfinite induction covers every $a\in S_{\Omega}$ above $a_{0}$.
:::
:::

::: {.pf-step #partd}
(d) $L$ is path connected.

::: pf-proof
Let $a_{1}=a_{0}^{+}$, so that $a_{1}\times0\in L$. Two facts about order type are used. A subset of an ordered set that has the order type of $[0,1)$ or of $(0,1)$ carries the order topology of its ordering, and so is homeomorphic to that interval of $\RR$; intervals of $\RR$ are path connected (Theorem 24.1, printed p. 153). Hence by part [](#partc){.pf-ref} each $[a_{0}\times0,\ a\times0)$ with $a>a_{0}$ is homeomorphic to $[0,1)$ and each $\{a\}\times[0,1)$ is homeomorphic to $[0,1)$.

First, a point $a_{0}\times t$ with $t\in(0,1)$ can be joined to $a_{1}\times0$ by a path in $L$: both lie in $[a_{0}\times0,\ a_{2}\times0)$ with $a_{2}=a_{1}^{+}$, which has the order type of $[0,1)$ by part [](#partc){.pf-ref} and is path connected.

Second, let $b\in S_{\Omega}$ with $b\geq a_{1}$ and $t\in[0,1)$. The point $b\times t$ lies in $\{b\}\times[0,1)$, which is homeomorphic to $[0,1)$, so it can be joined to $b\times0$ by a path there. If $b=a_{1}$ that path already ends at $a_{1}\times0$. If $b>a_{1}$, then $b\times0$ and $a_{1}\times0$ both lie in $[a_{1}\times0,\ b^{+}\times0)$, which has the order type of $[0,1)$ by part [](#parta){.pf-ref} applied to $a_{0}\times0<a_{1}\times0<b^{+}\times0$ using part [](#partc){.pf-ref}; so they can be joined by a path there.

Concatenating, every point of $L$ can be joined to $a_{1}\times0$, so $L$ is path connected.
:::
:::

::: {.pf-step #parte}
(e) Every point of $L$ has a neighbourhood homeomorphic with an open interval of $\RR$.

::: pf-proof
For a point $a_{0}\times t$ with $t\in(0,1)$, the set $\{a_{0}\}\times(0,1)$ is the open interval $(a_{0}\times0,\ a_{1}\times0)$ of $L$, has the order type of $(0,1)$, and is homeomorphic to $(0,1)$.

For a point $b\times t$ with $b>a_{0}$ and $t\in[0,1)$, let $b^{+}$ be the successor of $b$. The open interval $(a_{0}\times0,\ b^{+}\times0)$ of $L$ contains $b\times t$, because $a_{0}\times0<b\times t<b^{+}\times0$. Its order type is that of $(0,1)$: the interval $[a_{0}\times0,\ b^{+}\times0)$ has the order type of $[0,1)$ by part [](#partc){.pf-ref}, and deleting its least point, which is $a_{0}\times0$ and is not in $L$, leaves the order type of $(0,1)$. So it is homeomorphic to the open interval $(0,1)$ of $\RR$.
:::
:::

::: {.pf-step #partf}
(f) $L$ cannot be imbedded in $\RR^{n}$, for any $n$.

::: pf-proof
A subspace of $\RR^{n}$ has a countable basis: the balls with centre in $\QQ^{n}$ and positive rational radius form a countable basis for $\RR^{n}$, and their intersections with a subspace $A$ form a basis for $A$.

In a space with a countable basis $\mathcal{B}$, every family of pairwise disjoint nonempty open sets is countable: each member $U$ of the family contains some basis element $B_{U}$, since it is nonempty and open, and $U\neq V$ for disjoint nonempty $U,V$ forces $B_{U}\neq B_{V}$, so $U\mapsto B_{U}$ is an injection into the countable set $\mathcal{B}$.

For each $b\in S_{\Omega}$ with $b\neq a_{0}$, the set $\{b\}\times(0,1)$ is the open interval $(b\times0,\ b^{+}\times0)$ of $L$, hence is nonempty and open there; distinct $b$ give disjoint sets, since the second coordinate of a point of $\{b\}\times(0,1)$ determines $b$. There are uncountably many such $b$, because $S_{\Omega}$ is uncountable and $a_{0}$ is one point.

So $L$ has an uncountable family of pairwise disjoint nonempty open sets, has no countable basis, and therefore is not homeomorphic with any subspace of $\RR^{n}$.
:::
:::

:::

:::
