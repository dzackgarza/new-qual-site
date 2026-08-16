---
schema: qual/card@1
id: P-CWZF3
kind: problem
title: "We want to show that if $(p) \\normal R$ is a prime ideal then $R/(p)$\u2026"
classification:
  areas:
  - algebra
  topics:
  - prime-ideals
  - maximal-ideals
  - principal-ideal-domains
relations: []
review: draft
---

::: problem
We want to show that if $(p) \normal R$ is a prime ideal then $R/(p)$ is a field, so we'll proceed by letting $x + (p) \in R/(p)$ be arbitrary where $x\not \in (p)$ and producing a multiplicative inverse.

Since $R$ is a principal ideal domain, prime ideals are maximal, so $(p)$ is maximal.
Then $x\in R \setminus (p)$, so define
$$
I \definedas \theset{p + rx \suchthat p\in (p), r\in R} \normal R,
$$

which is an ideal in $R$.

In particular, since $x\not\in (p)$, we have a strict containment $(p) < I$, but since $(p)$ was maximal this forces $I = R$.

Then $1 \in I$, so there exists some $p, r$ such that $p + rx = 1$, i.e. $rx - 1 \in (p)$.

But then

$$
r + (p) \cdot x + (p) = rx + (p) = 1 + (p),
$$

which says that $(x + (p))\inv = r + (p)$ in $R/(p)$.
:::
