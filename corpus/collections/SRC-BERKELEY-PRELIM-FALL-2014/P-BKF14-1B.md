---
schema: qual/card@1
id: P-BKF14-1B
kind: problem
title: Real zeros of the truncated exponential series $\sum_{k\le n}x^k/k!$
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
    Independently checked the retained Fall 2014 solution packet and its
    induction using P_n'=P_{n-1}.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked monotonicity in the odd case and positivity of the unique global
    minimum in the even case.
---

::: {.problem}
Using induction or otherwise, show that the polynomial $P_n(x)=1+x^1/1!+\cdots+x^n/n!$ has exactly 1 real zero if $n$ is odd and none if $n$ is even.
:::

::: {.solution}
For $n\ge0$, write
$$
P_n(x)\coloneqq\sum_{k=0}^n\frac{x^k}{k!}.
$$

<1>1. For every $n\ge1$,
$$
P_n'(x)=P_{n-1}(x).
$$

::: {.proof}
Termwise differentiation gives
$$
P_n'(x)
=
\sum_{k=1}^n\frac{kx^{k-1}}{k!}
=
\sum_{j=0}^{n-1}\frac{x^j}{j!}
=
P_{n-1}(x).
$$
:::

<1>2. The assertion holds for $n=0$.

::: {.proof}
One has $P_0(x)=1$, which has no real zero, as required for even $n$.
:::

<1>3. Assume the assertion holds for $P_{n-1}$ and suppose $n$ is odd.
Then $P_n$ has exactly one real zero.

::: {.proof}
Now $n-1$ is even, so the induction hypothesis says that
$P_{n-1}$ has no real zero. Since
$$
P_{n-1}(0)=1>0,
$$
continuity implies $P_{n-1}(x)>0$ for every real $x$. By step <1>1,
$P_n'(x)>0$ everywhere, so $P_n$ is strictly increasing.

Because $P_n$ has odd degree and positive leading coefficient,
$$
\lim_{x\to-\infty}P_n(x)=-\infty,
\qquad
\lim_{x\to+\infty}P_n(x)=+\infty.
$$
The intermediate value theorem gives a real zero, and strict
monotonicity makes it unique.
:::

<1>4. Assume the assertion holds for $P_{n-1}$ and suppose $n$ is
even and positive. Then $P_n$ has no real zero.

::: {.proof}
Now $n-1$ is odd, so the induction hypothesis gives a unique real zero
$\alpha$ of $P_{n-1}$. Since
$$
P_{n-1}(0)=1,
$$
one has $\alpha\ne0$.

The polynomial $P_{n-1}$ has odd degree with positive leading
coefficient. Since it has only the one zero $\alpha$, its sign is
negative on $(-\infty,\alpha)$ and positive on $(\alpha,\infty)$.
By step <1>1, $P_n$ therefore decreases up to $\alpha$ and increases
after $\alpha$, so $\alpha$ is its unique global minimum.

At that point,
$$
P_n(\alpha)
=
P_{n-1}(\alpha)+\frac{\alpha^n}{n!}
=
\frac{\alpha^n}{n!}
>
0,
$$
because $n$ is even and $\alpha\ne0$. Hence $P_n(x)>0$ for every real
$x$, so $P_n$ has no real zero.
:::

<1>5. Therefore $P_n$ has exactly one real zero for odd $n$ and none
for even $n$.

::: {.proof}
Step <1>2 is the base case, and steps <1>3--<1>4 prove the induction
step according to the parity of $n$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is exactly the required conclusion.
:::
:::
