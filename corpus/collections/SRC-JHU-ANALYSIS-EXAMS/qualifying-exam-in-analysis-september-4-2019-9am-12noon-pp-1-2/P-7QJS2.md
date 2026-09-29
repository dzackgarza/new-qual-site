---
schema: qual/card@1
id: P-7QJS2
kind: problem
title: "A holomorphic function on the punctured disk dominated by a power of the logarithm"
classification:
  areas:
  - complex-analysis
  topics:
  - Isolated Singularities
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared all three parts with September 2019 Complex Analysis 4 in the retained extraction; part (c) does not assume the extra nonvanishing condition of part (b)."
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Repaired the false extra-credit conclusion, verified the example on the full radius-two disk and the exact logarithmic bound, and supplied the removable-singularity and identity-theorem steps."
---

::: {.problem}
4. Let f be a holomorphic function in the punctured disk $\{ z : 0 < | z | < 2 \}$ satisfying

$$
| f ( z ) | \leq ( \log { \frac { 1 } { | z | } } ) ^ { 1 0 0 } \mathrm { { i n } } \left\{ | z | \leq 1 / 2 \right\} ,
$$

$$
| f ( z ) | = 1 \ \mathrm { o n } \ | z | = 1 .
$$

a. Show that f has a removable singularity at the origin.

b. Show that if $f ( z ) \neq 0$ in $| z | < 1$ , then f is constant.

c. (Extra credit) True or false, explain.

$f = \alpha z ^ { n }$ for $\alpha \in \mathbb { C } , | \alpha | = 1$ and an integer $n \geq 0$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

(a) $f$ has a removable singularity at $0$.

::: pf-proof

With $t=\log(1/\abs z)$, the hypothesis gives $\abs{zf(z)}\le e^{-t}t^{100}\le101!/t$ for $\abs z\le1/2$, using $e^t\ge t^{101}/101!$, so $zf(z)\to0$ as $z\to0$. By the removable singularity theorem $h(z)=zf(z)$ extends holomorphically with $h(0)=0$, so $h(z)=zH(z)$ with $H$ holomorphic near $0$, and $H$ extends $f$ [@SS03].

:::

:::

::: {.pf-step #s2}

(b) If $f$, extended by step [](#s1){.pf-ref}, has no zero in $\abs z<1$, then $f$ is constant.

::: pf-proof

Both $f$ and $1/f$ are holomorphic on $\abs z\le1$ with modulus $1$ on $\abs z=1$, so the maximum modulus principle gives $\abs f\le1$ and $\abs{1/f}\le1$ there. So $\abs f\equiv1$ on $\abs z<1$, where $f$ attains its maximum modulus at an interior point; hence $f$ is constant on $\abs z<1$, and on the connected disk $\abs z<2$ by the identity theorem.

:::

:::

::: {.pf-step #s3}

(c) False: $f(z)=z^{100}\frac{z-1/3}{1-z/3}$ satisfies both hypotheses and is not of the form $\alpha z^n$.

::: pf-proof

$f$ is holomorphic on $\abs z<2$, since its only pole is $z=3$. For $a=1/3$, $\abs{1-az}^2-\abs{z-a}^2=(1-a^2)(1-\abs z^2)$, so the rational factor has modulus $1$ on $\abs z=1$ and at most $1$ on $\abs z\le1$. Hence $\abs f=1$ on $\abs z=1$, and for $0<r=\abs z\le1/2$, $\abs{f(z)}\le r^{100}\le(\log(1/r))^{100}$, because $\log(1/r)\ge\log2>1/2\ge r$. Finally $f(1/3)=0$, while $\alpha z^n$ with $\abs\alpha=1$ has no zero other than $0$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} answer parts (a), (b) and (c).

:::

:::

:::
