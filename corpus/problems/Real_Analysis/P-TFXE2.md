---
schema: qual/card@1
id: P-TFXE2
kind: problem
title: $Hf(x)\ge\frac{c}{(1+\norm{x})^n}$ for $0\neq f\in L^1(\RR^n)$
classification:
  areas:
  - real-analysis
  topics:
  - Maximal Functions
  - L¹
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source used Hf without defining it and did not quantify x; the statement now names Hf as the Hardy-Littlewood maximal function and asks for the bound for every x in R^n.
---

::: {.problem}

Let $f\in L^1(\RR^n)$ with $f\neq 0$, and let $Hf$ be its Hardy--Littlewood maximal function. Prove that there exists a $c>0$ such that for every $x\in\RR^n$,
$$
Hf(x) \geq \frac{c}{(1 + \abs x)^n}.
$$

:::

::: {.solution}

Here $Hf(x) = \sup_{s > 0}\frac{1}{m(B(x,s))}\int_{B(x,s)}\abs{f}$ is the Hardy--Littlewood maximal function, and $m(B(x,s)) = \omega_n s^n$ with $\omega_n$ the volume of the unit ball.

::: pf

::: pf-step

There is $r > 0$ with $\alpha \coloneqq \int_{B(0,r)}\abs{f} > 0$.

::: pf-proof

$\int_{B(0,k)}\abs{f} \to \int_{\RR^n}\abs{f} > 0$ as $k \to \infty$ by monotone convergence, and $\int \abs{f} > 0$ because $f \neq 0$ in $L^1$.

:::

:::

::: {.pf-step #s2}

$Hf(x) \ge \frac{\alpha}{\omega_n(\norm{x} + r)^n}$ for every $x$.

::: pf-proof

For $z \in B(0,r)$, $\norm{z - x} \le \norm{z} + \norm{x} < r + \norm{x}$, so $B(0,r) \subseteq B(x, \norm{x} + r)$. Taking $s = \norm{x} + r$ in the definition of $Hf$ gives $Hf(x) \ge \frac{1}{\omega_n(\norm{x} + r)^n}\int_{B(0,r)}\abs{f}$.

:::

:::

::: pf-qed

$\norm{x} + r \le (1 + r)(1 + \norm{x})$, so step [](#s2){.pf-ref} gives $Hf(x) \ge \frac{c}{(1+\norm{x})^n}$ with $c = \frac{\alpha}{\omega_n(1 + r)^n} > 0$.

:::

:::

:::
