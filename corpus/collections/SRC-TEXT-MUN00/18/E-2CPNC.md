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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked (a) through the closed-cover identity f^{-1}(C)
    as the union of the preimages in the finitely many closed pieces, (b) the countable
    closed cover of R by (-infinity,0], [1,infinity) and [1/(n-1),1/(n-2)] with the step
    function constant on each piece and discontinuous at 0 (n chosen as the largest integer
    not exceeding 1/x+2, §4 Exercise 9(a)), and (c) the restriction to the finite closed
    union meeting a neighbourhood of the point, after which (a) applies to the subspace.
    Whitman, Exercise 18.9, printed pp. 186-187, for (b) and (c); (a) is in the closed-cover
    form and the card says so. The printed statement needed no repair.
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
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 18.9, printed pp. 186--187** (`tmp/sources/munkres-solutions-whitman.pdf`); (b) and (c) are his, and (a) is proved here in the closed-cover form rather than by his induction on the number of sets. Whitman notes that the cover of (b) is not locally finite: every neighbourhood of $0$ meets infinitely many of its members.

::: pf

::: {.pf-step #preimage-union}
For $C\subset Y$, $\displaystyle f^{-1}(C)=\bigcup_{\alpha}\big(f\restriction_{A_{\alpha}}\big)^{-1}(C)$.

::: pf-proof
If $x\in f^{-1}(C)$ then $f(x)\in C$; choosing any $\alpha$ with $x\in A_{\alpha}$, which exists because $X=\bigcup_\alpha A_\alpha$, gives $x\in(f\restriction_{A_{\alpha}})^{-1}(C)$. If conversely $x\in(f\restriction_{A_{\alpha}})^{-1}(C)$ for some $\alpha$, then $x\in A_{\alpha}\subset X$ and $f(x)=(f\restriction_{A_{\alpha}})(x)\in C$, so $x\in f^{-1}(C)$.
:::

:::

::: {.pf-step #part-a}
(a) If the family $\{A_{\alpha}\}$ is finite and each $A_{\alpha}$ is closed in $X$, then $f$ is continuous.

:::: pf-proof

::: {.pf-step #a-pieces}
For each $\alpha$ and each closed $C\subset Y$, the set $(f\restriction_{A_{\alpha}})^{-1}(C)$ is closed in $X$.

::: pf-proof
Continuity of $f\restriction_{A_{\alpha}}$ makes $(f\restriction_{A_{\alpha}})^{-1}(C)$ closed in the subspace $A_{\alpha}$, so it equals $A_{\alpha}\cap F$ for some closed $F\subset X$. Since $A_{\alpha}$ is closed in $X$, that intersection is closed in $X$.
:::

:::

::: {.pf-step #a-conclusion}
$f$ is continuous.

::: pf-proof
Let $C\subset Y$ be closed. By step [](#preimage-union){.pf-ref} the set $f^{-1}(C)$ is the union of the sets $(f\restriction_{A_{\alpha}})^{-1}(C)$, which are closed in $X$ by step [](#a-pieces){.pf-ref}; the family is finite, so the union is closed in $X$. Hence the preimage of every closed set is closed, and $f$ is continuous by Theorem 18.1(3).
:::

:::

::: {.pf-step}
(a) holds.

::: pf-proof
Steps [](#a-pieces){.pf-ref} and [](#a-conclusion){.pf-ref} prove it for an arbitrary finite closed cover $\{A_{\alpha}\}$.
:::

:::

:::

:::

::: {.pf-step #part-b}
(b) The countable closed cover of $\RR$ by $A_{1}=(-\infty,0]$, $A_{2}=[1,\infty)$ and $A_{n}=[1/(n-1),1/(n-2)]$ for $n\ge3$ has every restriction $f\restriction_{A_{n}}$ constant, while $f(x)=1$ for $x\le0$ and $f(x)=0$ for $x>0$ is not continuous.

:::: pf-proof

::: {.pf-step #b-cover}
Each $A_{n}$ is closed in $\RR$ and $\bigcup_{n\in\ZZ_{+}}A_{n}=\RR$.

::: pf-proof
$(-\infty,0]$ and $[1,\infty)$ are closed, and each $[1/(n-1),1/(n-2)]$ is a closed interval because $n-2<n-1$ gives $1/(n-1)<1/(n-2)$. As $n$ runs over the integers $\ge3$, the intervals $[1/(n-1),1/(n-2)]$ have union
$$
\bigcup_{n\ge3}\Big[\tfrac1{n-1},\tfrac1{n-2}\Big]=(0,1],
$$
since every $x\in(0,1]$ satisfies $1/(n-1)\le x\le1/(n-2)$ exactly when $n-2\le 1/x\le n-1$, and such an integer $n$ is the largest integer not exceeding $1/x+2$, which exists by §4 Exercise 9(a) and satisfies $n\ge 1/x+1\ge3$. Adding $(-\infty,0]$ and $[1,\infty)$ gives $\RR$.
:::

:::

::: {.pf-step #b-constant}
$f\restriction_{A_{n}}$ is constant, hence continuous, for every $n$.

::: pf-proof
On $A_{1}=(-\infty,0]$ the function $f$ has the constant value $1$. On $A_{2}=[1,\infty)$ it has the constant value $0$. On $A_{n}=[1/(n-1),1/(n-2)]$ with $n\ge3$ every point satisfies $x\ge1/(n-1)>0$, so $f$ has the constant value $0$. A constant map is continuous (Theorem 18.2).
:::

:::

::: {.pf-step #b-discontinuous}
$f$ is not continuous.

::: pf-proof
$f(0)=1$ and $V=(\tfrac12,\tfrac32)$ is an open set containing $f(0)$ but no value $f(x)$ with $x>0$, since those values are $0$. Hence $f^{-1}(V)=(-\infty,0]$, which is not open in $\RR$ because every interval $(-\epsilon,\epsilon)$ around $0$ contains points where $f$ takes the value $0$. So the preimage of an open set is not open and $f$ is not continuous.
:::

:::

::: {.pf-step}
(b) holds.

::: pf-proof
Steps [](#b-cover){.pf-ref} and [](#b-constant){.pf-ref} give a countable closed cover on each member of which $f$ is continuous, and step [](#b-discontinuous){.pf-ref} shows $f$ is not continuous.
:::

:::

:::

:::

::: {.pf-step #part-c}
(c) If the family $\{A_{\alpha}\}$ is locally finite and each $A_{\alpha}$ is closed in $X$, then $f$ is continuous.

:::: pf-proof

::: {.pf-step #c-finite-piece}
Let $x\in X$ and let $U$ be a neighbourhood of $x$ meeting $A_{\alpha}$ only for $\alpha$ in the finite set $I(x)$. Then $A=\bigcup_{\alpha\in I(x)}A_{\alpha}$ is closed in $X$ and $U\subset A$.

::: pf-proof
$A$ is a finite union of sets closed in $X$, hence closed. If $y\in U$ then $y\in X=\bigcup_\alpha A_\alpha$, so $y\in A_{\alpha}$ for some $\alpha$, and that $\alpha$ lies in $I(x)$ because $U$ meets $A_{\alpha}$; hence $y\in A$.
:::

:::

::: {.pf-step #c-restriction}
$f\restriction_{A}$ is continuous.

::: pf-proof
The sets $A_{\alpha}$ with $\alpha\in I(x)$ form a finite family of closed subsets of the subspace $A$ whose union is $A$, and $f\restriction_{A_{\alpha}}$ is continuous for each of them, being the restriction of $f\restriction_{A}$ to that member. By step [](#part-a){.pf-ref} applied to the space $A$ in place of $X$, $f\restriction_{A}$ is continuous.
:::

:::

::: {.pf-step #c-continuity-at}
$f$ is continuous at $x$.

::: pf-proof
Let $V$ be a neighbourhood of $f(x)$ in $Y$. By step [](#c-restriction){.pf-ref} there is a set $W$, open in the subspace $A$, with $x\in W$ and $(f\restriction_{A})(W)\subset V$; write $W=A\cap O$ with $O$ open in $X$. Then $U\cap O$ is a neighbourhood of $x$ in $X$, because both $U$ and $O$ contain $x$ and $O$ is open, and
$$
f(U\cap O)\subset f(A\cap O)=(f\restriction_{A})(W)\subset V,
$$
where the inclusion holds because $U\subset A$ by step [](#c-finite-piece){.pf-ref}. So the image of a neighbourhood of $x$ lies in $V$, and $f$ is continuous at $x$.
:::

:::

::: {.pf-step}
(c) holds.

::: pf-proof
Step [](#c-continuity-at){.pf-ref} proves continuity at an arbitrary point $x$ of $X$.
:::

:::

:::

:::

::: {.pf-step}
All three parts hold.

::: pf-proof
Steps [](#part-a){.pf-ref}, [](#part-b){.pf-ref} and [](#part-c){.pf-ref} are the three assertions of the exercise.
:::

:::

:::
:::
