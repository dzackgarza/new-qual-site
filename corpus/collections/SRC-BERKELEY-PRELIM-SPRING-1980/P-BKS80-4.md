---
schema: qual/card@1
id: P-BKS80-4
kind: problem
title: A contour integral as the radius crosses a pole
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the double-pole residue at zero, the simple-pole residue at two,
    and the two contour-radius cases in the residue theorem.
---

::: {.problem}
Let $a>0$, $a\ne2$, and let $C_a$ be the positively oriented circle $|z|=a$.
Evaluate
\[
\int_{C_a}\frac{z^2+e^z}{z^2(z-2)}\,dz.
\]
:::

::: {.solution}
Set
$$
F(z)\coloneqq\frac{z^2+e^z}{z^2(z-2)}.
$$

<1>1. The residue of $F$ at the double pole $z=0$ is
$$
\Res_{z=0}F=-\frac34.
$$

::: {.proof}
Since
$$
z^2F(z)=\frac{z^2+e^z}{z-2},
$$
the double-pole residue formula gives
$$
\Res_{z=0}F
=
\left.
\frac{d}{dz}
\left(\frac{z^2+e^z}{z-2}\right)
\right|_{z=0}.
$$
The derivative is
$$
\frac{(2z+e^z)(z-2)-(z^2+e^z)}{(z-2)^2},
$$
whose value at $z=0$ is
$$
\frac{-2-1}{4}=-\frac34.
$$
:::

<1>2. The residue of $F$ at the simple pole $z=2$ is
$$
\Res_{z=2}F
=
1+\frac{e^2}{4}.
$$

::: {.proof}
By the simple-pole formula,
$$
\Res_{z=2}F
=
\left.
\frac{z^2+e^z}{z^2}
\right|_{z=2}
=
\frac{4+e^2}{4}
=
1+\frac{e^2}{4}.
$$
:::

<1>3. If $0<a<2$, then
$$
\int_{C_a}F(z)\,dz
=
-\frac{3\pi i}{2}.
$$

::: {.proof}
In this case the circle contains the pole at $0$ but not the pole at $2$.
The residue theorem and step <1>1 give
$$
\int_{C_a}F(z)\,dz
=
2\pi i\left(-\frac34\right)
=
-\frac{3\pi i}{2}.
$$
:::

<1>4. If $a>2$, then
$$
\int_{C_a}F(z)\,dz
=
\frac{\pi i}{2}(1+e^2).
$$

::: {.proof}
Now both poles lie inside $C_a$. By steps <1>1--<1>2, their residue sum is
$$
-\frac34+1+\frac{e^2}{4}
=
\frac{1+e^2}{4}.
$$
Thus the residue theorem gives
$$
\int_{C_a}F(z)\,dz
=
2\pi i\frac{1+e^2}{4}
=
\frac{\pi i}{2}(1+e^2).
$$
:::

<1>5. Therefore
$$
\boxed{
\int_{C_a}\frac{z^2+e^z}{z^2(z-2)}\,dz
=
\begin{cases}
-\dfrac{3\pi i}{2},&0<a<2,\\[6pt]
\dfrac{\pi i}{2}(1+e^2),&a>2.
\end{cases}
}
$$

::: {.proof}
The two cases in steps <1>3--<1>4 exhaust the hypothesis $a>0$,
$a\ne2$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the requested evaluation.
:::
:::
