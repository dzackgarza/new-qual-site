---
schema: qual/card@1
id: E-SS1.EX-17
kind: problem
title: "SS 1.17: The ratio test computes the radius of convergence"
classification:
  areas:
  - complex-analysis
  topics: ['Complex Numbers', 'Power Series', 'Cauchy-Riemann']
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: exercise
17. Show that if $\{ a _ { n } \} _ { n = 0 } ^ { \infty }$ is a sequence of non-zero complex numbers such that

$$
\lim _ {n \to \infty} \frac {| a _ {n + 1} |}{| a _ {n} |} = L,
$$

then

$$
\lim _ {n \to \infty} | a _ {n} | ^ {1 / n} = L.
$$

In particular, this exercise shows that when applicable, the ratio test can be used to calculate the radius of convergence of a power series.
:::

::: {.solution}
<1>1. Let $\varepsilon > 0$.
::: {.proof}
fix an arbitrary tolerance.
:::

<1>2. There exists $N$ such that for all $n \ge N$, $L - \varepsilon < \frac{|a_{n+1}|}{|a_n|} < L + \varepsilon$.
::: {.proof}
the hypothesis $\lim \frac{|a_{n+1}|}{|a_n|} = L$.
:::

<1>3. For $n > N$, $|a_n| = |a_N| \prod_{k=N}^{n-1} \frac{|a_{k+1}|}{|a_k|}$.
::: {.proof}
telescoping product.
:::

<1>4. Hence $|a_N| (L - \varepsilon)^{n-N} < |a_n| < |a_N| (L + \varepsilon)^{n-N}$.
::: {.proof}
<1>2 and <1>3.
:::

<1>5. Taking $n$-th roots: $|a_N|^{1/n} (L - \varepsilon)^{(n-N)/n} < |a_n|^{1/n} < |a_N|^{1/n} (L + \varepsilon)^{(n-N)/n}$.
::: {.proof}
<1>4, and $n$-th roots preserve order for positive quantities.
:::

<1>6. As $n \to \infty$, $|a_N|^{1/n} \to 1$ and $(n-N)/n \to 1$.
::: {.proof}
$|a_N|$ is a fixed positive constant.
:::

<1>7. Hence $L - \varepsilon \le \liminf |a_n|^{1/n} \le \limsup |a_n|^{1/n} \le L + \varepsilon$.
::: {.proof}
<1>5 and <1>6.
:::

<1>8. Since $\varepsilon > 0$ was arbitrary, $\lim |a_n|^{1/n} = L$.
::: {.proof}
<1>7, letting $\varepsilon \to 0$.
:::

<1>9. Q.E.D.
::: {.proof}
<1>8.
:::
:::
