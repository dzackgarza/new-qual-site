---
schema: qual/card@1
id: E-X4TVL
kind: problem
title: Rational and irrational anti-diagonals in the Sorgenfrey plane
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
    Checked line by line against Munkres, Topology (2000), Section 31 Exercise 9, printed p. 200,
    and against Exercise 5 of Section 27 (a compact Hausdorff space is not the union of countably
    many closed sets with empty interior, printed p. 178) and Lemma 13.2. The four parts run as the
    book indicates: (a) each irrational point of [0,1] is in some K_n because V is open, the
    rational points are countably many singletons; (b) the contrapositive of the Baire exercise
    applied to the closed sets cl(K_n) and the singletons; (c) the interpolation between a point
    t of K_n just below x and the point (x, -x + eps), which needs t in the interval
    (max{a, x - eps}, x), nonempty because K_n is dense in (a,b); (d) every basis element about
    (q,-q) is [c,d) x [e,f) with c <= q < d and e <= -q < f, and it contains (q,-q+eps) for small
    eps. No published solution was located: the only treatment found is the HTML page
    dbfin.com/topology/munkres/chapter-4/section-31-the-separation-axioms/problem-9-solution/,
    which prints no pagination and is therefore not cited from a card; Orellana's Section 31 stops
    at Exercise 6, "Doug's World" at Problem 31.7, and no other retained set reaches Chapter 4. The
    search is recorded in the COMPLAINTS.md entry for this batch.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: dbFin, "Section 31: Problem 9 Solution",
    https://dbfin.com/topology/munkres/chapter-4/section-31-the-separation-axioms/problem-9-solution/
    (read 2026-11-10; the text is kept at
    tmp/sources/dbfin/section-31-the-separation-axioms/problem-9-solution.txt), checked against
    Munkres, Topology (2000), Section 31 Exercise 9, printed p. 200, and Exercise 5 of Section 27,
    printed p. 178. Its four parts are the card's: (a) each irrational point of [0,1] lies in some
    K_n because V is open, the rational points being countably many singletons; (b) the Baire
    exercise applied to the closed sets cl(K_n) and the singletons; (c) interpolating between a
    point of K_n just below x and (x,-x+eps); (d) every basis element about (q,-q) contains such a
    point. What was corrected: in (c) the source writes "for each x in A and 0 < delta < 1/n there
    is a point z in (x - delta, x) cap K_n", using delta for the epsilon of the statement, and it
    replaces the printed parallelogram (a,b) x (0,1/n) by the smaller (a+eps, b-eps); the card keeps
    the printed parallelogram and the symbol eps throughout. The source's (b) writes the union of
    the cl(K_n) and the single rational points as having non-empty interior, which is the
    contrapositive of the printed exercise; the card states it that way. This supersedes the
    previous note, which recorded that no published solution had been found.
---

::: {.exercise}

Let $A$ be the set of all points of $\RR_\ell^2$ of the form $x \times (-x)$, for $x$ rational; let $B$ be the set of all points of this form for $x$ irrational.
If $V$ is an open set of $\RR_\ell^2$ containing $B$, show there exists no open set $U$ containing $A$ that is disjoint from $V$, as follows:

(a) Let $K_n$ consist of all irrational numbers $x$ in $[0, 1]$ such that $[x, x + 1/n) \times [-x, -x + 1/n)$ is contained in $V$.
Show that $[0, 1]$ is the union of the sets $K_n$ and countably many one-point sets.

(b) Use Exercise 5 of §27 to show that some set $\overline{K}_n$ contains an open interval $(a, b)$ of $\RR$.

(c) Show that $V$ contains the open parallelogram consisting of all points of the form $x \times (-x + \epsilon)$ for which $a < x < b$ and $0 < \epsilon < 1/n$.

(d) Conclude that if $q$ is a rational number with $a < q < b$, then the point $q \times (-q)$ of $\RR_\ell^2$ is a limit point of $V$.
:::

::: {.solution}
(a) For each irrational $x\in[0,1]$, the point $(x,-x)$ lies in the open set $V$. Hence there is $\varepsilon_x>0$ such that
$$
[x,x+\varepsilon_x)\times[-x,-x+\varepsilon_x)\subset V.
$$
Choose $n$ with $1/n<\varepsilon_x$. Then $x\in K_n$. Thus every irrational point of $[0,1]$ lies in some $K_n$, while the rational points form a countable union of one-point sets. Therefore
$$
[0,1]=\bigcup_{n\ge1}K_n\ \cup\ \bigcup_{q\in\QQ\cap[0,1]}\{q\}.
$$

(b) If every $\overline{K_n}$ had empty interior, then the compact Hausdorff space $[0,1]$ would be a countable union of closed sets with empty interior, together with countably many singleton closed sets, also of empty interior. This contradicts the Baire-category exercise of §27. Hence some $\overline{K_n}$ contains a nonempty open interval $(a,b)$.

(c) Since $(a,b)\subset\overline{K_n}$, the set $K_n$ is dense in $(a,b)$. Fix
$$
a<x<b,\qquad 0<\epsilon<1/n.
$$
Choose
$$
t\in K_n\cap(\max\{a,x-\epsilon\},x).
$$
Then $t<x<t+1/n$, and $t>x-\epsilon$ implies
$$
-t<-x+\epsilon.
$$
Also $t<x<x-\epsilon+1/n$, so
$$
-x+\epsilon<-t+1/n.
$$
Therefore
$$
(x,-x+\epsilon)\in[t,t+1/n)\times[-t,-t+1/n)\subset V.
$$
Thus $V$ contains the stated open parallelogram.

(d) Let $q\in(a,b)\cap\QQ$. Every basic neighborhood of $(q,-q)$ in the Sorgenfrey plane contains a point
$$
(q,-q+\epsilon)
$$
with $0<\epsilon<1/n$ sufficiently small. By (c) this point lies in $V$, and it differs from $(q,-q)$. Hence $(q,-q)$ is a limit point of $V$.

Now if $U$ were an open set containing $A$ and disjoint from $V$, then $U$ would contain $(q,-q)$, but every neighborhood of this point meets $V$, contradiction. Therefore no open neighborhood of $A$ is disjoint from $V$.
:::
