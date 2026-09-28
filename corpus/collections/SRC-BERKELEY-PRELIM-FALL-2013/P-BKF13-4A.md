---
schema: qual/card@1
id: P-BKF13-4A
kind: problem
title: 'Roots of $z^5-6z+3$: distinct, exactly three real'
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked against the recorded Fall 1986 statement, the repeated Fall 2013
    Berkeley prelim statement, and the retained Fall 2013 solution packet.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the exclusion of multiple roots, the three disjoint sign-change
    intervals, and the Rolle-theorem upper bound on the number of real roots.
---

::: {.problem}
Show that the polynomial $p ( z ) = z ^ { 5 } - 6 z + 3$ has five distinct complex roots, and that exactly three (and not five) are real.
:::

::: {.solution}
Let
$$
p(z)\coloneqq z^5-6z+3.
$$

<1>1. The polynomials $p$ and $p'$ have no common root.

::: {.proof}
One has
$$
p'(z)=5z^4-6.
$$
If $z$ were a common root of $p$ and $p'$, then it would also be a
root of
$$
5p(z)-zp'(z)
=-24z+15.
$$
Hence necessarily $z=5/8$. But
$$
p'\left(\frac58\right)
=5\left(\frac58\right)^4-6
\ne0.
$$
Thus no common root exists.
:::

<1>2. The polynomial $p$ has five distinct complex roots.

::: {.proof}
By the fundamental theorem of algebra, the degree-$5$ polynomial $p$
has five complex roots counted with multiplicity. A multiple root would
be a common root of $p$ and $p'$, contradicting step <1>1. Hence all
five roots are distinct.
:::

<1>3. The polynomial $p$ has at least three distinct real roots.

::: {.proof}
Direct evaluation gives
$$
p(-2)=-17<0,
\qquad
p(0)=3>0,
$$
$$
p(1)=-2<0,
\qquad
p(2)=23>0.
$$
By the intermediate value theorem, there is a root in each of the
pairwise disjoint intervals
$$
(-2,0),
\qquad
(0,1),
\qquad
(1,2).
$$
Thus there are at least three distinct real roots.
:::

<1>4. The polynomial $p$ has at most three distinct real roots.

::: {.proof}
The real zeros of
$$
p'(x)=5x^4-6
$$
are exactly
$$
x=\pm\left(\frac65\right)^{1/4},
$$
so $p'$ has only two real zeros. If $p$ had four distinct real roots,
Rolle's theorem applied between consecutive roots would give at least
three distinct real zeros of $p'$, a contradiction. Hence $p$ has at
most three real roots.
:::

<1>5. Exactly three of the five distinct roots of $p$ are real.

::: {.proof}
Step <1>3 gives at least three real roots, while step <1>4 gives at
most three. Therefore the number is exactly three. Together with step
<1>2, this proves that the remaining two roots are nonreal.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>2 and <1>5 prove both requested assertions.
:::
:::
