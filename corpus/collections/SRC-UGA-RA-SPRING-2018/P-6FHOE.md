---
schema: qual/card@1
id: P-6FHOE
kind: problem
title: Pointwise limit, non-uniform convergence, and $\lim\int_0^\infty\frac{x}{1+x^n}\,dx$
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
  - Uniform Convergence
  - Convergence of Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card carried no audit list; this one records the change. Sixteen steps asserted their claim with
    no justification and each now carries one: the three pointwise limit cases and the assembly of the
    limit function, the continuity of each $f_n$, the one-sided limits at $1$ that make the limit
    discontinuous, the uniform limit theorem and the conclusion that convergence is not uniform, the two
    domination estimates and the integrability of $g$ with $\int g = 2$, the dominated convergence
    application, and the evaluation $\int f = 1/2$. Checked while writing: the estimate on $(1,\infty)$
    needs $n \ge 3$ to turn $x^{1-n}$ into at most $x^{-2}$, which is why the tail $(f_n)_{n\ge3}$ rather
    than the whole sequence is dominated, and the point $x = 1$ does not affect the integral. One repair:
    the closing step had "Conclusion:" as its claim and now states the three conclusions. The statement
    is unchanged. The collection retains the UGA real analysis qualifying exam of Spring 2018 and no
    solution sheet, so the argument is the card's own.
---

::: {.problem}
Let
$$
f_n(x) = \frac{x}{1 + x^n}, \quad x \ge 0.
$$

(a) Show that $(f_n)$ converges pointwise on $[0, \infty)$ and find its limit. Is the convergence uniform on $[0, \infty)$?

(b) Compute
$$
\lim_{n \to \infty} \int_0^\infty f_n(x) \, dx.
$$
:::

::: {.solution}
**Goal:** Compute the pointwise limit function in (a), disprove uniform convergence via discontinuity, and evaluate the integral limit in (b) via the Dominated Convergence Theorem.

::: pf

::: pf-step
Part (a): Pointwise convergence of $(f_n)$.

::: pf-proof

::: pf-step
Case $x \in [0, 1)$:

- $\lim_{n \to \infty} x^n = 0$.
- Thus $\lim_{n \to \infty} f_n(x) = \lim_{n \to \infty} \frac{x}{1 + x^n} = \frac{x}{1 + 0} = x$.


::: pf-proof
For $0 \le x < 1$ the powers $x^n$ decrease to $0$, so $1 + x^n \to 1 > 0$ and the quotient converges to $\frac{x}{1+0} = x$ by continuity of $t \mapsto \frac{x}{1+t}$ at $t = 0$.
:::

:::

::: pf-step
Case $x = 1$:

- For all $n \ge 1$, $f_n(1) = \frac{1}{1 + 1^n} = \frac{1}{2}$.
- Thus $\lim_{n \to \infty} f_n(1) = \frac{1}{2}$.


::: pf-proof
Substituting $x = 1$ gives $f_n(1) = \frac{1}{1 + 1^n} = \frac12$ for every $n$, and a constant sequence converges to its value.
:::

:::

::: pf-step
Case $x > 1$:

- $\lim_{n \to \infty} x^n = \infty$.
- Thus $\lim_{n \to \infty} f_n(x) = \lim_{n \to \infty} \frac{x}{1 + x^n} = 0$.


::: pf-proof
For $x > 1$ the powers $x^n$ tend to $+\infty$ while the numerator is fixed, so the quotient tends to $0$.
:::

:::

::: pf-step
Thus $(f_n)$ converges pointwise on $[0, \infty)$ to the limit function:
$$f(x) = \begin{cases} x & \text{if } 0 \le x < 1, \\ \frac{1}{2} & \text{if } x = 1, \\ 0 & \text{if } x > 1. \end{cases}$$


::: pf-proof
The three cases $0 \le x < 1$, $x = 1$ and $x > 1$ cover $[0,\infty)$, and in each the limit is the value the displayed formula assigns to that $x$; that is pointwise convergence to $f$.
:::

:::

:::

:::

::: pf-step
Part (a): Non-uniformity of convergence on $[0, \infty)$.

::: pf-proof

::: pf-step
For each $n \ge 1$, $f_n(x) = \frac{x}{1 + x^n}$ is continuous on $[0, \infty)$ since the denominator $1 + x^n \ge 1 > 0$ never vanishes.


::: pf-proof
The denominator $1 + x^n$ is at least $1$ and so never vanishes, and numerator and denominator are polynomials, hence continuous on $[0,\infty)$; a quotient of continuous functions with nonvanishing denominator is continuous.
:::

:::

::: pf-step
The pointwise limit function $f$ is discontinuous at $x = 1$, because:
$$\lim_{x \to 1^-} f(x) = \lim_{x \to 1^-} x = 1 \ne \frac{1}{2} = f(1), \quad \lim_{x \to 1^+} f(x) = \lim_{x \to 1^+} 0 = 0 \ne \frac{1}{2}.$$


::: pf-proof
The limit from the left is $\lim_{x \to 1^-} x = 1$ because $f(x) = x$ below $1$, and it differs from $f(1) = \frac12$; the limit from the right is $\lim_{x \to 1^+} 0 = 0$, which also differs. A function whose one-sided limits at a point differ from its value there is discontinuous at that point.
:::

:::

::: pf-step
By the Uniform Limit Theorem, the uniform limit of a sequence of continuous functions on $[0, \infty)$ must be continuous on $[0, \infty)$.


::: pf-proof
The uniform limit theorem says that a uniform limit of continuous functions on a metric space is continuous: given $\varepsilon$, pick $N$ with $\sup\abs{f_n - f} < \varepsilon/3$ for $n \ge N$, then use continuity of $f_N$ at a point to make $\abs{f_N(x) - f_N(y)} < \varepsilon/3$ nearby, so that $\abs{f(x)-f(y)} < \varepsilon$.
:::

:::

::: pf-step
Because $f$ is not continuous, the sequence $(f_n)$ does not converge uniformly to $f$ on $[0, \infty)$.


::: pf-proof
If the convergence were uniform then the limit $f$ would be continuous by the previous step; $f$ is not continuous at $1$, so the convergence on $[0,\infty)$ is not uniform.
:::

:::

:::

:::

::: pf-step
Part (b): Construction of an integrable dominating function.

::: pf-proof

::: pf-step
For $x \in [0, 1]$ and all $n \ge 1$:
$$0 \le f_n(x) = \frac{x}{1 + x^n} \le x \le 1.$$


::: pf-proof
The numerator $x$ is nonnegative and the denominator $1 + x^n$ is at least $1$, so $f_n(x) \ge 0$ and $f_n(x) \le \frac{x}{1} = x$; and $x \le 1$ on this interval.
:::

:::

::: pf-step
For $x \in (1, \infty)$ and all $n \ge 3$:
$$0 \le f_n(x) = \frac{x}{1 + x^n} \le \frac{x}{x^n} = \frac{1}{x^{n-1}} \le \frac{1}{x^2}.$$


::: pf-proof
For $x > 1$ the denominator satisfies $1 + x^n > x^n$, so $f_n(x) < \frac{x}{x^n} = \frac{1}{x^{n-1}}$; since $x > 1$ and $n \ge 3$ give $x^{n-1} \ge x^2$, taking reciprocals gives $\frac{1}{x^{n-1}} \le \frac{1}{x^2}$.
:::

:::

::: pf-step
Define $g: [0, \infty) \to \RR$ by:
$$g(x) = \begin{cases} 1 & \text{if } 0 \le x \le 1, \\ \frac{1}{x^2} & \text{if } x > 1. \end{cases}$$


::: pf-proof
The formula assigns exactly one real number to each $x \ge 0$, according to which of the two complementary intervals contains it, so it defines a function on $[0,\infty)$.
:::

:::

::: pf-step
The function $g$ is Lebesgue integrable on $[0, \infty)$:
$$\int_0^\infty g(x) \, dx = \int_0^1 1 \, dx + \int_1^\infty \frac{1}{x^2} \, dx = 1 + \left[ -\frac{1}{x} \right]_1^\infty = 1 + 1 = 2 < \infty.$$


::: pf-proof
On $[0,1]$ the integral of the constant $1$ is $1$; on $[1,\infty)$ the integral of $x^{-2}$ is $\left[-x^{-1}\right]_1^{\infty} = 0 + 1$. Both pieces are measurable with finite integrals, so $g$ is Lebesgue integrable and its integral is $1 + 1 = 2$.
:::

:::

::: pf-step
For all $n \ge 3$ and all $x \ge 0$, $\abs{f_n(x)} \le g(x)$.


::: pf-proof
For $0 \le x \le 1$ the first estimate gives $f_n(x) \le x \le 1 = g(x)$, and for $x > 1$ the second gives $f_n(x) \le x^{-2} = g(x)$; in both ranges $f_n \ge 0$, so the absolute value is $f_n$ itself and $\abs{f_n(x)} \le g(x)$ for all $n \ge 3$ and all $x \ge 0$.
:::

:::

:::

:::

::: pf-step
Part (b): Application of the Dominated Convergence Theorem.

::: pf-proof

::: pf-step
The sequence $(f_n)_{n=3}^\infty$ is dominated by $g \in L^1([0, \infty))$ and converges pointwise almost everywhere to $f(x)$.


::: pf-proof
The domination is the estimate just proved, and the pointwise convergence was established in part (a) for every $x$, hence almost everywhere; so the two hypotheses of the dominated convergence theorem are satisfied by the tail $(f_n)_{n \ge 3}$.
:::

:::

::: pf-step
By the Dominated Convergence Theorem:
$$\lim_{n \to \infty} \int_0^\infty f_n(x) \, dx = \int_0^\infty f(x) \, dx.$$


::: pf-proof
The functions $f_n$ are measurable, converge pointwise almost everywhere to $f$, and are dominated in modulus by the integrable $g$; the dominated convergence theorem then says the integrals converge to the integral of the limit.
:::

:::

::: pf-step
Evaluate the integral:
$$\int_0^\infty f(x) \, dx = \int_0^1 x \, dx + \int_1^\infty 0 \, dx = \left[ \frac{x^2}{2} \right]_0^1 = \frac{1}{2}.$$


::: pf-proof
The function $f$ equals $x$ on $[0,1)$ and $0$ on $(1,\infty)$, differing from those formulas only at the single point $1$, which does not change the integral; hence $\int_0^\infty f = \int_0^1 x\,dx = \left[\frac{x^2}{2}\right]_0^1 = \frac12$.
:::

:::

:::

:::

::: pf-step
$(f_n)$ converges pointwise to $f$, the convergence is not uniform, and $\lim_n \int_0^\infty f_n = \frac12$.

::: pf-proof
$(f_n)$ converges pointwise to $f$, the convergence is not uniform, and $\lim_{n \to \infty} \int_0^\infty f_n(x) \, dx = \frac{1}{2}$.
:::

:::

:::

:::

