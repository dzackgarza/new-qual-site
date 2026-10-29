---
schema: qual/card@1
id: P-UCLAB13S-02
kind: problem
title: An error bound for Simpson's rule
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 2 of the retained UCLA Basic Examination, Spring 2013.
---

::: {.problem}
The approximation from Simpson's Rule for $\int_a^b f(x)\,dx$ is
$$
S_{[a,b]}f=
\left[
\frac23 f\!\left(\frac{a+b}{2}\right)
+\frac13\left(\frac{f(a)+f(b)}2\right)
\right](b-a).
$$
If $f$ has continuous derivatives up to order three, prove that
$$
\left|\int_a^b f(x)\,dx-S_{[a,b]}f\right|
\le C(b-a)^4\max_{[a,b]}|f^{(3)}(x)|,
$$
where $C$ does not depend on $f$.
:::

::: {.solution}

Set
$$
m=\frac{a+b}{2},
\qquad
h=\frac{b-a}{2},
$$
so that
$$
[a,b]=[m-h,m+h].
$$
Also set
$$
M=\max_{x\in[a,b]}|f^{(3)}(x)|.
$$

::: pf

::: {.pf-step #s1-1}

For every $t\in[-h,h]$, Taylor's theorem at $m$ gives
$$
f(m+t)
=
p(t)+R(t),
$$
where
$$
p(t)
=
f(m)+f'(m)t+\frac12f''(m)t^2
$$
and
$$
\boxed{|R(t)|\le\frac{M}{6}|t|^3}.
$$


::: pf-proof

Since $f$ has continuous derivatives through order $3$, Taylor's theorem with Lagrange remainder gives
$$
f(m+t)
=
f(m)+f'(m)t+\frac12f''(m)t^2
+
\frac16f^{(3)}(\xi_t)t^3
$$
for some $\xi_t$ between $m$ and $m+t$.
Therefore
$$
|R(t)|
\le
\frac16M|t|^3.
$$

:::

:::

::: {.pf-step #s1-2}

Simpson's rule is exact for the quadratic polynomial $p$:
$$
\int_{-h}^{h}p(t)\,dt
=
2h
\left[
\frac23p(0)
+
\frac16\bigl(p(-h)+p(h)\bigr)
\right].
$$


::: pf-proof

Write
$$
p(t)=\alpha+\beta t+\gamma t^2.
$$
Then
$$
\int_{-h}^{h}p(t)\,dt
=
2h\alpha+\frac{2}{3}\gamma h^3.
$$
Also,
$$
p(0)=\alpha
$$
and
$$
p(-h)+p(h)
=
2\alpha+2\gamma h^2.
$$
Hence
$$
\begin{aligned}
2h
\left[
\frac23p(0)
+
\frac16\bigl(p(-h)+p(h)\bigr)
\right]
&=
2h
\left[
\frac23\alpha
+
\frac13\alpha
+
\frac13\gamma h^2
\right]\\
&=
2h\alpha+\frac23\gamma h^3.
\end{aligned}
$$
This agrees with the integral.

:::

:::

::: {.pf-step #s1-3}

The quadrature error for $f$ equals the quadrature error for the remainder $R$:
$$
\begin{aligned}
\int_a^b f(x)\,dx-S_{[a,b]}f
&=
\int_{-h}^{h}R(t)\,dt\\
&\quad-
2h
\left[
\frac23R(0)
+
\frac16\bigl(R(-h)+R(h)\bigr)
\right].
\end{aligned}
$$


::: pf-proof

After the change of variables
$$
x=m+t,
$$
the integral over $[a,b]$ becomes an integral over $[-h,h]$.
Both integration and Simpson's rule are linear.
By step [](#s1-2){.pf-ref}, they agree exactly on the polynomial part $p$.
Subtracting therefore leaves only the remainder contribution.
Since
$$
R(0)=0
$$
by step [](#s1-1){.pf-ref}, this term will vanish in the estimate below.

:::

:::

::: {.pf-step #s1-4}

The integral remainder satisfies
$$
\left|
\int_{-h}^{h}R(t)\,dt
\right|
\le
\frac{M}{12}h^4.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\begin{aligned}
\left|
\int_{-h}^{h}R(t)\,dt
\right|
&\le
\int_{-h}^{h}|R(t)|\,dt\\
&\le
\frac{M}{6}
\int_{-h}^{h}|t|^3\,dt.
\end{aligned}
$$
Now
$$
\int_{-h}^{h}|t|^3\,dt
=
2\int_0^h t^3\,dt
=
\frac{h^4}{2}.
$$
Thus
$$
\left|
\int_{-h}^{h}R(t)\,dt
\right|
\le
\frac{M}{12}h^4.
$$

:::

:::

::: {.pf-step #s1-5}

The Simpson remainder satisfies
$$
\left|
2h
\left[
\frac16\bigl(R(-h)+R(h)\bigr)
\right]
\right|
\le
\frac{M}{9}h^4.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
|R(\pm h)|
\le
\frac{M}{6}h^3.
$$
Therefore
$$
\begin{aligned}
\left|
\frac{h}{3}
\bigl(R(-h)+R(h)\bigr)
\right|
&\le
\frac{h}{3}
\left(
\frac{M}{6}h^3
+
\frac{M}{6}h^3
\right)\\
&=
\frac{M}{9}h^4.
\end{aligned}
$$
Since
$$
2h\cdot\frac16=\frac h3,
$$
this is the displayed bound.

:::

:::

::: {.pf-step #s1-6}

Hence
$$
\left|
\int_a^b f(x)\,dx-S_{[a,b]}f
\right|
\le
\frac7{36}Mh^4.
$$


::: pf-proof

Apply the triangle inequality to the error identity in step [](#s1-3){.pf-ref}.
Use the estimates from steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref}:
$$
\frac{M}{12}h^4
+
\frac{M}{9}h^4
=
\left(
\frac3{36}
+
\frac4{36}
\right)
Mh^4
=
\frac7{36}Mh^4.
$$

:::

:::

::: {.pf-step #s1-7}

Since
$$
h=\frac{b-a}{2},
$$
one obtains
$$
\boxed{
\left|
\int_a^b f(x)\,dx-S_{[a,b]}f
\right|
\le
\frac7{576}
(b-a)^4
\max_{[a,b]}|f^{(3)}|.
}
$$


::: pf-proof

Substitute
$$
h^4
=
\frac{(b-a)^4}{16}
$$
into step [](#s1-6){.pf-ref}:
$$
\frac7{36}Mh^4
=
\frac7{36}\cdot\frac1{16}
(b-a)^4M
=
\frac7{576}(b-a)^4M.
$$
Thus the estimate holds with the universal constant
$$
\boxed{C=\frac7{576}}.
$$

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required Simpson-rule error bound.

:::

:::

:::
