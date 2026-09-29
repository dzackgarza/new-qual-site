---
schema: qual/card@1
id: P-BKF15-5B
kind: problem
title: Entire functions with real part $x^3y-xy^3$
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
    Independently checked the retained Fall 2015 solution packet: the real
    part of -i z^4/4 is x^3 y-x y^3, and any entire difference with zero
    real part is a purely imaginary constant.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the expansion of z^4 and the uniqueness argument via the open
    mapping theorem.
---

::: {.problem}
Find all entire functions $f(z)$ such that $\operatorname{Re}(f(x+iy))=x^3y-xy^3$. Express your answer directly in terms of $z$, not in terms of $x$ and $y$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For $z=x+iy$,
$$
\operatorname{Re}\left(-\frac{i}{4}z^4\right)
=
x^3y-xy^3.
$$

::: pf-proof

Expanding,
$$
\begin{aligned}
z^4
&=
(x+iy)^4\\
&=
x^4-6x^2y^2+y^4
+
i(4x^3y-4xy^3).
\end{aligned}
$$
If
$$
z^4=A+iB,
$$
then
$$
-\frac{i}{4}z^4
=
\frac B4-\frac{iA}{4}.
$$
Hence its real part is
$$
\frac{4x^3y-4xy^3}{4}
=
x^3y-xy^3.
$$

:::

:::

::: {.pf-step #s2}

For every real constant $C$, the entire function
$$
f_C(z)
\coloneqq
-\frac{i}{4}z^4+iC
$$
satisfies the required real-part condition.

::: pf-proof

The function is a polynomial plus a constant, hence entire. By step
[](#s1){.pf-ref},
$$
\operatorname{Re}\left(-\frac{i}{4}z^4\right)
=
x^3y-xy^3,
$$
while
$$
\operatorname{Re}(iC)=0
$$
for $C\in\RR$.

:::

:::

::: {.pf-step #s3}

Let $f$ be any entire function satisfying the required
condition, and define
$$
h(z)
\coloneqq
f(z)+\frac{i}{4}z^4.
$$
Then
$$
\operatorname{Re}h(z)=0
$$
for every $z\in\CC$.

::: pf-proof

By hypothesis,
$$
\operatorname{Re}f(x+iy)
=
x^3y-xy^3.
$$
By step [](#s1){.pf-ref},
$$
\operatorname{Re}\left(-\frac{i}{4}z^4\right)
=
x^3y-xy^3.
$$
Therefore
$$
\operatorname{Re}
\left(
f(z)-\left(-\frac{i}{4}z^4\right)
\right)
=
0,
$$
which is exactly the claim.

:::

:::

::: {.pf-step #s4}

The entire function $h$ from step [](#s3){.pf-ref} is constant.

::: pf-proof

Its image is contained in the imaginary axis
$$
i\RR,
$$
which is not an open subset of $\CC$. If $h$ were nonconstant, the
open mapping theorem would make $h(\CC)$ open in $\CC$, a
contradiction. Hence $h$ is constant.

:::

:::

::: {.pf-step #s5}

The constant value of $h$ is of the form
$$
iC
$$
for some $C\in\RR$.

::: pf-proof

By step [](#s3){.pf-ref}, every value of $h$ has real part $0$. In particular its
constant value lies on the imaginary axis.

:::

:::

::: {.pf-step #s6}

The complete family of solutions is
$$
\boxed{
f(z)
=
-\frac{i}{4}z^4+iC,
\qquad
C\in\RR.
}
$$

::: pf-proof

Steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} show that every solution has this form, and step
[](#s2){.pf-ref} shows that every function of this form is a solution.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} gives all entire functions satisfying the required
condition.

:::

:::

:::
