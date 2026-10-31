---
schema: qual/card@1
id: P-PRACT20-W6-04
kind: problem
title: Pointwise and uniform convergence of $x^n/(1+x^n)$ on $[0,1]$
classification:
  areas:
  - prelim
  topics:
  - Uniform Convergence
  - Pointwise Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Moved choice (C) out of a display into its labelled paragraph and restored the arrows lost from the solution display, checked against Week6_solns.pdf page 2 (Problem 4, which has only choices A-C).
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored two arrows lost from inline solution formulas and dropped a stray 2, checked against Week6_solns.pdf page 2 (Problem 4).
---

::: {.problem}
Define $f_n(x) = \frac{x^n}{1 + x^n}$ for $x \in [0, 1]$, $n \in \NN$. Which of the following is true?

(A) The sequence $\{f_n\}$ converges pointwise on $[0, 1]$ to a limit function $f$.

(B) The sequence $\{f_n\}$ converges uniformly on $[0, 1]$ to a limit function $f$.

(C) $\displaystyle\lim_{n \to \infty} \int_0^1 f_n(x)\,dx = \int_0^1 \left(\lim_{n \to \infty} f_n(x)\right) dx$
:::

::: {.solution}
(A) and (C) are true; (B) is false.

At $x=1$, $f_n(1)=1/2$ for all $n$. For $x\in[0,1)$,

$$
0\leq f_n(x)=\frac{x^n}{1+x^n}\leq x^n\to0\quad\text{as }n\to\infty.
$$

Thus $f_n$ converges pointwise to

$$
f(x)=\begin{cases}0,&x\in[0,1),\\1/2,&x=1.\end{cases}
$$

Each $f_n$ is continuous but $f$ is not, so the convergence is not uniform, since a uniform limit of continuous functions is continuous.

For (C),

$$
0\leq\int_0^1f_n(x)\,dx=\int_0^1\frac{x^n}{1+x^n}\,dx\leq\int_0^1x^n\,dx=\frac{1}{n+1}\to0,
$$

and $\int_0^1f(x)\,dx=0$, so $\int_0^1f_n\to\int_0^1f$.
:::
