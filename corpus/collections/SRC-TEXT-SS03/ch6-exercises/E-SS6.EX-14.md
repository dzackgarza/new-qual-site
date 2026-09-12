---
schema: qual/card@1
id: E-SS6.EX-14
kind: problem
title: "This exercise gives an asymptotic formula for log n!"
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Repaired a transcription defect in the exercise statement before solving.
---

::: exercise
14. This exercise gives an asymptotic formula for log n!. A more refined asymptotic formula for $\Gamma ( s )$ as $s \to \infty$ (Stirling’s formula) is given in Appendix A.

(a) Show that

$$
{\frac {d}{d x}} \int_ {x} ^ {x + 1} \log \Gamma (t) d t = \log x, \qquad {\mathrm{for}} x > 0,
$$

and as a result

$$
\int_ {x} ^ {x + 1} \log \Gamma (t) d t = x \log x - x + c.
$$

(b) Show as a consequence that log $\Gamma ( n ) \sim n$ log n as $n \to \infty$ . In fact, prove that $\log \Gamma(n)=n\log n+O(n)$ as $n\to\infty$. [Hint: Use the fact that $\Gamma ( x )$ is monotonically increasing for all large x.]
:::

::: solution
Let
\[
I(x)=\int_x^{x+1}\log\Gamma(t)\,dt.
\]
By Leibniz' rule,
\[
I'(x)=\log\Gamma(x+1)-\log\Gamma(x).
\]
Using $\Gamma(x+1)=x\Gamma(x)$,
\[
I'(x)=\log x.
\]
Therefore
\[
I(x)=x\log x-x+c
\]
for a constant $c$.

For part (b), $\Gamma(x)$ is increasing for all sufficiently large $x$. Hence for all sufficiently large integers $n$,
\[
\int_{n-1}^{n}\log\Gamma(t)\,dt
\le \log\Gamma(n)
\le \int_n^{n+1}\log\Gamma(t)\,dt.
\]
Applying part (a) at $x=n-1$ and $x=n$ gives
\[
(n-1)\log(n-1)-(n-1)+c
\le \log\Gamma(n)
\le n\log n-n+c.
\]
Now
\[
(n-1)\log(n-1)=n\log n+O(n),
\]
so both bounds imply
\[
\log\Gamma(n)=n\log n+O(n).
\]
Dividing by $n\log n$ yields
\[
\frac{\log\Gamma(n)}{n\log n}\to1,
\]
that is, $\log\Gamma(n)\sim n\log n$.
:::
