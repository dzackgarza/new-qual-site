---
schema: qual/card@1
id: P-L8LEM
kind: problem
title: $C_{\RR}(X)$ is complete in the maximum norm when $X$ is compact metric
classification:
  areas:
  - real-analysis
  topics:
  - Function Spaces
  - Completeness
  - Norms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 6 of the UGA Fall 2017 real-analysis qualifying exam recorded by SRC-UGA-RA-FALL-2017.
- event: solution-written
  by: prior-author
  date: 2026-08-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Merged P-UHFLP, a restatement of this problem for bounded continuous functions on an arbitrary metric space; its solution repeats this Cauchy-sequence argument and was not carried."
---

::: {.problem}
Let $X$ be a compact metric space and equip the space $C_{\RR}(X)$ of continuous functions from $X$ to $\RR$ with the maximum norm
$$
\norm{f}:=\max\{\abs{f(x)}:x\in X\}.
$$
Prove that this norm is complete.
:::

::: {.solution}

The argument is the card's own, the standard uniform-limit proof; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $X$ be a compact metric space and $\norm{f}=\max\{\abs{f(x)}:x\in X\}$ for $f\in C_{\RR}(X)$.

::: pf

::: {.pf-step #norm}
The maximum defining $\norm{f}$ exists, and $\norm{\cdot}$ is a norm on $C_{\RR}(X)$.

::: pf-proof
$x\mapsto\abs{f(x)}$ is continuous on the compact space $X$, so it attains its maximum: $x\mapsto\abs{f(x)}$ is continuous from the compact space $X$ to the ordered space $\RR$, so the extreme value theorem (Theorem 27.4) gives $d\in X$ with $\abs{f(x)}\le\abs{f(d)}$ for every $x$. The resulting expression is nonnegative, vanishes only at the zero function, is homogeneous under scalars, and satisfies the triangle inequality, since $\abs{(f+g)(x)}\le\abs{f(x)}+\abs{g(x)}\le\norm{f}+\norm{g}$ for every $x$.
:::

:::

::: {.pf-step #pointwise}
If $(f_{n})$ is Cauchy in $\norm{\cdot}$, then $(f_{n}(x))$ converges for every $x\in X$; define $f(x)=\lim_{n}f_{n}(x)$.

::: pf-proof
For $x\in X$, $\abs{f_{n}(x)-f_{m}(x)}\le\norm{f_{n}-f_{m}}$ because the maximum dominates each value, so $(f_{n}(x))$ is a Cauchy sequence in $\RR$; $\RR$ is complete, so it converges.
:::

:::

::: {.pf-step #uniform}
For every $\varepsilon>0$ there is $N$ with $\abs{f_{n}(x)-f(x)}\le\varepsilon$ for all $n\ge N$ and all $x\in X$.

::: pf-proof
Let $\varepsilon>0$ and choose $N$ with $\norm{f_{n}-f_{m}}<\varepsilon$ for all $n,m\ge N$, which the Cauchy property allows. Fix $n\ge N$ and $x\in X$; then $\abs{f_{n}(x)-f_{m}(x)}<\varepsilon$ for every $m\ge N$, and letting $m\to\infty$ along the convergent sequence of step [](#pointwise){.pf-ref} gives $\abs{f_{n}(x)-f(x)}\le\varepsilon$, the strict inequality passing to a non-strict one in the limit. Neither $N$ nor the estimate depends on $x$.
:::

:::

::: {.pf-step #complete}
$f\in C_{\RR}(X)$ and $\norm{f_{n}-f}\to0$, so $C_{\RR}(X)$ is complete.

::: pf-proof
Step [](#uniform){.pf-ref} says that $f_{n}\to f$ uniformly on $X$. A uniform limit of continuous functions is continuous: given $\varepsilon>0$ choose $n$ with $\abs{f_{n}(z)-f(z)}\le\varepsilon/3$ for all $z$, and for $x\in X$ a neighbourhood $U$ of $x$ with $\abs{f_{n}(z)-f_{n}(x)}<\varepsilon/3$ on $U$; then $\abs{f(z)-f(x)}<\varepsilon$ on $U$. So $f\in C_{\RR}(X)$, and the estimate of step [](#uniform){.pf-ref} with $\varepsilon$ arbitrary gives $\norm{f_{n}-f}\le\varepsilon$ for $n\ge N$, that is $\norm{f_{n}-f}\to0$. Every Cauchy sequence in $C_{\RR}(X)$ therefore converges in it, which is completeness.
:::

:::

:::
:::
