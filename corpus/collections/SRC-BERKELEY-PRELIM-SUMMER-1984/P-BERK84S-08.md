---
schema: qual/card@1
id: P-BERK84S-08
kind: problem
title: Two integrations by parts for an oscillatory integral
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 8 of the vendored Berkeley Preliminary Exam, Summer 1984.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified both integrations by parts and the L1 bound on the second derivative.
---

::: {.problem}
Let $\varphi ( s )$ be $a C ^ { 2 }$ function on [1, 2] with $\varphi$ and $\varphi ^ { \prime }$ vanishing at $s = 1 , 2$ . Prove that there is a constant $C > 0$ such that for any $\lambda > 1$ ,

$$
\left| \int _ { 1 } ^ { 2 } e ^ { i \lambda x } \varphi ( x ) d x \right| \leqslant { \frac { C } { \lambda ^ { 2 } } } \cdotp
$$
:::


::: {.solution}
Set
\[
I_\lambda=\int_1^2 e^{i\lambda x}\varphi(x)\,dx.
\]

<1>1. Integrating by parts once removes one power of $\lambda$ without a boundary term.
::: {.proof}
Since
\[
\frac{d}{dx}e^{i\lambda x}=i\lambda e^{i\lambda x},
\]
we have
\[
I_\lambda
=\left[\frac{e^{i\lambda x}}{i\lambda}\varphi(x)\right]_1^2
-\frac1{i\lambda}\int_1^2 e^{i\lambda x}\varphi'(x)\,dx.
\]
Because $\varphi(1)=\varphi(2)=0$, the boundary term vanishes, so
\[
I_\lambda
=-\frac1{i\lambda}\int_1^2 e^{i\lambda x}\varphi'(x)\,dx.
\]
:::

<1>2. A second integration by parts gives a factor $\lambda^{-2}$.
::: {.proof}
Using also $\varphi'(1)=\varphi'(2)=0$,
\[
\int_1^2 e^{i\lambda x}\varphi'(x)\,dx
=-\frac1{i\lambda}\int_1^2 e^{i\lambda x}\varphi''(x)\,dx.
\]
Therefore
\[
I_\lambda
=\frac1{(i\lambda)^2}\int_1^2 e^{i\lambda x}\varphi''(x)\,dx
=-\frac1{\lambda^2}\int_1^2 e^{i\lambda x}\varphi''(x)\,dx.
\]
:::

<1>3. The desired estimate follows with a constant independent of $\lambda$.
::: {.proof}
Taking absolute values and using $|e^{i\lambda x}|=1$ gives
\[
|I_\lambda|
\le \frac1{\lambda^2}\int_1^2|\varphi''(x)|\,dx.
\]
Thus, with
\[
C=\int_1^2|\varphi''(x)|\,dx,
\]
we obtain for every $\lambda>1$
\[
\boxed{
\left|\int_1^2 e^{i\lambda x}\varphi(x)\,dx\right|
\le \frac{C}{\lambda^2}.
}
\]
:::
:::
