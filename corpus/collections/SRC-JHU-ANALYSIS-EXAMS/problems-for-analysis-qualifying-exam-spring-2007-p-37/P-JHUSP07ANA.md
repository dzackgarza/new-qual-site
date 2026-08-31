---
schema: qual/card@1
id: P-JHUSP07ANA
kind: problem
title: "Zeros of a sextic in the unit disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

1) How many zeros does the polynomial $z ^ { 6 } - 2 z ^ { 5 } + 7 z ^ { 4 } + z ^ { 3 } - z + 1$ have in the open unit disc $D = \{ z : | z | < 1 \} ?$

::: {.solution}
<1>1. Let $p(z) = z^6 - 2z^5 + 7z^4 + z^3 - z + 1$ and $q(z) = 7z^4$.
::: {.proof}
choose a dominant term.
:::

<1>2. On $|z| = 1$, $|p(z) - q(z)| = |z^6 - 2z^5 + z^3 - z + 1| \le 1 + 2 + 1 + 1 + 1 = 6 < 7 = |q(z)|$.
::: {.proof}
triangle inequality on the unit circle.
:::

<1>3. Hence by Rouché's theorem, $p$ and $q$ have the same number of zeros in $|z| < 1$.
::: {.proof}
<1>2 and Rouché's theorem.
:::

<1>4. $q(z) = 7z^4$ has exactly $4$ zeros in $|z| < 1$ (a zero of order $4$ at $z = 0$).
::: {.proof}
$q(z) = 7z^4$ vanishes only at $z = 0$, where it has a zero of order $4$ (the factor $z^4$), and $0$ lies in the open unit disc.
:::

<1>5. Hence $p$ has $4$ zeros in the open unit disc.
::: {.proof}
<1>3 and <1>4.
:::

<1>6. Q.E.D.
::: {.proof}
<1>5.
:::
:::

(
