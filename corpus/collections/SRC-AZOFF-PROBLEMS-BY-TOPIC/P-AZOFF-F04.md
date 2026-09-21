---
schema: qual/card@1
id: P-AZOFF-F04
kind: problem
title: Laurent series and singularities of $\frac{\sin^2 z}{z}$, $ze^{1/z^2}$, and $\frac{1}{z(4-z)}$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Laurent expansions and singularities, Problem 4, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Expanded sin^2(z)/z from the cosine series, z exp(1/z^2) from the
    exponential series, and 1/[z(4-z)] geometrically on both maximal annuli.
    The principal parts classify the singularities at zero as removable,
    essential, and a simple pole, respectively.
---

::: {.problem}
Find the Laurent series for the following functions about 0 and classify their singularities there.

a) $\frac { \sin ^ { 2 } z } { z }$

b) $\scriptstyle z \exp ( { \frac { 1 } { z ^ { 2 } } } )$

c) $\frac { 1 } { z ( 4 - z ) }$
:::

::: {.solution}
<1>1. For part (a),
$$
\boxed{
\frac{\sin^2 z}{z}
=
\sum_{n=1}^{\infty}
\frac{(-1)^{n+1}2^{2n-1}}{(2n)!}z^{2n-1}.
}
$$
The singularity at $0$ is removable.

::: {.proof}
Using
$$
\sin^2z=\frac{1-\cos(2z)}2
$$
and the Taylor series for cosine,
$$
\cos(2z)
=
\sum_{n=0}^{\infty}
\frac{(-1)^n(2z)^{2n}}{(2n)!},
$$
one gets
$$
1-\cos(2z)
=
\sum_{n=1}^{\infty}
\frac{(-1)^{n+1}2^{2n}z^{2n}}{(2n)!}.
$$
Dividing by $2z$ gives the displayed series. It contains no negative
powers, so the singularity at $0$ is removable. The series has infinite
radius of convergence and represents the holomorphic extension at $0$.
:::

<1>2. For part (b),
$$
\boxed{
z e^{1/z^2}
=
\sum_{n=0}^{\infty}\frac{z^{1-2n}}{n!}.
}
$$
The singularity at $0$ is essential.

::: {.proof}
The exponential series gives
$$
e^{1/z^2}
=
\sum_{n=0}^{\infty}\frac{z^{-2n}}{n!}
$$
for every $z\neq0$. Multiplying by $z$ yields the displayed Laurent
series, valid on
$$
0<\abs{z}<\infty.
$$
Its principal part contains infinitely many nonzero terms,
$$
z^{-1}+\frac{z^{-3}}{2!}+\frac{z^{-5}}{3!}+\cdots.
$$
Therefore $0$ is an essential singularity.
:::

<1>3. For part (c), on the annulus $0<\abs{z}<4$,
$$
\boxed{
\frac1{z(4-z)}
=
\sum_{n=0}^{\infty}\frac{z^{n-1}}{4^{n+1}}.
}
$$
In particular, the singularity at $0$ is a simple pole.

::: {.proof}
For $\abs{z}<4$,
$$
\begin{aligned}
\frac1{z(4-z)}
&=
\frac1{4z}\frac1{1-z/4}\\
&=
\frac1{4z}
\sum_{n=0}^{\infty}\left(\frac z4\right)^n\\
&=
\sum_{n=0}^{\infty}\frac{z^{n-1}}{4^{n+1}}.
\end{aligned}
$$
The principal part consists of the single nonzero term
$$
\frac1{4z}.
$$
Hence $0$ is a pole of order $1$.
:::

<1>4. For part (c), on the other maximal annulus $\abs{z}>4$,
$$
\boxed{
\frac1{z(4-z)}
=
-\sum_{n=0}^{\infty}4^n z^{-n-2}.
}
$$

::: {.proof}
If $\abs{z}>4$, then
$$
\begin{aligned}
\frac1{z(4-z)}
&=
-\frac1{z^2}\frac1{1-4/z}\\
&=
-\frac1{z^2}
\sum_{n=0}^{\infty}\left(\frac4z\right)^n\\
&=
-\sum_{n=0}^{\infty}4^n z^{-n-2}.
\end{aligned}
$$
The two annuli in steps <1>3 and <1>4 are maximal because the other finite
singularity is at $z=4$.
:::

<1>5. The singularities at $0$ are respectively removable, essential, and
a simple pole.

::: {.proof}
Step <1>1 gives a Laurent series with no principal part; step <1>2 gives
infinitely many negative-power terms; and step <1>3 gives exactly one
negative-power term of order $1$. These are precisely the three stated
classifications.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>5 provide the requested Laurent series and classifications.
:::
:::
