---
schema: qual/card@1
id: P-BKF81-7
kind: problem
title: A polynomial for $\sqrt2+\sqrt[3]{3}$
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Eliminated sqrt(2) after cubing x-sqrt(2), then squared once to obtain an explicit degree-six polynomial over Q."
---

::: {.problem}
Find a specific polynomial with rational coefficients having $\sqrt2+\sqrt[3]{3}$ as a root.
:::

::: {.solution}
Set
$$
\alpha=\sqrt2+\sqrt[3]{3}.
$$
Write
$$
a=\sqrt2,
\qquad
b=\sqrt[3]{3},
$$
so $\alpha=a+b$, $a^2=2$, and $b^3=3$.

<1>1. Eliminate the cube root in favor of $a$ and $\alpha$.
::: {.proof}
Since
$$
b=\alpha-a,
$$
the equation $b^3=3$ gives
$$
(\alpha-a)^3=3.
$$
Expanding and using $a^2=2$ and $a^3=2a$,
$$
\alpha^3-3\alpha^2a+6\alpha-2a=3.
$$
Thus
$$
\alpha^3+6\alpha-3
=a(3\alpha^2+2).
$$
:::

<1>2. Eliminate $a=\sqrt2$.
::: {.proof}
Squaring the identity from step <1>1 and using $a^2=2$ yields
$$
(\alpha^3+6\alpha-3)^2
=2(3\alpha^2+2)^2.
$$
Hence $\alpha$ is a root of
$$
p(x)=(x^3+6x-3)^2-2(3x^2+2)^2.
$$
Expanding,
$$
\boxed{
p(x)=x^6-6x^4-6x^3+12x^2-36x+1.}
$$
This polynomial has integer, hence rational, coefficients, and satisfies
$p(\sqrt2+\sqrt[3]{3})=0$.
:::
:::
