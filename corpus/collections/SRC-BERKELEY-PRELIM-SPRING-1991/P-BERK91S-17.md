---
schema: qual/card@1
id: P-BERK91S-17
kind: problem
title: An $L^2$ growth bound on circles truncates the negative Laurent tail
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $f$ be analytic on the punctured disk
\[
0<|z|<r_0
\]
with Laurent expansion
\[
f(z)=\sum_{n=-\infty}^{\infty}c_nz^n.
\]
Suppose there is $M>0$ such that
\[
r^4\int_0^{2\pi}|f(re^{i\theta})|^2\,d\theta<M
\qquad(0<r<r_0).
\]
Prove that
\[
c_n=0
\qquad(n<-2).
\]
:::

::: {.solution}
Fix an integer $n$.

::: pf

::: {.pf-step #s1}

For every $0<r<r_0$,
$$
2\pi\abs{c_n}^2r^{2n+4}
\le
r^4\int_0^{2\pi}\abs{f(re^{i\theta})}^2\,d\theta.
$$

::: pf-proof

The Laurent coefficient formula on the circle $\abs{z}=r$ gives
$$
c_nr^n
=\frac1{2\pi}\int_0^{2\pi}
f(re^{i\theta})e^{-in\theta}\,d\theta.
$$
By the Cauchy--Schwarz inequality,
$$
\abs{c_n}^2r^{2n}
\le
\frac1{(2\pi)^2}
\left(\int_0^{2\pi}\abs{f(re^{i\theta})}^2\,d\theta\right)
\left(\int_0^{2\pi}1\,d\theta\right),
$$
which is the claimed inequality after multiplying by $2\pi r^4$.

:::

:::

::: {.pf-step #s2}

If $n<-2$, then $c_n=0$.

::: pf-proof

The hypothesis and step [](#s1){.pf-ref} give
$$
2\pi\abs{c_n}^2r^{2n+4}<M
\qquad(0<r<r_0).
$$
For $n<-2$, the exponent $2n+4$ is negative. If $c_n\ne0$, then the
left-hand side tends to $+\infty$ as $r\downarrow0$, contradicting
the uniform upper bound $M$. Hence $c_n=0$.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} applies to every integer $n<-2$.

:::

:::

:::
