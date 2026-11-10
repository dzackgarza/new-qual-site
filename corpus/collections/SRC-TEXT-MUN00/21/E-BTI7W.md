---
schema: qual/card@1
id: E-BTI7W
kind: problem
title: Pointwise but not uniform convergence to the zero function
classification:
  areas:
  - topology
  topics:
  - Uniform Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §21 Exercise 9, printed p. 134, with Figure 21.1
    and Theorem 21.6; both parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 21.9, PDF pp. 25-26. The pointwise limit is 0 — at
    the origin because the denominator is n+1, and elsewhere because n^2(nx^2 - 2x)
    dominates — while at x_n = 1/n each f_n equals 1, so the convergence is not uniform;
    with continuous f_n that also follows from Exercise 21.8. (tmp/sources/munkres-
    solutions-positron-ch2.pdf).
---

::: {.exercise}

Let $f_n: \RR \to \RR$ be the function

$$
f_n(x) = \frac{1}{n^3[x - (1/n)]^2 + 1}.
$$

Let $f: \RR \to \RR$ be the zero function.

(a) Show that $f_n(x) \to f(x)$ for each $x \in \RR$.

(b) Show that $f_n$ does not converge uniformly to $f$.
(This shows that the converse of Theorem 21.6 does not hold; the limit function $f$ may be continuous even though the convergence is not uniform.)
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 21.9, PDF pp. 25--26** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); both parts are theirs.

Let $f_{n}(x)=1/\big(n^{3}[x-(1/n)]^{2}+1\big)$ and let $f$ be the zero function.

(a) *Pointwise convergence.* For $x=0$, $f_{n}(0)=1/(n+1)\to0$. For $x\ne0$ and $n$ large, the denominator is
$$
n^{3}\Big(x^{2}-\frac{2x}{n}+\frac{1}{n^{2}}\Big)+1=n^{2}\big(nx^{2}-2x\big)+n+1,
$$
which tends to $+\infty$ with $n$ because $x^{2}>0$; so $f_{n}(x)\to0=f(x)$. (Concretely, for any $x\ne0$ and $0<\varepsilon<1$ choose $N$ with $n^{2}(nx^{2}-2x)>2/\varepsilon$ and $n>\varepsilon^{-1}$; then $\abs{f_{n}(x)}<1/n<\varepsilon$ for $n\ge N$.)

(b) *The convergence is not uniform.* At $x_{n}=1/n$,
$$
f_{n}(x_{n})=\frac{1}{n^{3}\cdot0+1}=1
$$
for every $n$, while $x_{n}\to0$ and $f(0)=0$; so $f_{n}(x_{n})\not\to f(0)$. Each $f_{n}$ is continuous, so by Exercise 21.8 the convergence cannot be uniform. Directly: $\sup_{x}\abs{f_{n}(x)-f(x)}=1$ for every $n$.
:::
