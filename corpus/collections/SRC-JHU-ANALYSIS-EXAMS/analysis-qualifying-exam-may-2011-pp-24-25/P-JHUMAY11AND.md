---
schema: qual/card@1
id: P-JHUMAY11AND
kind: problem
title: A logarithmic upper bound forces an entire harmonic function to be constant
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared May 2011 problem 4 on PDF page 24; retained the one-sided logarithmic bound, corrected the title and removed the next subject heading."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the global harmonic conjugate, polynomial growth of its exponential, the Cauchy coefficient limits and the zero-free polynomial step; no lower bound on u is assumed."
---

4. Suppose that $u : \mathbb { C } \to \mathbb { R }$ is a harmonic function such that

$$
u ( z ) \leq 1 0 \log ( | z | + 2 ) ,
$$

for all $z \in \mathbb { C }$ . Prove that u is constant.

::: solution
<1>1. The harmonic function is the real part of an entire function.

::: proof
The plane is simply connected, so $u$ has a globally
defined harmonic conjugate $v$; consequently $H=u+iv$
is entire [@SS03]. One explicit construction, writing
$z=x+iy$, is
$$
v(x,y)=-\int_0^x u_y(t,0)\,dt+\int_0^y u_x(x,s)\,ds.
$$
Indeed, $v_y=u_x$, while harmonicity gives
$$
v_x=-u_y(x,0)+\int_0^y u_{xx}(x,s)\,ds
=-u_y(x,0)-\int_0^y u_{yy}(x,s)\,ds=-u_y(x,y).
$$
Thus the Cauchy–Riemann equations hold everywhere and
$\operatorname{Re}H=u$.
:::

<1>2. The exponential of $H$ is a polynomial.

::: proof
The entire function $F=e^H$ satisfies
$$
|F(z)|=e^{u(z)}\leq e^{10\log(|z|+2)}=(|z|+2)^{10}.
$$
Write its entire Taylor expansion as $F(z)=\sum_{k\geq0}a_kz^k$.
Cauchy's coefficient estimate on $|z|=R$ gives
$$
|a_k|\leq\frac{(R+2)^{10}}{R^k}
$$
[@SS03]. For every integer $k>10$, the right-hand side
tends to zero as $R\to\infty$. Hence $a_k=0$ for all
such $k$, so $F$ is a polynomial of degree at most ten.
:::

<1>3. This polynomial is constant, and so is $u$.

::: proof
An exponential has no zero. By the fundamental theorem
of algebra, a nonconstant complex polynomial has a zero
[@SS03]. The polynomial $F=e^H$ from step <1>2 must
therefore be a nonzero constant. Differentiating gives
$0=F'=H'e^H$, and nonvanishing of $e^H$ implies $H'=0$.
Thus $H$ is constant on the connected plane, and its
real part $u$ is constant as well.
:::
:::
