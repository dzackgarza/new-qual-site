---
schema: qual/card@1
id: P-TRIV-DE04
kind: problem
title: Bernoulli equation $y'=f(x)y+g(x)y^n$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 4, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash contains a leading nonprinting control byte at this source position; the byte was removed from the authored card as a nonsemantic extraction artifact.
---

::: {.problem}
Solve $y ^ { \prime } ( x ) = f ( x ) y ( x ) + g ( x ) y ^ { n } ( x )$
:::

::: {.solution}
Assume $f$ and $g$ are continuous on an interval $I$.

<1>1. First suppose
$$
n\neq1
$$
and work on a subinterval where $y$ is nonzero and the power $y^{1-n}$ is defined.

::: {.proof}
The Bernoulli substitution used below contains the factor $y^{-n}$, so it is applied where $y\neq0$.
:::

<1>2. Define
$$
z=y^{1-n}.
$$
Then
$$
z'
=
(1-n)y^{-n}y'.
$$

::: {.proof}
Differentiate $y^{1-n}$ by the chain rule.
:::

<1>3. Substituting the differential equation into step <1>2 gives
$$
z'
=
(1-n)f(x)z
+
(1-n)g(x).
$$

::: {.proof}
Using
$$
y'
=
fy+gy^n,
$$
one obtains
$$
\begin{aligned}
z'
&=
(1-n)y^{-n}(fy+gy^n)\\
&=
(1-n)f y^{1-n}
+
(1-n)g.
\end{aligned}
$$
Now use $z=y^{1-n}$.
:::

<1>4. Thus $z$ satisfies the linear equation
$$
z'
-
(1-n)f(x)z
=
(1-n)g(x).
$$

::: {.proof}
Rearrange step <1>3.
:::

<1>5. Choose a reference point $x_0\in I$ and define
$$
F(x)
=
\int_{x_0}^{x}f(s)\,ds.
$$
An integrating factor for step <1>4 is
$$
\mu(x)
=
e^{(n-1)F(x)}.
$$

::: {.proof}
The coefficient of $z$ in step <1>4 is
$$
-(1-n)f=(n-1)f.
$$
The standard integrating factor is therefore
$$
\exp\left(\int (n-1)f\right)
=
e^{(n-1)F}.
$$
:::

<1>6. Multiplying by $\mu$ gives
$$
\frac d{dx}
\left(
e^{(n-1)F(x)}z(x)
\right)
=
(1-n)
e^{(n-1)F(x)}g(x).
$$

::: {.proof}
This is the defining property of the integrating factor from step <1>5.
:::

<1>7. Hence
$$
e^{(n-1)F(x)}z(x)
=
C
+
(1-n)
\int_{x_0}^{x}
e^{(n-1)F(s)}g(s)
\,ds.
$$

::: {.proof}
Integrate step <1>6 from $x_0$ to $x$ and absorb the initial value into the constant $C$.
:::

<1>8. Therefore, for $n\neq1$,
$$
\boxed{
y(x)
=
e^{F(x)}
\left[
C
+
(1-n)
\int_{x_0}^{x}
e^{(n-1)F(s)}g(s)
\,ds
\right]^{1/(1-n)}.
}
$$

::: {.proof}
By step <1>7,
$$
z(x)
=
e^{(1-n)F(x)}
\left[
C
+
(1-n)
\int_{x_0}^{x}
e^{(n-1)F(s)}g(s)
\,ds
\right].
$$
Use $z=y^{1-n}$ and raise both sides to the power $1/(1-n)$.
:::

<1>9. Now suppose
$$
n=1.
$$
Then the equation becomes
$$
y'
=
(f+g)y.
$$

::: {.proof}
Substitute $n=1$ into the original equation.
:::

<1>10. Hence, for $n=1$,
$$
\boxed{
y(x)
=
C
\exp\left(
\int_{x_0}^{x}
[f(s)+g(s)]\,ds
\right).
}
$$

::: {.proof}
Separate variables in step <1>9:
$$
\frac{y'}y=f+g.
$$
Integrate and exponentiate. The case $C=0$ gives the zero solution.
:::

<1>11. When the original power $y^n$ is defined at $y=0$, the identically zero function is also a solution for every $n$ for which the right-hand side vanishes at $y=0$.

::: {.proof}
Substituting $y\equiv0$ gives $y'=0$ and right-hand side
$$
f(x)\cdot0
+
g(x)0^n.
$$
Whenever $0^n$ is defined and equals $0$, the equation is satisfied.
:::

<1>12. Q.E.D.

::: {.proof}
Step <1>8 gives the Bernoulli family for $n\neq1$, and step <1>10 gives the exceptional linear case $n=1$.
:::
:::
