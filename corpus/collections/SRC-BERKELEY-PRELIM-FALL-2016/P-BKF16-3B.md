---
schema: qual/card@1
id: P-BKF16-3B
kind: problem
title: Contraction mapping iteration and the fixed point of $\cos$
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
    Independently checked the retained Fall 2016 solution packet: the
    derivative bound gives a contraction estimate toward the unique fixed
    point, and the cosine iteration enters an invariant interval on which
    |sin x| is uniformly less than 1.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked existence and uniqueness of the fixed point, the geometric
    convergence estimate, invariance of the cosine interval, and its
    derivative bound.
---

::: {.problem}
(a) Suppose that $I$ is a closed interval and $f:I\to I$ is smooth with $|f'|$ bounded by some number $r<1$ on $I$.
Let $a_0\in I$ and put $a_{n+1}=f(a_n)$.
Prove that the sequence $(a_n)$ tends to the unique root of $f(x)=x$ in $I$.

(b) Show that if $a_0$ is real and $a_{n+1}=\cos(a_n)$, then $a_n$ tends to a root of $\cos(x)=x$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Under the hypotheses of part (a), the equation
$$
f(x)=x
$$
has at least one solution in $I$.

::: pf-proof

Write
$$
I=[\alpha,\beta].
$$
Since $f(I)\subseteq I$,
$$
f(\alpha)-\alpha\ge0
$$
and
$$
f(\beta)-\beta\le0.
$$
The continuous function
$$
h(x)\coloneqq f(x)-x
$$
therefore has a zero in $I$ by the intermediate value theorem.

:::

:::

::: {.pf-step #s2}

The fixed point of $f$ in $I$ is unique.

::: pf-proof

Suppose
$$
f(x)=x,
\qquad
f(y)=y,
\qquad
x<y.
$$
By the mean value theorem there is $c\in(x,y)$ such that
$$
f'(c)
=
\frac{f(y)-f(x)}{y-x}
=
1.
$$
This contradicts
$$
|f'(c)|\le r<1.
$$

:::

:::

::: {.pf-step #s3}

If $p$ is the unique fixed point from steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, then
$$
|a_{n+1}-p|
\le
r|a_n-p|
$$
for every $n\ge0$.

::: pf-proof

Since $a_n,p\in I$, the mean value theorem gives a point between them
at which
$$
|f(a_n)-f(p)|
\le
r|a_n-p|.
$$
Using
$$
a_{n+1}=f(a_n)
\qquad\text{and}\qquad
f(p)=p
$$
gives the claim.

:::

:::

::: {.pf-step #s4}

The sequence in part (a) converges to $p$.

::: pf-proof

Iterating step [](#s3){.pf-ref} gives
$$
|a_n-p|
\le
r^n|a_0-p|.
$$
Since $0\le r<1$,
$$
r^n\longrightarrow0.
$$
Hence
$$
a_n\longrightarrow p.
$$
This proves part (a).

:::

:::

::: {.pf-step #s5}

For the cosine iteration, after two steps one has
$$
a_2\in[\cos1,1].
$$

::: pf-proof

For arbitrary real $a_0$,
$$
a_1=\cos(a_0)\in[-1,1].
$$
On the interval $[-1,1]$, the cosine takes values between
$\cos1$ and $1$. Therefore
$$
a_2=\cos(a_1)\in[\cos1,1].
$$

:::

:::

::: {.pf-step #s6}

Put
$$
c\coloneqq\cos1,
\qquad
d\coloneqq\cos c,
\qquad
J\coloneqq[c,d].
$$
Then
$$
a_3\in J
\qquad\text{and}\qquad
\cos(J)\subseteq J.
$$

::: pf-proof

By step [](#s5){.pf-ref},
$$
a_2\in[c,1].
$$
Since
$$
0<c<1<\frac\pi2
$$
and cosine is decreasing on $[0,1]$,
$$
a_3=\cos(a_2)\in[\cos1,\cos c]=[c,d]=J.
$$

Now take $x\in J$. Since
$$
c\le x\le d<1,
$$
monotonicity of cosine gives
$$
\cos d
\le
\cos x
\le
\cos c=d.
$$
Also $d<1$, so
$$
\cos d>\cos1=c.
$$
Hence
$$
c<\cos d\le\cos x\le d,
$$
which proves $\cos(J)\subseteq J$.

:::

:::

::: {.pf-step #s7}

On $J$,
$$
|\cos'(x)|
\le
\sin d
<
1.
$$

::: pf-proof

The interval $J$ lies in $(0,1)$ by step [](#s6){.pf-ref}. Therefore
$$
|\cos'(x)|
=
\sin x
\le
\sin d.
$$
Since $d<1<\pi/2$,
$$
\sin d<1.
$$

:::

:::

::: {.pf-step #s8}

The cosine iteration converges to the unique solution of
$$
\cos x=x
$$
in $J$.

::: pf-proof

By steps [](#s6){.pf-ref} and [](#s7){.pf-ref}, the function
$$
f(x)=\cos x
$$
maps the closed interval $J$ into itself and satisfies the derivative
bound required in part (a). Starting from $a_3\in J$, step [](#s4){.pf-ref} shows
that the tail
$$
a_3,a_4,\ldots
$$
converges to the unique fixed point of cosine in $J$. A finite initial
segment does not affect convergence, so the whole sequence $(a_n)$ has
the same limit.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} proves part (a), and step [](#s8){.pf-ref} proves part (b).

:::

:::

:::
