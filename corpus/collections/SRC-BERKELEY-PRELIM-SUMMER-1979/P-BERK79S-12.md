---
schema: qual/card@1
id: P-BERK79S-12
kind: problem
title: Rational inputs making $3t^3+10t^2-3t$ integral
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Wrote t=a/b in lowest terms. Integrality forces
    b^3 | 3a^2+10ab-3b^2, hence reducing modulo b gives b|3. For b=3,
    coprimality gives 3∤a and the divisibility condition reduces to
    9 | a(a+1), forcing a≡-1 mod 9. Thus the solutions are all integers
    together with t=3k-1/3.
---

::: {.problem}
Determine all rational numbers $t$ such that
\[
3t^3+10t^2-3t
\]
is an integer.
:::

::: {.solution}
Write
$$
t=\frac ab
$$
in lowest terms, with
$$
a\in\ZZ,
\qquad
b\in\NN,
\qquad
\gcd(a,b)=1.
$$

::: pf

::: {.pf-step #s1}

If
$$
3t^3+10t^2-3t
$$
is an integer, then
$$
b^3
\mid
3a^2+10ab-3b^2.
$$

::: pf-proof

Substituting $t=a/b$ gives
$$
3t^3+10t^2-3t
=
\frac{
a(3a^2+10ab-3b^2)
}{b^3}.
$$
If this number is an integer, then
$$
b^3
\mid
a(3a^2+10ab-3b^2).
$$
Since $\gcd(a,b)=1$, one also has
$$
\gcd(a,b^3)=1.
$$
Euclid's lemma therefore gives the stated divisibility.

:::

:::

::: {.pf-step #s2}

Under the hypothesis of step [](#s1){.pf-ref},
$$
b\mid3.
$$

::: pf-proof

Step [](#s1){.pf-ref} implies in particular
$$
b
\mid
3a^2+10ab-3b^2.
$$
Reducing the right-hand side modulo $b$ gives
$$
3a^2\equiv0\pmod b.
$$
Because $\gcd(a,b)=1$, the element $a$ is invertible modulo every prime
power dividing $b$. Hence
$$
b\mid3.
$$
Equivalently, since $\gcd(a^2,b)=1$, Euclid's lemma applied to
$b\mid3a^2$ gives the same conclusion.

:::

:::

::: {.pf-step #s3}

Therefore
$$
b\in\{1,3\}.
$$

::: pf-proof

The denominator $b$ is positive, and step [](#s2){.pf-ref} says that it is a positive
divisor of $3$.

:::

:::

::: {.pf-step #s4}

If $b=1$, then $t$ is an integer, and every integer $t$ is a
solution.

::: pf-proof

If $b=1$, then $t=a\in\ZZ$. Since
$$
3t^3+10t^2-3t
$$
is a polynomial with integer coefficients, it is an integer at every
integer input.

:::

:::

::: {.pf-step #s5}

Suppose $b=3$. Then
$$
3\nmid a,
$$
and integrality is equivalent to
$$
9\mid a^2+10a-9.
$$

::: pf-proof

Since $a/3$ is in lowest terms,
$$
3\nmid a.
$$
Step [](#s1){.pf-ref} becomes
$$
27
\mid
3a^2+30a-27
=
3(a^2+10a-9).
$$
Dividing by $3$ gives the displayed condition.

:::

:::

::: {.pf-step #s6}

Under the hypotheses of step [](#s5){.pf-ref},
$$
a\equiv-1\pmod9.
$$

::: pf-proof

Modulo $9$,
$$
a^2+10a-9
\equiv
a^2+a
=
a(a+1).
$$
Thus step [](#s5){.pf-ref} gives
$$
9\mid a(a+1).
$$
Since $3\nmid a$, all factors of $3$ in this product must come from
$a+1$. Therefore
$$
9\mid a+1,
$$
which is equivalent to
$$
a\equiv-1\pmod9.
$$

:::

:::

::: {.pf-step #s7}

Hence every nonintegral solution has the form
$$
t=3k-\frac13
$$
for some $k\in\ZZ$.

::: pf-proof

By step [](#s6){.pf-ref},
$$
a=9k-1
$$
for some $k\in\ZZ$. Since $b=3$,
$$
t
=
\frac{9k-1}{3}
=
3k-\frac13.
$$

:::

:::

::: {.pf-step #s8}

Every number
$$
t=3k-\frac13,
\qquad
k\in\ZZ,
$$
is indeed a solution.

::: pf-proof

Let
$$
a=9k-1.
$$
Then
$$
\begin{aligned}
a^2+10a-9
&=
(9k-1)^2+10(9k-1)-9\\
&=
81k^2+72k-18\\
&=
9(9k^2+8k-2).
\end{aligned}
$$
Hence
$$
3a^2+30a-27
=
27(9k^2+8k-2).
$$
Therefore
$$
\begin{aligned}
3t^3+10t^2-3t
&=
\frac{
a(3a^2+30a-27)
}{27}\\
&=
a(9k^2+8k-2)
\in
\ZZ.
\end{aligned}
$$

:::

:::

::: {.pf-step #s9}

The complete set of rational solutions is
$$
\boxed{
\ZZ
\ \cup\
\left\{
3k-\frac13:
k\in\ZZ
\right\}.
}
$$

::: pf-proof

Steps [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} show that every solution lies in the displayed set.
Steps [](#s4){.pf-ref} and [](#s8){.pf-ref} show that every number in the displayed set is a
solution.

:::

:::

::: pf-qed

Step [](#s9){.pf-ref} is the required classification.

:::

:::

:::
