---
schema: qual/card@1
id: P-BKS16-1A
kind: problem
title: Rationality of an integral of nested radicals $\sqrt{-6+5\sqrt{\cdots}}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Checked the statement against Problem 1A in the vendored Berkeley Spring 2016 solution packet.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the fourfold T-composition inside the outer square root, the polynomial inverse, the endpoint values, and the inverse-function integral identity.
---

::: {.problem}
Show that
$$
\int_4^9 \sqrt{-6+5\sqrt{-6+5\sqrt{-6+5\sqrt{-6+5\sqrt{x}}}}}\,dx
$$
is a rational number.
:::

::: {.solution}
Define
$$
T(x)
\coloneqq
-6+5\sqrt{x}.
$$
Then the integrand is
$$
f(x)=\sqrt{T^{\circ4}(x)}.
$$

<1>1. The function $T$ is a strictly increasing bijection
$$
T:[4,9]\longrightarrow[4,9].
$$

::: {.proof}
For $x\in[4,9]$,
$$
2\leq\sqrt{x}\leq3,
$$
so
$$
4\leq-6+5\sqrt{x}\leq9.
$$
Thus $T(x)\in[4,9]$. The square-root function and the affine map $u\mapsto-6+5u$ are strictly increasing, so $T$ is strictly increasing. Finally,
$$
T(4)=4,
\qquad
T(9)=9.
$$
Continuity and strict monotonicity therefore give the stated bijection.
:::

<1>2. The inverse of $T$ is
$$
\psi(u)
\coloneqq
\left(\frac{u+6}{5}\right)^2,
$$
which is a polynomial with rational coefficients.

::: {.proof}
If $u=T(x)$, then
$$
u=-6+5\sqrt{x},
$$
so
$$
\sqrt{x}=\frac{u+6}{5}
$$
and hence
$$
x=\left(\frac{u+6}{5}\right)^2.
$$
Thus $T^{-1}=\psi$ on $[4,9]$.
:::

<1>3. The function $f$ is a strictly increasing bijection
$$
f:[4,9]\longrightarrow[2,3],
$$
and
$$
f^{-1}(y)=\psi^{\circ4}(y^2).
$$
In particular, $f^{-1}$ is a polynomial with rational coefficients.

::: {.proof}
By step <1>1, every iterate $T^{\circ r}$ is a strictly increasing bijection of $[4,9]$ onto itself and fixes $4$ and $9$. The square-root map is a strictly increasing bijection from $[4,9]$ onto $[2,3]$. Hence
$$
f(x)=\sqrt{T^{\circ4}(x)}
$$
is a strictly increasing bijection from $[4,9]$ onto $[2,3]$.

If $y=f(x)$, then
$$
y^2=T^{\circ4}(x).
$$
Applying $T^{-1}=\psi$ four times gives
$$
x=\psi^{\circ4}(y^2).
$$
Since $\psi$ is a polynomial with rational coefficients, so is $y\mapsto\psi^{\circ4}(y^2)$.
:::

<1>4. One has the inverse-function identity
$$
\int_4^9 f(x)\,dx
+
\int_2^3 f^{-1}(y)\,dy
=
19.
$$

::: {.proof}
Use the substitution $y=f(x)$. Since $x=f^{-1}(y)$,
$$
dx=(f^{-1})'(y)\,dy,
$$
and the endpoints $x=4,9$ correspond to $y=2,3$. Therefore
$$
\int_4^9f(x)\,dx
=
\int_2^3 y(f^{-1})'(y)\,dy.
$$
Integration by parts gives
$$
\begin{aligned}
\int_4^9f(x)\,dx
&=
\left[yf^{-1}(y)\right]_2^3
-
\int_2^3f^{-1}(y)\,dy\\
&=
3\cdot9-2\cdot4
-
\int_2^3f^{-1}(y)\,dy\\
&=
19
-
\int_2^3f^{-1}(y)\,dy.
\end{aligned}
$$
Rearrange.
:::

<1>5. The integral in the problem is a rational number.

::: {.proof}
By step <1>3, $f^{-1}$ is a polynomial with rational coefficients. Hence
$$
\int_2^3 f^{-1}(y)\,dy
$$
is rational, because a polynomial over $\QQ$ has an antiderivative over $\QQ$ and the endpoints $2,3$ are rational. Step <1>4 then shows that
$$
\int_4^9 f(x)\,dx
=
19-
\int_2^3 f^{-1}(y)\,dy
$$
is rational.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
