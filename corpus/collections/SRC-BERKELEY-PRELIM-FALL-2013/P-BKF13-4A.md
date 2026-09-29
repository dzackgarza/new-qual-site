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

::: pf

::: {.pf-step #s1}

The polynomials $p$ and $p'$ have no common root.

::: pf-proof

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

:::

::: {.pf-step #s2}

The polynomial $p$ has five distinct complex roots.

::: pf-proof

By the fundamental theorem of algebra, the degree-$5$ polynomial $p$
has five complex roots counted with multiplicity. A multiple root would
be a common root of $p$ and $p'$, contradicting step [](#s1){.pf-ref}. Hence all
five roots are distinct.

:::

:::

::: {.pf-step #s3}

The polynomial $p$ has at least three distinct real roots.

::: pf-proof

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

:::

::: {.pf-step #s4}

The polynomial $p$ has at most three distinct real roots.

::: pf-proof

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

:::

::: {.pf-step #s5}

Exactly three of the five distinct roots of $p$ are real.

::: pf-proof

Step [](#s3){.pf-ref} gives at least three real roots, while step [](#s4){.pf-ref} gives at
most three. Therefore the number is exactly three. Together with step
[](#s2){.pf-ref}, this proves that the remaining two roots are nonreal.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref} and [](#s5){.pf-ref} prove both requested assertions.

:::

:::

:::
