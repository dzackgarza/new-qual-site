---
schema: qual/card@1
id: E-OHHSA
kind: problem
title: A regular space that is not completely regular
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 33 Exercise 11, printed p. 214,
    and repaired. No complete published solution was located: dbFin, "Section 33: Problem 11
    Solution", https://dbfin.com/topology/munkres/chapter-4/section-33-the-urysohn-lemma/problem-11-solution/
    (read 2026-11-10; kept at tmp/sources/dbfin/section-33-the-urysohn-lemma/problem-11-solution.txt)
    answers (a) by a table of the ten intersections among the four basis types, which is a genuine
    check, but its (b) and (c) are too compressed to follow (the countability of S_{n,k} is asserted
    without the G_delta step, and the limit f((n-1) x d) = lim f(p_{n,k}) is not derived); Moller's
    S33 stops at Exercise 8 in this section, Doug's World at Problem 33.8, and Orellana has
    Exercises 1 and 3 only. What was repaired: part (c) now shows first that one-point sets are
    closed, which Munkres's regularity and complete regularity both require and which the card had
    omitted, and then shrinks basis neighbourhoods of the four types; part (b) derives the
    countability of S_{n,k} from the G_delta property of the level set and the finiteness of the
    deleted sets, which is the step the printed text leaves to the reader. This exercise is in the
    COMPLAINTS.md entry.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Read for #169 against Munkres, Topology (2000), Section 33 Exercise 11, printed p. 214, and
    repaired in parts (b) and (c), where the argument had been asserted rather than proved. Part
    (b): for an arbitrary open $U_r$ containing $p_{n,k}$ the step took a type-(ii) neighbourhood
    $C_{n,k}\setminus F_r$ inside it, which needs the refinement that a basis element containing
    $p_{n,k}$ and not of type (ii) contains all of $C_{n,k}$ -- true of type (iii) because $n<m$
    with $m$ even gives $m\ge n+1>n+1-1/k$, and of type (iv) because $m<n$ gives
    $m\le n-1<n-1+1/k$ -- and the refinement is now written. Part (c): the regularity argument
    rested on "$C_{n,k}$ is closed in $X$", which was asserted, and its two closure claims for a
    type-(i) segment and for a type-(iii) set were asserted too. All three are now proved. $C_{n,k}$
    is closed: a point of the complement on a line $L_m$ has horizontal distance at least $1/k$
    from it and a short type-(i) segment about it meets it nowhere; a point on another circle, or
    a top point of another circle, is separated by deleting the finite intersection
    $C_{n',k'}\cap C_{n,k}$, which is finite because two distinct circles meet twice, a circle
    meets a vertical segment twice, and the segments are disjoint for distinct pairs; and $a$ and
    $b$ are separated by the one-sided basis sets with $m\le n-1$ and $m\ge n+1$. The closure of a
    type-(i) segment inside a larger one is settled by separating each point outside the larger one
    in four cases, of which the top point is the one that needs a type-(ii) neighbourhood, the
    others being a horizontal segment at the point's own height or the one-sided sets for $a$ and
    $b$. The closure of $B_{m'}$ inside $B_m$ is settled by a basis element about any point outside
    $B_m$ that misses $B_{m'}$, the top-point case using $n\ge m$ and $n-1+1/k>m'$. Re-read and
    unchanged: the countability of each $S_{n,k}$ from the $G_\delta$ property, the choice of $d$,
    the two limits and $f(a)=f(b)$; the $T_1$ argument; and the conclusion that $X$ is regular but
    not completely regular. What the repair changes in the audit trail: the earlier note's "four
    types" are three headings here, types (iii) and (iv) being handled together. Not checked: the
    folio, the checkout's extraction carrying only three page-range markers at this pass.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Part (a) is converted to numbered steps, the first of three commits on this card; parts (b) and (c)
    remain prose and are converted in the next two commits. Part (a) is now three steps, each with a
    `pf-proof`: the four basis families (i)--(iv) cover $X$; the intersection condition in its four
    cases, the type-(iii) and type-(iv) cutoffs at $a$ and $b$, the finite exceptional sets at a top
    point $p_{n,k}$, a short horizontal segment at any other point, and the half-plane shortening when
    a type-(iii) or type-(iv) set meets a type-(i) or type-(ii) one; and the conclusion that these are
    the two conditions for a basis (Munkres, §13). The statement and the four basis types are cited by
    number, no page. Not checked in this commit: nothing of parts (b) and (c) was touched or re-read.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Part (b) is converted to numbered steps, the second of three commits on this card; part (c) remains
    prose and is converted in the next commit. Part (b) is now three steps, each with a `pf-proof`: the
    level set of a continuous real-valued function is a $G_\delta$; the countability of $S_{n,k}$, from
    the fact that a basis element through $p_{n,k}$ is of type (ii), (iii) or (iv) and the last two
    contain all of $C_{n,k}$ by the parity of $m$ against $n\pm1$, so that each $U_r$ contains
    $C_{n,k}$ minus a finite set; and the choice of $d$ outside countably many ordinates, the two
    sequences $q^\pm_{n,k}$, their limits by the type-(i) neighbourhoods, and the conclusion
    $f(a)=f(b)$ through the type-(iii) and type-(iv) neighbourhoods. The statement and the basis types
    are cited by number, no page. Not checked in this commit: nothing of part (c) was touched or
    re-read.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Part (c) is converted to numbered steps, the third and last commit on this card, and the card is now
    wholly structured: ten steps in three `pf` blocks, each step with a `pf-proof`. Part (c) is four
    steps: one-point sets are closed, giving $T_1$; each $C_{n,k}$ is closed, separating a point off it
    on a line $L_m$ by horizontal distance at least $1/k$, on another $C_{n',k'}$ by the finiteness of
    the intersection, and the points $a,b$ by the one-sided type-(iii) and type-(iv) sets; every basis
    element of each of the four types contains one whose closure lies inside it, including the
    closedness of $C_{n,k}\setminus F$ used in type (ii); and $X$ is regular by Theorem 33.1 while it
    is not completely regular, because part (b) forces $f(a)=f(b)$ for every continuous real-valued
    $f$, so no such function separates $a$ from the closed set $\{b\}$. Cited by number: Munkres §33
    Exercise 11, Theorem 33.1, and the basis types (i)--(iv). No page in the new text.

---

::: {.exercise}

Define a set $X$ as follows.
For each even integer $m$, let $L_m$ denote the line segment $m \times [-1, 0]$ in the plane.
For each odd integer $n$ and each integer $k \geq 2$, let $C_{n,k}$ denote the union of the line segments $(n + 1 - 1/k) \times [-1, 0]$ and $(n - 1 + 1/k) \times [-1, 0]$ and the semicircle

$$
\theset{x \times y \mid (x - n)^2 + y^2 = (1 - 1/k)^2 \text{ and } y \geq 0}
$$

in the plane.
Let $p_{n,k}$ denote the topmost point $n \times (1 - 1/k)$ of this semicircle.
Let $X$ be the union of all the sets $L_m$ and $C_{n,k}$, along with two extra points $a$ and $b$.
Topologize $X$ by taking sets of the following four types as basis elements:

(i) The intersection of $X$ with a horizontal open line segment that contains none of the points $p_{n,k}$.

(ii) A set formed from one of the sets $C_{n,k}$ by deleting finitely many points.

(iii) For each even integer $m$, the union of $\theset{a}$ and the set of points $x \times y$ of $X$ for which $x < m$.

(iv) For each even integer $m$, the union of $\theset{b}$ and the set of points $x \times y$ of $X$ for which $x > m$.

(a) Sketch $X$; show that these sets form a basis for a topology on $X$.

(b) Let $f$ be a continuous real-valued function on $X$.
Show that for any $c$, the set $f^{-1}(c)$ is a $G_\delta$ set in $X$.
(This is true for any space $X$.)
Conclude that the set $S_{n,k}$ consisting of those points $p$ of $C_{n,k}$ for which $f(p) \neq f(p_{n,k})$ is countable.
Choose $d \in [-1, 0]$ so that the line $y = d$ intersects none of the sets $S_{n,k}$.
Show that for $n$ odd,

$$
f((n - 1) \times d) = \lim_{k \to \infty} f(p_{n,k}) = f((n + 1) \times d).
$$

Conclude that $f(a) = f(b)$.

(c) Show that $X$ is regular but not completely regular.
:::

::: {.solution}
::: pf

::: {.pf-step #basis-covers}
(a) The four families (i)--(iv) cover $X$.

::: pf-proof
An ordinary point of a segment $L_m$ or of a set $C_{n,k}$, other than a top point $p_{n,k}$, lies in a basis element of type (i): a short horizontal open segment about it contains no $p_{n,k}$. Each top point $p_{n,k}$ lies in the type-(ii) set $C_{n,k}$ itself, which is that set with no points deleted. The point $a$ lies in the type-(iii) set $B_m$ for every even $m$ larger than the first coordinate of every point considered so far, and in particular for $m$ larger than any given first coordinate, and $b$ lies in the type-(iv) sets similarly.
:::

:::

::: {.pf-step #basis-intersection}
(a) The intersection of two basis elements containing a point $x$ contains a basis element containing $x$, so the four families form a basis for a topology on $X$.

::: pf-proof
Four cases. If $x=a$, the type-(iii) sets $B_m$ decrease with $m$, so the smaller of the two cutoffs gives a $B_m$ inside both; the case $x=b$ with type-(iv) sets is the same with the order reversed. If $x=p_{n,k}$, intersecting two basis elements containing it can be refined by deleting from $C_{n,k}$ the union of the two finite exceptional sets, which is again a type-(ii) set containing $p_{n,k}$. If $x$ is any other point of $X$, a sufficiently short horizontal open segment about $x$ avoids the finitely many excluded points and the finitely many top points of the two basis elements, and lies inside their intersection; that is a type-(i) set containing $x$. An intersection of a type-(iii) or type-(iv) set with an ordinary or type-(ii) neighbourhood is handled by shortening the latter inside the half-plane the former prescribes, which keeps a type-(i) or type-(ii) set containing $x$.
:::

:::

::: {.pf-step #part-a}
(a) The families (i)--(iv) are a basis for a topology on $X$.

::: pf-proof
Step [#basis-covers]{.pf-ref} gives the covering condition and step [#basis-intersection]{.pf-ref} the intersection condition, which are the two conditions for a basis of a topology (Munkres, §13).
:::

:::

:::

::: pf

::: {.pf-step #level-gdelta}
(b) For every continuous $f:X\to\RR$ and every $c$ the level set $f^{-1}(c)$ is a $G_\delta$ in $X$.

::: pf-proof
$f^{-1}(c)=\bigcap_{r=1}^{\infty}f^{-1}((c-1/r,c+1/r))$, an intersection of countably many open sets, each inverse image of an open interval under the continuous $f$.
:::

:::

::: {.pf-step #countable-exceptions}
(b) For odd $n$ and $k\ge2$, the set $S_{n,k}=\{p\in C_{n,k}:f(p)\ne f(p_{n,k})\}$ is countable.

::: pf-proof
Put $c=f(p_{n,k})$ and write the $G_\delta$ set $f^{-1}(c)=\bigcap_rU_r$ with each $U_r$ open and containing $p_{n,k}$, which step [#level-gdelta]{.pf-ref} allows. A basis element containing $p_{n,k}$ is of type (ii), (iii) or (iv): type (i) is excluded because a horizontal open segment through $p_{n,k}$ contains that point, and types (iii) and (iv) contain all of $C_{n,k}$, since a type-(iii) element $B_m$ containing $p_{n,k}$ has $n<m$ with $m$ even, hence $m\ge n+1>n+1-1/k$, so every point of $C_{n,k}$ has first coordinate below $m$, while a type-(iv) element containing $p_{n,k}$ has $m<n$, hence $m\le n-1<n-1+1/k$, so every point of $C_{n,k}$ has first coordinate above $m$. Each $U_r$ therefore contains $C_{n,k}$ minus a finite set $F_r$, and $S_{n,k}\subseteq\bigcup_rF_r$ is a countable union of finite sets.
:::

:::

::: {.pf-step #part-b}
(b) Choosing $d\in[-1,0]$ outside the countably many ordinates occurring in the sets $S_{n,k}$, one has $f((n-1)\times d)=f((n+1)\times d)$ for odd $n$, and consequently $f(a)=f(b)$.

::: pf-proof
The pairs $(n,k)$ are countable and each $S_{n,k}$ is countable by step [#countable-exceptions]{.pf-ref}, so the set of ordinates of points of $\bigcup S_{n,k}$ is countable and some $d\in[-1,0]$ avoids it. For that $d$ the points $q^-_{n,k}=(n-1+1/k,d)$ and $q^+_{n,k}=(n+1-1/k,d)$ lie in $C_{n,k}\setminus S_{n,k}$, so $f(q^-_{n,k})=f(p_{n,k})=f(q^+_{n,k})$; as $k\to\infty$ these converge to $(n-1,d)$ and $(n+1,d)$, by the type-(i) horizontal neighbourhoods, and continuity gives $f((n-1)\times d)=\lim_kf(p_{n,k})=f((n+1)\times d)$. Hence $f$ takes one value $c_0$ at all points $(m,d)$ with $m$ even, and $(m,d)\to a$ as $m\to-\infty$ through even integers while $(m,d)\to b$ as $m\to+\infty$, by the type-(iii) and type-(iv) definitions; so $f(a)=c_0=f(b)$.
:::

:::

:::

::: pf

::: {.pf-step #t1}
(c) One-point sets in $X$ are closed, so $X$ is $T_1$.

::: pf-proof
Let $y\ne z$. If $z$ is an ordinary point, a short horizontal segment through $z$ avoiding $y$ and the top points $p_{n,k}$ is a type-(i) neighbourhood of $z$ missing $y$ if $y$ has the same height, and otherwise any short type-(i) segment through $z$ misses $y$; if $z=p_{n,k}$, the type-(ii) set obtained from $C_{n,k}$ by deleting $y$ as well is a neighbourhood of $z$ missing $y$; if $z=a$ (respectively $z=b$), the type-(iii) sets $B_m$ with $m$ large (the type-(iv) sets with $m$ small) contain $z$ and miss $y$ once $\abs{m}$ exceeds the modulus of $y$'s first coordinate.
:::

:::

::: {.pf-step #c-closed}
(c) Each $C_{n,k}$ is closed in $X$.

::: pf-proof
Let $z\in X-C_{n,k}$. If $z=(m,y)$ lies on a line $L_m$, then every point of $C_{n,k}$ has first coordinate in $[n-1+1/k,n+1-1/k]$ and $\abs{m-n}\ge1$, so the horizontal distance from $z$ to $C_{n,k}$ is at least $1/k$, and a horizontal segment about $z$ of half-width below $1/k$ and below $1$, containing no $p_{n',k'}$ because the top points on that line lie at odd integers, is a type-(i) neighbourhood missing $C_{n,k}$. If $z$ is an ordinary point of $C_{n',k'}$, or a top point $p_{n',k'}$, with $(n',k')\ne(n,k)$, then $C_{n',k'}\cap C_{n,k}$ is finite, since two circles meet in at most two points, a circle meets one of these segments in at most two, and two of the segments are disjoint or equal, the latter impossible; so $C_{n',k'}$ minus that finite intersection is a type-(ii) neighbourhood of $z$ missing $C_{n,k}$, and it contains $z$ because $z\notin C_{n,k}$. Finally $a$ has the type-(iii) set $B_m$ for even $m\le n-1$, which misses $C_{n,k}$ as every point of $C_{n,k}$ has first coordinate above $n-1$, and $b$ has the type-(iv) set with $m\ge n+1$.
:::

:::

::: {.pf-step #c-shrink}
(c) Every basis element $B\ni x$ contains a basis element $V\ni x$ with $\overline V\subseteq B$, in each of the four types.

::: pf-proof
Type (i): let $B=X\cap((x_0-\epsilon,x_0+\epsilon)\times\{y_0\})$ contain no $p_{n,k}$ and let $V$ be the same with $0<\epsilon'<\epsilon$. A point $z\in X-B$ is separated from $V$ by a basis element: if $z$ has height $y_0$ and $\abs{x_z-x_0}\ge\epsilon$, a short horizontal segment at that height misses $V$; if $z$ has another height and is ordinary, a short horizontal segment misses $V$; if $z=p_{n,k}$, then $C_{n,k}$ minus the finitely many of its points in $V$ is a type-(ii) neighbourhood of $z$ missing $V$; and $a$ is separated from $V$ by $B_m$ for even $m<x_0-\epsilon'$, $b$ by the type-(iv) set for even $m>x_0+\epsilon'$. Type (ii): let $x=p_{n,k}$ and $B=C_{n,k}\setminus F$ with $F$ finite not containing $p_{n,k}$. No point of $F$ is a top point, so each $z\in F$ is ordinary and a short horizontal segment through $z$ meets $C_{n,k}$ in $z$ alone, $F$ being open in the subspace $C_{n,k}$; then $B$ is closed in $C_{n,k}$ and $C_{n,k}$ is closed in $X$ by step [#c-closed]{.pf-ref}, so $B$ is closed in $X$ and $V=B$ serves. Types (iii) and (iv): for $B_m$ with $m$ even take an even $m'<m$ and $V=B_{m'}$; a point $z\notin B_m$ has a basis element missing $B_{m'}$ — a horizontal segment of half-width below $m-m'$ at an ordinary point, a type-(ii) set about $p_{n,k}$ with $n\ge m$ (so every point of $C_{n,k}$ has first coordinate at least $n-1+1/k>m'$), and the type-(iv) sets for $b$ — so $\overline{B_{m'}}\subseteq B_m$; the type-(iv) case is the mirror image in $x\mapsto-x$.
:::

:::

::: {.pf-step #part-c}
(c) $X$ is regular but not completely regular.

::: pf-proof
Steps [#t1]{.pf-ref} and [#c-shrink]{.pf-ref} show that $X$ is $T_1$ and that every basis neighbourhood of a point contains a smaller one whose closure lies inside it, which is regularity for a $T_1$ space (Munkres, Theorem 33.1). For complete regularity, part (b) shows that every continuous $f:X\to\RR$ satisfies $f(a)=f(b)$; so no continuous real-valued function separates the point $a$ from the closed set $\{b\}$, and $X$ is not completely regular.
:::

:::

:::

:::