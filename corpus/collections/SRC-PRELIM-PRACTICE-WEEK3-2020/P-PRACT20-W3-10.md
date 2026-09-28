---
schema: qual/card@1
id: P-PRACT20-W3-10
kind: problem
title: Error of the quadratic Taylor approximation to $\sqrt{1.01}$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
The polynomial $\begin{array} { r } { p ( x ) = 1 + \frac { 1 } { 2 } ( x - 1 ) - \frac { 1 } { 8 } ( x - 1 ) ^ { 2 } } \end{array}$ is used to approximate $\sqrt { 1 . 0 1 }$ Which of the following best approximates the error ${ \sqrt { 1 . 0 1 } } - p ( 1 . 0 1 ) !$

(A) $\textstyle { \frac { 1 } { 1 6 } } \times 1 0 ^ { - 6 }$ (B) $\scriptstyle { \frac { 1 } { 4 8 } } \times 1 0 ^ { - 8 }$ (C) $\frac { 3 } { 8 } \times 1 0 ^ { - 1 0 }$ (D) $- \frac { 3 } { 8 } \times 1 0 ^ { - 1 0 }$ (E) $\begin{array} { r } { - \frac { 1 } { 1 6 } \times 1 0 ^ { - 6 } . } \end{array}$
:::

::: {.solution}
By Problem 4, we have

$$
\sqrt { 1 + \varepsilon } \approx 1 + \left( \frac { 1 } { 2 } \right) \frac { \varepsilon } { 1 ! } + \left( \frac { 1 } { 2 } \right) \left( - \frac { 1 } { 2 } \right) \frac { \varepsilon ^ { 2 } } { 2 ! } + \left( \frac { 1 } { 2 } \right) \left( - \frac { 1 } { 2 } \right) \left( - \frac { 3 } { 2 } \right) \frac { \varepsilon ^ { 3 } } { 3 ! } = 1 + \frac { \varepsilon } { 2 } - \frac { \varepsilon ^ { 2 } } { 8 } + \frac { \varepsilon ^ { 3 } } { 1 6 }
$$

when $\left| \varepsilon \right| \ll 1$ . Thus

$$
\sqrt { 1 + \varepsilon } - p ( 1 + \varepsilon ) \approx \frac { \varepsilon ^ { 3 } } { 1 6 } .
$$

Plugging in $\varepsilon = 0 . 0 1$ shows that (A) is the correct answer.
[Quicker answer: you should note that $p$ is a second order approximation, so the error should be on the order of $\varepsilon ^ { 3 }$ where $\varepsilon = 1 0 ^ { - 2 }$ ; thus answers (B), (C), (D) can be eliminated very easily and all that remains to find the sign of the third derivative of $f ( x ) = { \sqrt { x } }$ at $x = 1 . ]$
:::
