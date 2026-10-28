---
schema: qual/card@1
id: P-WESCA13J-II1
kind: problem
title: 'Classify three singularities and find their residues'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
For each function, classify the singularity at the indicated point and find the residue:

(a) $f(z)=z^2e^{-1/z^3}$ at $z_0=0$;

(b) $f(z)=\dfrac{z^2}{(z-1)^2}$ at $z_0=1$;

(c) $f(z)=\dfrac{\sin(z^3)}{(1-\cos z)^3}$ at $z_0=0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For part (a),
$$
z^2e^{-1/z^3}
=
\sum_{n=0}^{\infty}
\frac{(-1)^n}{n!}
z^{2-3n}.
$$


::: pf-proof

Use the exponential series
$$
e^w
=
\sum_{n=0}^{\infty}
\frac{w^n}{n!}
$$
with
$$
w=-\frac1{z^3}.
$$
Then
$$
e^{-1/z^3}
=
\sum_{n=0}^{\infty}
\frac{(-1)^n}{n!}z^{-3n}.
$$
Multiplying by
$$
z^2
$$
gives the displayed Laurent series.

:::

:::

::: {.pf-step #s1-2}

The singularity in part (a) is essential.


::: pf-proof

The Laurent expansion from step [](#s1-1){.pf-ref} contains infinitely many negative powers
$$
z^{2-3n},
\qquad
n\ge1.
$$
Therefore the principal part has infinitely many nonzero terms, so
$$
z=0
$$
is an essential singularity.

:::

:::

::: {.pf-step #s1-3}

The residue in part (a) is
$$
\boxed{-1}.
$$


::: pf-proof

The residue is the coefficient of
$$
z^{-1}.
$$
In step [](#s1-1){.pf-ref} this exponent occurs when
$$
2-3n=-1,
$$
so
$$
n=1.
$$
The corresponding coefficient is
$$
\frac{(-1)^1}{1!}
=
-1.
$$

:::

:::

::: {.pf-step #s1-4}

For part (b), writing
$$
w=z-1,
$$
one has
$$
\frac{z^2}{(z-1)^2}
=
\frac{(1+w)^2}{w^2}
=
\frac1{w^2}
+\frac2w
+1.
$$


::: pf-proof

Since
$$
z=1+w,
$$
expand
$$
z^2
=(1+w)^2
=
1+2w+w^2
$$
and divide by
$$
w^2.
$$

:::

:::

::: {.pf-step #s1-5}

The singularity in part (b) is a pole of order
$$
\boxed{2}
$$
with residue
$$
\boxed{2}.
$$


::: pf-proof

The Laurent expansion from step [](#s1-4){.pf-ref} has leading term
$$
w^{-2}
$$
with nonzero coefficient, so
$$
z=1
$$
is a pole of order
$$
2.
$$
The coefficient of
$$
w^{-1}
$$
is
$$
2,
$$
which is the residue.

:::

:::

::: {.pf-step #s1-6}

For part (c),
$$
\sin(z^3)
=
z^3+O(z^9)
$$
and
$$
1-\cos z
=
\frac{z^2}{2}
\left(
1-\frac{z^2}{12}+O(z^4)
\right).
$$


::: pf-proof

The Taylor series give
$$
\sin(z^3)
=
z^3
-\frac{z^9}{6}
+O(z^{15}),
$$
and
$$
1-\cos z
=
\frac{z^2}{2}
-\frac{z^4}{24}
+O(z^6).
$$
Factoring
$$
z^2/2
$$
from the second expression yields the displayed form.

:::

:::

::: {.pf-step #s1-7}

One has
$$
\frac1{(1-\cos z)^3}
=
8z^{-6}
\left(
1+\frac{z^2}{4}+O(z^4)
\right).
$$


::: pf-proof

By step [](#s1-6){.pf-ref},
$$
(1-\cos z)^{-3}
=
8z^{-6}
\left(
1-\frac{z^2}{12}+O(z^4)
\right)^{-3}.
$$
Using
$$
(1+u)^{-3}
=
1-3u+O(u^2),
$$
with
$$
u=-\frac{z^2}{12}+O(z^4),
$$
gives
$$
\left(
1-\frac{z^2}{12}+O(z^4)
\right)^{-3}
=
1+\frac{z^2}{4}+O(z^4).
$$

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\frac{\sin(z^3)}{(1-\cos z)^3}
=
8z^{-3}
+2z^{-1}
+O(z).
$$


::: pf-proof

Multiply the expansions from steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref}:
$$
\begin{aligned}
\frac{\sin(z^3)}{(1-\cos z)^3}
&=
\left(
z^3+O(z^9)
\right)
8z^{-6}
\left(
1+\frac{z^2}{4}+O(z^4)
\right)\\
&=
8z^{-3}
\left(
1+\frac{z^2}{4}+O(z^4)
\right)
+O(z^3)\\
&=
8z^{-3}
+2z^{-1}
+O(z).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-9}

The singularity in part (c) is a pole of order
$$
\boxed{3}
$$
with residue
$$
\boxed{2}.
$$


::: pf-proof

Step [](#s1-8){.pf-ref} has leading term
$$
8z^{-3},
$$
so the pole order is
$$
3.
$$
The coefficient of
$$
z^{-1}
$$
is
$$
2,
$$
which is the residue.

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} solve part (a), steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} solve part (b), and steps [](#s1-6){.pf-ref} through [](#s1-9){.pf-ref} solve part (c).

:::

:::

:::
