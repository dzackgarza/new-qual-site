---
schema: qual/card@1
id: P-RA19J1
kind: problem
title: 'UGA analysis qualifying exam, January 2019, problem 1'
classification:
  areas:
  - real-analysis
  topics:
  - convergence-of-functions
  - uniform-convergence
  - equicontinuity
relations: []
review: draft
---

:::{.problem title="?"}
(a) Let
$$f_n(x)=\frac{1}{1+n^2x^2}\qquad\text{and}\qquad g_n(x)=nx(1-x)^n,\qquad x\in[0,1].$$
Prove that $\{f_n\}$ and $\{g_n\}$ converge pointwise but not uniformly on $[0,1]$.

(b) Are the families $\{f_n\}$, respectively $\{g_n\}$ given in part (a) equicontinuous? Clearly motivate
your answer.
:::

:::: {.solution}
> **AI-Generated Solution**
**Goal:** (a) Prove $f_n(x) = \frac{1}{1+n^2x^2}$ and $g_n(x) = nx(1-x)^n$ converge pointwise but not uniformly on $[0,1]$; (b) decide equicontinuity of the two families.

<1>1. (a) $f_n$ converges pointwise to $f(x) = 1$ at $x = 0$ and $f(x) = 0$ on $(0,1]$.
    Proof: $f_n(0) = 1$ for all $n$; for $x > 0$, $n^2x^2 \to \infty$, so $f_n(x) \to 0$.

<1>2. $f_n$ does not converge uniformly on $[0,1]$.
    Proof: the pointwise limit $f$ is discontinuous at $0$, while each $f_n$ is continuous; a uniform limit of continuous functions is continuous. Equivalently $\|f_n - f\|_\infty = 1$ for all $n$ (as $x \to 0^+$, $f_n(x) \to 1$ while $f(0) = 1$ and $f_n(0) = 1$: the sup of $|f_n - f|$ is approached, e.g. $\|f_n - f\|_\infty \ge \lim_{x \to 0^+}|f_n(x) - f(x)|$).

<1>3. (a) $g_n$ converges pointwise to $g \equiv 0$.
    Proof: $g_n(1) = 0$ and $g_n(0) = 0$; for $x \in (0,1)$, $nx(1-x)^n \to 0$ since exponential decay beats linear growth.

<1>4. $g_n$ does not converge uniformly.
    <2>1. $g_n$ attains its maximum at $x_n = \frac{1}{n+1}$ with $g_n(x_n) = \frac{n}{n+1}\left(1 - \frac{1}{n+1}\right)^n \to e^{-1} \neq 0$.
        Proof: $\frac{d}{dx}nx(1-x)^n = n(1-x)^{n-1}(1 - (n+1)x)$, zero at $x = 1/(n+1)$; the value tends to $e^{-1}$.
    <2>2. Q.E.D.
        Proof: <2>1 gives $\|g_n\|_\infty \to e^{-1} > 0$, so $g_n \not\to 0$ uniformly.

<1>5. (b) Neither family is equicontinuous on $[0,1]$.
    <2>1. $\{f_n\}$ fails equicontinuity at $0$: $f_n(1/n) = \frac{1}{1 + n^2/n^2} = \frac12$ while $f_n(0) = 1$, so $|f_n(1/n) - f_n(0)| = 1/2$ even though $1/n \to 0$.
        Proof: no $\delta > 0$ can force $|f_n(x) - f_n(0)| < 1/4$ for all $n$ simultaneously, since $x = 1/n < \delta$ eventually but the difference stays $1/2$.
    <2>2. $\{g_n\}$ fails equicontinuity at $0$: $g_n(x_n) \to e^{-1} \neq 0$ at $x_n = 1/(n+1) \to 0$ while $g_n(0) = 0$.
        Proof: by <1>4<2>1, $|g_n(x_n) - g_n(0)| \to e^{-1} > 0$ with $x_n \to 0$; again no $\delta$ works for all $n$.
    <2>3. Q.E.D.
        Proof: <2>1 and <2>2 show both families fail the equicontinuity definition at $0$.

:::
