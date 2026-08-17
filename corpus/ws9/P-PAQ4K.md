---
schema: qual/card@1
id: P-PAQ4K
kind: problem
title: Assume that $f_1, f_2, \ldots$ is a sequence of positive continuous fu…
classification:
  areas:
  - real-analysis
  topics:
  - fatou
  - convergence-of-integrals
  - counterexamples
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Assume that $f_1, f_2, \ldots$ is a sequence of positive continuous functions defined on $[0,1]$ with $$f(x) = \lim_{n\to\infty} f_n(x) \text{ for every } x \in [0,1]$$ and $$\int_0^1 f_n(x)dx = 1.$$

a. Is it always true that $\int_0^1 f(x)dx \le 1$?
Provide a proof if it is true or provide a counter example if it is false.
b. Is it always true that $\int_0^1 f(x)dx \ge 1$?
Provide a proof if it is true or provide a counter example if it is false.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. (a) is TRUE: $\int_0^1 f \le 1$.
Proof: $f_n > 0$ for all $n$, so by Fatou's lemma, \[\int_0^1 f(x)\,dx = \int_0^1 \liminf_{n\to\infty} f_n(x)\,dx \le \liminf_{n\to\infty}\int_0^1 f_n(x)\,dx = \liminf_{n\to\infty}1 = 1.\] <1>2. (b) is FALSE: $\int_0^1 f \ge 1$ need not hold.
Proof: construct continuous positive spikes of integral $1$ collapsing to $0$ off a point.
Let $\phi$ be the continuous tent $\phi(t) = \max(0, 1 - |t|)$ and set $f_n(x) = n\,\phi\big(n(x - \tfrac{1}{n})\big)$ for $x \in [0,1]$ (with $f_n = 0$ where the tent is $0$). Each $f_n$ is continuous, non-negative, supported in $[0, 2/n]$, and \[\int_0^1 f_n(x)\,dx = n\int_0^{2/n}\big(1 - n|x - 1/n|\big)dx = n\cdot\frac{1}{n} = 1.\] For every fixed $x \in (0,1]$ we have $x > 2/n$ for all large $n$, so $f_n(x) = 0$ eventually; and $f_n(0) = 0$ for all $n$ (as $0$ is an endpoint of the tent's support).
Hence $f_n \to f \equiv 0$ pointwise, so $\int_0^1 f = 0 < 1$.
<1>3. Q.E.D.
:::
