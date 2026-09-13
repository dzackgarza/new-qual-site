---
schema: qual/card@1
id: PR-IV2DEGREVEN
kind: proposition
title: The ramification divisor has even degree
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ramification
  - Riemann-Hurwitz
  - Curves
relations:
- kind: uses
  target: T-LKT0U
- kind: uses
  target: D-IV2RAM
review: draft
prompts:
- Show that $\deg R$ is even for a finite separable morphism of curves.
- A degree-$3$ cover of $\PP^1$ is branched at how many points, if the ramification is tame and simple?
---

::: {.proposition}
Let $f : X \to Y$ be a finite separable morphism of curves.
Then $\deg R$ is even.
:::

::: {.proof}
$R \sim K_X - f^* K_Y$, so
\[
\deg R = (2 g_X - 2) - \deg(f)(2 g_Y - 2) ,
\]
a difference of two even integers.
:::

::: {.remark title="What it is for"}
The proof is Riemann--Hurwitz with the terms moved, so the content is not the derivation but the parity constraint it hands back, which is a free consistency check on any ramification count.
A proposed branching pattern with $\deg R$ odd is wrong before any geometry is examined, and that is the fastest way to catch an arithmetic slip under exam conditions.

Used forward with tame simple ramification, where every $e_p = 2$ and $\deg R$ counts the branch points, it says such a cover has an even number of branch points.
This is the reason a degree-$2$ cover of $\PP^1$ is branched at $2g+2$ points rather than an arbitrary number, and the reason the Legendre normal form of an elliptic curve has exactly four branch points and not three.
It also rules out possibilities directly: no simply branched cover of $\PP^1$ has an odd branch count, whatever its degree.

The hypothesis that bites is separability, since the whole statement descends from $K_X \sim f^* K_Y + R$, which needs the cotangent sequence to be short exact.
In characteristic $p$ there is no parity statement about an inseparable morphism because there is no $R$; see [[PR-IV2INSEP]].
:::
