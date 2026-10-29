---
schema: qual/card@1
id: P-TIE-S15-18
kind: problem
title: Univalent functions on a punctured plane are Möbius transformations
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 18.
---

::: {.problem}
Let $f ( z )$ be an analytic function on $\CC \backslash \{ z _ { 0 } \}$ , where $z _ { \mathrm { 0 } }$ is a fixed point.
Assume that $f ( z )$ is bijective from $\CC \backslash \{ z _ { 0 } \}$ onto its image, and that $f ( z )$ is bounded outside $D _ { r } ( z _ { 0 } )$ , where r is some fixed positive number.
Show that there exist $a , b , c , d \in \CC$ with $a d - b c \neq 0 , c \neq 0$ such that $f ( z ) = { \frac { a z + b } { c z + d } } .$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The singularity of $f$ at $z_0$ is not removable.


::: pf-proof

Suppose it were removable. Then $f$ would extend to an entire function
$$
\widetilde f:\CC\to\CC.
$$
By hypothesis, $f$ is bounded outside some disk centered at $z_0$. On the remaining compact disk, the continuous extension $\widetilde f$ is also bounded. Hence $\widetilde f$ is bounded on all of $\CC$. Liouville's theorem would make $\widetilde f$ constant, contradicting the injectivity of $f$ on $\CC\setminus\{z_0\}$.

:::

:::

::: {.pf-step #s1-2}

The singularity of $f$ at $z_0$ is not essential.


::: pf-proof

Suppose it were essential. By the Great Picard theorem, in every punctured neighborhood of $z_0$ the function $f$ assumes every complex value, with at most one exception, infinitely many times.

Choose a point
$$
w\in\CC\setminus\{z_0\}.
$$
The value $f(w)$ is attained at $w$, so it cannot be the exceptional value omitted near $z_0$. Hence every punctured neighborhood of $z_0$ contains infinitely many points $z$ satisfying
$$
f(z)=f(w).
$$
At least one such point differs from $w$, contradicting injectivity. Therefore the singularity is not essential.

:::

:::

::: pf-step

Hence $z_0$ is a pole of $f$.


::: pf-proof

An isolated singularity is removable, a pole, or essential. Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} exclude the first and third possibilities, so $z_0$ is a pole.

:::

:::

::: {.pf-step #s1-4}

The pole at $z_0$ has order exactly $1$.


::: pf-proof

Suppose the pole had order $m\ge2$. Its local Laurent expansion has the form
$$
f(z)
=
\frac{A}{(z-z_0)^m}
\left(1+o(1)\right),
\qquad
A\ne0.
$$
The local mapping theorem for a pole of order $m$ says that every sufficiently large value has exactly $m$ preimages near $z_0$, counted with multiplicity. For $m\ge2$, this contradicts injectivity. Therefore $m=1$.

:::

:::

::: {.pf-step #s1-5}

There exists $A\ne0$ such that
$$
f(z)-\frac{A}{z-z_0}
$$
extends to an entire function.


::: pf-proof

By step [](#s1-4){.pf-ref}, the Laurent expansion of $f$ at $z_0$ has principal part
$$
\frac{A}{z-z_0}
$$
with $A\ne0$. Subtracting this principal part removes the pole, so
$$
H(z)
\coloneqq
f(z)-\frac{A}{z-z_0}
$$
extends holomorphically across $z_0$. Away from $z_0$ it is already holomorphic, hence the extension is entire.

:::

:::

::: {.pf-step #s1-6}

The entire function $H$ from step [](#s1-5){.pf-ref} is bounded.


::: pf-proof

By hypothesis, there are $r>0$ and $M>0$ such that
$$
\abs{f(z)}\le M
$$
whenever
$$
\abs{z-z_0}\ge r.
$$
On the same region,
$$
\abs{\frac{A}{z-z_0}}
\le
\frac{\abs A}{r}.
$$
Thus
$$
\abs{H(z)}
\le
M+\frac{\abs A}{r}
$$
outside the disk. On the remaining compact disk, the entire function $H$ is bounded by continuity. Hence $H$ is bounded on all of $\CC$.

:::

:::

::: {.pf-step #s1-7}

There exists $B\in\CC$ such that
$$
f(z)
=
B+\frac{A}{z-z_0}.
$$


::: pf-proof

By step [](#s1-6){.pf-ref} and Liouville's theorem, the entire function $H$ is constant:
$$
H(z)\equiv B.
$$
Substituting the definition of $H$ from step [](#s1-5){.pf-ref} gives the formula.

:::

:::

::: {.pf-step #s1-8}

The function $f$ has the required Möbius form
$$
\boxed{
f(z)
=
\frac{az+b}{cz+d},
}
$$
with
$$
ad-bc\ne0,
\qquad
c\ne0.
$$


::: pf-proof

Rewrite step [](#s1-7){.pf-ref} as
$$
f(z)
=
\frac{B(z-z_0)+A}{z-z_0}
=
\frac{Bz+(A-Bz_0)}{z-z_0}.
$$
Set
$$
a=B,
\qquad
b=A-Bz_0,
\qquad
c=1,
\qquad
d=-z_0.
$$
Then $c\ne0$, and
$$
ad-bc
=
-Bz_0-(A-Bz_0)
=
-A
\ne0.
$$
Thus the Möbius representation has nonzero determinant.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is exactly the required conclusion.

:::

:::

:::
