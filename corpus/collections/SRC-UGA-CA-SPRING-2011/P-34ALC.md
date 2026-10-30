---
schema: qual/card@1
id: P-34ALC
kind: problem
title: Meromorphic functions with a simple pole at $2$ and a double pole at $\infty$
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
Find all meromorphic functions that have a simple pole at $z=2$ and a double pole at $z=\infty$, but are analytic elsewhere. Prove that your list is complete.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $f$ has a simple pole at $2$, then there is a unique
$A\in\CC^\times$ such that
$$
g(z)=f(z)-\frac{A}{z-2}
$$
is holomorphic at $z=2$.

::: pf-proof

The Laurent expansion of $f$ at $2$ has the form
$$
f(z)=\frac{A}{z-2}+\sum_{n=0}^\infty c_n(z-2)^n,
$$
with $A\ne0$ because the pole is simple. Subtracting the principal part
removes the pole, so $g$ extends holomorphically across $2$. The
coefficient $A$ is uniquely determined as the residue of $f$ at $2$.

:::

:::

::: {.pf-step #s2}

The function $g$ from step [](#s1){.pf-ref} is entire on $\CC$ and has a
double pole at $\infty$.

::: pf-proof

The function $f$ is holomorphic on $\CC\setminus\{2\}$ and step [](#s1){.pf-ref}
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

:::

::: {.pf-step #s3}

An entire function has a pole of order exactly $2$ at infinity if
and only if it is a polynomial of degree exactly $2$.

::: pf-proof

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

Equivalently, the Laurent expansion of $h(z)$ for large $\abs{z}$ has the
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

:::

::: {.pf-step #s4}

Therefore every function in the problem has the form
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

::: pf-proof

By step [](#s2){.pf-ref}, $g=f-A/(z-2)$ is entire with a double pole at infinity.
Step [](#s3){.pf-ref} therefore gives
$$
g(z)=Bz^2+Cz+D
$$
with $B\ne0$. The coefficient $A$ is nonzero by step [](#s1){.pf-ref}, giving the
displayed form.

:::

:::

::: {.pf-step #s5}

Every function of the displayed form has exactly the required
singularities.

::: pf-proof

The term $A/(z-2)$ has a simple pole at $2$ when $A\ne0$, while the
polynomial part is holomorphic there. Hence the sum has a simple pole at
$2$.

Away from $2$ the function is holomorphic on $\CC$. At infinity the
rational term $A/(z-2)$ is holomorphic and vanishes, while the quadratic
polynomial has a pole of order exactly $2$ because $B\ne0$. Thus the only
poles on the sphere are a simple pole at $2$ and a double pole at
$\infty$.

:::

:::

::: pf-qed

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} give the complete list and verify both necessity and
sufficiency.

:::

:::

:::
