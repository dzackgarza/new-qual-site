---
schema: qual/card@1
id: P-CHAVAN-CA-4-2
kind: problem
title: A partial sum of the cosine series has a zero near the origin
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The extraction omits the center value in the source phrase "disc with center and radius pi/2"; the card records the intended disk centered at the origin.
---

::: {.problem}
Consider the Taylor series
$$
\cos z=\sum_{k=0}^{\infty}\frac{(-1)^kz^{2k}}{(2k)!}.
$$
Show that at least one partial sum has a zero in the disk
$$
|z|<\frac{\pi}{2}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The partial sum through the quadratic term is
$$
p_1(z)=1-\frac{z^2}{2}.
$$


::: pf-proof

Taking the terms with $k=0$ and $k=1$ in the cosine series gives
$$
p_1(z)
=\frac{(-1)^0z^0}{0!}+\frac{(-1)^1z^2}{2!}
=1-\frac{z^2}{2}.
$$

:::

:::

::: {.pf-step #s1-2}

The zeros of $p_1$ are
$$
z=\pm\sqrt2.
$$


::: pf-proof

The equation $p_1(z)=0$ is equivalent to
$$
1-\frac{z^2}{2}=0,
$$
hence to $z^2=2$. Thus its two zeros are $\sqrt2$ and $-\sqrt2$.

:::

:::

::: {.pf-step #s1-3}

Both zeros from step [](#s1-2){.pf-ref} lie in the disk $|z|<\pi/2$.


::: pf-proof

Since
$$
2\sqrt2<3<\pi,
$$
one has
$$
\sqrt2<\frac{\pi}{2}.
$$
Here $2\sqrt2<3$ follows by squaring the positive quantities, since
$8<9$, while $3<\pi$ follows because the circumference $2\pi$ of the
unit circle is strictly larger than the perimeter $6$ of its inscribed
regular hexagon.
Therefore
$$
|\pm\sqrt2|=\sqrt2<\frac{\pi}{2}.
$$

:::

:::

::: {.pf-step #s1-4}

At least one partial sum of the cosine series has a zero in $|z|<\pi/2$.


::: pf-proof

The partial sum $p_1$ from step [](#s1-1){.pf-ref} has the two zeros identified in
step [](#s1-2){.pf-ref}, and step [](#s1-3){.pf-ref} places both of them in the required disk.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
