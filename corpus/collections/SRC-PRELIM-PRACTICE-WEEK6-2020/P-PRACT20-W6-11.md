---
schema: qual/card@1
id: P-PRACT20-W6-11
kind: problem
title: Open, closed and uncountable sets containing $\QQ$
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
  note: Removed a stray figure caption from another page and separated the choices, checked against Week6_solns.pdf page 5 (Problem 11).
---

::: {.problem}
Which of the following necessarily holds for $\QQ \subseteq A \subseteq \RR$?

(A) If $A$ is open, then $A = \RR$.

(B) If $A$ is closed, then $A = \RR$.

(C) If $A$ is uncountable, then $A = \RR$.

(D) If $A$ is uncountable, then $A$ is open.

(E) If $A$ is countable, then $A$ is closed.
:::

::: {.solution}
(A) is false, and this is a bit surprising because if A is open and contains each rationals, then it contains open intervals around each rational.
Now if each interval had a fixed length, then we would have $A = \RR$ by density of $\QQ .$ . However, the intervals around the rationals could get infinitesimally small so that $A \neq \RR$ . To make this really rigorous, one needs to know a bit about the Lebesgue measure, but the idea is this: let $\{ q _ { n } \} _ { n = 1 } ^ { \infty } = \QQ$ and let $\begin{array} { r } { A = \cup _ { n = 1 } ^ { \infty } ( q _ { n } - \frac { 1 } { 2 ^ { n + 1 } } , q _ { n } + \frac { 1 } { 2 ^ { n + 1 } } ) } \end{array}$ Then certainly $\QQ \subset A$ , but the total length of A satisfies

$$
\ell ( A ) \leq \sum _ { n = 1 } ^ { \infty } \ell \left( \left( q _ { n } - { \frac { 1 } { 2 ^ { n + 1 } } } , q _ { n } + { \frac { 1 } { 2 ^ { n + 1 } } } \right) \right) = \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { 2 ^ { n } } } = 1 ,
$$

whereas the length of R is +∞. Thus $A \neq \RR { \mathrm { ~ s o ~ } } ( { \mathrm { A } } )$ is false.
[Indeed, replacing $1 / 2 ^ { n + 1 }$ with $\varepsilon / 2 ^ { n + 1 }$ for arbitrarily small $\varepsilon > 0$ , this argument shows that the Lebesgue measure of $\QQ$ [or any other countable set] is zero).

(C) is false: take $A = ( 0 , 1 ) \cup \QQ$

(D) is false: take $A = ( 0 , 1 ) \cup \QQ$

(E) is false: take $A = \QQ$

(B) is true: if A is closed and contains the rationals, then it contains the closure of the rationals which is R, thus $A = \RR$
:::
