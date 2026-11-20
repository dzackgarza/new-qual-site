---
schema: qual/card@1
id: E-XNYTJ
kind: problem
title: Monotone pointwise convergence to a continuous limit is uniform
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Uniform Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §26 Exercise 10, printed p. 171, with Exercise
    21.9; the theorem and both counterexample requests are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 26.10, PDF p. 13. Monotone pointwise convergence
    plus continuity of the terms and the limit gives uniform convergence by a finite
    subcover of the neighbourhoods on which the first N_x terms are within epsilon; the two
    examples show monotonicity and compactness are both needed. (tmp/sources/munkres-
    solutions-positron-ch3.pdf).
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the same two parts. What was checked while doing it: the
    monotonicity example is the function of Exercise 9 of Section 21, which the book defines on all of R,
    and the card restricts it to [0,1] and now proves that the restriction is not monotone increasing ---
    g_{n+1}(1/n) = 1/((n+1)/n^2 + 1) < 1 = g_n(1/n) --- which the earlier prose did not, leaving open
    whether the example actually drops the hypothesis it is meant to drop. Continuity of the terms, the
    pointwise limit and the failure of uniformity are each justified for both examples, and the arctan
    example is shown monotone increasing rather than asserted. The statement was checked against
    Munkres, Topology (2000), Section 26 Exercise 10, printed p. 171.
---

::: {.exercise}

(a) Prove the following partial converse to the uniform limit theorem.

Theorem.
Let $f_n: X \to \RR$ be a sequence of continuous functions, with $f_n(x) \to f(x)$ for each $x \in X$.
If $f$ is continuous, and if the sequence $f_n$ is monotone increasing, and if $X$ is compact, then the convergence is uniform.
[We say that $f_n$ is monotone increasing if $f_n(x) \leq f_{n+1}(x)$ for all $n$ and $x$.]

(b) Give examples to show that this theorem fails if you delete the requirement that $X$ be compact, or if you delete the requirement that the sequence be monotone.
[Hint: See the exercises of §21.]
:::

::: {.solution}

Both parts are **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 26.10** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the finite subcover of the neighbourhoods on which the first $N_{x}$ terms are already within $\varepsilon$ is that solution's, and the two examples are its choices. Verified here against the book and, for the first example, added to: the functions of Exercise 9 of §21 are defined on all of $\RR$, and the card restricts them to $[0,1]$ and shows that the restriction is *not* monotone increasing, which is the hypothesis this example is meant to drop.

The statement was checked against Munkres, *Topology* (2000), §26 Exercise 10, with Exercise 9 of §21, Theorem 21.5 and Theorem 18.1. Throughout $X$ is a topological space, $f_{n},f\colon X\to\RR$, convergence is pointwise unless stated, and the sequence $(f_{n})$ is *monotone increasing* when $f_{n}(x)\leq f_{n+1}(x)$ for all $n$ and all $x$, as the exercise defines it; a sequence of functions converges uniformly to $f$ when for each $\varepsilon>0$ some $N$ makes $\abs{f_{n}(x)-f(x)}<\varepsilon$ for every $n\geq N$ and every $x\in X$.

::: pf

::: {.pf-step #a}

(a) If $f_{n}\to f$ pointwise, $f$ and every $f_{n}$ are continuous, $(f_{n})$ is monotone increasing and $X$ is compact, then the convergence is uniform.

:::: pf-proof

Let $\varepsilon>0$. The argument produces from the compactness of $X$ a single $N$ that works at every point.

::: {.pf-step #differences}

For each $x\in X$ the sequence $\big(f(x)-f_{n}(x)\big)$ decreases to $0$.

::: pf-proof

Pointwise convergence gives $f_{n}(x)\to f(x)$, so $f(x)-f_{n}(x)\to0$, and monotonicity gives $f_{n}(x)\leq f_{n+1}(x)\leq f(x)$, so the differences are nonnegative and nonincreasing.

:::

:::

::: {.pf-step #neighbourhoods}

For $\varepsilon>0$ and $x\in X$ there is $N_{x}$ with $f(x)-f_{n}(x)<\varepsilon$ for every $n\geq N_{x}$, and a neighbourhood $U_{x}$ of $x$ with $f(z)-f_{N_{x}}(z)<\varepsilon$ for every $z\in U_{x}$.

::: pf-proof

The first claim follows from step [](#differences){.pf-ref}: choose $N_{x}$ with $f(x)-f_{N_{x}}(x)<\varepsilon$, and monotonicity extends it to $n\geq N_{x}$. For the second, the map $g\coloneqq f-f_{N_{x}}$ is continuous, being a difference of continuous real-valued functions (Theorem 21.5), and $g(x)<\varepsilon$; so $x$ lies in the open set $g^{-1}\big((-\infty,\varepsilon)\big)$ (Theorem 18.1), which is the neighbourhood $U_{x}$ wanted.

:::

:::

::: {.pf-step #subcover}

Finitely many of the sets $U_{x}$ cover $X$; say $U_{x_{1}},\dots,U_{x_{k}}$ do, and put $N\coloneqq\max\theset{N_{x_{1}},\dots,N_{x_{k}}}$.

::: pf-proof

The family $\theset{U_{x}\mid x\in X}$ is an open cover of $X$ by step [](#neighbourhoods){.pf-ref}, and $X$ is compact; so it has a finite subcover, and $N$ is a maximum of finitely many positive integers.

:::

:::

::: {.pf-step #uniform-bound}

For every $z\in X$ and every $n\geq N$ one has $\abs{f(z)-f_{n}(z)}<\varepsilon$.

::: pf-proof

Given $z$, choose $i$ with $z\in U_{x_{i}}$. Since $n\geq N\geq N_{x_{i}}$ and $f_{n}(z)\leq f(z)$, and since $n\geq N$ gives $f_{N}(z)\geq f_{n}(z)$ by monotonicity,
$$
0\leq f(z)-f_{n}(z)\leq f(z)-f_{N}(z)\leq f(z)-f_{N_{x_{i}}}(z)<\varepsilon,
$$
the last inequality by the choice of $U_{x_{i}}$ in step [](#neighbourhoods){.pf-ref}. Hence $\abs{f(z)-f_{n}(z)}=f(z)-f_{n}(z)<\varepsilon$.

:::

:::

::::

:::

::: {.pf-step #without-compactness}

(b) The compactness hypothesis cannot be dropped: there are continuous $h_{n}\colon\RR\to\RR$ with $h_{n}\leq h_{n+1}$, converging pointwise to a continuous limit but not uniformly, on the non-compact space $\RR$.

:::: pf-proof

Take $h_{n}(x)\coloneqq\arctan(x+n)$ on $X=\RR$.

::: {.pf-step #compact-example-pointwise}

Each $h_{n}$ is continuous, the sequence is monotone increasing, and $h_{n}\to\pi/2$ pointwise on $\RR$.

::: pf-proof

$h_{n}(x)=\arctan(x+n)$ is continuous, being a composite of continuous functions, and $h_{n}(x)\leq h_{n+1}(x)$ because $\arctan$ is increasing and $x+n<x+n+1$. For fixed $x$ one has $x+n\to+\infty$, so $h_{n}(x)\to\pi/2$, the limit being the constant function $\pi/2$, which is continuous.

:::

:::

::: {.pf-step #compact-example-fails}

The convergence $h_{n}\to\pi/2$ on $\RR$ is not uniform.

::: pf-proof

For every $n$ one has $h_{n}(-n)=\arctan(0)=0$, so $\big(h_{n}-\pi/2\big)(-n)=-\pi/2$ and $\sup_{x}\abs{h_{n}(x)-\pi/2}\geq\pi/2$ for every $n$; the sup does not tend to $0$.

:::

:::

::::

:::

::: {.pf-step #without-monotonicity}

(b) The monotonicity hypothesis cannot be dropped: there are continuous $g_{n}\colon[0,1]\to\RR$, converging pointwise to a continuous limit but not uniformly, on the compact space $[0,1]$, and not monotone increasing.

:::: pf-proof

Take $g_{n}$ to be the function of Exercise 9 of §21 , $g_{n}(x)\coloneqq 1/\big(n^{3}(x-1/n)^{2}+1\big)$, restricted to $X=[0,1]$.

::: {.pf-step #monotone-example-pointwise}

Each $g_{n}$ is continuous and $g_{n}\to0$ pointwise on $[0,1]$.

::: pf-proof

$g_{n}$ is a quotient of continuous functions whose denominator $n^{3}(x-1/n)^{2}+1$ never vanishes. For $x\in[0,1]$ the denominator is at least $n^{3}(x-1/n)^{2}$, which tends to infinity as $n\to\infty$ for fixed $x\neq0$ because $(x-1/n)^{2}\to x^{2}>0$; for $x=0$ the denominator is $n+1$. In both cases the denominator tends to infinity, so $g_{n}(x)\to0$, and the zero function is continuous.

:::

:::

::: {.pf-step #monotone-example-fails}

The convergence $g_{n}\to0$ on $[0,1]$ is not uniform, and the sequence $(g_{n})$ is not monotone increasing.

::: pf-proof

For each $n$ one has $g_{n}(1/n)=1/(0+1)=1$ and $1/n\in[0,1]$, so $\sup_{x}\abs{g_{n}(x)-0}=1\not\to0$ and the convergence is not uniform. And
$$
g_{n+1}(1/n)=\frac{1}{(n+1)^{3}\big(1/n-1/(n+1)\big)^{2}+1}=\frac{1}{(n+1)^{3}/\big(n^{2}(n+1)^{2}\big)+1}=\frac{1}{(n+1)/n^{2}+1}<1=g_{n}(1/n),
$$
so $g_{n+1}(1/n)<g_{n}(1/n)$ and $(g_{n})$ is not monotone increasing.

:::

:::

::::

:::

::: pf-step

Therefore monotonicity and compactness are both needed for the partial converse, and neither can be deleted.

::: pf-proof

Step [](#a){.pf-ref} proves the theorem under both hypotheses. Step [](#without-monotonicity){.pf-ref} exhibits a compact space, continuous terms and a continuous limit with pointwise but not uniform convergence, and a sequence that is not monotone increasing; step [](#without-compactness){.pf-ref} exhibits a non-compact space with continuous terms, a continuous limit and a monotone increasing sequence, again not uniformly convergent. So each hypothesis in turn is necessary, which is what part (b) asks for.

:::

:::

:::

:::
