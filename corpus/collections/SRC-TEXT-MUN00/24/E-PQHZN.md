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
