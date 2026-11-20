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

(c) First, one-point sets are closed, so $X$ is $T_1$: given distinct points $y\ne z$, a short horizontal segment through $z$ avoiding both $y$ and the points $p_{n,k}$ is a type-(i) neighbourhood of $z$ missing $y$ when $z$ is an ordinary point, a type-(ii) neighbourhood with $F$ enlarged by $y$ does the same when $z=p_{n,k}$, and the type-(iii) sets $B_m$ with $m$ large contain $z$ but not $y$ while the type-(iv) sets with $m$ small do the same for $z=b$.

We prove regularity by shrinking basis neighbourhoods: for a point $x$ and a basis element $B\ni x$, a basis element $V$ with $x\in V$ and $\overline{V}\subseteq B$ is produced, which is the form the axiom takes in a space whose one-point sets are closed.

**The sets $C_{n,k}$ are closed.** Let $z\in X-C_{n,k}$. If $z=(m,y)$ lies on a line $L_m$, with $m$ even, then every point of $C_{n,k}$ has first coordinate in $[n-1+1/k,n+1-1/k]$ and $\abs{m-n}\ge1$, so the horizontal distance from $z$ to $C_{n,k}$ is at least $1/k$; a horizontal segment about $z$ of half-width less than $1/k$ and less than $1$, which contains no $p_{n',k'}$ because the top points on the horizontal line through $z$ lie at odd integers, is a type-(i) neighbourhood of $z$ missing $C_{n,k}$. If $z$ is an ordinary point of some $C_{n',k'}$, or a top point $p_{n',k'}$, with $(n',k')\ne(n,k)$, then $C_{n',k'}\cap C_{n,k}$ is finite --- two distinct circles meet in at most two points, a circle meets one of these vertical segments in at most two, and two of the segments are either disjoint or equal, the latter impossible for distinct pairs --- and $p_{n',k'}\notin C_{n,k}$; so $C_{n',k'}$ minus that finite intersection is a type-(ii) neighbourhood of $z$ missing $C_{n,k}$. Finally $a$ has the type-(iii) neighbourhood $B_m$ for any even $m\le n-1$, which misses $C_{n,k}$ because every point of $C_{n,k}$ has first coordinate greater than $n-1$, and $b$ has the type-(iv) neighbourhood with $m\ge n+1$, which misses it for the same reason on the other side.

**Type (i).** Let $B=X\cap((x_0-\epsilon,x_0+\epsilon)\times\{y_0\})$ contain $x$ and contain no $p_{n,k}$, and let $B'=X\cap((x_0-\epsilon',x_0+\epsilon')\times\{y_0\})$ with $0<\epsilon'<\epsilon$. Then $\overline{B'}\subseteq B$, because a point $z\in X-B$ is separated from $B'$ by a basis element containing it: if $z$ has second coordinate $y_0$ and $\abs{x_z-x_0}\ge\epsilon$, a horizontal segment about $z$ at height $y_0$, short enough to miss $B'$ and to contain no $p_{n,k}$, which is possible because the top points on that line lie at odd integers; if $z$ has second coordinate $y_z\ne y_0$ and is an ordinary point of its line or its circle, a short horizontal segment at height $y_z$ misses $B'$; if $z=p_{n,k}$, the set obtained from $C_{n,k}$ by deleting the finitely many of its points that lie in $B'$ is a type-(ii) neighbourhood of $z$ missing $B'$, and it contains $z$ because $z\notin B'$; and $a$ is separated from $B'$ by $B_m$ for an even $m<x_0-\epsilon'$, and $b$ by the type-(iv) set for an even $m>x_0+\epsilon'$.

**Type (ii).** Let $x=p_{n,k}$ and $B=C_{n,k}\setminus F$ with $F$ finite and $p_{n,k}\notin F$. No point of $F$ is a top point, since $C_{n,k}$ meets $\{p_{n',k'}\}$ only at $p_{n,k}$; so each $z\in F$ is an ordinary point of $C_{n,k}$, and a horizontal segment through $z$ short enough to contain no $p_{n',k'}$ meets $C_{n,k}$ in $z$ alone, a horizontal line meeting $C_{n,k}$ in at most four points, pairwise separated. Such a segment is a type-(i) basis element, so $F$ is open in the subspace $C_{n,k}$ and $B$ is closed in $C_{n,k}$; and $C_{n,k}$ is closed in $X$, so $B$ is closed in $X$. Since $x\in B$, the set $B$ itself is a basis element with $\overline{B}=B\subseteq B$.

**Types (iii) and (iv).** Let $B_m=\{a\}\cup\{(x,y)\in X:x<m\}$ with $m$ even and take an even $m'<m$. If $z\notin B_m$ then $z\ne a$ and $x_z\ge m$, and $z$ has a basis element containing it and missing $B_{m'}$: for an ordinary point $z$ a horizontal segment at its own height and of half-width less than $m-m'$ stays at first coordinate greater than $m'$; for $z=p_{n,k}$ one has $n\ge m$, so every point of $C_{n,k}$ has first coordinate at least $n-1+1/k\ge m-1+1/k>m'$, and the type-(ii) set $C_{n,k}$ itself is a neighbourhood of $z$ missing $B_{m'}$. Hence $\overline{B_{m'}}\subseteq B_m$. The type-(iv) case at $b$ is symmetric, with $m'>m$.

Thus every point and every basis element containing it admit a basis element with closure inside the given one, so $X$ is regular.

It is not completely regular. The points $a\ne b$ are closed, but part (b) shows that every continuous real-valued function on $X$ satisfies $f(a)=f(b)$. Complete regularity would provide a continuous $f:X\to[0,1]$ separating $a$ from the closed set $\{b\}$, impossible. Hence $X$ is regular but not completely regular.
:::
