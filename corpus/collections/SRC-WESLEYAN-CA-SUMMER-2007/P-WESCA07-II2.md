---
schema: qual/card@1
id: P-WESCA07-II2
kind: problem
title: "Evaluate a twice-wound contour integral"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis Section II, problem 2 (Summer 2007) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Let
$$
\gamma(t)=2e^{it},\qquad 0\le t\le4\pi.
$$
Evaluate
$$
\int_\gamma\frac{\sin z}{z^3+z}\,dz.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The apparent singularity at $z=0$ is removable.


::: pf-proof

Since
$$
\sin z=z+O(z^3)
$$
and
$$
z^3+z=z(1+z^2),
$$
one has
$$
\frac{\sin z}{z^3+z}
=\frac{\sin z/z}{1+z^2}
\longrightarrow1
$$
as $z\to0$.

:::

:::

::: pf-step

The only poles inside $|z|=2$ are the simple poles $z=i$ and $z=-i$.


::: pf-proof

The denominator factors as
$$
z^3+z=z(z-i)(z+i).
$$
By step [](#s1-1){.pf-ref}, the factor $z$ produces no pole. The remaining zeros $\pm i$ both lie inside the circle of radius $2$.

:::

:::

::: pf-step

The residues at $i$ and $-i$ are
$$
\operatorname{Res}_{z=i}
\frac{\sin z}{z^3+z}
=-\frac{i\sinh1}{2},
$$
and
$$
\operatorname{Res}_{z=-i}
\frac{\sin z}{z^3+z}
=\frac{i\sinh1}{2}.
$$


::: pf-proof

For a simple zero $a$ of $q(z)=z^3+z$,
$$
\operatorname{Res}_{z=a}\frac{\sin z}{q(z)}
=\frac{\sin a}{q'(a)}.
$$
Since
$$
q'(z)=3z^2+1,
$$
one has
$$
q'(\pm i)=-2.
$$
Also
$$
\sin i=i\sinh1,
\qquad
\sin(-i)=-i\sinh1.
$$
Substitution gives the displayed residues.

:::

:::

::: pf-step

The curve $\gamma(t)=2e^{it}$, $0\le t\le4\pi$, winds twice positively around both poles.


::: pf-proof

As $t$ runs from $0$ to $4\pi$, the circle $|z|=2$ is traversed counterclockwise exactly twice. Both $i$ and $-i$ lie in its interior.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
\int_\gamma\frac{\sin z}{z^3+z}\,dz=0.}
$$


::: pf-proof

By the residue theorem with winding numbers,
$$
\begin{aligned}
\int_\gamma\frac{\sin z}{z^3+z}\,dz
&=2\pi i\cdot2
\left(
\operatorname{Res}_{z=i}\frac{\sin z}{z^3+z}
+
\operatorname{Res}_{z=-i}\frac{\sin z}{z^3+z}
\right)\\
&=4\pi i\left(-\frac{i\sinh1}{2}+\frac{i\sinh1}{2}\right)\\
&=0.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required value of the contour integral.

:::

:::

:::
