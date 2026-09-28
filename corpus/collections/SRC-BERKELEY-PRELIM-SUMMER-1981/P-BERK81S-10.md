---
schema: qual/card@1
id: P-BERK81S-10
kind: problem
title: Shift eigenvectors, Fibonacci recurrence, and Binet's formula
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    The shift eigenvalue equation is a_{n+1}=lambda a_n, so every
    eigenspace is spanned by (1,lambda,lambda^2,...). A recurrence solution
    is uniquely determined by x_1,x_2, giving a two-dimensional invariant
    subspace. The characteristic roots alpha=(1+sqrt(5))/2 and
    beta=(1-sqrt(5))/2 give the basis
    (alpha^{n-1}) and (beta^{n-1}), and uniqueness of the recurrence yields
    Binet's formula f_n=(alpha^n-beta^n)/sqrt(5).
---

::: {.problem}
Let $S$ be the vector space of complex sequences and define the left-shift operator
\[
T(a_1,a_2,a_3,\ldots)=(a_2,a_3,a_4,\ldots).
\]

1. Describe the eigenvectors of $T$.

2. Consider the recurrence
   \[
   x_{n+2}=x_{n+1}+x_n.
   \]
   Show that its solutions form a two-dimensional subspace $E\subset S$ with $T(E)\subset E$, and find an explicit basis for $E$.

3. The Fibonacci numbers satisfy $f_1=f_2=1$ and $f_{n+2}=f_{n+1}+f_n$.
   Find an explicit formula for $f_n$.
:::

::: {.solution}
<1>1. A nonzero sequence
$$
a=(a_1,a_2,\ldots)
$$
is an eigenvector of $T$ with eigenvalue $\lambda$ if and only if
$$
a_{n+1}=\lambda a_n
$$
for every $n\geq1$.

::: {.proof}
The equation
$$
T(a)=\lambda a
$$
means
$$
(a_2,a_3,\ldots)
=
(\lambda a_1,\lambda a_2,\ldots),
$$
which is exactly the displayed coordinate relation.
:::

<1>2. For every $\lambda\in\CC$, the $\lambda$-eigenspace of $T$ is
$$
\operatorname{span}_{\CC}
\left\{
(1,\lambda,\lambda^2,\ldots)
\right\}.
$$

::: {.proof}
By step <1>1,
$$
a_n=a_1\lambda^{n-1}
$$
for every $n$. If $a_1=0$, the whole sequence is zero. Thus every nonzero
eigenvector is a nonzero scalar multiple of
$$
(1,\lambda,\lambda^2,\ldots).
$$
Conversely, this geometric sequence satisfies $a_{n+1}=\lambda a_n$, so
$$
T(a)=\lambda a.
$$
:::

<1>3. Let $E$ be the set of sequences satisfying
$$
x_{n+2}=x_{n+1}+x_n.
$$
Then $E$ is a vector subspace of $S$.

::: {.proof}
The recurrence is homogeneous and linear. If $x,y\in E$ and
$a,b\in\CC$, then
$$
\begin{aligned}
(ax+by)_{n+2}
&=
a x_{n+2}+b y_{n+2}\\
&=
a(x_{n+1}+x_n)
+
b(y_{n+1}+y_n)\\
&=
(ax+by)_{n+1}+(ax+by)_n.
\end{aligned}
$$
Thus $ax+by\in E$.
:::

<1>4. Every pair
$$
(c,d)\in\CC^2
$$
occurs as the first two entries of a unique sequence in $E$.

::: {.proof}
Starting from
$$
x_1=c,
\qquad
x_2=d,
$$
the recurrence determines
$$
x_3=x_2+x_1,
$$
then $x_4=x_3+x_2$, and inductively every later term. Hence existence and
uniqueness follow recursively.
:::

<1>5. The map
$$
\Phi:E\longrightarrow\CC^2,
\qquad
\Phi(x)=(x_1,x_2),
$$
is a linear isomorphism. Consequently,
$$
\boxed{
\dim_{\CC}E=2.
}
$$

::: {.proof}
Linearity is immediate. Step <1>4 says precisely that $\Phi$ is bijective.
Therefore $E\cong\CC^2$.
:::

<1>6. The subspace $E$ is invariant under $T$:
$$
\boxed{
T(E)\subseteq E.
}
$$

::: {.proof}
Let $x\in E$ and set
$$
y=T(x),
\qquad
y_n=x_{n+1}.
$$
Then
$$
\begin{aligned}
y_{n+2}
&=
x_{n+3}\\
&=
x_{n+2}+x_{n+1}\\
&=
y_{n+1}+y_n.
\end{aligned}
$$
Thus $y\in E$.
:::

<1>7. Let
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
The numbers $\alpha,\beta$ are the two roots of
$$
r^2-r-1=0.
$$
:::

<1>8. The two sequences
$$
u=(1,\alpha,\alpha^2,\ldots)
$$
and
$$
v=(1,\beta,\beta^2,\ldots)
$$
belong to $E$.

::: {.proof}
For $u$,
$$
u_{n+2}
=
\alpha^{n+1}
=
\alpha^{n-1}\alpha^2
=
\alpha^{n-1}(\alpha+1)
=
u_{n+1}+u_n
$$
by step <1>7. The proof for $v$ is identical.
:::

<1>9. The sequences $u$ and $v$ are linearly independent.

::: {.proof}
By step <1>2, $u$ and $v$ are eigenvectors of $T$ with distinct
eigenvalues
$$
\alpha\neq\beta.
$$
Eigenvectors belonging to distinct eigenvalues are linearly independent.
:::

<1>10. An explicit basis of $E$ is
$$
\boxed{
\left\{
(1,\alpha,\alpha^2,\ldots),
(1,\beta,\beta^2,\ldots)
\right\}.
}
$$

::: {.proof}
Steps <1>8--<1>9 give two linearly independent elements of the
two-dimensional space $E$ from step <1>5. Hence they form a basis.
:::

<1>11. Define
$$
F_n
=
\frac{\alpha^n-\beta^n}{\sqrt5}.
$$
Then
$$
F_1=F_2=1.
$$

::: {.proof}
Since
$$
\alpha-\beta=\sqrt5,
$$
one has
$$
F_1=1.
$$
Also
$$
\alpha+\beta=1,
$$
so
$$
\begin{aligned}
F_2
&=
\frac{\alpha^2-\beta^2}{\sqrt5}\\
&=
\frac{(\alpha-\beta)(\alpha+\beta)}{\sqrt5}\\
&=
1.
\end{aligned}
$$
:::

<1>12. The sequence $(F_n)$ satisfies
$$
F_{n+2}=F_{n+1}+F_n.
$$

::: {.proof}
By step <1>7,
$$
\alpha^{n+2}
=
\alpha^{n+1}+\alpha^n
$$
and
$$
\beta^{n+2}
=
\beta^{n+1}+\beta^n.
$$
Subtract the two identities and divide by $\sqrt5$.
:::

<1>13. The Fibonacci numbers are
$$
\boxed{
f_n
=
\frac1{\sqrt5}
\left[
\left(
\frac{1+\sqrt5}{2}
\right)^n
-
\left(
\frac{1-\sqrt5}{2}
\right)^n
\right].
}
$$

::: {.proof}
Steps <1>11--<1>12 show that $(F_n)$ satisfies the Fibonacci recurrence
and the initial conditions
$$
F_1=F_2=1.
$$
By uniqueness of a sequence determined by a second-order recurrence and
its first two terms,
$$
f_n=F_n
$$
for every $n$.
:::

<1>14. Q.E.D.

::: {.proof}
Step <1>2 answers part (1), steps <1>5--<1>10 prove part (2), and step
<1>13 answers part (3).
:::
:::
