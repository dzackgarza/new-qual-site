---
schema: qual/card@1
id: P-ZNVSP
kind: problem
title: Density of $f(\mathbb{H})$ for a holomorphic map of the half-plane real precisely
  on $\mathbb{R}$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Reflection
  - Picard
  - Open Mapping Theorem
relations: []
review: draft
---

::: {.problem}
Suppose $f: \HH\union \RR\to \CC$ satisfies the following:

- $f(i) = i$

- $f$ is continuous

- $f$ is analytic on $\HH$

- $f(z) \in \RR \iff z\in \RR$.

Show that $f(\HH)$ is a dense subset of $\HH$.
:::

::: {.solution}
<1>1. One has
$$
f(\HH)\subseteq\HH.
$$

::: {.proof}
By hypothesis, $f(z)\notin\RR$ for every $z\in\HH$. Since $\HH$ is
connected and $f$ is continuous, the connected set $f(\HH)$ must lie
entirely in one of the two connected components of $\CC\setminus\RR$.
Because $f(i)=i\in\HH$, that component is the upper half-plane.
:::

<1>2. Schwarz reflection extends $f$ to an entire function
$F:\CC\to\CC$ satisfying
$$
F(\bar z)=\overline{F(z)}.
$$

::: {.proof}
For $\Im z<0$, define
$$
F(z)=\overline{f(\bar z)},
$$
and on $\HH\cup\RR$ set $F=f$. The boundary values of $f$ on $\RR$ are
real by hypothesis, so the upper and lower definitions agree
continuously on $\RR$.

At each real point, the Schwarz reflection theorem applies on a small
disk centered at that point because $f$ is holomorphic in the upper
half-disk, continuous on the diameter, and real-valued there. Hence the
reflected function is holomorphic across every real point. It is already
holomorphic off $\RR$, so $F$ is entire on $\CC$.
:::

<1>3. The extension satisfies
$$
F(\{\Im z<0\})\subseteq\{\Im w<0\}
$$
and $F(\RR)\subseteq\RR$.

::: {.proof}
The second assertion is part of the hypothesis. If $\Im z<0$, then
$\bar z\in\HH$, so step <1>1 gives $f(\bar z)\in\HH$. Therefore
$$
F(z)=\overline{f(\bar z)}
$$
lies in the lower half-plane.
:::

<1>4. The entire function $F$ is nonconstant.

::: {.proof}
One has $F(i)=f(i)=i$. On the other hand, for every real $x$,
$F(x)=f(x)\in\RR$. Thus $F(x)\ne i$ for any real $x$, so $F$ cannot be
constant.
:::

<1>5. If $f(\HH)$ were not dense in $\HH$, then the entire function
$F$ would omit a nonempty open subset of $\CC$.

::: {.proof}
Assume $f(\HH)$ is not dense in $\HH$. Then there exist
$w_0\in\HH$ and $\varepsilon>0$ such that
$$
B(w_0,\varepsilon)\subseteq\HH
$$
and
$$
B(w_0,\varepsilon)\cap f(\HH)=\varnothing.
$$

No point of this disk can be attained by $F$ from the lower half-plane,
because step <1>3 maps that half-plane into itself. No point can be
attained from the real axis, because $F(\RR)\subseteq\RR$. No point can
be attained from the upper half-plane by the choice of the disk.
Therefore
$$
B(w_0,\varepsilon)\cap F(\CC)=\varnothing.
$$
:::

<1>6. A nonconstant entire function cannot omit a nonempty open subset
of $\CC$.

::: {.proof}
If an entire function is a nonconstant polynomial, then it is surjective
onto $\CC$: for any $w\in\CC$, the nonconstant polynomial $F-w$ has a
zero by the Fundamental Theorem of Algebra.

If an entire function is not a polynomial, then $\infty$ is an essential
singularity. Casorati--Weierstrass implies that the image of every
punctured neighborhood of $\infty$ is dense in $\CC$. Such a function
therefore cannot omit any nonempty open subset of $\CC$.

Thus in either case a nonconstant entire function cannot omit an open
disk.
:::

<1>7. The set $f(\HH)$ is dense in $\HH$.

::: {.proof}
If it were not dense, step <1>5 would force the nonconstant entire
function $F$ from step <1>4 to omit a nonempty open set, contradicting
step <1>6.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required conclusion.
:::
:::
