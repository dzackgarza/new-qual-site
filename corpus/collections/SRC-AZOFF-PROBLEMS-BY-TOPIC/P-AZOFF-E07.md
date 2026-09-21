---
schema: qual/card@1
id: P-AZOFF-E07
kind: problem
title: Absolute and uniform convergence of power series inside the disk of convergence
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Liouville, FTA, and power series, Problem 7, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Convergence at z_0 makes the terms a_n z_0^n bounded. Comparing
    |a_n z^n| with a geometric series proves absolute convergence for
    |z|<|z_0|, and the same bound with |z| replaced by r gives the
    Weierstrass M-test uniformly on |z|<=r.
---

::: {.problem}
Suppose the complex power series $\textstyle \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }$ converges for some $z _ { 0 } \neq 0$

a) Prove that the series converges absolutely for each z with $| z | < | z _ { 0 } |$

b) Suppose $0 < r < | z _ { 0 } |$ . Show that the series converges uniformly on $| z | \leq r$
:::

::: {.solution}
Since
$$
\sum_{n=0}^{\infty}a_nz_0^n
$$
converges, its terms form a bounded sequence. Choose $M\geq0$ such that
$$
\abs{a_nz_0^n}\leq M
$$
for every $n\geq0$.

<1>1. If $\abs{z}<\abs{z_0}$, then
$$
\sum_{n=0}^{\infty}a_nz^n
$$
converges absolutely.

::: {.proof}
Set
$$
q=\frac{\abs{z}}{\abs{z_0}}.
$$
Then $0\leq q<1$, and for every $n$,
$$
\begin{aligned}
\abs{a_nz^n}
&=
\abs{a_nz_0^n}
\left(\frac{\abs{z}}{\abs{z_0}}\right)^n\\
&\leq
Mq^n.
\end{aligned}
$$
The geometric series
$$
\sum_{n=0}^{\infty}Mq^n
$$
converges, so comparison proves
$$
\sum_{n=0}^{\infty}\abs{a_nz^n}<\infty.
$$
:::

<1>2. If $0<r<\abs{z_0}$, then the series converges uniformly on
$$
\abs{z}\leq r.
$$

::: {.proof}
Put
$$
q_r=\frac{r}{\abs{z_0}},
$$
so $0<q_r<1$. For every $z$ with $\abs{z}\leq r$ and every $n$,
$$
\begin{aligned}
\abs{a_nz^n}
&=
\abs{a_nz_0^n}
\left(\frac{\abs{z}}{\abs{z_0}}\right)^n\\
&\leq
Mq_r^n.
\end{aligned}
$$
The numerical series
$$
\sum_{n=0}^{\infty}Mq_r^n
$$
converges. Hence the Weierstrass M-test gives uniform convergence on
$\abs{z}\leq r$.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>1 proves part (a), and step <1>2 proves part (b).
:::
:::
