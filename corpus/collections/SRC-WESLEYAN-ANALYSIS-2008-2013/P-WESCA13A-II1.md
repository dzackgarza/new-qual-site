---
schema: qual/card@1
id: P-WESCA13A-II1
kind: problem
title: 'Isolated singularities of $(\cos z-1)/z^2$, $e^{1/z^2}/(z-1)$ and $\sqrt z/(z-1)$'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md. The first two subparts are clear.
- event: source-corrected
  by: claude-opus-5-5
  date: 2026-10-30
  note: The extraction renders the third function with a conjugate bar. Part (c) was read from the page image of assets/attachments/analysis_2008-2013.pdf, page 3, which shows the square root of z over z-1.
---

::: {.problem}
Find and classify all isolated singularities, giving pole orders and residues where applicable, for
$$
\frac{\cos z-1}{z^2},
\qquad
\frac{e^{1/z^2}}{z-1},
\qquad
\frac{\sqrt z}{z-1}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For
$$
f_1(z)
=
\frac{\cos z-1}{z^2},
$$
the only possible finite singularity is
$$
z=0.
$$


::: pf-proof

The numerator is entire and the denominator vanishes only at
$$
z=0.
$$

:::

:::

::: {.pf-step #s1-2}

The point
$$
z=0
$$
is a removable singularity of $f_1$.


::: pf-proof

Use the Taylor expansion
$$
\cos z
=
1-\frac{z^2}{2}
+\frac{z^4}{4!}
-\cdots.
$$
Then
$$
\frac{\cos z-1}{z^2}
=
-\frac12
+\frac{z^2}{4!}
-\frac{z^4}{6!}
+\cdots.
$$
Thus the Laurent expansion has no negative powers.
Hence the singularity is removable, with extended value
$$
f_1(0)=-\frac12.
$$

:::

:::

::: {.pf-step #s1-3}

The residue of $f_1$ at $0$ is
$$
\boxed{0}.
$$


::: pf-proof

The residue is the coefficient of
$$
z^{-1}
$$
in the Laurent expansion.
Step [](#s1-2){.pf-ref} shows there is no such term.

:::

:::

::: {.pf-step #s1-4}

For
$$
f_2(z)
=
\frac{e^{1/z^2}}{z-1},
$$
the only finite singularities are
$$
z=0
\qquad\text{and}\qquad
z=1.
$$


::: pf-proof

The factor
$$
e^{1/z^2}
$$
is holomorphic on
$$
\CC\setminus\{0\},
$$
while
$$
z-1
$$
vanishes only at
$$
z=1.
$$

:::

:::

::: {.pf-step #s1-5}

The point
$$
z=1
$$
is a simple pole of $f_2$ with residue
$$
\boxed{e}.
$$


::: pf-proof

The numerator is holomorphic and nonzero at $1$:
$$
e^{1/1^2}
=
e.
$$
Therefore
$$
f_2(z)
=
\frac{g(z)}{z-1}
$$
with
$$
g(1)=e\ne0.
$$
Hence the pole has order $1$, and
$$
\operatorname{Res}_{z=1}f_2
=
g(1)
=
e.
$$

:::

:::

::: {.pf-step #s1-6}

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
\frac{z^{-2n}}{n!}
$$
contains infinitely many nonzero negative powers.
Thus
$$
e^{1/z^2}
$$
has an essential singularity at $0$.

The factor
$$
\frac1{z-1}
$$
is holomorphic and nonzero near $0$.
Multiplying by such a factor preserves essentiality.
Therefore $f_2$ is essential at $0$.

:::

:::

::: {.pf-step #s1-7}

The residue of $f_2$ at $0$ is
$$
\boxed{
1-e.
}
$$


::: pf-proof

Near
$$
z=0,
$$
expand
$$
\frac1{z-1}
=
-\frac1{1-z}
=
-\sum_{m=0}^{\infty}z^m
$$
for
$$
\abs{z}<1.
$$
Also
$$
e^{1/z^2}
=
\sum_{n=0}^{\infty}
\frac{z^{-2n}}{n!}.
$$
Therefore
$$
f_2(z)
=
-\sum_{m,n\ge0}
\frac{z^{m-2n}}{n!}.
$$
The coefficient of
$$
z^{-1}
$$
occurs when
$$
m-2n=-1,
$$
that is,
$$
m=2n-1.
$$
This requires
$$
n\ge1.
$$
Hence
$$
\operatorname{Res}_{z=0}f_2
=
-\sum_{n=1}^{\infty}
\frac1{n!}.
$$
Therefore
$$
\operatorname{Res}_{z=0}f_2
=
-(e-1)
=
1-e.
$$

:::

:::

::: {.pf-step #s1-8}

For
$$
f_3(z)
=
\frac{\sqrt z}{z-1},
$$
the point $z=0$ is a branch point, not an isolated singularity.


::: pf-proof

No branch of $\sqrt z$ is holomorphic on a punctured disc $0<\abs z<r$:
continuing any branch once around the circle $\abs z=r/2$ multiplies it by $e^{\pi i}=-1$.
Since $1/(z-1)$ is holomorphic and nonzero near $0$, the same holds for $f_3$.
So $f_3$ is not holomorphic on any punctured neighborhood of $0$, and the classification into removable singularities, poles and essential singularities does not apply there.

:::

:::

::: {.pf-step #s1-9}

Fix a branch of $\sqrt z$ on a disc about $1$ not containing $0$.
Then $z=1$ is a simple pole of $f_3$ with residue $\sqrt 1$, which is
$$
\boxed{1}
$$
for the principal branch and $-1$ for the other branch.


::: pf-proof

On that disc $\sqrt z$ is holomorphic and $(\sqrt 1)^2=1$, so $\sqrt 1=\pm1\neq0$.
As in step [](#s1-5){.pf-ref}, $f_3=g/(z-1)$ with $g=\sqrt z$ and $g(1)\neq0$, so the pole is simple and $\operatorname{Res}_{z=1}f_3=g(1)=\sqrt 1$.

:::

:::

::: pf-step

The recoverable classification is therefore
$$
\boxed{
\begin{array}{c|c}
\dfrac{\cos z-1}{z^2}
&
0\text{ removable, residue }0,
\\[3mm]
\dfrac{e^{1/z^2}}{z-1}
&
0\text{ essential, residue }1-e;
\quad
1\text{ simple pole, residue }e,
\\[3mm]
\dfrac{\sqrt z}{z-1}
&
0\text{ branch point};
\quad
1\text{ simple pole, residue }\sqrt1=\pm1.
\end{array}
}
$$


::: pf-proof

Collect steps [](#s1-1){.pf-ref} through [](#s1-9){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-9){.pf-ref} classify every singularity of the three functions.

:::

:::

:::
