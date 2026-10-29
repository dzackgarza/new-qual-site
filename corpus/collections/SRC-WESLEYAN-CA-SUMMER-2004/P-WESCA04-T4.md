---
schema: qual/card@1
id: P-WESCA04-T4
kind: problem
title: "State the Open Mapping Theorem"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1.1, item 4 (August 2, 2004) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
State the Open Mapping Theorem.
:::

::: {.solution}

::: pf

::: pf-step

Let
\[
\Omega\subseteq\CC
\]
be a domain and let
\[
f:\Omega\to\CC
\]
be a nonconstant holomorphic function. Then
\[
\boxed{
f(\Omega)
\text{ is open in }\CC.
}
\]
Equivalently, $f$ maps every open subset of $\Omega$ to an open subset of
$\CC$.


::: pf-proof

This is the Open Mapping Theorem. The remaining steps prove the local
statement at an arbitrary point of $\Omega$.

:::

:::

::: {.pf-step #s1-2}

Fix
\[
z_0\in\Omega
\]
and set
\[
w_0=f(z_0).
\]
Then there is an integer
\[
m\ge1
\]
and a holomorphic function $g$ near $z_0$ such that
\[
f(z)-w_0
=
(z-z_0)^m g(z),
\qquad
g(z_0)\ne0.
\]


::: pf-proof

The holomorphic function
\[
f-w_0
\]
vanishes at $z_0$. Since $f$ is nonconstant on the connected domain
$\Omega$, the identity theorem implies that $f-w_0$ is not identically
zero.

Therefore $z_0$ is a zero of finite order $m\ge1$, which gives the stated
factorization with $g(z_0)\ne0$.

:::

:::

::: {.pf-step #s1-3}

There exists
\[
r>0
\]
such that
\[
\overline{B(z_0,r)}
\subset\Omega
\]
and $z_0$ is the only zero of $f-w_0$ in that closed disk.


::: pf-proof

Zeros of a nonzero holomorphic function are isolated. Thus there is a
neighborhood of $z_0$ containing no other zero of $f-w_0$.

Because $\Omega$ is open, choose $r>0$ small enough that the closed disk
lies in both that neighborhood and $\Omega$.

:::

:::

::: pf-step

Define
\[
\delta
\coloneqq
\min_{|z-z_0|=r}
|f(z)-w_0|.
\]
Then
\[
\delta>0.
\]


::: pf-proof

By step [](#s1-3){.pf-ref}, the continuous function
\[
|f(z)-w_0|
\]
is strictly positive on the compact circle
\[
|z-z_0|=r.
\]
It therefore attains a positive minimum there.

:::

:::

::: {.pf-step #s1-5}

If
\[
|w-w_0|<\delta,
\]
then $f(z)=w$ has at least one solution in
\[
B(z_0,r).
\]


::: pf-proof

On the circle
\[
|z-z_0|=r,
\]
one has
\[
|(f(z)-w)-(f(z)-w_0)|
=
|w-w_0|
<
\delta
\le
|f(z)-w_0|.
\]

Rouché's theorem therefore says that
\[
f(z)-w
\]
and
\[
f(z)-w_0
\]
have the same number of zeros inside the circle, counted with
multiplicity.

By step [](#s1-2){.pf-ref}, the second function has a zero of multiplicity $m\ge1$ at
$z_0$ and no other zero in the disk by step [](#s1-3){.pf-ref}. Hence
\[
f(z)-w
\]
has $m$ zeros in the disk, in particular at least one.

:::

:::

::: {.pf-step #s1-6}

Thus
\[
B(w_0,\delta)
\subseteq
f(\Omega).
\]


::: pf-proof

Let
\[
w\in B(w_0,\delta).
\]
Step [](#s1-5){.pf-ref} gives
\[
z\in B(z_0,r)\subseteq\Omega
\]
with
\[
f(z)=w.
\]
Hence every point of the disk around $w_0$ lies in the image.

:::

:::

::: {.pf-step #s1-7}

Therefore
\[
f(\Omega)
\]
is open.


::: pf-proof

Every point
\[
w_0\in f(\Omega)
\]
has the form
\[
w_0=f(z_0)
\]
for some $z_0\in\Omega$. Step [](#s1-6){.pf-ref} gives an open disk centered at $w_0$
contained in $f(\Omega)$.

Thus every point of $f(\Omega)$ is an interior point, so the image is open.

:::

:::

::: {.pf-step #s1-8}

More generally, if
\[
V\subseteq\Omega
\]
is open, then
\[
f(V)
\]
is open.


::: pf-proof

Each connected component $V_\alpha$ of $V$ is an open connected subset of
$\Omega$.

If $f$ is nonconstant on $V_\alpha$, step [](#s1-7){.pf-ref} applied to the restriction
\[
f|_{V_\alpha}
\]
shows that
\[
f(V_\alpha)
\]
is open.

The restriction cannot be constant on any nonempty component
$V_\alpha$: if it were, the identity theorem would make $f$ constant on
the connected domain $\Omega$.

Therefore
\[
f(V)
=
\bigcup_\alpha f(V_\alpha)
\]
is a union of open sets.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the standard Open Mapping Theorem, and step [](#s1-8){.pf-ref} gives the
equivalent open-map formulation.

:::

:::

:::
