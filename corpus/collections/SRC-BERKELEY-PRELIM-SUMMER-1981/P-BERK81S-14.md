---
schema: qual/card@1
id: P-BERK81S-14
kind: problem
title: Differentiability of the modulus near a simple zero approached from one side
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
    Extended f continuously by f(0)=0 and used the limit f'(t)->C to write
    f(t)=int_0^t f'(s) ds, yielding f(t)/t->C. Hence f(t) is nonzero for
    all sufficiently small t. On that interval,
    g'(t)=Re(f'(t) conjugate(f(t))/|f(t)|), and the unit vector
    f(t)/|f(t)| tends to C/|C|, so g'(t)->|C|.
---

::: {.problem}
Let $f:(0,1)\to\mathbb C$ be $C^1$.
Suppose
\[
f(t)\to0,
\qquad
f'(t)\to C\ne0
\qquad(t\to0^+).
\]
Show that $g(t)=|f(t)|$ is $C^1$ for all sufficiently small $t>0$, and that
\[
\lim_{t\to0^+}g'(t)
\]
exists.
Evaluate this limit.
:::

::: {.solution}
<1>1. There is a number $\delta_0>0$ such that $f'$ is bounded on
$(0,\delta_0]$.

::: {.proof}
The hypothesis
$$
f'(t)\longrightarrow C
\qquad
(t\to0^+)
$$
implies that there is $\delta_0>0$ such that
$$
\abs{f'(t)-C}<1
$$
whenever $0<t\leq\delta_0$. Thus
$$
\abs{f'(t)}
\leq
\abs{C}+1
$$
on this interval.
:::

<1>2. For every $0<t\leq\delta_0$,
$$
f(t)
=
\int_0^t f'(s)\,ds,
$$
where the integral is taken componentwise in $\CC\cong\RR^2$.

::: {.proof}
Fix $t\leq\delta_0$. For $0<a<t$, the fundamental theorem of calculus gives
$$
f(t)-f(a)
=
\int_a^t f'(s)\,ds.
$$
By hypothesis,
$$
f(a)\longrightarrow0
$$
as $a\to0^+$. By step <1>1, the derivative is bounded near $0$, so the
improper integral
$$
\int_0^t f'(s)\,ds
$$
exists. Letting $a\to0^+$ in the displayed identity gives the formula.
:::

<1>3. One has
$$
\boxed{
\frac{f(t)}{t}\longrightarrow C
}
$$
as $t\to0^+$.

::: {.proof}
By step <1>2,
$$
\frac{f(t)}t-C
=
\frac1t
\int_0^t
\bigl(f'(s)-C\bigr)\,ds.
$$
Therefore
$$
\abs{
\frac{f(t)}t-C
}
\leq
\sup_{0<s\leq t}\abs{f'(s)-C}.
$$
The right-hand side tends to zero because $f'(s)\to C$ as $s\to0^+$.
:::

<1>4. There is $\delta\in(0,\delta_0]$ such that
$$
f(t)\neq0
$$
for every $0<t<\delta$.

::: {.proof}
Since $C\neq0$, step <1>3 gives a $\delta\in(0,\delta_0]$ such that
$$
\abs{
\frac{f(t)}t-C
}
<
\frac{\abs{C}}{2}
$$
for $0<t<\delta$. Hence
$$
\abs{
\frac{f(t)}t
}
\geq
\abs{C}
-
\abs{
\frac{f(t)}t-C
}
>
\frac{\abs{C}}{2}
>
0.
$$
Thus $f(t)\neq0$ on that interval.
:::

<1>5. The function
$$
g(t)=\abs{f(t)}
$$
is $C^1$ on $(0,\delta)$, and
$$
g'(t)
=
\operatorname{Re}
\left(
f'(t)
\frac{\overline{f(t)}}{\abs{f(t)}}
\right).
$$

::: {.proof}
The modulus map
$$
\CC\sm\{0\}\longrightarrow\RR,
\qquad
z\longmapsto\abs{z},
$$
is $C^1$. By step <1>4, the image of $(0,\delta)$ under $f$ avoids $0$,
so the composition $g=\abs{\cdot}\circ f$ is $C^1$.

Writing $f=u+iv$ with real-valued $C^1$ functions $u,v$,
$$
g(t)
=
\sqrt{u(t)^2+v(t)^2}.
$$
Since $g(t)>0$,
$$
\begin{aligned}
g'(t)
&=
\frac{u(t)u'(t)+v(t)v'(t)}{g(t)}\\
&=
\operatorname{Re}
\left(
(u'(t)+iv'(t))
\frac{u(t)-iv(t)}{\abs{f(t)}}
\right),
\end{aligned}
$$
which is the displayed formula.
:::

<1>6. One has
$$
\frac{f(t)}{\abs{f(t)}}
\longrightarrow
\frac{C}{\abs{C}}
$$
as $t\to0^+$.

::: {.proof}
Because $t>0$,
$$
\frac{f(t)}{\abs{f(t)}}
=
\frac{f(t)/t}{\abs{f(t)/t}}.
$$
Step <1>3 gives
$$
\frac{f(t)}t\longrightarrow C\neq0.
$$
The map
$$
z\longmapsto\frac z{\abs{z}}
$$
is continuous on $\CC\sm\{0\}$, so the stated limit follows.
:::

<1>7. The derivative of $g$ has the limit
$$
\boxed{
\lim_{t\to0^+}g'(t)=\abs{C}.
}
$$

::: {.proof}
By step <1>5,
$$
g'(t)
=
\operatorname{Re}
\left(
f'(t)
\frac{\overline{f(t)}}{\abs{f(t)}}
\right).
$$
The hypotheses give
$$
f'(t)\longrightarrow C,
$$
while step <1>6 gives
$$
\frac{\overline{f(t)}}{\abs{f(t)}}
\longrightarrow
\frac{\overline C}{\abs{C}}.
$$
Therefore
$$
\begin{aligned}
\lim_{t\to0^+}g'(t)
&=
\operatorname{Re}
\left(
C\frac{\overline C}{\abs{C}}
\right)\\
&=
\operatorname{Re}(\abs{C})\\
&=
\abs{C}.
\end{aligned}
$$
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>5 proves that $g$ is $C^1$ for all sufficiently small positive
$t$, and step <1>7 evaluates the required derivative limit.
:::
:::
