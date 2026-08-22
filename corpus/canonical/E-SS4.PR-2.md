---
schema: qual/card@1
id: E-SS4.PR-2
kind: exercise
title: "SS 4.PR-2: Solving a linear ODE with the Fourier transform"
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Contour Integration
relations: []
review: draft
solved: false
---

::: exercise
2. The problem is to solve the diferential equation

$$

a _ {n} \frac {d ^ {n}}{d t ^ {n}} u (t) + a _ {n - 1} \frac {d ^ {n - 1}}{d t ^ {n - 1}} u (t) + \dots + a _ {0} u (t) = f (t),

$$

where $a _ { 0 } , a _ { 1 } , \ldots , a _ { n }$ are complex constants, and $f$ is a given function. Here we suppose that $f$ has bounded support and is smooth (say of class $C ^ { 2 } )$

(a) Let

$$

\hat {f} (z) = \int_ {- \infty} ^ {\infty} f (t) e ^ {- 2 \pi i z t} d t.

$$

Observe that $\hat { f }$ is an entire function, and using integration by parts show that

$$

| \hat {f} (x + i y) | \leq \frac {A}{1 + x ^ {2}}

$$

if $| y | \le a$ for any fixed $a \geq 0$

(b) Write

$$

P (z) = a _ {n} (2 \pi i z) ^ {n} + a _ {n - 1} (2 \pi i z) ^ {n - 1} + \dots + a _ {0}.

$$

Find a real number c so that $P ( z )$ does not vanish on the line

$$

L = \{z: z = x + i c, x \in \mathbb {R} \}.

$$

(c) Set

$$

u (t) = \int_ {L} \frac {e ^ {2 \pi i z t}}{P (z)} \hat {f} (z) d z.

$$
:::
