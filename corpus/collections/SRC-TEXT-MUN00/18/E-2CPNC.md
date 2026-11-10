---
schema: qual/card@1
id: E-2CPNC
kind: problem
title: Pasting over a locally finite closed cover
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §18 Exercise 9, printed p. 112, with Theorem 18.1
    and Exercise 17.2; the three parts and the definition of locally finite are stored as
    printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 18.9, printed pp.
    186-187. His are the countable closed cover of R by (-infinity,0], [1,infinity) and the
    intervals [1/(n-1),1/(n-2)], on each of which the step function is constant while the
    function is discontinuous at 0; and the locally finite argument, which restricts to the
    closed union of the finitely many sets meeting a neighbourhood of the point and then
    applies the finite case. (a) is proved through the closed-cover identity f^{-1}(C) =
    union of the preimages in the pieces instead of by his induction. (tmp/sources/munkres-
    solutions-whitman.pdf).
---

::: {.exercise}

Let $\theset{A_\alpha}$ be a collection of subsets of $X$; let $X = \bigcup_\alpha A_\alpha$.
Let $f: X \to Y$; suppose that $f \mid A_\alpha$ is continuous for each $\alpha$.

(a) Show that if the collection $\theset{A_\alpha}$ is finite and each set $A_\alpha$ is closed, then $f$ is continuous.

(b) Find an example where the collection $\theset{A_\alpha}$ is countable and each $A_\alpha$ is closed, but $f$ is not continuous.

(c) An indexed family of sets $\theset{A_\alpha}$ is said to be locally finite if each point $x$ of $X$ has a neighborhood that intersects $A_\alpha$ for only finitely many values of $\alpha$.
Show that if the family $\theset{A_\alpha}$ is locally finite and each $A_\alpha$ is closed, then $f$ is continuous.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 18.9, printed pp. 186--187** (`tmp/sources/munkres-solutions-whitman.pdf`); (b) and (c) are his, and (a) is proved below in the standard closed-cover form rather than by his induction on the number of sets.

(a) Let $C\subset Y$ be closed. For each $\alpha$, continuity of $f\restrict_{A_{\alpha}}$ makes $(f\restrict_{A_{\alpha}})^{-1}(C)$ closed in the subspace $A_{\alpha}$, so it is $A_{\alpha}\cap F_{\alpha}$ for some closed $F_{\alpha}\subset X$; since $A_{\alpha}$ is closed in $X$, the set $(f\restrict_{A_{\alpha}})^{-1}(C)$ is closed in $X$. Now $x\in f^{-1}(C)$ if and only if $f(x)\in C$, if and only if $x\in A_{\alpha}$ and $f\restrict_{A_{\alpha}}(x)\in C$ for the (or any) $\alpha$ with $x\in A_{\alpha}$; hence
$$
f^{-1}(C)=\bigcup_{\alpha}\big(f\restrict_{A_{\alpha}}\big)^{-1}(C),
$$
a finite union of closed sets, so closed in $X$. By Theorem 18.1(3) $f$ is continuous.

(b) Let $A_{1}=(-\infty,0]$, $A_{2}=[1,\infty)$ and $A_{n}=[1/(n-1),1/(n-2)]$ for $n\ge3$. Each $A_{n}$ is closed in $\RR$ and
$$
\bigcup_{n\in\ZZ_{+}}A_{n}=(-\infty,0]\cup[1,\infty)\cup(0,1]=\RR
$$
because the intervals $[1/(n-1),1/(n-2)]$ for $n\ge3$ fill $(0,1]$. Let
$$
f:\RR\to\RR,\qquad f(x)=\begin{cases}1,&x\le0,\\ 0,&x>0.\end{cases}
$$
Then $f\restrict_{A_{n}}$ is constant, hence continuous, for every $n$: on $A_{1}$ it is $1$, and on $A_{n}$ for $n\ge2$ every point satisfies $x\ge1/(n-1)>0$, so it is $0$. But $f$ is not continuous: the open set $(-\tfrac12,\tfrac12)$ around $f(0)=1$ contains no $f(x)$ for $x>0$, so $f^{-1}\big((-\tfrac12,\tfrac12)\big)=(-\infty,0]$ is not open in $\RR$.

(c) Let $\{A_{\alpha}\}$ be locally finite with every $A_{\alpha}$ closed. Let $x\in X$ and let $U$ be a neighbourhood of $x$ meeting only the finitely many members $A_{\alpha}$ with $\alpha\in I(x)$. Put $A=\bigcup_{\alpha\in I(x)}A_{\alpha}$, closed as a finite union of closed sets. Each $y\in U$ lies in no $A_{\alpha}$ with $\alpha\notin I(x)$, hence $y\in A$; so $U\subset A$, and $U$ is a neighbourhood of $x$ in the subspace $A$. The family $\{A_{\alpha}\}_{\alpha\in I(x)}$ is a finite closed cover of $A$ and $f\restrict_{A_{\alpha}}$ is continuous for each of its members, so $f\restrict_{A}$ is continuous by (a). Let $V$ be a neighbourhood of $f(x)$; continuity of $f\restrict_{A}$ gives a neighbourhood $W$ of $x$ in $A$ with $(f\restrict_{A})(W)\subset V$, and $W=A\cap O$ for some open $O\subset X$. Then $U\cap O$ is a neighbourhood of $x$ in $X$, and
$$
f(U\cap O)\subset f(A\cap O)=(f\restrict_{A})(W)\subset V .
$$
So $f$ is continuous at each $x\in X$.

Whitman notes that the example of (b) is not locally finite: every neighbourhood of $0$ meets infinitely many $A_{n}$.
:::
