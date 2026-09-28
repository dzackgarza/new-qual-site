---
schema: qual/card@1
id: P-TFXE2
kind: problem
title: $Hf(x)\ge\frac{c}{(1+|x|)^n}$ for $0\neq f\in L^1(\RR^n)$
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
---

::: {.problem}
Let $f\in L^1(\RR^n)$ with $f\neq 0$.

a. Prove that there exists a $c>0$ such that
\[
Hf(x) \geq {c \over (1 + \abs x)^n }
.\]
:::
::: {.solution}
Here $Hf(x) = \sup_{s > 0}\frac{1}{m(B(x,s))}\int_{B(x,s)}|f|$ is the Hardy--Littlewood maximal function, and $m(B(x,s)) = \omega_n s^n$ with $\omega_n$ the volume of the unit ball.

<1>1. There is $r > 0$ with $\alpha \coloneqq \int_{B(0,r)}|f| > 0$.

::: {.proof}
$\int_{B(0,k)}|f| \to \int_{\RR^n}|f| > 0$ as $k \to \infty$ by monotone convergence, and $\int |f| > 0$ because $f \neq 0$ in $L^1$.
:::

<1>2. $Hf(x) \ge \frac{\alpha}{\omega_n(|x| + r)^n}$ for every $x$.

::: {.proof}
For $z \in B(0,r)$, $|z - x| \le |z| + |x| < r + |x|$, so $B(0,r) \subseteq B(x, |x| + r)$. Taking $s = |x| + r$ in the definition of $Hf$ gives $Hf(x) \ge \frac{1}{\omega_n(|x| + r)^n}\int_{B(0,r)}|f|$.
:::

<1>3. Q.E.D.

::: {.proof}
$|x| + r \le (1 + r)(1 + |x|)$, so step <1>2 gives $Hf(x) \ge \frac{c}{(1+|x|)^n}$ with $c = \frac{\alpha}{\omega_n(1 + r)^n} > 0$.
:::
:::
