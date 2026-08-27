---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-14
kind: problem
title: Use an epsilon–delta proof for a quotient of convergent sequences
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
(January 2008 #6b) Suppose that $\lim_{n\to\infty}s_n=s$ and $\lim_{n\to\infty}t_n=t$ with $s\ne t$ and $s_n\ne t_n$ for all $n$.
Use an $\epsilon$-$\delta$ proof to show that
$$
\lim_{n\to\infty}\frac{s_n+t_n}{s_n-t_n}=\frac{s+t}{s-t}.
$$
:::

:::: {.solution}
<1>1. Reduce to a direct $\epsilon$-$N$ estimate on the difference.
Proof: put the two quotients over a common denominator: \[\frac{s_n + t_n}{s_n - t_n} - \frac{s + t}{s - t} = \frac{(s_n + t_n)(s - t) - (s + t)(s_n - t_n)}{(s_n - t_n)(s - t)} = \frac{2(s t_n - s_n t)}{(s_n - t_n)(s - t)}.\] Adding and subtracting $st$ in the numerator, $s t_n - s_n t = s(t_n - t) - t(s_n - s)$, so \[\frac{s_n + t_n}{s_n - t_n} - \frac{s+t}{s-t} = \frac{2\big(s(t_n - t) - t(s_n - s)\big)}{(s_n - t_n)(s - t)}.\] <1>2. Bound the numerator.
Proof: since $s \ne t$, $\delta := |s - t|/2 > 0$; and $s_n \to s$, $t_n \to t$, so for large $n$, $|s_n - s| < \delta/2$ and $|t_n - t| < \delta/2$, giving $|s_n - t_n| \ge |s - t| - |s_n - s| - |t_n - t| \ge \delta > 0$; the denominator is bounded below in modulus by $\delta|s-t| = 2\delta^2$... precisely $|(s_n - t_n)(s-t)| \ge \delta \cdot |s-t|$.
<1>3. $\epsilon$-$N$ conclusion.
Proof: let $\epsilon > 0$.
Choose $N$ so that for $n \ge N$: $|s_n - s| < \frac{\epsilon\,\delta\,|s-t|}{4|t| + 4|s| + 1}$ (and similarly for $t_n - t$) and $|s_n - t_n| \ge \delta$.
Then \[\left|\frac{s_n + t_n}{s_n - t_n} - \frac{s+t}{s-t}\right| \le \frac{2\big(|s||t_n - t| + |t||s_n - s|\big)}{\delta\,|s - t|} < \epsilon.\] Hence the quotient converges to $\frac{s+t}{s-t}$.
<1>4. Q.E.D.
:::
