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
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2, the four printed steps as the top-level parts and
    the conclusion as the QED step. Re-checked: $V$ is open in the Sorgenfrey plane, so a basic
    half-open rectangle about each irrational point $(x,-x)$ lies in $V$, giving $x\in K_n$ for some
    $n$; $[0,1]$ is compact Hausdorff, hence Baire, so some $\overline{K_n}$ has nonempty interior;
    the density of $K_n$ in $(a,b)$ yields $t$ with $t<x<t+1/n$ and $-t<-x+\varepsilon<-t+1/n$,
    which puts $x\times(-x+\varepsilon)$ inside the rectangle $[t,t+1/n)\times[-t,-t+1/n)\subseteq V$;
    and every basic neighbourhood of $q\times(-q)$ contains such a point, so $(q,-q)$ is a limit
    point of $V$, which contradicts an open $U\ni A$ disjoint from $V$. Added: the description of the
    basic open sets of the Sorgenfrey plane, the two inequalities pinning the second coordinate, and
    the density of the rationals. One presentation repair: the statement wrote `\epsilon`, which
    STYLE-04 spells `\varepsilon`; the wording is unchanged. No defect found in the statement, §31
    Exercise 8. No retained solution set covers the exercise.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The card said "No retained solution set covers this exercise", and that is false: dbFin's Section
    31 problem 9 solution is exactly this exercise and is retained at
    `tmp/sources/dbfin/section-31-the-separation-axioms/problem-9-solution.txt`, read 2026-11-10 from
    https://dbfin.com/topology/munkres/chapter-4/section-31-the-separation-axioms/problem-9-solution/.
    Its four parts are the card's four: the $K_n$ cover of $[0,1]$, the Baire-category step citing
    Exercise 5 of §27, the interval on which $x\mapsto(-x,-x+\varepsilon)$ lies in $V$, and the
    limit-point conclusion at each rational $q$. The rendered sentence now cites it and says what the
    card adds, namely the two inequalities that place $x\times(-x+\varepsilon)$ in the rectangle
    $[t,t+1/n)\times[-t,-t+1/n)$.
---

::: {.exercise}

Let $A$ be the set of all points of $\RR_\ell^2$ of the form $x \times (-x)$, for $x$ rational; let $B$ be the set of all points of this form for $x$ irrational.
If $V$ is an open set of $\RR_\ell^2$ containing $B$, show there exists no open set $U$ containing $A$ that is disjoint from $V$, as follows:

(a) Let $K_n$ consist of all irrational numbers $x$ in $[0, 1]$ such that $[x, x + 1/n) \times [-x, -x + 1/n)$ is contained in $V$.
Show that $[0, 1]$ is the union of the sets $K_n$ and countably many one-point sets.

(b) Use Exercise 5 of §27 to show that some set $\overline{K}_n$ contains an open interval $(a, b)$ of $\RR$.

(c) Show that $V$ contains the open parallelogram consisting of all points of the form $x \times (-x + \varepsilon)$ for which $a < x < b$ and $0 < \varepsilon < 1/n$.

(d) Conclude that if $q$ is a rational number with $a < q < b$, then the point $q \times (-q)$ of $\RR_\ell^2$ is a limit point of $V$.
:::

::: {.solution}
The retained published solution is dbFin, *Section 31: Problem 9 Solution* (`https://dbfin.com/topology/munkres/chapter-4/section-31-the-separation-axioms/problem-9-solution/`, read 2026-11-10, kept at `tmp/sources/dbfin/section-31-the-separation-axioms/problem-9-solution.txt`), which runs the same four steps: the $K_n$ cover of $[0,1]$ by Baire category, an interval $(a',b')$ on which $x\mapsto(-x,-x+\varepsilon)$ stays in $V$, and the limit-point conclusion at each rational $q$. The card states the same argument with the inequalities of step (c) written out. Write $\RR_\ell^2$ for the Sorgenfrey plane, whose basic open sets are the half-open rectangles $[x,x+\varepsilon)\times[y,y+\varepsilon')$.

::: pf

::: {.pf-step #part-a}
(a) With $K_n=\{x\in[0,1]\setminus\QQ:[x,x+\tfrac1n)\times[-x,-x+\tfrac1n)\subseteq V\}$, the interval $[0,1]$ is the union of the sets $K_n$ and of countably many one-point sets.

::: pf-proof
For irrational $x\in[0,1]$ the point $(x,-x)$ lies in $B\subseteq V$, and $V$ is open, so there is $\varepsilon_x>0$ with $[x,x+\varepsilon_x)\times[-x,-x+\varepsilon_x)\subseteq V$, a basic neighbourhood of $(x,-x)$; choosing $n$ with $\tfrac1n<\varepsilon_x$ gives $x\in K_n$. The rational points of $[0,1]$ are countably many and each is a one-point set, so they contribute the second family.
:::

:::

::: {.pf-step #part-b}
(b) Some $\overline{K_n}$ contains an interval $(a,b)$ of $\RR$.

::: pf-proof
By step [](#part-a){.pf-ref}, $[0,1]$ is the union of the closed sets $\overline{K_n}$ and the countably many singletons $\{q\}$ with $q$ rational. The space $[0,1]$ is compact Hausdorff, hence a Baire space (Exercise 5 of §27): it is not a countable union of nowhere dense sets. The singletons have empty interior, so unless some $\overline{K_n}$ had nonempty interior the union would be countable and nowhere dense, a contradiction. Hence some $\overline{K_n}$ contains a nonempty open interval $(a,b)$.
:::

:::

::: {.pf-step #part-c}
(c) $V$ contains every point $x\times(-x+\varepsilon)$ with $a<x<b$ and $0<\varepsilon<\tfrac1n$, for the $n$ of step [](#part-b){.pf-ref}.

::: pf-proof
Fix $x\in(a,b)$ and $0<\varepsilon<\tfrac1n$. Since $(a,b)\subseteq\overline{K_n}$, the set $K_n$ is dense in $(a,b)$, so there is $t\in K_n\cap(\max\{a,x-\varepsilon\},x)$. Then $t<x<t+\tfrac1n$ because $t>x-\varepsilon$ and $\varepsilon<\tfrac1n$, so $x\in[t,t+\tfrac1n)$; further $-t<-x+\varepsilon$, and $-x+\varepsilon<-t+\tfrac1n$ because $t<x<x-\varepsilon+\tfrac1n$. Hence $x\times(-x+\varepsilon)\in[t,t+\tfrac1n)\times[-t,-t+\tfrac1n)$, and that rectangle is contained in $V$ because $t\in K_n$.
:::

:::

::: {.pf-step #part-d}
(d) For rational $q$ with $a<q<b$, the point $q\times(-q)$ is a limit point of $V$.

::: pf-proof
A basic neighbourhood of $q\times(-q)$ in the Sorgenfrey plane contains $q\times(-q+\varepsilon)$ for all small $\varepsilon>0$, in particular for some $0<\varepsilon<\tfrac1n$. By step [](#part-c){.pf-ref} that point lies in $V$, and it differs from $q\times(-q)$. So every neighbourhood of $q\times(-q)$ meets $V$ in a point other than it.
:::

:::

::: {.pf-step}
$\boxed{\text{No open set containing }A\text{ is disjoint from }V}$.

::: pf-proof
Suppose $U\ni A$ were open and disjoint from $V$. Choose rational $q$ with $a<q<b$, possible because the rationals are dense; then $q\times(-q)\in A\subseteq U$, and $U$ is a neighbourhood of that point, so $U$ meets $V$ by step [](#part-d){.pf-ref}, contradicting disjointness. Hence no open neighbourhood of $A$ misses $V$, which is the assertion. Parts (a)--(d) are steps [](#part-a){.pf-ref}, [](#part-b){.pf-ref}, [](#part-c){.pf-ref} and [](#part-d){.pf-ref}.
:::

:::

:::
:::
