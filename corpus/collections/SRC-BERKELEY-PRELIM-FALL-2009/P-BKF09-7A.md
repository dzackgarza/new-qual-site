---
schema: qual/card@1
id: P-BKF09-7A
kind: problem
title: The Schwarzian derivative is holomorphic at a simple pole
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Moved the displayed expression and all TeX in the statement and solution inside math delimiters against f09solutions.pdf page 3 problem 7A.
---

::: {.problem}
If $f$ is a meromorphic function which has a pole of order 1 at $z_0$ show that

$$
\frac{f'''(z)}{f'(z)} - \frac{3}{2} \left( \frac{f''(z)}{f'(z)} \right)^2
$$

can be extended to a holomorphic function at $z_0$.
:::

::: {.solution}
If $f(z) = az^{-1} + \text{holomorphic}$, then $f' = -az^{-2}(1 + z^2 \times \text{holomorphic})$, $f'' = 2az^{-3}(1 + z^3 \times \text{holomorphic})$, $f''' = -6az^{-4}(1 + z^4 \times \text{holomorphic})$. Therefore $f'''/f' = 6z^{-2} + \text{holomorphic}$, and $f''/f' = -2z^{-1} + z \times (\text{holomorphic})$, so $(f''/f')^2 = 4z^{-2} + \text{holomorphic}$.
The result follows from this.
:::
