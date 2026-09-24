---
schema: qual/card@1
id: P-BKF12-6B
kind: problem
title: Eigenvalues and eigenvectors of the cyclic shift on $\mathbb C^n$
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
    Checked against Problem 6B in the retained Fall 2012 Berkeley prelim exam
    and independently reviewed the retained solution packet F12_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the coordinate recurrence for an eigenvector and the converse for
    every nth root of unity.
---

::: {.problem}
Find all eigenvalues and eigenvectors of the linear map $T \colon \mathbb { C } ^ { n } \to \mathbb { C } ^ { n }$ given by $T ( ( x _ { 1 } , \dots , x _ { n } ) ) =$ $\left( x _ { 2 } , x _ { 3 } , \ldots , x _ { n } , x _ { 1 } \right)$
:::

::: {.solution}
Let
$$
v=(x_1,\ldots,x_n)\in\CC^n
$$
be a nonzero eigenvector with eigenvalue $\lambda$.

<1>1. The equation $Tv=\lambda v$ is equivalent to
$$
x_{j+1}=\lambda x_j
\quad(1\le j<n),
\qquad
x_1=\lambda x_n.
$$

::: {.proof}
By definition,
$$
Tv=(x_2,\ldots,x_n,x_1),
$$
while
$$
\lambda v=(\lambda x_1,\ldots,\lambda x_n).
$$
Equality of the coordinates gives exactly the displayed relations.
:::

<1>2. Every eigenvalue satisfies $\lambda^n=1$, and every eigenvector
with eigenvalue $\lambda$ has the form
$$
v=c(1,\lambda,\lambda^2,\ldots,\lambda^{n-1})
$$
for some $c\in\CC^\times$.

::: {.proof}
By step <1>1,
$$
x_j=\lambda^{j-1}x_1
\qquad(1\le j\le n).
$$
If $x_1=0$, then all coordinates vanish, contradicting $v\ne0$.
Thus $x_1\ne0$. The last relation in step <1>1 gives
$$
x_1=\lambda x_n
=\lambda^n x_1,
$$
so $\lambda^n=1$. Taking $c=x_1$ yields the displayed form.
:::

<1>3. Conversely, every $n$th root of unity is an eigenvalue.

::: {.proof}
Let $\omega^n=1$ and set
$$
v_\omega=(1,\omega,\omega^2,\ldots,\omega^{n-1}).
$$
Then
$$
\begin{aligned}
Tv_\omega
&=(\omega,\omega^2,\ldots,\omega^{n-1},1)\\
&=(\omega,\omega^2,\ldots,\omega^{n-1},\omega^n)\\
&=\omega v_\omega.
\end{aligned}
$$
Hence $\omega$ is an eigenvalue and $v_\omega$ is an eigenvector.
:::

<1>4. Writing
$$
\omega_k\coloneqq e^{2\pi i k/n}
\qquad(0\le k<n),
$$
the complete answer is
$$
\boxed{
\lambda=\omega_k\quad(0\le k<n),
\qquad
E_{\omega_k}
=\operatorname{span}_{\CC}
\{(1,\omega_k,\ldots,\omega_k^{n-1})\}.
}
$$

::: {.proof}
Step <1>2 shows that every eigenvalue is an $n$th root of unity and
that its eigenspace is at most the displayed line. Step <1>3 shows
that every $n$th root occurs and that the displayed line is contained
in the corresponding eigenspace.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 lists all eigenvalues and all their eigenvectors.
:::
:::
