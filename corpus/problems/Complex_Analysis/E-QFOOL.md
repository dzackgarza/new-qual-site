---
schema: qual/card@1
id: E-QFOOL
kind: problem
title: Special case of bijections
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Biholomorphisms
relations: []
review: draft
---

:::{.exercise}
Show that if $f: \Delta\to\Delta$ is a biholomorphism with $f(0) = 0$ then $f$ is a rotation.

:::

:::{.solution}
By Schwarz, $\abs{f(z)} \leq \abs{z}$, and if we write $h \da f\inv$ then $h(0) = 0$ and $\abs{h(z)} \leq \abs{z}$ as well.
Schwarz says $f$ will be a rotation if there is any $z_0$ such that $\abs{f(z_0)} = \abs{z_0}$.
Write $f(z) = w$, we'll then show that in fact $\abs{f(z)} = \abs{z}$ for all $z\in \DD$.
\[
\abs{z} = \abs{(h\circ f)(z)} = \abs{h(w)} \leq \abs{w} = \abs{f(z)}\leq \abs{z}
.\]
:::

:::{.solution title="Shorter version"}
By Schwarz, $\abs{f'(0)} \leq 1$ -- the claim is that we have equality, so that by Schwarz $f(z) = \lambda z$ for some $\abs{\lambda} = 1$.
Use that $f'(0) \neq 0$ since $f$ is a bijection near zero and if $g\da f\inv$ then $g'(0) = 1/f'(0)$.
Moreover Schwarz applies to $g$, so $1 \geq \abs{g'(0)} \geq {1\over \abs{f'(0)} }$, forcing $\abs{ f'(0) } = 1$.
By the equality clause in the Schwarz lemma for $f$, $f$ is rotation.
:::
