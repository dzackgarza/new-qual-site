---
schema: qual/card@1
id: P-XQRCI
kind: problem
title: "Let $f_n(x) = \\frac{x}{1+nx^2}$ for"
classification:
  areas:
  - real-analysis
  topics:
  - equicontinuity
  - convergence-of-functions
relations: []
review: draft
---

::: problem
Let $f_n(x) = \frac{x}{1+nx^2}$ for $n \in \mathbb{N}$.
Let $\mathcal{F} := \{f_n \, \colon \, n = 1, 2, 3, \ldots\}$ and $[a,b]$ be any compact subset of $\mathbb{R}$.
Is $\mathcal{F}$ equicontinuous?
Justify your answer.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. Compute the derivative.
    Proof: $f_n(x) = \frac{x}{1+nx^2}$, so
    \[
    f_n'(x) = \frac{(1+nx^2) - 2nx^2}{(1+nx^2)^2} = \frac{1 - nx^2}{(1+nx^2)^2}.
    \]
<1>2. $|f_n'(x)| \le 1$ for all $n$ and all $x$.
    Proof: let $u = nx^2 \ge 0$; then $|f_n'(x)| = \frac{|1-u|}{(1+u)^2}$. For $0 \le u \le 1$: $\frac{1-u}{(1+u)^2} \le \frac{1}{(1+u)^2} \le 1$. For $u > 1$: $\frac{u-1}{(1+u)^2} \le \frac{u}{(1+u)^2} \cdot \frac{u}{u} \le 1$ (indeed $u-1 < u \le (1+u)^2$). Hence $|f_n'| \le 1$ everywhere.
<1>3. $\mathcal{F}$ is equicontinuous on $\RR$, hence on every compact $[a,b]$.
    Proof: by the mean value theorem and <1>2, for all $n$ and all $x, y$,
    \[
    |f_n(x) - f_n(y)| \le \sup |f_n'| \cdot |x - y| \le |x - y|.
    \]
    So the family is uniformly $1$-Lipschitz: given $\eps > 0$, take $\delta = \eps$ independently of $n$ and $x$. In particular $\mathcal{F}$ is equicontinuous on any compact $[a,b]$ (and in fact on all of $\RR$).
<1>4. Q.E.D.
:::
