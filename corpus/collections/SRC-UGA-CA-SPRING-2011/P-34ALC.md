---
schema: qual/card@1
id: P-34ALC
kind: problem
title: Functions on the Riemann sphere with a simple pole at $2$ and a double pole
  at infinity
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
  - Poles
  - Riemann Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Find all functions on the Riemann sphere that have a simple pole at $z=2$ and a double pole at $z=\infty$, but are analytic elsewhere.
:::

::: {.solution}
<1>1. If $f$ has a simple pole at $2$, then there is a unique
$A\in\CC^\times$ such that
$$
g(z)=f(z)-\frac{A}{z-2}
$$
is holomorphic at $z=2$.

::: {.proof}
The Laurent expansion of $f$ at $2$ has the form
$$
f(z)=\frac{A}{z-2}+\sum_{n=0}^\infty c_n(z-2)^n,
$$
with $A\ne0$ because the pole is simple. Subtracting the principal part
removes the pole, so $g$ extends holomorphically across $2$. The
coefficient $A$ is uniquely determined as the residue of $f$ at $2$.
:::

<1>2. The function $g$ from step <1>1 is entire on $\CC$ and has a
double pole at $\infty$.

::: {.proof}
The function $f$ is holomorphic on $\CC\setminus\{2\}$ and step <1>1
removes the only finite pole, so $g$ is entire.

Moreover,
$$
\frac{A}{z-2}\longrightarrow0
\qquad(z\to\infty),
$$
so this rational term is holomorphic at $\infty$ and vanishes there.
Subtracting it cannot change the order of the pole of $f$ at infinity.
Hence $g$ has a pole of order exactly $2$ at $\infty$.
:::

<1>3. An entire function has a pole of order exactly $2$ at infinity if
and only if it is a polynomial of degree exactly $2$.

::: {.proof}
Let $h$ be entire and put
$$
H(w)=h(1/w).
$$
If $h$ has a pole of order $2$ at infinity, then $H$ has a pole of order
$2$ at $w=0$. Thus its Laurent series near $0$ has only the negative
powers $w^{-2}$ and $w^{-1}$:
$$
H(w)=a_2w^{-2}+a_1w^{-1}+a_0+a_{-1}w+a_{-2}w^2+\cdots,
$$
with $a_2\ne0$.

Equivalently, the Laurent expansion of $h(z)$ for large $|z|$ has the
form
$$
h(z)=a_2z^2+a_1z+a_0+O(1/z).
$$
Subtract the quadratic polynomial
$$
P(z)=a_2z^2+a_1z+a_0.
$$
Then $h-P$ is entire and tends to $0$ as $z\to\infty$, hence is bounded
on $\CC$. Liouville's theorem implies that $h-P$ is constant; the limit
at infinity forces that constant to be $0$. Thus $h=P$ and has degree
$2$.

Conversely, if $h(z)=a_2z^2+a_1z+a_0$ with $a_2\ne0$, then
$$
h(1/w)=a_2w^{-2}+a_1w^{-1}+a_0,
$$
which has a pole of order exactly $2$ at $w=0$. Hence $h$ has a double
pole at infinity.
:::

<1>4. Therefore every function in the problem has the form
$$
\boxed{
f(z)=\frac{A}{z-2}+Bz^2+Cz+D
}
$$
with
$$
A\ne0,
\qquad
B\ne0,
\qquad
C,D\in\CC.
$$

::: {.proof}
By step <1>2, $g=f-A/(z-2)$ is entire with a double pole at infinity.
Step <1>3 therefore gives
$$
g(z)=Bz^2+Cz+D
$$
with $B\ne0$. The coefficient $A$ is nonzero by step <1>1, giving the
displayed form.
:::

<1>5. Every function of the displayed form has exactly the required
singularities.

::: {.proof}
The term $A/(z-2)$ has a simple pole at $2$ when $A\ne0$, while the
polynomial part is holomorphic there. Hence the sum has a simple pole at
$2$.

Away from $2$ the function is holomorphic on $\CC$. At infinity the
rational term $A/(z-2)$ is holomorphic and vanishes, while the quadratic
polynomial has a pole of order exactly $2$ because $B\ne0$. Thus the only
poles on the sphere are a simple pole at $2$ and a double pole at
$\infty$.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>4--<1>5 give the complete list and verify both necessity and
sufficiency.
:::
:::
