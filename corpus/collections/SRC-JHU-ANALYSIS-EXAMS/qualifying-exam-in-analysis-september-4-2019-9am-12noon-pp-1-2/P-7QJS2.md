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
**(a).**

<1>1. On $|z| \le 1/2$, $|f(z)| \le (\log \frac{1}{|z|})^{100}$.
::: {.proof}
hypothesis.
:::

<1>2. $\lim_{z \to 0} |z| \cdot |f(z)| \le \lim_{z \to 0} |z| (\log \frac{1}{|z|})^{100} = 0$.
::: {.proof}
Put $t=\log(1/|z|)$. The upper bound becomes
$e^{-t}t^{100}$, which tends to zero since
$e^t\geq t^{101}/101!$ for $t>0$.
:::

<1>3. Hence $|z f(z)| \to 0$ as $z \to 0$, so $f$ has a removable singularity at $0$ (by Riemann's removable singularity theorem, since $f$ is bounded by $o(1/|z|)$).
::: {.proof}
The function $h(z)=zf(z)$ tends to zero, so it is bounded
near zero and extends holomorphically with $h(0)=0$ by
the removable-singularity theorem [@SS03]. Its Taylor
series has zero constant term, so $h(z)=zH(z)$ for a
holomorphic $H$ near zero. For $z\ne0$ one has $H=f$.
This extends $f$ holomorphically across zero.
:::

**(b).**

<1>1. By (a), $f$ extends to a holomorphic function on $|z| < 2$, still denoted $f$.
::: {.proof}
(a).
:::

<1>2. $|f(z)| = 1$ on $|z| = 1$, and $f$ is holomorphic on $|z| \le 1$.
::: {.proof}
hypothesis and <1>1.
:::

<1>3. If $f(z) \neq 0$ in $|z| < 1$, then $1/f$ is holomorphic on $|z| < 1$ and $|1/f(z)| = 1$ on $|z| = 1$.
::: {.proof}
<1>2 and the nonvanishing hypothesis.
:::

<1>4. By the maximum modulus principle, $|f(z)| \le 1$ and $|1/f(z)| \le 1$ on $|z| < 1$, so $|f(z)| = 1$ on $|z| < 1$.
::: {.proof}
<1>2 and <1>3 (both $f$ and $1/f$ attain their maximum modulus on the boundary, where it is $1$).
:::

<1>5. Hence $f$ has constant modulus $1$ on the connected domain $|z| < 1$, so $f$ is constant.
::: {.proof}
The maximum modulus principle makes $f$ constant on the
unit disk, and the identity theorem extends that constant
to the connected disk $|z|<2$ [@SS03]. The nonvanishing
hypothesis in part (b) includes the extended value at zero.
:::

**(c).**

<1>1. The statement is false: take
$$
f(z)=z^{100}\frac{z-1/3}{1-z/3}.
$$
::: {.proof}
Its only possible finite pole is at $z=3$, so it is
holomorphic on the full disk $|z|<2$. For $a=1/3$,
direct expansion gives
$$
|1-az|^2-|z-a|^2=(1-a^2)(1-|z|^2).
$$
Thus the rational factor has modulus at most one for
$|z|\leq1$, and exactly one for $|z|=1$.
Consequently the example has the required unit boundary modulus.
:::

<1>2. The example satisfies the logarithmic bound with coefficient one.
::: {.proof}
For $0<r=|z|\leq1/2$, the preceding factor estimate gives
$|f(z)|\leq r^{100}$. Also
$\log(1/r)\geq\log2>1/2\geq r$, where
$\log2=\int_1^2dt/t>1/2$. Raising to the hundredth
power gives $|f(z)|\leq(\log(1/|z|))^{100}$.
:::

<1>3. The example is not a monomial of the asserted form.
::: {.proof}
It vanishes at $z=1/3$, whereas $\alpha z^n$ with
$|\alpha|=1$ has no nonzero zero. Thus it is a
counterexample satisfying all the original hypotheses.
The extra nonvanishing assumption in part (b) is not
an assumption in part (c).
:::

<1>4. Q.E.D.
::: {.proof}
<1>3 (a), <1>5 (b), <1>3 (c).
:::
:::
