---
schema: qual/card@1
id: E-MUN-7-9
kind: problem
title: Recursion formulas that fall outside the standard principle
classification:
  areas:
  - topology
  topics:
  - Countable and Uncountable Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 7, Exercise 9; the stored statement and printed hint match the source. The printed hint in part (b) is incorrect as stated; the solution supplies a corrected recursive second solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

(a) The formula

(\*)

$$
\begin{array}{l} h (1) = 1, \\ h (2) = 2, \\ h (n) = [ h (n + 1) ] ^ {2} - [ h (n - 1) ] ^ {2} \quad \text { for } n \geq 2 \end{array}
$$

is not one to which the principle of recursive definition applies.
Show that nevertheless there does exist a function $h: \mathbb{Z}_+ \to \mathbb{R}$ satisfying this formula.
[Hint: Reformulate (\*) so that the principle will apply and require $h$ to be positive.]

(b) Show that the formula (\*) of part (a) does not determine $h$ uniquely.
[Hint: If $h$ is a positive function satisfying (\*), let $f(i) = h(i)$ for $i \neq 3$, and let $f(3) = -h(3)$ .]

(c) Show that there is no function $h: \mathbb{Z}_{+} \to \mathbb{R}$ satisfying the formula

$$
\begin{array}{l} h (1) = 1, \\ h (2) = 2, \\ h (n) = [ h (n + 1) ] ^ {2} + [ h (n - 1) ] ^ {2} \quad \text { for } n \geq 2. \end{array}
$$
:::

::: {.solution}
(a) Rewrite the recurrence as
\[
[h(n+1)]^2=h(n)+[h(n-1)]^2.
\]
Require all values to be positive, and define recursively
\[
h(1)=1,\qquad h(2)=2,
\]
\[
h(n+1)=\sqrt{h(n)+[h(n-1)]^2}\qquad(n\ge2),
\]
where the positive square root is chosen. The radicand is positive, so the recursive definition is valid. Squaring the defining equation gives
\[
h(n)=[h(n+1)]^2-[h(n-1)]^2
\]
for every \(n\ge2\). Hence a solution exists.

(b) The printed hint suggesting that one merely negate \(h(3)\) and leave all later values unchanged is not correct: the equation for \(n=3\) would then fail. Instead define a second solution \(f\) by
\[
f(1)=1,\qquad f(2)=2,\qquad f(3)=-\sqrt3,
\]
and then, for \(n\ge3\), recursively set
\[
f(n+1)=\sqrt{f(n)+[f(n-1)]^2}.
\]
For \(n=3\), the radicand is \(4-\sqrt3>0\); thereafter the newly defined terms are positive, so every later radicand is positive as well. At \(n=2\),
\[
[f(3)]^2-[f(1)]^2=3-1=2=f(2).
\]
For every \(n\ge3\), squaring the recursive definition gives exactly
\[
f(n)=[f(n+1)]^2-[f(n-1)]^2.
\]
Thus \(f\) is a solution distinct from the positive solution of part (a), so the original formula does not determine \(h\) uniquely.

(c) Suppose instead that
\[
h(n)=[h(n+1)]^2+[h(n-1)]^2.
\]
At \(n=2\),
\[
2=[h(3)]^2+1,
\]
so \([h(3)]^2=1\), hence \(h(3)=\pm1\). But at \(n=3\),
\[
h(3)=[h(4)]^2+[h(2)]^2=[h(4)]^2+4\ge4,
\]
contradicting \(h(3)=\pm1\). Therefore no such function exists.
:::
