---
schema: qual/card@1
id: P-BKF79-7
kind: problem
title: Shift-operator eigenvectors and the Fibonacci subspace
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Solved Sa=lambda a coordinatewise, identified W with C^2 by its
    first two coordinates, and used the two roots of r^2-r-1 to obtain
    an eigenbasis of W and Binet's formula.
---

::: {.problem}
Let $V$ be the vector space of complex sequences and let
\[
S(a_1,a_2,a_3,\ldots)=(a_2,a_3,a_4,\ldots).
\]

1. Find the eigenvectors of $S$.
2. Let $W$ be the subspace of sequences satisfying
\[
x_{n+2}=x_{n+1}+x_n.
\]
Show that $W$ is two-dimensional and $S$-invariant, and give an explicit basis.
3. Derive an explicit formula for the Fibonacci numbers $f_1=f_2=1$, $f_{n+2}=f_{n+1}+f_n$.
:::

::: {.solution}
<1>1. A nonzero sequence $a=(a_1,a_2,\ldots)$ is a $\lambda$-eigenvector
of $S$ if and only if
$$
a_{n+1}=\lambda a_n
$$
for every $n\geq1$.

::: {.proof}
The equation $S(a)=\lambda a$ is the coordinatewise equality
$$
(a_2,a_3,\ldots)
=
(\lambda a_1,\lambda a_2,\ldots),
$$
which is equivalent to the displayed recurrence.
:::

<1>2. For every $\lambda\in\CC$, the $\lambda$-eigenspace of $S$ is
$$
\boxed{
\operatorname{span}_{\CC}
\{(1,\lambda,\lambda^2,\ldots)\}.
}
$$

::: {.proof}
By step <1>1,
$$
a_n=a_1\lambda^{n-1}
$$
for all $n\geq1$. Thus every nonzero $\lambda$-eigenvector is a
nonzero scalar multiple of
$$
(1,\lambda,\lambda^2,\ldots),
$$
and this sequence is directly checked to satisfy $S(a)=\lambda a$.
:::

<1>3. A sequence in $W$ is uniquely determined by its first two
coordinates.

::: {.proof}
Given $x_1,x_2\in\CC$, the recurrence
$$
x_{n+2}=x_{n+1}+x_n
$$
successively determines $x_3,x_4,\ldots$. Conversely, the resulting
sequence satisfies the recurrence by construction.
:::

<1>4. The map
$$
\Phi:W\longrightarrow\CC^2,
\qquad
\Phi(x)=(x_1,x_2),
$$
is a linear isomorphism. In particular,
$$
\boxed{\dim_{\CC}W=2}.
$$

::: {.proof}
The recurrence is homogeneous and linear, so $W$ is a vector
subspace. The map $\Phi$ is linear, and step <1>3 says exactly that
it is bijective.
:::

<1>5. The subspace $W$ is $S$-invariant.

::: {.proof}
Let $x\in W$ and put $y=Sx$, so $y_n=x_{n+1}$. Then
$$
\begin{aligned}
y_{n+2}
&=x_{n+3}\\
&=x_{n+2}+x_{n+1}\\
&=y_{n+1}+y_n.
\end{aligned}
$$
Hence $y\in W$.
:::

<1>6. Set
$$
\alpha=\frac{1+\sqrt5}{2},
\qquad
\beta=\frac{1-\sqrt5}{2}.
$$
Then
$$
\alpha^2=\alpha+1,
\qquad
\beta^2=\beta+1.
$$

::: {.proof}
The numbers $\alpha$ and $\beta$ are the two roots of
$$
r^2-r-1=0.
$$
:::

<1>7. The sequences
$$
u=(1,\alpha,\alpha^2,\ldots),
\qquad
v=(1,\beta,\beta^2,\ldots)
$$
belong to $W$.

::: {.proof}
For $u$, step <1>6 gives
$$
u_{n+2}
=
\alpha^{n+1}
=
\alpha^{n-1}\alpha^2
=
\alpha^n+\alpha^{n-1}
=
u_{n+1}+u_n.
$$
The same calculation with $\beta$ proves the assertion for $v$.
:::

<1>8. The sequences $u$ and $v$ form the explicit basis
$$
\boxed{
\{(1,\alpha,\alpha^2,\ldots),
(1,\beta,\beta^2,\ldots)\}
}
$$
of $W$.

::: {.proof}
By step <1>2, $u$ and $v$ are eigenvectors of $S$ with distinct
eigenvalues $\alpha\neq\beta$, so they are linearly independent.
Step <1>4 gives $\dim W=2$, hence they form a basis.
:::

<1>9. Define
$$
F_n
\coloneqq
\frac{\alpha^n-\beta^n}{\sqrt5}.
$$
Then $F_1=F_2=1$.

::: {.proof}
Since
$$
\alpha-\beta=\sqrt5
$$
and
$$
\alpha+\beta=1,
$$
one has
$$
F_1=1
$$
and
$$
F_2
=
\frac{(\alpha-\beta)(\alpha+\beta)}{\sqrt5}
=
1.
$$
:::

<1>10. The sequence $(F_n)$ satisfies the Fibonacci recurrence
$$
F_{n+2}=F_{n+1}+F_n.
$$

::: {.proof}
By step <1>6,
$$
\alpha^{n+2}=\alpha^{n+1}+\alpha^n
$$
and
$$
\beta^{n+2}=\beta^{n+1}+\beta^n.
$$
Subtracting and dividing by $\sqrt5$ gives the claim.
:::

<1>11. The Fibonacci numbers are
$$
\boxed{
f_n
=
\frac1{\sqrt5}
\left[
\left(\frac{1+\sqrt5}{2}\right)^n
-
\left(\frac{1-\sqrt5}{2}\right)^n
\right].
}
$$

::: {.proof}
Steps <1>9--<1>10 show that $(F_n)$ satisfies the same recurrence and
the same initial conditions as $(f_n)$. A second-order recurrence is
uniquely determined by its first two terms, so $f_n=F_n$ for every
$n\geq1$.
:::

<1>12. Q.E.D.

::: {.proof}
Step <1>2 answers part 1, steps <1>4--<1>8 answer part 2, and step
<1>11 answers part 3.
:::
:::
