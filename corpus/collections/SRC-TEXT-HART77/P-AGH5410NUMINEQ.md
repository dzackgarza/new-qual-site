---
schema: qual/card@1
id: P-AGH5410NUMINEQ
kind: problem
title: A numerical inequality underlying the ampleness criterion on the cubic surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.10 and the retained Egbert note, which supplies no
    proof and points only to Nagata/case analysis. The direct proof below is
    elementary. First prove that positive x_i with x_i+x_j<A and total sum
    at most 2A satisfy sum x_i^2<A^2. If s=sum b_i is at most 2a, this
    applies immediately. If s>2a, put t=s-2a and c_i=b_i-t. The five-term
    inequalities give c_i>0; the pair inequalities give
    c_i+c_j<a-2t; and sum c_i<2(a-2t). Applying the lemma and expanding
    sum(c_i+t)^2 gives exactly a^2 as the comparison value.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete elementary proof. Checked strictness in both cases
    of the auxiliary lemma, the positivity of A=a-2t after translation, the
    identity sum c_i=2a-5t, and the final expansion back to a^2. No geometric
    input or later-card result is used.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Published-solution pass for issue #121. Read the printed exercise in
    Hartshorne, Algebraic Geometry (1977), V.4.10, printed p. 408 (text
    version tmp/sources/hartshorne-1977-algebraic-geometry.md, where printed
    p. N is PDF p. N+15), with (4.11) and (4.13)(a), printed p. 406, whose
    inequalities its hypotheses are. Read at the cited places: Math
    StackExchange 2475661, answer 2476483 by Dap, text version
    tmp/sources/mse-2475661-hart-v410-freshman-calculus.md; National Taiwan
    University Algebraic Geometry II (2020 Spring), Chapter V §4 Exercise 10
    (Shuang-Yen Lee), printed p. 17, text version
    tmp/sources/ntu-ag2-chapter5.md, and the same page of the PDF, where the
    text version damages two formulas. Checked: the exercise's hypotheses
    imply the sorted weak thresholds b_5+b_6 <= a and b_2+...+b_6 <= 2a, so
    the sources' reduction to the weak form needs no separate equivalence;
    and each endpoint value the sources print (a^2, 15a^2/16, 24a^2/25,
    2b_4b_5-2b_5^2, 2b_4b_5-b_5^2) recomputed from the maximiser displayed
    with it. Defects found: the MSE answer's Case 1 prints 4b_4^2 for the
    five equal terms 5b_4^2 of its own maximiser while reporting a^2 at both
    endpoints, which is the value for 5b_4^2; its Case 2 is stated for
    a/3 <= b_4 <= a/2 although its own ordering forces b_4 = a/3; the NTU
    second case leaves its constant term as * and its printed vertex line
    has (1/3)(2b_2-(b_3+b_4+b_5)) on the right where the left side is
    (1/3)(b_2-2(b_3+b_4+b_5)). Not checked: no source outside these two was
    read for this card.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The solution is now the two published arguments transcribed, each step
    naming its source with its answer id or printed page; the card's earlier
    elementary proof, which was not a transcription of any source, is
    replaced by it. Steps sorted-hypotheses and strict-from-weak are the
    book's hypotheses and the MSE passage from the sharp to the weak form;
    steps maximiser, case-small-max, case-large-max and case-open transcribe
    that answer's four bullets and its Cases 1, 2a, 2b and 0; step
    second-argument transcribes NTU's Exercise 10 with both of its cases,
    including the three defects the remark names.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Re-read the whole card beside both sources. Checked the arithmetic of
    every displayed maximiser and of every endpoint value; checked that
    steps case-small-max, case-large-max and case-open exhaust the
    maximisers step maximiser allows, namely b_5+b_6 = a with b_4 <= a/3,
    the same with b_4 >= a/3, and b_5+b_6 < a; checked that step
    second-argument's two cases are the two branches of a = max{b_1+b_2,
    (b_1+...+b_5)/2} and that its endpoint inequalities need only
    0 < b_5 <= b_4. Not reviewed and not supplied: a proof of the three
    reduction assertions the sources make without proof (the three
    "otherwise one can increase" bullets of the first answer and NTU's
    reduction of its second case to b_1+b_2 = b_3+b_4+b_5), and no such
    proof was added; the 2026-11-16 COMPLAINTS record names what is left
    open.
---

::: {.problem}
A curious consequence of the implication (iv) $\Rightarrow$ (iii) of (4.11) is the following numerical fact: Given integers $a, b_1, \ldots, b_6$ such that $b_i>0$ for each $i$, $a-b_i-b_j>0$ for each $i, j$ and $2 a-\sum_{i \neq j} b_i>0$ for each $j$, we must necessarily have $a^2-\sum b_i^2>0$.
Prove this directly (for $a, b_1, \ldots, b_6 \in \RR$) using methods of freshman calculus.
:::

::: {.solution}

The exercise is the numerical statement behind the implication $(iv)\Rightarrow(iii)$ of (4.11):
for the class $D=a\ell-\sum_ib_ie_i$ on the cubic surface the hypotheses $b_i>0$,
$a-b_i-b_j>0$ and $2a-\sum_{i\neq j}b_i>0$ are the conditions of (4.13)(a), and the conclusion
$a^2-\sum_ib_i^2>0$ is $D^2>0$. The pair condition is read with $i\neq j$, the reading both
published arguments below adopt. The exercise asks for integers $a,b_1,\ldots,b_6$ and then for
real $a,b_1,\ldots,b_6$; both arguments are for real variables.

Two published arguments are transcribed, and the steps name which supplies them. Math StackExchange
question 2475661, answer 2476483 (Dap, 2017-10-17; text version
`tmp/sources/mse-2475661-hart-v410-freshman-calculus.md`) maximises $\sum_ib_i^2$ over the
feasible set for fixed $a$ and classifies the maximisers; the National Taiwan University
*Algebraic Geometry II*, 2020 Spring, Chapter V §4, Exercise 10 (Shuang-Yen Lee), printed p. 17
(text version `tmp/sources/ntu-ag2-chapter5.md`) reduces to one boundary configuration and
evaluates two quadratics.

::: pf

::: {.pf-step #sorted-hypotheses}
After reordering the indices one may assume
$$
b_1\ge b_2\ge\cdots\ge b_6>0,
$$
and then
$$
a>b_1+b_2,
\qquad
2a>b_1+\cdots+b_5 .
$$
In particular
$$
b_5+b_6\le a,
\qquad
b_2+\cdots+b_6\le 2a .
$$

::: pf-proof
The hypotheses are symmetric in the indices, so reordering them preserves them; this is the first
word of the second argument, "WLOG let $b_1\ge b_2\ge\cdots\ge b_6$". Among the pair conditions
$a>b_i+b_j$ with $i\ne j$ the strongest is the one at the two largest variables, and among the
conditions $2a>\sum_{j\ne i}b_j$ the strongest is the one that omits the smallest variable $b_6$.
Then $b_5+b_6\le b_1+b_2<a$ and
$b_2+\cdots+b_6=(b_1+\cdots+b_5)-b_1+b_6\le b_1+\cdots+b_5<2a$, since $b_6\le b_1$. These are the
hypotheses the first argument states its problem in: reals $0\le b_1\le\cdots\le b_6$ with
$a\ge b_5+b_6$ and $2a\ge b_2+\cdots+b_6$.
:::

:::

::: {.pf-step #strict-from-weak}
It suffices to prove
$$
a^2\ge\sum_{i=1}^6b_i^2 .
$$

::: pf-proof
If $a$ satisfies the strict hypotheses, then so does $a'=a-\varepsilon$ for small
$\varepsilon>0$, because there are finitely many strict inequalities to preserve; a weak conclusion
$a'^2\ge\sum_ib_i^2$ for that $a'$ gives $a^2>\sum_ib_i^2$. This is the first argument's opening
parenthesis, which passes from the sharp hypotheses to the weak conclusion in the other direction.
:::

:::

::: {.pf-step #maximiser}
Fix $a>0$. On the set of $b$ with
$$
0\le b_1\le\cdots\le b_6,
\qquad
b_5+b_6\le a,
\qquad
b_2+\cdots+b_6\le 2a
$$
the function $\sum_ib_i^2$ attains a maximum, and at a maximiser
$$
b_2+\cdots+b_6=2a
\quad\text{or}\quad
b_5+b_6=a,
$$
and
$$
b_1=b_2,
\qquad
b_5\le\frac a2,
\qquad
b_5=b_4 .
$$

::: pf-proof
The set is closed and bounded, so $\sum_ib_i^2$ attains a maximum on it. The four reductions are the
first argument's list, stated there in exactly this one-clause form. If both $b_2+\cdots+b_6<2a$
and $b_5+b_6<a$, then $b_6$ can be increased, which preserves the ordering and both constraints and
increases the sum of squares. If $b_1<b_2$, then $b_1$ can be increased with the ordering and both
constraints preserved. If $b_5>a/2$, then $b_6\ge b_5$ gives $b_5+b_6>a$. For fixed $b_5+b_6=S$
the maximum of $b_5^2+(S-b_5)^2$ over $b_5\in[b_4,S/2]$ is attained at an endpoint, and $b_5=a/2$
gives a smaller value than either endpoint does.
:::

:::

::: {.pf-step #case-small-max}
If a maximiser satisfies $b_5+b_6=a$ and $b_4\le a/3$, then
$$
\sum_{i=1}^6b_i^2\le a^2 .
$$

::: pf-proof
By step [](#maximiser){.pf-ref} a maximiser has $b_1=b_2=b_3=b_4=b_5$ and $b_5+b_6=a$, so it is
$$
b=(b_4,b_4,b_4,b_4,b_4,a-b_4),
\qquad
0\le b_4\le\frac a3,
$$
and
$$
\sum_ib_i^2=5b_4^2+(a-b_4)^2=6b_4^2-2ab_4+a^2 .
$$
This is a quadratic in $b_4$ with positive leading coefficient, so on the interval its values are at
most the larger of the two endpoint values; at $b_4=0$ the value is $a^2$ and at $b_4=a/3$ it is
$5a^2/9+4a^2/9=a^2$. This is the first argument's Case 1, which prints $4b_4^2$ for the five equal
terms $5b_4^2$ of this maximiser while reporting $a^2$ at both endpoints.
:::

:::

::: {.pf-step #case-large-max}
If a maximiser satisfies $b_5+b_6=a$ and $b_4\ge a/3$, then
$$
\sum_{i=1}^6b_i^2\le a^2 .
$$

::: pf-proof
By step [](#maximiser){.pf-ref} a maximiser has $b_1=b_2$ and $b_5=b_4$, and the first argument's
Case 2 writes it as
$$
b=(b_2,b_2,a-b_4-b_2,b_4,b_4,a-b_4)
$$
with $2b_2+b_4\le a$, so that the part of $\sum_ib_i^2$ depending on $b_2$ is
$$
2b_2^2+(a-b_4-b_2)^2 ,
$$
a quadratic with positive leading coefficient, whose maximum over the allowed range of $b_2$ is at
an endpoint. At the endpoint $b_2=\frac12(a-b_4)$ it writes
$$
b=\left(\tfrac12(a-b_4),\tfrac12(a-b_4),\tfrac12(a-b_4),b_4,b_4,a-b_4\right),
\qquad
\sum_ib_i^2=\tfrac74(a-b_4)^2+2b_4^2,
$$
which is $a^2$ at $b_4=a/3$ and $\frac{15}{16}a^2$ at $b_4=a/2$, and at the endpoint
$b_2=a-2b_4$ it writes
$$
b=(a-2b_4,a-2b_4,b_4,b_4,b_4,a-b_4),
\qquad
\sum_ib_i^2=2(a-2b_4)^2+3b_4^2+(a-b_4)^2,
$$
which is $a^2$ at both $b_4=a/3$ and $b_4=a/2$. In each subcase the displayed value is a convex
function of $b_4$ on $\left[\frac a3,\frac a2\right]$, so it is at most the larger endpoint value,
namely $a^2$. The ordering $b_2\ge b_3\ge b_4$ of a maximiser requires
$\frac12(a-b_4)\le b_2\le a-2b_4$, so the configuration of this step exists only for $b_4\le a/3$,
where both subcases reduce to $b_4=a/3$; the first argument states the step for
$\frac a3\le b_4\le\frac a2$ without that restriction.
:::

:::

::: {.pf-step #case-open}
If $b_5+b_6<a$ at a maximiser, then
$$
\sum_{i=1}^6b_i^2\le a^2 .
$$

::: pf-proof
By step [](#maximiser){.pf-ref} a maximiser with $b_5+b_6<a$ satisfies $b_2+\cdots+b_6=2a$, and the
first argument's Case 0 reduces it to the form
$$
b=(b_1,b_1,b_1,b_5,b_5,b_6),
$$
as follows: with $b_1=b_2$ and $b_5=b_4$ held fixed and $b_3+b_6$ then fixed, the maximum of
$b_3^2+b_6^2$ is attained by decreasing $b_3$ as far as the constraints allow, which either gives
$b_1=b_2=b_3$ or brings the maximiser to the boundary $b_5+b_6=a$ treated in steps
[](#case-small-max){.pf-ref} and [](#case-large-max){.pf-ref}; holding $b_1$ fixed afterwards, the
maximum of $2b_5^2+b_6^2$ is again attained on the boundary, at $b_5=b_1$, at $b_5=b_6$, or at
$b_5+b_6=a$. Of the maximisers of this form, those with $b_5+b_6=a$ are covered by the preceding steps, and the
extreme one that is not is $b_1=b_6=\frac{2a}{5}$, that is, all six entries equal $\frac{2a}{5}$,
with
$$
\sum_ib_i^2=6\cdot\frac{4a^2}{25}=\frac{24}{25}a^2<a^2 .
$$
The first argument states this case in this order and refers forward to its Cases 1 and 2 for the
part of it that returns to $b_5+b_6=a$.
:::

:::

::: {.pf-step #second-argument}
The inequality $a^2\ge\sum_ib_i^2$ also follows from the second argument, which needs no maximiser.

::: pf-proof
Its opening observation is that
$$
x+y=z+w
\quad\text{and}\quad
\abs{x-y}>\abs{z-w}
\quad\Longrightarrow\quad
x^2+y^2>z^2+w^2,
$$
which is the identity $x^2+y^2=\frac12\left((x+y)^2+(x-y)^2\right)$ for each pair. With the ordering
of step [](#sorted-hypotheses){.pf-ref} one has $a>b_1+b_2$ and $a>\frac12(b_1+\cdots+b_5)$, so the
argument assumes
$$
a=\max\left\{b_1+b_2,\ \tfrac12(b_1+\cdots+b_5)\right\},
$$
which is legitimate because a smaller $a$ makes the conclusion $a^2\ge\sum_ib_i^2$ harder and keeps
the strict hypotheses. It then splits into two cases.

If $b_1+b_2\ge b_3+b_4+b_5$, then $a=b_1+b_2$. Increasing $b_3,b_4,b_5$ one may assume
$b_1+b_2=b_3+b_4+b_5$; replacing $(b_1,b_2,b_6)$ by
$(b_1+b_2-b_3,\ b_3,\ b_5)$ preserves that equality and the sum $b_1+\cdots+b_5$, and by the
observation above it does not decrease $\sum_ib_i^2$, so one may assume $b_2=b_3$ and, the same way,
$b_5=b_6$. Then $b_1=b_4+b_5\ge b_2$, and
$$
a^2-\sum_ib_i^2=2b_2b_4+2b_2b_5-b_2^2-b_4^2-2b_5^2 .
$$
This is a quadratic in $b_2$, so on the range $b_4\le b_2\le b_4+b_5$ it suffices to check the two
endpoints, where it is
$$
2b_4b_5-2b_5^2\ge0
\qquad\text{and}\qquad
2b_4b_5-b_5^2\ge0,
$$
both nonnegative since $0<b_5\le b_4$.

If $b_1+b_2\le b_3+b_4+b_5$, then $a=\frac12(b_1+\cdots+b_5)$ and
$$
a^2-\sum_ib_i^2=-\tfrac34b_1^2+\tfrac12(b_2+b_3+b_4+b_5)b_1+\ast
$$
for a constant $\ast$ not depending on $b_1$. This is a quadratic in $b_1$ with negative leading
coefficient, and the argument locates its vertex at $b_1=b_3+b_4+b_5-b_2$, which is the boundary of
this case $b_1+b_2=b_3+b_4+b_5$, so that the case reduces to the preceding one. The printed line for
that vertex computation reads
$$
\frac{-\frac12(b_2+b_3+b_4+b_5)}{-\frac34\cdot2}-b_2-(b_3+b_4+b_5-b_2)
=\frac13\left(2b_2-(b_3+b_4+b_5)\right)\le0,
$$
whose two sides differ by $\frac13\left(b_2+b_3+b_4+b_5\right)-\frac13\left(b_3+b_4+b_5\right)
=\frac13b_2$: the left side is $\frac13\left(b_2-2(b_3+b_4+b_5)\right)$, and the constant $\ast$
is not written out, so this case is not carried out in full in the source.
:::

:::

::: {.pf-step #conclusion}
Consequently
$$
a^2-\sum_{i=1}^6b_i^2>0 .
$$

::: pf-proof
Steps [](#case-small-max){.pf-ref}, [](#case-large-max){.pf-ref} and [](#case-open){.pf-ref}
treat the maximiser of $\sum_ib_i^2$ in the three cases into which step
[](#maximiser){.pf-ref} divides the feasible set, and step [](#second-argument){.pf-ref} gives the
inequality by a second route over the two cases of the second argument. Either way
$a^2\ge\sum_ib_i^2$, and step [](#strict-from-weak){.pf-ref} upgrades the inequality to the strict
one under the strict hypotheses of the exercise.
:::

:::

::: pf-qed
Steps [](#sorted-hypotheses){.pf-ref}, [](#strict-from-weak){.pf-ref} and [](#maximiser){.pf-ref}
set up the maximisation, steps [](#case-small-max){.pf-ref}, [](#case-large-max){.pf-ref} and
[](#case-open){.pf-ref} bound the sum of squares at a maximiser, and step
[](#second-argument){.pf-ref} is the second published route to the same inequality.
:::

:::
:::

::: {.remark title="Published solution"}
Math StackExchange 2475661, *Freshman calculus question in Hartshorne, chapter V*, answer 2476483 by
Dap (2017-10-17), text version `tmp/sources/mse-2475661-hart-v410-freshman-calculus.md`. The answer
reads $a-b_i-b_j>0$ with $i\ne j$, rewrites the problem as one about reals
$0\le b_1\le\cdots\le b_6$ with $a\ge b_5+b_6$ and $2a\ge b_2+\cdots+b_6$, and says of the
rewriting only that "the equivalence can be shown by approximation by rationals, scaling and
sorting"; step [](#sorted-hypotheses){.pf-ref} instead reads the weak thresholds off the book's own
hypotheses, so no equivalence is used. The parenthetical about a smaller $a$ is step
[](#strict-from-weak){.pf-ref}; the bullet list about a maximiser is step [](#maximiser){.pf-ref};
its Cases 1, 2a, 2b and 0 are steps [](#case-small-max){.pf-ref}, [](#case-large-max){.pf-ref} and
[](#case-open){.pf-ref}. Three defects of the answer are recorded at those steps: Case 1 prints
$4b_4^2$ for $5b_4^2$; Case 2 is stated for $\frac a3\le b_4\le\frac a2$ although its own ordering
restricts it to $b_4=\frac a3$; and Case 0 refers forward to the other cases for part of itself. The
answer's own comment thread records two further corrections, by user228054 and by the author, of an
earlier version that assumed $b_5+b_6=a$ without justification.

National Taiwan University, *Algebraic Geometry II* (2020 Spring, Chin-Lung Wang), Chapter V §4,
Exercise 10, by Shuang-Yen Lee, printed p. 17, text version
`tmp/sources/ntu-ag2-chapter5.md`. Its observation on $x+y=z+w$ and its two cases are step
[](#second-argument){.pf-ref}. The first case is carried out: the two endpoint values of the
quadratic in $b_2$ are computed and are nonnegative. The second case leaves its constant term as
$\ast$, and its printed line identifying the vertex carries the slip recorded at that step, so the
reduction to the boundary $b_1+b_2=b_3+b_4+b_5$ is asserted there rather than proved.
:::
