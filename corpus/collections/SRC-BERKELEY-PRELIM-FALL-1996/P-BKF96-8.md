---
schema: qual/card@1
id: P-BKF96-8
kind: problem
title: Denominator of $\binom{1/2}{n}$ is a power of two
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained extraction preserves the request “Show the denominator ... is a power of 2 for all integers n” but corrupts the displayed generalized binomial coefficient as `\left({1\atop n}\right)`. The missing part of the numerator is not independently recoverable from repository sources, so it is not guessed.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Direct inspection of page 2 of assets/attachments/Fall96.pdf recovers
    the displayed stacked coefficient as (1/2 choose n): pdftotext -layout
    preserves 1/2 directly above n in the binomial display. The earlier
    unrecoverable-source note is therefore superseded.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Rewrote the generalized binomial coefficient as an integer Catalan
    number divided by a power of two; negative lower indices are zero under
    the standard integer-index extension.
---

::: {.problem}
Show that the denominator of
\[
\binom{1/2}{n}
\]
is a power of $2$ for every integer $n$.
:::

::: {.solution}

Use the standard integer-index convention
$$
\binom{\alpha}{n}=0
\qquad(n<0),
$$
and for $n\geq0$ use the usual generalized binomial formula.

::: pf

::: {.pf-step #denominator-n-negative}
If $n<0$, then the reduced denominator of
$$
\binom{1/2}{n}
$$
is $1$, hence a power of $2$.

::: pf-proof
By the stated convention the binomial coefficient is $0$, whose reduced
rational form is $0/1$. Since
$$
1=2^0,
$$
the claim holds.
:::

:::

::: {.pf-step #denominator-n-zero}
If $n=0$, then the reduced denominator is again $1$.

::: pf-proof
One has
$$
\binom{1/2}{0}=1.
$$
:::

:::

::: {.pf-step #binomial-formula-positive-n}
Suppose $n\geq1$. Then
$$
\binom{1/2}{n}
=
(-1)^{n-1}
\frac{(2n-3)!!}{2^n n!}.
$$

::: pf-proof
Expanding the generalized binomial coefficient gives
$$
\begin{aligned}
\binom{1/2}{n}
&=
\frac{
(1/2)(1/2-1)(1/2-2)\cdots(1/2-n+1)
}{n!}\\
&=
(-1)^{n-1}
\frac{1\cdot3\cdot5\cdots(2n-3)}{2^n n!}.
\end{aligned}
$$
For $n=1$, the empty odd product is interpreted as $(-1)!!=1$, so the
same formula applies.
:::

:::

::: {.pf-step #catalan-number-integer}
For every $n\geq1$,
$$
C_{n-1}
\coloneqq
\frac1n\binom{2n-2}{n-1}
$$
is an integer.

::: pf-proof
The identity
$$
\frac1n\binom{2n-2}{n-1}
=
\binom{2n-2}{n-1}
-
\binom{2n-2}{n-2}
$$
expresses $C_{n-1}$ as a difference of two integers.
:::

:::

::: {.pf-step #binomial-via-catalan}
For $n\geq1$,
$$
\binom{1/2}{n}
=
(-1)^{n-1}
\frac{C_{n-1}}{2^{2n-1}}.
$$

::: pf-proof
The double-factorial identity
$$
(2n-2)!
=
2^{n-1}(n-1)!(2n-3)!!
$$
gives
$$
\begin{aligned}
C_{n-1}
&=
\frac{(2n-2)!}{n!(n-1)!}\\
&=
2^{n-1}
\frac{(2n-3)!!}{n!}.
\end{aligned}
$$
Hence
$$
\frac{(2n-3)!!}{n!}
=
\frac{C_{n-1}}{2^{n-1}}.
$$
Substitute this into step [](#binomial-formula-positive-n){.pf-ref}.
:::

:::

::: {.pf-step #denominator-power-of-two-positive-n}
For every $n\geq1$, the reduced denominator of
$$
\binom{1/2}{n}
$$
is a power of $2$.

::: pf-proof
By steps [](#catalan-number-integer){.pf-ref} and [](#binomial-via-catalan){.pf-ref}, the number has the form
$$
\frac{m}{2^{2n-1}}
$$
with $m\in\ZZ$. Reducing this fraction can only cancel factors of $2$
from the denominator. Therefore the reduced denominator is
$$
2^r
$$
for some integer $r\geq0$.
:::

:::

::: {.pf-step #claim-for-every-n}
The claim holds for every integer $n$.

::: pf-proof
Steps [](#denominator-n-negative){.pf-ref} and [](#denominator-n-zero){.pf-ref} handle $n\leq0$, and step [](#denominator-power-of-two-positive-n){.pf-ref} handles $n\geq1$.
:::

:::

::: pf-qed
Step [](#claim-for-every-n){.pf-ref} is the required conclusion.
:::

:::

:::
