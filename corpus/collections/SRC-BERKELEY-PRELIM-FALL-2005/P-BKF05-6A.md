---
schema: qual/card@1
id: P-BKF05-6A
kind: problem
title: A real square root of a unipotent matrix
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Fall 2005 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained truncated-square-root construction.
    The degree-(m-1) Taylor polynomial squares to 1+x modulo x^m, so
    substitution of N=A-I with N^m=0 gives an exact real square root.
---

::: {.problem}
Let \(A\) be a real \(n\times n\) matrix such that
\[
(A-I)^m=0
\]
for some \(m\ge1\). Prove that there is a real \(n\times n\) matrix \(B\) satisfying
\[
B^2=A.
\]
:::

::: {.solution}
Set
$$
N=A-I.
$$
Then $N$ is a real matrix and $N^m=0$.

<1>1. There is a polynomial $P\in\RR[x]$ such that
$$
P(x)^2=1+x+x^mQ(x)
$$
for some $Q\in\RR[x]$.

::: {.proof}
Let $P$ be the Taylor polynomial of degree $m-1$ at $0$ for
$$
h(x)=\sqrt{1+x}.
$$
Thus
$$
P(x)=\sum_{k=0}^{m-1}\binom{1/2}{k}x^k,
$$
so $P$ has real coefficients. Taylor's theorem gives
$$
h(x)-P(x)=O(x^m)
$$
as $x\to0$. Since $h(x)^2=1+x$,
$$
\begin{aligned}
P(x)^2-(1+x)
&=
P(x)^2-h(x)^2
\\
&=
\bigl(P(x)-h(x)\bigr)
\bigl(P(x)+h(x)\bigr)
\\
&=
O(x^m).
\end{aligned}
$$
The left-hand side is a polynomial. Being $O(x^m)$ at $0$ means that
its coefficients of degrees $0,\ldots,m-1$ vanish, so it is divisible
by $x^m$. Hence
$$
P(x)^2-(1+x)=x^mQ(x)
$$
for some $Q\in\RR[x]$.
:::

<1>2. Define
$$
B=P(N).
$$
Then $B$ is a real $n\times n$ matrix.

::: {.proof}
The matrix $N$ has real entries, and step <1>1 gives
$P\in\RR[x]$. Therefore the polynomial expression $P(N)$ has real
entries and the same size as $N$.
:::

<1>3. The matrix $B$ satisfies
$$
B^2=A.
$$

::: {.proof}
Substitute $N$ into the polynomial identity from step <1>1:
$$
\begin{aligned}
B^2
&=
P(N)^2
\\
&=
I+N+N^mQ(N)
\\
&=
I+N
\\
&=
A,
\end{aligned}
$$
because $N^m=0$.
:::

<1>4. Hence a real square root of $A$ is
$$
\boxed{B=P(A-I)}.
$$

::: {.proof}
Step <1>2 shows that $B$ is real, and step <1>3 shows that
$B^2=A$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the required real matrix.
:::
:::
