---
schema: qual/card@1
id: P-BKS13-2A
kind: problem
title: Quadratic convergence of Newton's method
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared all three parts with pages 1--2 of the retained Spring 2013 solution PDF and independently reviewed the Newton-error estimate.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked existence and uniqueness of the zero, the quadratic error recurrence, the initial-error bound from |f(x0)|, and convergence of the scaled errors.
---

::: {.problem}
Suppose that $f$ is a smooth real function defined for all real $x$, such that $\abs{f'(x)} \geq \epsilon > 0$ and $\abs{f''(x)} \leq M > 0$ for all $x$.

(1) Show that $f$ has a unique zero $z$.

(2) Given $x _ { 0 } ,$ define a sequence by $x _ { n + 1 } = x _ { n } - f ( x _ { n } ) / f ^ { \prime } ( x _ { n } )$ . Show that

$$
| x _ { n + 1 } - z | \leq | x _ { n } - z | ^ { 2 } M / \epsilon .
$$

(Hint: $f(x_n) = \int_z^{x_n} f'(x)\,dx$.)

(3) Show that the sequence $\{ x _ { n } \}$ converges to the zero $z$ of $f$ provided that $\abs{f(x_0)} < \epsilon^2/M$.
:::

::: {.solution}
<1>1. The derivative $f'$ has a constant sign on $\RR$.

::: {.proof}
The hypothesis
$$
\abs{f'(x)}\geq\varepsilon>0
$$
shows that $f'$ never vanishes. Since $f'$ is continuous and $\RR$ is
connected, its image cannot contain both a positive and a negative value:
otherwise the intermediate value theorem would give a zero. Thus either
$$
f'(x)\geq\varepsilon
$$
for every $x$, or
$$
f'(x)\leq-\varepsilon
$$
for every $x$.
:::

<1>2. The function $f$ has at most one zero.

::: {.proof}
If
$$
f(a)=f(b)=0
$$
with $a<b$, Rolle's theorem would give a point $c\in(a,b)$ with
$$
f'(c)=0,
$$
contradicting the hypothesis.
:::

<1>3. The function $f$ has at least one zero.

::: {.proof}
Suppose first that
$$
f'(x)\geq\varepsilon
$$
everywhere. For $x>0$, the mean value theorem gives
$$
f(x)-f(0)
\geq
\varepsilon x,
$$
so $f(x)\to+\infty$ as $x\to+\infty$. For $x<0$, the same theorem gives
$$
f(x)-f(0)
\leq
\varepsilon x,
$$
so $f(x)\to-\infty$ as $x\to-\infty$. The intermediate value theorem
therefore gives a zero.

If instead
$$
f'(x)\leq-\varepsilon,
$$
then the two limiting signs are reversed, and the same intermediate-value
argument gives a zero.
:::

<1>4. There is a unique zero
$$
z\in\RR
$$
of $f$.

::: {.proof}
Combine steps <1>2 and <1>3. This proves part (1).
:::

<1>5. For every real $x$,
$$
\abs{f(x)}
\geq
\varepsilon\abs{x-z}.
$$

::: {.proof}
If $x=z$, the assertion is immediate. Otherwise, the mean value theorem
gives a point $c$ between $x$ and $z$ such that
$$
f(x)-f(z)
=
f'(c)(x-z).
$$
Since $f(z)=0$ and $\abs{f'(c)}\geq\varepsilon$, taking absolute values
gives the claim.
:::

<1>6. For every $n\geq0$,
$$
x_{n+1}-z
=
\frac{
\int_z^{x_n}
\bigl(f'(x_n)-f'(t)\bigr)\,dt
}{
f'(x_n)
}.
$$

::: {.proof}
Since $f(z)=0$, the fundamental theorem of calculus gives
$$
f(x_n)
=
\int_z^{x_n}f'(t)\,dt.
$$
Therefore
$$
\begin{aligned}
x_{n+1}-z
&=
x_n-z-\frac{f(x_n)}{f'(x_n)}\\
&=
\frac{
(x_n-z)f'(x_n)
-\int_z^{x_n}f'(t)\,dt
}{
f'(x_n)
}\\
&=
\frac{
\int_z^{x_n}
\bigl(f'(x_n)-f'(t)\bigr)\,dt
}{
f'(x_n)
}.
\end{aligned}
$$
The denominator never vanishes by hypothesis, so every Newton iterate is
defined.
:::

<1>7. For all real $s,t$,
$$
\abs{f'(s)-f'(t)}
\leq
M\abs{s-t}.
$$

::: {.proof}
Apply the mean value theorem to $f'$ on the interval with endpoints
$s,t$. There is a point $c$ between them such that
$$
f'(s)-f'(t)
=
f''(c)(s-t).
$$
The bound
$$
\abs{f''(c)}\leq M
$$
gives the result.
:::

<1>8. The Newton errors satisfy the stronger estimate
$$
\abs{x_{n+1}-z}
\leq
\frac{M}{2\varepsilon}
\abs{x_n-z}^2.
$$

::: {.proof}
Apply steps <1>6 and <1>7 and use
$$
\abs{f'(x_n)}\geq\varepsilon.
$$
If $x_n\geq z$, then
$$
\begin{aligned}
\abs{x_{n+1}-z}
&\leq
\frac1\varepsilon
\int_z^{x_n}
M(x_n-t)\,dt\\
&=
\frac{M}{2\varepsilon}(x_n-z)^2.
\end{aligned}
$$
If $x_n<z$, reversing the integration limits gives the same formula with
$\abs{x_n-z}$. Thus the estimate holds in all cases.
:::

<1>9. In particular,
$$
\boxed{
\abs{x_{n+1}-z}
\leq
\frac{M}{\varepsilon}
\abs{x_n-z}^2
}.
$$

::: {.proof}
Step <1>8 is stronger because
$$
\frac{M}{2\varepsilon}
\leq
\frac{M}{\varepsilon}.
$$
This proves part (2).
:::

<1>10. If
$$
\abs{f(x_0)}
<
\frac{\varepsilon^2}{M},
$$
then
$$
q_0
\coloneqq
\frac{M}{\varepsilon}\abs{x_0-z}
<
1.
$$

::: {.proof}
Step <1>5 gives
$$
\abs{x_0-z}
\leq
\frac{\abs{f(x_0)}}{\varepsilon}.
$$
Therefore
$$
q_0
\leq
\frac{M\abs{f(x_0)}}{\varepsilon^2}
<
1.
$$
:::

<1>11. If
$$
q_n
\coloneqq
\frac{M}{\varepsilon}\abs{x_n-z},
$$
then
$$
q_{n+1}\leq q_n^2.
$$

::: {.proof}
Multiply the estimate in step <1>9 by $M/\varepsilon$:
$$
\begin{aligned}
q_{n+1}
&=
\frac{M}{\varepsilon}\abs{x_{n+1}-z}\\
&\leq
\frac{M^2}{\varepsilon^2}\abs{x_n-z}^2\\
&=
q_n^2.
\end{aligned}
$$
:::

<1>12. Under the hypothesis of part (3),
$$
x_n\longrightarrow z.
$$

::: {.proof}
By steps <1>10 and <1>11,
$$
0\leq q_n\leq q_0^{2^n}
$$
for every $n$, by induction. Since
$$
0\leq q_0<1,
$$
the right-hand side tends to $0$. Thus $q_n\to0$, and hence
$$
\abs{x_n-z}
=
\frac{\varepsilon}{M}q_n
\longrightarrow0.
$$
This proves part (3).
:::

<1>13. Q.E.D.

::: {.proof}
Step <1>4 proves part (1), step <1>9 proves part (2), and step <1>12 proves
part (3).
:::
:::
