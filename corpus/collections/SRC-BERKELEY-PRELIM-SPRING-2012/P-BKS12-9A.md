---
schema: qual/card@1
id: P-BKS12-9A
kind: problem
title: Smooth functions with an entire asymptotic Taylor series
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
  note: Compared the authored statement with page 3 of the retained Spring 2012 solution PDF and independently reviewed the flat-function counterexample.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked smoothness and flatness of e^{-1/x^2} at zero and verified every stated asymptotic condition with all coefficients a_n equal to zero.
---

::: {.problem}
Suppose the power series $\sum _ { n } a _ { n } x ^ { n }$ converges for all real $x ,$ and the smooth real valued function $f$ has the property that

$$
\operatorname* { l i m } _ { x \to 0 } { \frac { f ( x ) - \sum _ { j = 0 } ^ { n } a _ { j } x ^ { j } } { x ^ { n } } } = 0
$$

for all n. Prove or give a counterexample to the claim that $\textstyle f ( x ) = \sum _ { n } a _ { n } x ^ { n }$
:::

::: {.solution}
Take
$$
a_n=0
$$
for every $n\geq0$, and define
$$
f(x)
\coloneqq
\begin{cases}
e^{-1/x^2},&x\neq0,\\
0,&x=0.
\end{cases}
$$

::: pf

::: {.pf-step #s1}

For every integer $N\geq0$,
$$
\lim_{x\to0}
\frac{e^{-1/x^2}}{\abs{x}^N}
=
0.
$$

::: pf-proof

Put
$$
t=\frac1{x^2}.
$$
Then $t\to+\infty$ as $x\to0$, and
$$
\frac{e^{-1/x^2}}{\abs{x}^N}
=
t^{N/2}e^{-t}.
$$
Choose an integer $m>N/2$. Since
$$
e^t
\geq
\frac{t^m}{m!},
$$
one has
$$
0
\leq
t^{N/2}e^{-t}
\leq
m!t^{N/2-m}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s2}

The function $f$ is smooth on $\RR$, and
$$
f^{(k)}(0)=0
$$
for every $k\geq0$.

::: pf-proof

Away from $0$, the function is smooth. Repeated differentiation shows
inductively that for every $k\geq0$ there is a polynomial $P_k$ such that
for $x\neq0$,
$$
f^{(k)}(x)
=
P_k(1/x)e^{-1/x^2}.
$$
For $k=0$ take $P_0=1$. Differentiating
$P_k(1/x)e^{-1/x^2}$ gives
$$
\bigl(-x^{-2}P_k'(1/x)+2x^{-3}P_k(1/x)\bigr)e^{-1/x^2},
$$
so $P_{k+1}(t)=-t^2P_k'(t)+2t^3P_k(t)$.

Step [](#s1){.pf-ref} implies that every such expression tends to $0$ as $x\to0$.
Inductively, if $f^{(k)}(0)=0$, then
$$
f^{(k+1)}(0)
=
\lim_{x\to0}\frac{f^{(k)}(x)}x
=
0
$$
again by step [](#s1){.pf-ref}. The same decay shows that $f^{(k+1)}(x)\to0$ as
$x\to0$, so each derivative is continuous there. Thus $f\in C^\infty(\RR)$
and all derivatives at $0$ vanish.

:::

:::

::: {.pf-step #s3}

The power series
$$
\sum_{n=0}^{\infty}a_nx^n
$$
converges for every real $x$.

::: pf-proof

Every coefficient is zero, so the series is identically zero.

:::

:::

::: {.pf-step #s4}

For every integer $n\geq0$,
$$
\lim_{x\to0}
\frac{
f(x)-\sum_{j=0}^n a_jx^j
}{x^n}
=
0.
$$

::: pf-proof

Since all $a_j$ vanish, the quotient is
$$
\frac{f(x)}{x^n}.
$$
For $x\neq0$ its absolute value is
$$
\frac{e^{-1/x^2}}{\abs{x}^n},
$$
which tends to $0$ by step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s5}

The claimed identity fails.

::: pf-proof

The power series is identically zero by step [](#s3){.pf-ref}, while
$$
f(1)=e^{-1}\neq0.
$$
Thus
$$
f(x)\neq\sum_{n=0}^{\infty}a_nx^n.
$$

:::

:::

::: {.pf-step #s6}

Therefore the claim is
$$
\boxed{\text{false}}.
$$

::: pf-proof

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} give a smooth function and an everywhere-convergent
power series satisfying every hypothesis but not the proposed conclusion.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} supplies the requested counterexample.

:::

:::

:::
