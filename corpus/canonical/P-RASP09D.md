---
schema: qual/card@1
id: P-RASP09D
kind: problem
title: "Principal value of 1/(x1 + x2) defines a distribution on R^2"
classification:
  areas:
  - real-analysis
  topics:
  - Distributions
  - Principal Value
relations: []
review: draft
---

::: problem
Show that on $\mathbb{R}^2$ (with coordinates $(x_1, x_2)$),
$$
\left\langle \operatorname{PV}\left(\frac{x_1 + x_2}{|x|^3}\right), \varphi \right\rangle = \lim_{\varepsilon \to 0} \int_{|x| > \varepsilon} \varphi(x) \frac{x_1 + x_2}{|x|^3} \, dm, \quad \varphi \in C_c^\infty(\mathbb{R}^2),
$$
exists and defines a distribution on $\mathbb{R}^2$.
:::
