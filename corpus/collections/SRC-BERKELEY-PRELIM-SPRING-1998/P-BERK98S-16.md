---
schema: qual/card@1
id: P-BERK98S-16
kind: problem
title: A quadratic rational function maps the left half-plane into the unit disk
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $a>0$. Show that
\[
f(z)=\frac{1+z+az^2}{1-z+az^2}
\]
satisfies
\[
|f(z)|<1
\]
for every $z$ in the open left half-plane $\operatorname{Re}z<0$.
:::

::: {.solution}
Put
$$
w\coloneqq1+az^2.
$$
Then
$$
1+z+az^2=w+z,
\qquad
1-z+az^2=w-z.
$$

::: pf

::: {.pf-step #s1}

For every $z\in\CC$,
$$
\abs{w-z}^2-\abs{w+z}^2
=
-4(1+a\abs z^2)\operatorname{Re}z.
$$

::: pf-proof

Using
$$
\abs{u-v}^2-\abs{u+v}^2
=-4\operatorname{Re}(u\overline v),
$$
with $u=w$ and $v=z$ gives
$$
\abs{w-z}^2-\abs{w+z}^2
=
-4\operatorname{Re}\bigl((1+az^2)\overline z\bigr).
$$
Since
$$
z^2\overline z=\abs z^2z,
$$
the real part on the right is
$$
\operatorname{Re}\overline z
+a\abs z^2\operatorname{Re}z
=
(1+a\abs z^2)\operatorname{Re}z.
$$
Substitution gives the claimed identity.

:::

:::

::: {.pf-step #s2}

If $\operatorname{Re}z<0$, then
$$
\abs{1-z+az^2}
>
\abs{1+z+az^2}.
$$

::: pf-proof

Because $a>0$,
$$
1+a\abs z^2>0.
$$
If $\operatorname{Re}z<0$, step [](#s1){.pf-ref} therefore gives
$$
\abs{1-z+az^2}^2
-
\abs{1+z+az^2}^2
>0.
$$
Both norms are nonnegative, so the stated strict inequality follows.

:::

:::

::: {.pf-step #s3}

The denominator $1-z+az^2$ is nonzero throughout the open left
half-plane.

::: pf-proof

If it vanished at such a point, then its modulus would be $0$, contradicting
the strict inequality in step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

For every $z$ with $\operatorname{Re}z<0$,
$$
\boxed{\abs{f(z)}<1}.
$$

::: pf-proof

By step [](#s3){.pf-ref}, $f(z)$ is defined, and by step [](#s2){.pf-ref},
$$
\abs{f(z)}
=
\frac{\abs{1+z+az^2}}{\abs{1-z+az^2}}
<1.
$$

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
