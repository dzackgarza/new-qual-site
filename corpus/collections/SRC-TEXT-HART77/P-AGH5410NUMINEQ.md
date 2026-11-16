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
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Second pass, on the reader's findings for this card. The first pass had
    sorted the variables decreasingly while transcribing an answer that sorts
    them increasingly (text version
    tmp/sources/mse-2475661-hart-v410-freshman-calculus.md, line 31:
    "0 <= b_1 <= ... <= b_6"); in the decreasing order the answer's b_5+b_6
    is the pair of the two smallest variables and its b_2+...+b_6 the sum
    that omits the largest, so the two thresholds read off in that order
    were not the answer's; the step is rewritten in the answer's increasing
    order, where
    b_5+b_6 is the pair of the two largest and b_2+...+b_6 the sum omitting
    the smallest, so both thresholds are the book's own hypotheses. Three
    findings of the first pass are withdrawn as misreadings and removed from
    the card and from the COMPLAINTS record of this date: that the first
    answer's Case 2 is empty for b_4 > a/3 (with increasing order its own
    ordering gives a-2b_4 <= b_2 <= (a-b_4)/2, nonempty exactly for
    b_4 >= a/3, and its 2b subcase is the maximiser (0,0,a/2,a/2,a/2,a/2)
    that it lists); that its Case 0 refers forward as a defect (the answer
    says its later cases do not depend on Case 0); and that the NTU second
    case misidentifies its vertex (PDF p. 17: the line compares the vertex
    with the midpoint of the range, the comparison is correct because
    2b_2 <= b_3+b_4+b_5 follows from b_1+b_2 <= b_3+b_4+b_5 and b_1 >= b_2,
    and the only slip is a factor 2 on the right-hand side; the constant is
    not needed). Checked in this pass: the two NTU endpoint computations,
    the midpoint comparison, the vertex at (b_2+b_3+b_4+b_5)/3, and the
    replacement of three entries that preserves b_1+b_2, b_1+...+b_5 and
    the ordering while not decreasing the sum of squares. Found in this
    pass and now named on the card: NTU's increase of b_3,b_4,b_5 to reach
    b_1+b_2 = b_3+b_4+b_5 fails once b_1 > 2b_2, for instance at
    (10,1,1,1,1,1); and the first answer's equalities b_2=b_3=b_4 and
    b_2+b_3+b_4=a rest on its one-clause reason. The step that said the
    chosen a keeps the strict hypotheses is corrected: a is replaced by
    max{b_1+b_2,(b_1+...+b_5)/2}, at which one hypothesis holds with
    equality. Not checked: no source outside these two was read, and no
    proof of the two open reductions was supplied.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Rewritten in the increasing order of the first answer, with the four
    cases of its maximiser analysis, the two open reductions named as its
    reasons, and the NTU argument in its own decreasing order with the
    b_1 <= 2b_2 condition on its first case. Provenance and process
    commentary is removed from the rendered card; the sources and their
    pages are named at the steps and in the remark.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Re-read against both sources. Recomputed every displayed value: a^2 and
    a^2 at the endpoints of 5b_4^2+(a-b_4)^2; a^2 and 15a^2/16 for
    7(a-b_4)^2/4+2b_4^2; a^2 at both ends for
    2(a-2b_4)^2+3b_4^2+(a-b_4)^2; 24a^2/25 at the all-equal vector;
    2b_4b_5-2b_5^2 and 2b_4b_5-b_5^2 at the two endpoints of the quadratic
    in b_2. Checked that the three cases exhaust the maximisers allowed by
    b_5+b_6 = a or b_5+b_6 < a together with b_4 <= a/3 or b_4 >= a/3.
    Left open and recorded in COMPLAINTS: the two reductions the answer
    states without proof, and the range of NTU's first case.
---

::: {.problem}
A curious consequence of the implication (iv) $\Rightarrow$ (iii) of (4.11) is the following numerical fact: Given integers $a, b_1, \ldots, b_6$ such that $b_i>0$ for each $i$, $a-b_i-b_j>0$ for each $i, j$ and $2 a-\sum_{i \neq j} b_i>0$ for each $j$, we must necessarily have $a^2-\sum b_i^2>0$.
Prove this directly (for $a, b_1, \ldots, b_6 \in \RR$) using methods of freshman calculus.
:::

::: {.solution}

The exercise's hypotheses are the conditions of (4.13)(a) of the book for the class
$D=a\ell-\sum_ib_ie_i$ on the cubic surface, with the pair condition read for $i\ne j$, and its
conclusion $a^2-\sum_ib_i^2>0$ is $D^2>0$; the exercise asks for integers and then for real
$a,b_1,\ldots,b_6$.

Math StackExchange question 2475661, answer 2476483 (Dap, 2017-10-17), orders the variables
increasingly and supplies steps [](#ordered-hypotheses){.pf-ref} to [](#case-open){.pf-ref}.
Chapter V §4 Exercise 10 of the National Taiwan University *Algebraic Geometry II* homework (2020
Spring), by Shuang-Yen Lee, printed p. 17, orders them decreasingly and supplies step
[](#second-argument){.pf-ref}, which is transcribed in that order.

::: pf

::: {.pf-step #ordered-hypotheses}
After reordering the indices one may assume
$$
0<b_1\le b_2\le\cdots\le b_6,
$$
and then
$$
a\ge b_5+b_6,
\qquad
2a\ge b_2+\cdots+b_6 .
$$

::: pf-proof
The hypotheses are symmetric in the indices, so reordering preserves them. Among the conditions
$a>b_i+b_j$ with $i\ne j$ the strongest is the one at the two largest variables, namely
$a>b_5+b_6$; among the conditions $2a>\sum_{j\ne i}b_j$ the strongest is the sum that omits the
smallest variable, namely $b_2+\cdots+b_6<2a$. These two are the hypotheses of the argument that
follows.
:::

:::

::: {.pf-step #smaller-a}
It suffices to prove
$$
a^2\ge\sum_{i=1}^6b_i^2
$$
under the two weak inequalities of step [](#ordered-hypotheses){.pf-ref}.

::: pf-proof
If $a>b_5+b_6$ and $2a>b_2+\cdots+b_6$, then $a-\varepsilon$ satisfies the same strict inequalities
for small $\varepsilon>0$; a proof of $(a-\varepsilon)^2\ge\sum_ib_i^2$ for that smaller number gives
$a^2>\sum_ib_i^2$.
:::

:::

::: {.pf-step #maximiser}
Fix $a>0$ and let $M$ be the set of $b$ with
$$
0<b_1\le\cdots\le b_6,
\qquad
b_5+b_6\le a,
\qquad
b_2+\cdots+b_6\le 2a .
$$
The function $\sum_ib_i^2$ attains a maximum on $M$, and at every maximiser
$$
b_2+\cdots+b_6=2a
\quad\text{or}\quad
b_5+b_6=a,
$$
$$
b_1=b_2,
\qquad
b_5\le\frac a2,
\qquad
b_5=b_4 .
$$

::: pf-proof
$M$ is closed and bounded, so a maximum is attained. If both $b_2+\cdots+b_6<2a$ and
$b_5+b_6<a$, then $b_6$ can be increased, which keeps $b$ in $M$ and raises $\sum_ib_i^2$. If
$b_1<b_2$ then $b_1$ can be increased, which keeps $b$ in $M$ and raises the sum, since $b_1$ occurs
in neither constraint. If $b_5>a/2$ then $b_6\ge b_5$ gives $b_5+b_6>a$. Last, for fixed
$b_5+b_6=S$ the function $b_5^2+(S-b_5)^2$ on $b_4\le b_5\le S/2$ attains its maximum at an
endpoint, and $b_5=a/2$ gives a smaller value than either endpoint does.
:::

:::

::: {.pf-step #case-small}
If a maximiser satisfies $b_5+b_6=a$ and $b_4\le a/3$, then
$$
\sum_{i=1}^6b_i^2\le a^2 .
$$

::: pf-proof
At such a maximiser $b_2=b_3=b_4$: the reason given in the answer is that otherwise $b_3$ or $b_2$
could be increased. Together with $b_1=b_2$ and $b_5=b_4$ from step [](#maximiser){.pf-ref} this
makes $b_1,\ldots,b_5$ equal to $b_4$, and $b_6=a-b_4$, so
$$
\sum_ib_i^2=5b_4^2+(a-b_4)^2=6b_4^2-2ab_4+a^2 .
$$
This is a quadratic in $b_4$ with positive leading coefficient, so on $0\le b_4\le a/3$ it is at most
the larger endpoint value; at $b_4=0$ the value is $a^2$ and at $b_4=a/3$ it is
$5a^2/9+4a^2/9=a^2$. The answer writes $4b_4^2$ in place of the five equal terms $5b_4^2$ and reports
$a^2$ at both endpoints, which are the endpoint values of $5b_4^2+(a-b_4)^2$.
:::

:::

::: {.pf-step #case-large}
If a maximiser satisfies $b_5+b_6=a$ and $b_4\ge a/3$, then
$$
\sum_{i=1}^6b_i^2\le a^2 .
$$

::: pf-proof
At such a maximiser $b_2+b_3+b_4=a$, the reason given in the answer being again that otherwise
$b_3$ or $b_2$ could be increased; with $b_2=b_3$ this gives
$$
b=(b_2,b_2,a-b_4-b_2,b_4,b_4,a-b_4).
$$
The ordering forces $a-2b_4\le b_2\le\frac12(a-b_4)$, an interval nonempty exactly for $b_4\ge a/3$,
and the part of $\sum_ib_i^2$ depending on $b_2$ is
$$
2b_2^2+(a-b_4-b_2)^2 ,
$$
a quadratic with positive leading coefficient, so its maximum on that interval is at an endpoint. At
$b_2=\frac12(a-b_4)$ it gives
$$
b=\left(\tfrac12(a-b_4),\tfrac12(a-b_4),\tfrac12(a-b_4),b_4,b_4,a-b_4\right),
\qquad
\sum_ib_i^2=\tfrac74(a-b_4)^2+2b_4^2,
$$
which is $a^2$ at $b_4=a/3$ and $\frac{15}{16}a^2$ at $b_4=a/2$; at $b_2=a-2b_4$ it gives
$$
b=(a-2b_4,a-2b_4,b_4,b_4,b_4,a-b_4),
\qquad
\sum_ib_i^2=2(a-2b_4)^2+3b_4^2+(a-b_4)^2,
$$
which is $a^2$ at both $b_4=a/3$ and $b_4=a/2$, the second being the vector
$(0,0,\frac a2,\frac a2,\frac a2,\frac a2)$. In each subcase the value is a convex function of $b_4$
on $[\frac a3,\frac a2]$, so it is at most the larger endpoint value, namely $a^2$.
:::

:::

::: {.pf-step #case-open}
If a maximiser satisfies $b_5+b_6<a$, then
$$
\sum_{i=1}^6b_i^2\le a^2 .
$$

::: pf-proof
By step [](#maximiser){.pf-ref} such a maximiser has $b_2+\cdots+b_6=2a$. The answer reduces it to the
form
$$
b=(b_1,b_1,b_1,b_5,b_5,b_6),
$$
as follows: with $b_1=b_2$ and $b_4=b_5$ held fixed the sum $b_3+b_6$ is fixed, so the maximum of
$b_3^2+b_6^2$ is attained by decreasing $b_3$ as far as the constraints allow, which either makes
$b_1=b_2=b_3$ or brings the maximiser to $b_5+b_6=a$, the two cases of steps
[](#case-small){.pf-ref} and [](#case-large){.pf-ref}; and with $b_1$ held fixed the maximum of
$2b_5^2+b_6^2$ is likewise attained on the boundary, at $b_5=b_1$, at $b_5=b_6$, or at
$b_5+b_6=a$. Of the maximisers of that form, those with $b_5+b_6=a$ are the two steps above, and the
remaining one is $b_1=b_6=\frac{2a}{5}$, all six entries equal to $\frac{2a}{5}$, with
$$
\sum_ib_i^2=6\cdot\frac{4a^2}{25}=\frac{24}{25}a^2<a^2 .
$$
:::

:::

::: {.pf-step #second-argument}
The inequality holds as well by the second argument, which needs no maximiser.

::: pf-proof
The second argument keeps the decreasing order $b_1\ge b_2\ge\cdots\ge b_6$ and opens with the
observation that
$$
x+y=z+w
\quad\text{and}\quad
\abs{x-y}>\abs{z-w}
\quad\Longrightarrow\quad
x^2+y^2>z^2+w^2,
$$
which is the identity $x^2+y^2=\frac12\left((x+y)^2+(x-y)^2\right)$ applied to both pairs. In that
order the hypotheses give $a>b_1+b_2$ and $2a>b_1+\cdots+b_5$, so
$$
a\ge\max\left\{b_1+b_2,\ \tfrac12(b_1+\cdots+b_5)\right\},
$$
and since the conclusion $a^2\ge\sum_ib_i^2$ becomes harder as $a$ decreases, it suffices to prove it
for the value $a=\max\{b_1+b_2,\frac12(b_1+\cdots+b_5)\}$.

If $b_1+b_2\ge b_3+b_4+b_5$ then $a=b_1+b_2$, and the argument increases $b_3,b_4,b_5$ so as to have
$b_1+b_2=b_3+b_4+b_5$; that increase is available only while $b_3\le b_2$, so it fails once
$b_1>2b_2$, for instance at $b=(10,1,1,1,1,1)$, where $b_3+b_4+b_5$ cannot reach $b_1+b_2=11$ under
the ordering. Under $b_1+b_2=b_3+b_4+b_5$, replacing the three entries $b_1,b_2,b_6$ by
$b_1+b_2-b_3$, $b_3$ and $b_5$ keeps $b_1+b_2$ and $b_1+\cdots+b_5$, keeps the ordering, and by the
observation does not decrease $\sum_ib_i^2$, so one may assume $b_2=b_3$ and $b_5=b_6$. Then
$b_1=b_4+b_5\ge b_2$ and
$$
a^2-\sum_ib_i^2=2b_2b_4+2b_2b_5-b_2^2-b_4^2-2b_5^2,
$$
a quadratic in $b_2$, so on the range $b_4\le b_2\le b_4+b_5$ it suffices to check the endpoints,
where it is
$$
2b_4b_5-2b_5^2\ge0
\qquad\text{and}\qquad
2b_4b_5-b_5^2\ge0,
$$
both nonnegative since $0<b_5\le b_4$.

If $b_1+b_2\le b_3+b_4+b_5$ then $a=\frac12(b_1+\cdots+b_5)$ and
$$
a^2-\sum_ib_i^2=-\tfrac34b_1^2+\tfrac12(b_2+b_3+b_4+b_5)b_1+\ast
$$
for a constant $\ast$ in $b_1$. This is a quadratic in $b_1$ opening downwards, with vertex
$b_1^{*}=\frac13(b_2+b_3+b_4+b_5)$; its argument range is $b_2\le b_1\le b_3+b_4+b_5-b_2$, whose
midpoint is $\frac12(b_3+b_4+b_5)$. Since $b_1+b_2\le b_3+b_4+b_5$ and $b_1\ge b_2$ give
$2b_2\le b_3+b_4+b_5$, one has
$$
b_1^{*}-\tfrac12(b_3+b_4+b_5)=\tfrac16\left(2b_2-(b_3+b_4+b_5)\right)\le0,
$$
so the vertex lies at or to the left of the midpoint, the right endpoint is the farther one, and the
minimum on the range is at $b_1=b_3+b_4+b_5-b_2$, that is, at $b_1+b_2=b_3+b_4+b_5$, which is the
preceding case. The printed line states this comparison with the right-hand side
$\frac13(2b_2-(b_3+b_4+b_5))$, twice the value of the left-hand side, and leaves the constant $\ast$
unwritten; the sign, which is what the comparison uses, is that of $2b_2-(b_3+b_4+b_5)$ on both
sides.
:::

:::

::: {.pf-step #conclusion}
Consequently
$$
a^2-\sum_{i=1}^6b_i^2>0 .
$$

::: pf-proof
The maximiser of $\sum_ib_i^2$ on $M$ falls under step [](#case-open){.pf-ref} if $b_5+b_6<a$, and
otherwise under step [](#case-small){.pf-ref} or [](#case-large){.pf-ref} according as $b_4\le a/3$ or
$b_4\ge a/3$, so $a^2\ge\sum_ib_i^2$ in every case; step [](#second-argument){.pf-ref} gives the same
inequality by the second route, for the data its first case reaches. Step
[](#smaller-a){.pf-ref} turns the weak inequality into the strict one required by the exercise.
:::

:::

::: pf-qed
Steps [](#ordered-hypotheses){.pf-ref}, [](#smaller-a){.pf-ref} and [](#maximiser){.pf-ref} set up the
maximisation, steps [](#case-small){.pf-ref}, [](#case-large){.pf-ref} and [](#case-open){.pf-ref}
bound the sum of squares at a maximiser, and step [](#second-argument){.pf-ref} is the second
argument, which reaches the first case's equality configuration only while $b_1\le 2b_2$.
:::

:::
:::

::: {.remark title="Published solution"}
Math StackExchange 2475661, *Freshman calculus question in Hartshorne, chapter V*, answer 2476483 by
Dap (2017-10-17): the weak threshold form of the hypotheses, the four properties of a maximiser of
$\sum b_i^2$ on the feasible set, and the four cases bounding that maximum by $a^2$. The answer
writes $4b_4^2$ in place of $5b_4^2$ in its first case, and its equalities $b_2=b_3=b_4$ and
$b_2+b_3+b_4=a$ are stated with the reason that otherwise $b_3$ or $b_2$ could be increased.

National Taiwan University, *Algebraic Geometry II* (2020 Spring, Chin-Lung Wang), Chapter V §4,
Exercise 10, by Shuang-Yen Lee, printed p. 17: the observation on $x+y=z+w$ and $\abs{x-y}>\abs{z-w}$, the
reduction to $a=\max\{b_1+b_2,\frac12(b_1+\cdots+b_5)\}$ in the decreasing order, and the two cases;
the first is carried out at the two endpoint values of the quadratic in $b_2$, and its initial
increase of $b_3,b_4,b_5$ to $b_1+b_2=b_3+b_4+b_5$ needs $b_1\le2b_2$; the second compares the vertex
of a downward quadratic with the midpoint of its range, with the factor $2$ noted on the card.
:::
