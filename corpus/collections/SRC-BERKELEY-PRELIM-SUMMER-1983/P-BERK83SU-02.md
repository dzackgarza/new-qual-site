---
schema: qual/card@1
id: P-BERK83SU-02
kind: problem
title: Polynomial growth of one derivative forces eventual vanishing of higher derivatives
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    With g=f^{(m)}, the hypothesis gives |g(z)|<=C(1+|z|^k).
    Cauchy's estimate for g^{(k+1)} on circles of radius R centered at
    an arbitrary point is O(R^{-1}), hence tends to zero as R tends to
    infinity. Thus f^{(m+k+1)}=0 and all higher derivatives vanish.
    The example f(z)=z^{m+k} shows the threshold m+k+1 is sharp.
---

::: {.problem}
Let $f:\mathbb C\to\mathbb C$ be entire and suppose that for some nonnegative integers $k,m$,
\[
\frac{f^{(m)}(z)}{1+|z|^k}
\]
is bounded on $\mathbb C$.
Prove that $f^{(n)}$ is identically zero for all sufficiently large $n$. How large must $n$ be in terms of $k$ and $m$?
:::

::: {.solution}
Put
$$
g=f^{(m)}.
$$
By hypothesis there is a constant $C>0$ such that
$$
\abs{g(z)}
\leq
C(1+\abs{z}^k)
$$
for every $z\in\CC$.

<1>1. For every $z_0\in\CC$ and every $R>0$,
$$
\abs{g^{(k+1)}(z_0)}
\leq
\frac{(k+1)!C}{R^{k+1}}
\left(1+(R+\abs{z_0})^k\right).
$$

::: {.proof}
On the circle
$$
\abs{z-z_0}=R,
$$
the triangle inequality gives
$$
\abs{z}\leq R+\abs{z_0}.
$$
Hence
$$
\max_{\abs{z-z_0}=R}\abs{g(z)}
\leq
C\left(1+(R+\abs{z_0})^k\right).
$$
Cauchy's derivative estimate of order $k+1$ therefore gives
$$
\abs{g^{(k+1)}(z_0)}
\leq
\frac{(k+1)!}{R^{k+1}}
\max_{\abs{z-z_0}=R}\abs{g(z)},
$$
which is the claimed inequality.
:::

<1>2. One has
$$
g^{(k+1)}\equiv0.
$$

::: {.proof}
Fix $z_0\in\CC$. In step <1>1, let $R\to\infty$. Since
$$
\frac{1+(R+\abs{z_0})^k}{R^{k+1}}
\longrightarrow0,
$$
we obtain
$$
\abs{g^{(k+1)}(z_0)}=0.
$$
The point $z_0$ was arbitrary, so $g^{(k+1)}$ is identically zero.
:::

<1>3. One has
$$
f^{(m+k+1)}\equiv0.
$$

::: {.proof}
Since $g=f^{(m)}$,
$$
g^{(k+1)}
=
f^{(m+k+1)}.
$$
Now apply step <1>2.
:::

<1>4. For every integer
$$
n\geq m+k+1,
$$
one has
$$
\boxed{f^{(n)}\equiv0}.
$$

::: {.proof}
Step <1>3 gives the assertion for $n=m+k+1$. Every higher derivative is
a derivative of the zero function and is therefore also identically
zero.
:::

<1>5. The threshold $m+k+1$ is the best possible uniform bound.

::: {.proof}
Take
$$
f(z)=z^{m+k}.
$$
Then $f^{(m)}$ is a polynomial of degree $k$, so for some constant
$C>0$,
$$
\abs{f^{(m)}(z)}
\leq
C(1+\abs{z}^k).
$$
Thus the hypothesis is satisfied. However,
$$
f^{(m+k)}
$$
is a nonzero constant, while
$$
f^{(m+k+1)}\equiv0.
$$
Hence no smaller derivative order works for all functions satisfying
the hypothesis.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>4 gives the required vanishing range, and step <1>5 shows that
the bound is sharp.
:::
:::
