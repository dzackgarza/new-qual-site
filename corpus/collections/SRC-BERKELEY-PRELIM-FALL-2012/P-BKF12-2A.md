---
schema: qual/card@1
id: P-BKF12-2A
kind: problem
title: Functions mapping every closed interval onto a closed interval need not be continuous
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked against Problem 2A in the retained Fall 2012 Berkeley prelim exam
    and its retained solution packet F12_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked discontinuity at zero and the image of every interval, including
    the one-sided intervals containing zero.
---

::: {.problem}
Prove or disprove the following assertion:

If $f:\RR\to\RR$ has the property that $f([a,b])$ is a bounded
closed interval for every $a\le b$, then $f$ is continuous.
:::

::: {.solution}
Define
$$
f(x)\coloneqq
\begin{cases}
\sin(1/x),&x\ne0,\\
0,&x=0.
\end{cases}
$$

<1>1. The function $f$ is not continuous at $0$.

::: {.proof}
Set
$$
x_n\coloneqq\frac{1}{\frac\pi2+2\pi n},
\qquad
y_n\coloneqq\frac{1}{\frac{3\pi}{2}+2\pi n}.
$$
Then $x_n\to0$ and $y_n\to0$, while
$$
f(x_n)=1,
\qquad
f(y_n)=-1
$$
for every $n$. Hence $\lim_{x\to0}f(x)$ does not exist, so $f$ is
discontinuous at $0$.
:::

<1>2. If $0\notin[a,b]$, then $f([a,b])$ is a bounded closed interval.

::: {.proof}
On $\RR\setminus\{0\}$ the function $f$ is continuous. Thus its
restriction to $[a,b]$ is continuous. The interval $[a,b]$ is compact
and connected, so its continuous image is compact and connected.
Compact subsets of $\RR$ are closed and bounded, and connected
subsets of $\RR$ are intervals. Therefore $f([a,b])$ is a bounded
closed interval.
:::

<1>3. If $0\in[a,b]$, then $f([a,b])$ is again a bounded closed
interval.

::: {.proof}
If $a=b=0$, then
$$
f([a,b])=\{0\}=[0,0].
$$
Suppose now that $a<b$. Since $0\in[a,b]$, at least one of
$b>0$ or $a<0$ holds.

Fix $t\in[-1,1]$ and choose $\alpha\in\RR$ with
$\sin\alpha=t$. The numbers
$$
\alpha+2\pi k
$$
take arbitrarily large positive values, while
$$
\alpha-2\pi k
$$
take arbitrarily large negative values. Hence, if $b>0$, there is a
positive $q$ with $\sin q=t$ and $1/q\in(0,b]$; if $a<0$, there is
a negative $q$ with $\sin q=t$ and $1/q\in[a,0)$. In either case,
some $x\in[a,b]$ satisfies $f(x)=t$.

Thus every value in $[-1,1]$ occurs on $[a,b]$. Since
$\abs{f(x)}\le1$ everywhere,
$$
f([a,b])=[-1,1].
$$
:::

<1>4. The assertion in the problem is false.

::: {.proof}
Steps <1>2 and <1>3 show that the function above maps every closed
interval to a bounded closed interval, while step <1>1 shows that it
is not continuous. Therefore
$$
\boxed{\text{the stated assertion is false}}.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 supplies the required counterexample.
:::
:::
