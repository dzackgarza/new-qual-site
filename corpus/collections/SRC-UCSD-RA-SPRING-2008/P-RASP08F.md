---
schema: qual/card@1
id: P-RASP08F
kind: problem
title: "Translation of distributions and distributional derivative"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
---

::: problem
For $f : \mathbb{R} \to \mathbb{C}$ and $h \in \mathbb{R}$, denote by $\tau_h f : \mathbb{R} \to \mathbb{C}$ the function defined by $\tau_h f(x) := f(x + h)$ for all $x \in \mathbb{R}$.

(a) Show that if $T$ is a distribution on $\mathbb{R}$ and $h \in \mathbb{R}$, then
$$
\tau_h T(\phi) := T(\tau_{-h}\phi), \qquad \phi \in C_0^\infty(\mathbb{R}),
$$
defines a distribution $\tau_h T$ on $\mathbb{R}$.

(b) Show that the following holds in $\mathcal{D}'(\mathbb{R})$:
$$
\lim_{h \to 0} \frac{\tau_h T - T}{h} = T'.
$$

(c) Show that if $T$ is a tempered distribution then $\tau_h T$ is also a tempered distribution.
Find the Fourier transform of $\tau_h T$ in terms of the Fourier transform of $T$.
:::
