---
schema: qual/card@1
id: P-BKF20-5A
kind: problem
title: Laurent series for $1/(z(1+z^2))$
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked both recorded source appearances. The inner Laurent
    expansion is valid on the punctured disk 0<|z|<1 and the outer expansion
    on |z|>1, obtained from the corresponding geometric series.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked both geometric-series substitutions, the powers after multiplying
    by 1/z or 1/z^3, and the exact annuli of convergence.
---

::: {.problem}
Let $f(z)=1/(z(1+z^2))$.

(a) Find a Laurent series representing $f$ for $|z|<1$.

(b) Find another Laurent series representing $f$ for $|z|>1$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

On
$$
0<|z|<1,
$$
one has
$$
\frac1{1+z^2}
=
\sum_{n=0}^{\infty}(-1)^n z^{2n}.
$$

::: pf-proof

For $|z|<1$, one has $|z^2|<1$, so the geometric-series identity
$$
\frac1{1-w}
=
\sum_{n=0}^{\infty}w^n
$$
applied to $w=-z^2$ gives
$$
\frac1{1+z^2}
=
\sum_{n=0}^{\infty}(-z^2)^n
=
\sum_{n=0}^{\infty}(-1)^n z^{2n}.
$$
The puncture at $z=0$ is required because $f$ itself has a pole there.

:::

:::

::: {.pf-step #s2}

Therefore, for
$$
0<|z|<1,
$$
the Laurent series of $f$ is
$$
\boxed{
f(z)
=
\sum_{n=0}^{\infty}(-1)^n z^{2n-1}.
}
$$

::: pf-proof

By step [](#s1){.pf-ref},
$$
\begin{aligned}
f(z)
&=
\frac1z\frac1{1+z^2}\\
&=
\frac1z
\left(
\sum_{n=0}^{\infty}(-1)^n z^{2n}
\right)\\
&=
\sum_{n=0}^{\infty}(-1)^n z^{2n-1}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s3}

On
$$
|z|>1,
$$
one has
$$
\frac1{1+z^{-2}}
=
\sum_{n=0}^{\infty}(-1)^n z^{-2n}.
$$

::: pf-proof

If $|z|>1$, then
$$
|z^{-2}|<1.
$$
Applying the geometric series to $w=-z^{-2}$ gives the displayed
identity.

:::

:::

::: {.pf-step #s4}

Therefore, for
$$
|z|>1,
$$
the Laurent series of $f$ is
$$
\boxed{
f(z)
=
\sum_{n=0}^{\infty}(-1)^n z^{-2n-3}.
}
$$

::: pf-proof

Rewrite
$$
f(z)
=
\frac1{z(1+z^2)}
=
\frac1{z^3}\frac1{1+z^{-2}}.
$$
Using step [](#s3){.pf-ref},
$$
\begin{aligned}
f(z)
&=
\frac1{z^3}
\left(
\sum_{n=0}^{\infty}(-1)^n z^{-2n}
\right)\\
&=
\sum_{n=0}^{\infty}(-1)^n z^{-2n-3}.
\end{aligned}
$$

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref} and [](#s4){.pf-ref} give the two requested Laurent expansions and
their domains.

:::

:::

:::
