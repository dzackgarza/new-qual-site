---
schema: qual/card@1
id: P-WESCA04-P3
kind: problem
title: "Evaluate a contour integral around a spiral closed by a segment"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1.3, problem 3 (August 2, 2004) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Let
$$
\beta(t)=te^{it},\qquad 0\le t\le4\pi,
$$
and let $\gamma$ be the closed curve obtained by following $\beta$ and then the line segment from $4\pi$ to $0$.
Evaluate
$$
\int_\gamma \frac{z^2+1}{(z+1)(z+4)}\,dz.
$$
:::

::: {.solution}

Set
$$
F(z)
\coloneqq
\frac{z^2+1}{(z+1)(z+4)}.
$$

::: pf

::: {.pf-step #s1-1}

The only poles of $F$ are
$$
z=-1
\qquad\text{and}\qquad
z=-4,
$$
and both are simple.


::: pf-proof

The denominator is
$$
(z+1)(z+4),
$$
and the numerator does not vanish at either point:
$$
(-1)^2+1=2,
\qquad
(-4)^2+1=17.
$$

:::

:::

::: {.pf-step #s1-2}

The residues are
$$
\operatorname{Res}_{z=-1}F
=
\frac23
$$
and
$$
\operatorname{Res}_{z=-4}F
=
-\frac{17}{3}.
$$


::: pf-proof

For the pole at $-1$,
$$
\operatorname{Res}_{z=-1}F
=
\evaluated{
\frac{z^2+1}{z+4}
}_{z=-1}
=
\frac{2}{3}.
$$

For the pole at $-4$,
$$
\operatorname{Res}_{z=-4}F
=
\evaluated{
\frac{z^2+1}{z+1}
}_{z=-4}
=
\frac{17}{-3}
=
-\frac{17}{3}.
$$

:::

:::

::: {.pf-step #s1-3}

The closing line segment from
$$
4\pi
$$
to
$$
0
$$
contributes zero change of argument about either pole $-1$ or $-4$.


::: pf-proof

For a point
$$
-a,
\qquad
a>0,
$$
the vector from $-a$ to a point $x$ of the closing segment is
$$
x+a.
$$
Along the entire segment
$$
0\le x\le4\pi,
$$
this is a positive real number.
Its argument is therefore constantly
$$
0.
$$

:::

:::

::: pf-step

For $a>0$, the winding number of $\gamma$ about $-a$ is the total
change of argument of
$$
q_a(t)
\coloneqq
a+t e^{it},
\qquad
0\le t\le4\pi,
$$
divided by $2\pi$.


::: pf-proof

Along the spiral,
$$
\beta(t)-(-a)
=
a+t e^{it}
=
q_a(t).
$$
By step [](#s1-3){.pf-ref}, the closing segment adds no argument change.
Thus the winding number of the full closed curve is determined entirely by
the lifted argument of $q_a$.

:::

:::

::: {.pf-step #s1-5}

The curve $q_a$ can meet the negative real axis only at odd multiples
of $\pi$ satisfying
$$
t>a.
$$


::: pf-proof

The imaginary part is
$$
\operatorname{Im}q_a(t)
=
t\sin t.
$$
Thus a real-axis crossing can occur only when
$$
t=k\pi.
$$
At an odd multiple
$$
t=(2j+1)\pi,
$$
the real part is
$$
a-t.
$$
This is negative exactly when
$$
t>a.
$$
At an even multiple of $\pi$,
$$
q_a(t)=a+t>0,
$$
so the crossing is on the positive real axis.

:::

:::

::: {.pf-step #s1-6}

Every negative-real-axis crossing in step [](#s1-5){.pf-ref} contributes
$$
+1
$$
to the winding number.


::: pf-proof

At
$$
t=(2j+1)\pi,
$$
the imaginary part
$$
y(t)=t\sin t
$$
has derivative
$$
y'(t)
=
\sin t+t\cos t
=
-t
<
0.
$$
Hence as $t$ increases, $q_a(t)$ crosses the negative real axis from the
upper half-plane to the lower half-plane.

For a continuous lifted argument, this is the passage
$$
\pi^-\longrightarrow\pi^+,
$$
so the lifted argument continues increasing through $\pi$ rather than
jumping to $-\pi$.
Since the curve begins and ends on the positive real axis, each such crossing
adds one full turn, i.e. an argument increase of $2\pi$.

:::

:::

::: {.pf-step #s1-7}

The winding number about $-1$ is
$$
\boxed{
\operatorname{Ind}(\gamma,-1)=2.
}
$$


::: pf-proof

Take
$$
a=1.
$$
The odd multiples of $\pi$ in
$$
[0,4\pi]
$$
are
$$
\pi
\qquad\text{and}\qquad
3\pi.
$$
Both satisfy
$$
t>1.
$$
Thus step [](#s1-5){.pf-ref} gives two negative-axis crossings, and step [](#s1-6){.pf-ref} gives one
positive winding for each.

:::

:::

::: {.pf-step #s1-8}

The winding number about $-4$ is
$$
\boxed{
\operatorname{Ind}(\gamma,-4)=1.
}
$$


::: pf-proof

Take
$$
a=4.
$$
At the first odd multiple,
$$
t=\pi<4,
$$
so
$$
q_4(\pi)=4-\pi>0
$$
and there is no negative-axis crossing.

At
$$
t=3\pi>4,
$$
one has
$$
q_4(3\pi)=4-3\pi<0.
$$
Thus there is exactly one negative-axis crossing, giving one positive
winding by step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

The residue theorem for a possibly nonsimple closed curve gives
$$
\int_\gamma F(z)\,dz
=
2\pi i
\left[
\operatorname{Ind}(\gamma,-1)
\operatorname{Res}_{-1}F
+
\operatorname{Ind}(\gamma,-4)
\operatorname{Res}_{-4}F
\right].
$$


::: pf-proof

This is the residue theorem with winding numbers:
$$
\int_\gamma F(z)\,dz
=
2\pi i
\sum_a
\operatorname{Ind}(\gamma,a)
\operatorname{Res}_{z=a}F.
$$
The only poles are those in step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{
\int_\gamma
\frac{z^2+1}{(z+1)(z+4)}
\,dz
=
-\frac{26\pi i}{3}.
}
$$


::: pf-proof

Substitute steps [](#s1-2){.pf-ref} and [](#s1-7){.pf-ref}, and [](#s1-8){.pf-ref} into step [](#s1-9){.pf-ref}:
$$
\begin{aligned}
\int_\gamma F(z)\,dz
&=
2\pi i
\left(
2\cdot\frac23
+
1\cdot\left(-\frac{17}{3}\right)
\right)\\
&=
2\pi i
\left(
\frac4{3}
-
\frac{17}{3}
\right)\\
&=
2\pi i
\left(
-\frac{13}{3}
\right)\\
&=
-\frac{26\pi i}{3}.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the requested contour integral.

:::

:::

:::
