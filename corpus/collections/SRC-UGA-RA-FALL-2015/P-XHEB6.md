---
schema: qual/card@1
id: P-XHEB6
kind: problem
title: An even-degree polynomial with positive leading coefficient attains a global
  minimum
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Polynomials
relations: []
review: draft
---

::: problem
Define
\[
f(x)=c_{0}+c_{1} x^{1}+c_{2} x^{2}+\ldots+c_{n} x^{n} \text { with } n \text { even and } c_{n}>0.
\]

Show that there is a number $x_m$ such that $f(x_m) \leq f(x)$ for all $x\in \RR$.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. $f(x) \to +\infty$ as $|x| \to \infty$.
Proof: $f(x) = x^n\big(c_n + c_{n-1}x^{-1} + \cdots + c_0 x^{-n}\big)$, and the bracket tends to $c_n > 0$ as $|x|\to\infty$; hence $f(x) \sim c_n x^n \to +\infty$ ($n$ even, so $x^n \to +\infty$ on both sides).
<1>2. Choose $R$ with $f(x) > f(0)$ whenever $|x| > R$.
Proof: by <1>1, $\lim_{|x|\to\infty} f(x) = +\infty > f(0)$, so such $R$ exists.
<1>3. $f$ attains a minimum on $[-R,R]$.
Proof: $f$ is a polynomial, hence continuous, and $[-R,R]$ is compact; a continuous function on a compact set attains its minimum.
<1>4. There is $x_m \in \RR$ with $f(x_m) \le f(x)$ for all $x \in \RR$.
Proof: by <1>3, let $x_m \in [-R,R]$ satisfy $f(x_m) = \min_{[-R,R]} f$.
For $|x| \le R$: $f(x_m) \le f(x)$ by choice.
For $|x| > R$: $f(x) > f(0) \ge f(x_m)$ by <1>2 and $0 \in [-R,R]$.
Hence $f(x_m) \le f(x)$ for every $x \in \RR$.
<1>5. Q.E.D.
:::
