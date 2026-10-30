---
schema: qual/card@1
id: E-SS4.EX-2
kind: problem
title: Derivatives of functions in $\mathfrak F_a$ lie in $\mathfrak F_b$ for $b<a$
classification:
  areas:
  - complex-analysis
  topics:
  - Fourier Transform
  - Cauchy Estimates
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Stein--Shakarchi Chapter 4 notation and exercise statement.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
2. If $f \in \mathfrak { F } _ { a }$ with $a > 0$ , then for any positive integer n one has $f ^ { ( n ) } \in \mathfrak { F } _ { b }$ whenever $0 \leq b < a$

[Hint: Modify the solution to Exercise 8 in Chapter 2.]
:::

::: {.solution}
By definition, $f\in\mathfrak F_a$ means that $f$ is holomorphic on
$$
S_a=\{z:\abs{\Im z}<a\}
$$
and that for some $A>0$,
$$
\abs{f(x+iy)}\le \frac{A}{1+x^2}
\qquad(x\in\RR,\ \abs{y}<a).
\tag{1}
$$
Fix $0\le b<a$ and an integer $n\ge1$. Put
$$
\rho=\frac{a-b}{2}>0.
$$
If $z=x+iy$ with $\abs{y}<b$, then the closed circle $\abs{w-z}=\rho$ lies in $S_a$. Cauchy's inequalities give
$$
\abs{f^{(n)}(z)}\le \frac{n!}{\rho^n}
\sup_{\abs{w-z}=\rho}\abs{f(w)}.
\tag{2}
$$
Write $w=u+iv$. Then $\abs{u-x}\le\rho$. Hence
$$
x^2\le 2u^2+2\rho^2,
$$
so
$$
1+x^2\le (2+2\rho^2)(1+u^2).
$$
Therefore (1) implies
$$
\abs{f(w)}\le \frac{A(2+2\rho^2)}{1+x^2}
$$
on the circle. Substituting in (2),
$$
\abs{f^{(n)}(x+iy)}
\le \frac{A_n}{1+x^2},
\qquad \abs{y}<b,
$$
where
$$
A_n=\frac{n!A(2+2\rho^2)}{\rho^n}.
$$
Thus $f^{(n)}\in\mathfrak F_b$ for every $0\le b<a$.
:::
