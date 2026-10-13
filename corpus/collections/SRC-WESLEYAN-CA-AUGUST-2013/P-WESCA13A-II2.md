---
schema: qual/card@1
id: P-WESCA13A-II2
kind: problem
title: 'Three contour integrals from repeated Wesleyan problems'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md. Each subpart is an exact repeated problem elsewhere in the same packet family; they are grouped because the 2013 source presents them as one numbered problem.
---

::: {.problem}
Evaluate:

(a)
\[
\int_{|z|=1}\frac{\Log(z+e)}{z^2}\,dz;
\]

(b)
\[
\int_{|z|=4}\left(\frac{\sin z}{z}\right)^{100}\,dz;
\]

(c) if $\beta(t)=te^{it}$ for $0\le t\le4\pi$ and $\gamma$ is $\beta$ followed by the segment from $4\pi$ to $0$, evaluate
\[
\int_\gamma\frac{z^2+1}{(z+1)(z+4)}\,dz.
\]
:::

::: {.solution}
<1>1. For part (a), let
\[
h(z)=\Log(z+e).
\]
Then $h$ is holomorphic on a neighborhood of the closed unit disk.

::: {.proof}
If $|z|\le1$, then
\[
\operatorname{Re}(z+e)\ge e-1>0.
\]
Thus $z+e$ stays in the right half-plane, where the principal logarithm is
holomorphic.
:::

<1>2. Cauchy's integral formula for derivatives gives
\[
\int_{|z|=1}\frac{\Log(z+e)}{z^2}\,dz
=2\pi i\,h'(0).
\]

::: {.proof}
Apply
\[
h'(0)=\frac1{2\pi i}\int_{|z|=1}\frac{h(z)}{z^2}\,dz.
\]
:::

<1>3. Since
\[
h'(z)=\frac1{z+e},
\]
\[
\boxed{
\int_{|z|=1}\frac{\Log(z+e)}{z^2}\,dz
=\frac{2\pi i}{e}.
}
\]

::: {.proof}
Substitute
\[
h'(0)=\frac1e
\]
into step <1>2.
:::

<1>4. For part (b), the function
\[
g(z)=\frac{\sin z}{z}
\]
for $z\ne0$, extended by
\[
g(0)=1,
\]
is entire.

::: {.proof}
The power series
\[
\frac{\sin z}{z}
=1-\frac{z^2}{3!}+\frac{z^4}{5!}-\cdots
\]
shows that the singularity at $0$ is removable.
:::

<1>5. Therefore
\[
\boxed{
\int_{|z|=4}
\left(\frac{\sin z}{z}\right)^{100}\,dz
=0.
}
\]

::: {.proof}
The integrand extends to an entire function, so Cauchy's theorem applies.
:::

<1>6. For part (c), set
\[
F(z)
\coloneqq
\frac{z^2+1}{(z+1)(z+4)}.
\]
Its poles are $-1$ and $-4$, with
\[
\operatorname{Res}_{z=-1}F
=
\frac23,
\qquad
\operatorname{Res}_{z=-4}F
=
-\frac{17}{3}.
\]

::: {.proof}
Both poles are simple:
\[
\operatorname{Res}_{z=-1}F
=
\left.
\frac{z^2+1}{z+4}
\right|_{z=-1}
=
\frac23,
\]
and
\[
\operatorname{Res}_{z=-4}F
=
\left.
\frac{z^2+1}{z+1}
\right|_{z=-4}
=
-\frac{17}{3}.
\]
:::

<1>7. The winding numbers of the closed curve $\gamma$ are
\[
\operatorname{Ind}(\gamma,-1)=2,
\qquad
\operatorname{Ind}(\gamma,-4)=1.
\]

::: {.proof}
Along the spiral
\[
\beta(t)=te^{it},
\qquad
0\le t\le4\pi,
\]
the shifted curve about the point $-a$ is
\[
a+te^{it}.
\]
It crosses the negative real axis at odd multiples
\[
t=(2k+1)\pi
\]
for which
\[
t>a.
\]
Each such crossing contributes one positive winding.

For $a=1$, both
\[
\pi
\quad\text{and}\quad
3\pi
\]
contribute, so the index is $2$.
For $a=4$, only
\[
3\pi
\]
contributes, so the index is $1$.

The closing segment from $4\pi$ to $0$ lies on the positive real axis and
contributes no further change of argument about either negative pole.
:::

<1>8. Hence
\[
\boxed{
\int_\gamma
\frac{z^2+1}{(z+1)(z+4)}
\,dz
=
-\frac{26\pi i}{3}.
}
\]

::: {.proof}
The residue theorem with winding numbers gives
\[
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
-\frac{26\pi i}{3}.
\end{aligned}
\]
:::

<1>9. The three values are
\[
\boxed{
\frac{2\pi i}{e},
\qquad
0,
\qquad
-\frac{26\pi i}{3}.
}
\]

::: {.proof}
Collect steps <1>3, <1>5, and <1>8.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 answers all three subparts.
:::
:::
