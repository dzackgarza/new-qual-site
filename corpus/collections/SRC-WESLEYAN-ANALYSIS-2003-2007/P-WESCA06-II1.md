---
schema: qual/card@1
id: P-WESCA06-II1
kind: problem
title: "Classify isolated singularities of three functions"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis Problems, problem 1 (August 9, 2006) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Find and classify all isolated singularities of the following functions, giving full justification:
$$
f_1(z)=\frac{\cos z-1}{z^2},
\qquad
f_2(z)=\frac{e^{1/z^2}}{z-1},
\qquad
f_3(z)=\sqrt z.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The only finite singularity of
$$
f_1(z)
=
\frac{\cos z-1}{z^2}
$$
is
$$
z=0.
$$


::: pf-proof

The numerator and denominator are entire, and the denominator vanishes only
at
$$
z=0.
$$
Thus $f_1$ is holomorphic on
$$
\CC\setminus\{0\}.
$$

:::

:::

::: {.pf-step #s1-2}

The singularity of $f_1$ at $0$ is removable, with removable value
$$
\boxed{
f_1(0)=-\frac12.
}
$$


::: pf-proof

The Taylor expansion is
$$
\cos z
=
1-\frac{z^2}{2}
+\frac{z^4}{4!}
-\cdots.
$$
Hence
$$
\cos z-1
=
-\frac{z^2}{2}
+\frac{z^4}{4!}
-\cdots,
$$
so for
$$
z\ne0,
$$
$$
\frac{\cos z-1}{z^2}
=
-\frac12
+\frac{z^2}{4!}
-\cdots.
$$
The right-hand side extends holomorphically to $z=0$ with value
$$
-\frac12.
$$

:::

:::

::: {.pf-step #s1-3}

The function
$$
f_2(z)
=
\frac{e^{1/z^2}}{z-1}
$$
is holomorphic on
$$
\CC\setminus\{0,1\}.
$$


::: pf-proof

The function
$$
e^{1/z^2}
$$
is holomorphic for
$$
z\ne0,
$$
and the additional denominator
$$
z-1
$$
vanishes only at
$$
z=1.
$$

:::

:::

::: {.pf-step #s1-4}

The point
$$
z=1
$$
is a simple pole of $f_2$.


::: pf-proof

The numerator
$$
e^{1/z^2}
$$
is holomorphic near $1$ and
$$
e^{1/1^2}
=
e
\ne
0.
$$
Thus
$$
f_2(z)
=
\frac{g(z)}{z-1},
$$
where
$$
g(1)=e\ne0.
$$
Hence $z=1$ is a pole of order $1$.

:::

:::

::: {.pf-step #s1-5}

The point
$$
z=0
$$
is an essential singularity of $f_2$.


::: pf-proof

The Laurent expansion
$$
e^{1/z^2}
=
\sum_{n=0}^{\infty}
\frac1{n!}z^{-2n}
$$
contains infinitely many nonzero negative powers.
Therefore
$$
e^{1/z^2}
$$
has an essential singularity at $0$.

The factor
$$
\frac1{z-1}
$$
is holomorphic and nonzero near $0$.
Multiplication by a holomorphic nonvanishing factor cannot turn an essential
singularity into a pole or a removable singularity.
Hence $f_2$ is also essential at $0$.

:::

:::

::: {.pf-step #s1-6}

The expression
$$
f_3(z)=\sqrt z
$$
does not define a single-valued holomorphic function on
$$
\CC\setminus\{0\}.
$$


::: pf-proof

Suppose there were a holomorphic function
$$
g
$$
on a punctured disk
$$
0<\abs{z}<r
$$
such that
$$
g(z)^2=z.
$$

Then $g$ never vanishes on the punctured disk.
Differentiate:
$$
2g(z)g'(z)=1,
$$
so
$$
\frac{g'(z)}{g(z)}
=
\frac1{2z}.
$$

Integrate around the positively oriented circle
$$
\abs{z}=\rho<r.
$$
The left-hand side satisfies
$$
\frac1{2\pi i}
\int_{\abs{z}=\rho}
\frac{g'(z)}{g(z)}
\,dz
\in
\ZZ
$$
by the argument principle.
But the right-hand side gives
$$
\frac1{2\pi i}
\int_{\abs{z}=\rho}
\frac1{2z}
\,dz
=
\frac12,
$$
a contradiction.

Therefore no single-valued holomorphic square root exists on a punctured
neighborhood of $0$.

:::

:::

::: {.pf-step #s1-7}

Consequently,
$$
\boxed{
z=0
\text{ is a branch point of }\sqrt z,
\text{ not an isolated singularity of a holomorphic function}.
}
$$


::: pf-proof

An isolated singularity requires a single-valued holomorphic function on a
full punctured disk around the point.
Step [](#s1-6){.pf-ref} proves that no such branch of
$$
\sqrt z
$$
exists around $0$.

On any slit domain, for example
$$
\CC\setminus(-\infty,0],
$$
one may choose a holomorphic branch of the square root, but then $0$ lies on
the boundary of the branch domain rather than being an isolated singularity
in that domain.

:::

:::

::: {.pf-step #s1-8}

The complete classification is therefore
$$
\boxed{
\begin{array}{c|c}
\text{function}&\text{finite singularities}\\
\hline
\dfrac{\cos z-1}{z^2}
&
0\text{ removable},\\[3mm]
\dfrac{e^{1/z^2}}{z-1}
&
0\text{ essential},\quad
1\text{ simple pole},\\[3mm]
\sqrt z
&
0\text{ branch point, not an isolated singularity}.
\end{array}
}
$$


::: pf-proof

Collect steps [](#s1-1){.pf-ref} through [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} gives all requested classifications.

:::

:::

:::
