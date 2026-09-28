---
schema: qual/card@1
id: P-BKF08-9A
kind: problem
title: Pointwise convergence to $0$ does not force the integrals to converge to $0$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 9A of the retained Berkeley Fall 2008 preliminary-exam solution packet f08solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked continuity of the triangular spikes, pointwise convergence at
    x=0 and x>0 separately, and the exact unit integral.
---

::: {.problem}
Suppose $(f_n)_{n>0}$ is a sequence of continuous real-valued functions on $[0,1]$ such that $f_n(x)\to0$ for every $x$.
Prove or give a counterexample to
$$
\lim_{n\to\infty}\int_0^1 f_n(x)\,dx=0.
$$
:::

::: {.solution}
<1>1. For $n\ge1$, define the continuous triangular spike
$$
\boxed{
f_n(x)\coloneqq
\begin{cases}
4n^2x,&0\le x\le \dfrac1{2n},\\[4pt]
4n^2\left(\dfrac1n-x\right),&\dfrac1{2n}\le x\le\dfrac1n,\\[6pt]
0,&\dfrac1n\le x\le1.
\end{cases}
}
$$

::: {.proof}
At $x=1/(2n)$, both nonzero formulas equal $2n$, and at $x=1/n$
the second formula equals $0$, matching the last piece. The value at
$x=0$ is also $0$. Thus the pieces join continuously, so
$f_n\colon[0,1]\to\RR$ is continuous.
:::

<1>2. For every fixed $x\in[0,1]$,
$$
f_n(x)\longrightarrow0.
$$

::: {.proof}
If $x=0$, then $f_n(0)=0$ for every $n$. If $x>0$, choose $N$ such
that $1/N<x$. For every $n\ge N$, one has $1/n\le1/N<x$, so
$x>1/n$ and hence $f_n(x)=0$ by the last branch in step <1>1.
Therefore $f_n(x)\to0$ for every $x\in[0,1]$.
:::

<1>3. For every $n\ge1$,
$$
\int_0^1 f_n(x)\,dx=1.
$$

::: {.proof}
Using the two nonzero pieces from step <1>1,
$$
\begin{aligned}
\int_0^1 f_n(x)\,dx
&=\int_0^{1/(2n)}4n^2x\,dx
 +\int_{1/(2n)}^{1/n}4n^2\left(\frac1n-x\right)\,dx\\
&=\frac12+\frac12\\
&=1.
\end{aligned}
$$
:::

<1>4. The proposed implication is false.

::: {.proof}
Step <1>2 gives pointwise convergence $f_n\to0$, while step <1>3 gives
$$
\lim_{n\to\infty}\int_0^1 f_n(x)\,dx=1\ne0.
$$
Thus the sequence from step <1>1 is a counterexample.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the required counterexample.
:::
:::
